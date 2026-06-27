"""Tool 节点模块"""
import logging
import json
from typing import Dict, Any
from langchain_core.messages import ToolMessage

from src.state import AgentState, add_message, add_tool_result, get_tool_calls
from src.tools import get_all_tools

logger = logging.getLogger(__name__)


def tool_node(state: AgentState) -> AgentState:
    """
    Tool 节点：执行工具调用

    职责：
    1. 执行所有工具调用
    2. 处理工具返回结果
    3. 封装 ToolMessage
    4. 返回更新后的状态

    Args:
        state: 当前 Agent 状态

    Returns:
        更新后的 Agent 状态
    """
    logger.info("=" * 50)
    logger.info("进入 Tool Node")
    logger.info(f"当前步骤: {state['current_step']}")
    logger.info(f"消息数量: {len(state['messages'])}")

    # 1. 获取工具调用列表
    tool_calls = get_tool_calls(state)
    logger.info(f"工具调用数量: {len(tool_calls)}")

    if not tool_calls:
        logger.warning("没有工具调用，Tool Node 不应该被调用")
        return state

    # 2. 获取所有工具并建立映射
    tools = get_all_tools()
    tools_map: Dict[str, Any] = {tool.name: tool for tool in tools}
    logger.info(f"已加载 {len(tools_map)} 个工具")

    # 3. 执行所有工具调用
    tool_messages: list[ToolMessage] = []
    tool_results: list[Dict[str, Any]] = []

    for tool_call in tool_calls:
        tool_name = tool_call["name"]
        tool_args = tool_call["args"]
        tool_call_id = tool_call["id"]

        logger.info(f"执行工具: {tool_name}")
        logger.info(f"工具参数: {tool_args}")
        logger.info(f"调用 ID: {tool_call_id}")

        # 查找工具
        tool = tools_map.get(tool_name)

        if tool is None:
            logger.error(f"工具不存在: {tool_name}")
            result = {"error": f"工具 {tool_name} 不存在"}
        else:
            # 执行工具
            try:
                result = tool.invoke(tool_args)
                logger.info(f"工具执行成功")
                logger.info(f"工具返回结果: {json.dumps(result, ensure_ascii=False)}")
            except Exception as e:
                logger.error(f"工具执行失败: {str(e)}")
                result = {"error": f"工具执行失败: {str(e)}"}

        # 封装 ToolMessage
        tool_message = ToolMessage(
            content=json.dumps(result, ensure_ascii=False),
            tool_call_id=tool_call_id
        )
        tool_messages.append(tool_message)

        # 记录工具结果
        tool_result_record = {
            "tool_name": tool_name,
            "tool_args": tool_args,
            "tool_call_id": tool_call_id,
            "result": result
        }
        tool_results.append(tool_result_record)

        logger.info(f"工具 {tool_name} 执行完成")

    # 4. 更新状态
    # 添加所有 ToolMessage
    new_state = state
    for tool_message in tool_messages:
        new_state = add_message(new_state, tool_message)

    # 添加所有工具结果记录
    for tool_result in tool_results:
        new_state = add_tool_result(new_state, tool_result)

    logger.info(f"更新后步骤: {new_state['current_step']}")
    logger.info(f"更新后消息数量: {len(new_state['messages'])}")
    logger.info(f"更新后工具结果数量: {len(new_state['tool_results'])}")
    logger.info("离开 Tool Node")
    logger.info("=" * 50)

    return new_state