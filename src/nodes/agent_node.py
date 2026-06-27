"""Agent 节点模块"""
import logging
from typing import Dict, Any
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage

from src.config import OPENAI_API_KEY, OPENAI_API_BASE, MODEL_NAME
from src.state import AgentState, add_message
from src.prompts import get_system_prompt
from src.tools import get_all_tools

logger = logging.getLogger(__name__)


def agent_node(state: AgentState) -> AgentState:
    """
    Agent 节点：调用 LLM 进行推理

    职责：
    1. 调用 LLM API
    2. 处理 LLM 响应
    3. 返回更新后的状态

    Args:
        state: 当前 Agent 状态

    Returns:
        更新后的 Agent 状态
    """
    logger.info("=" * 50)
    logger.info("进入 Agent Node")
    logger.info(f"当前步骤: {state['current_step']}")
    logger.info(f"消息数量: {len(state['messages'])}")

    # 1. 初始化 LLM
    logger.info("初始化 LLM...")
    llm = ChatOpenAI(
        model=MODEL_NAME,
        temperature=0,
        api_key=OPENAI_API_KEY,
        base_url=OPENAI_API_BASE
    )

    # 2. 绑定工具
    logger.info("绑定工具...")
    tools = get_all_tools()
    llm_with_tools = llm.bind_tools(tools)
    logger.info(f"已绑定 {len(tools)} 个工具")

    # 3. 准备消息
    messages = state["messages"]

    # 如果是第一次调用，添加 System Prompt
    if not any(isinstance(msg, SystemMessage) for msg in messages):
        logger.info("添加 System Prompt")
        system_prompt = get_system_prompt()
        messages = [SystemMessage(content=system_prompt)] + messages

    # 4. 调用 LLM
    logger.info("调用 LLM...")
    logger.info(f"发送 {len(messages)} 条消息")

    try:
        response = llm_with_tools.invoke(messages)
        logger.info("LLM 响应成功")

        # 打印响应信息
        if response.content:
            logger.info(f"响应内容: {response.content[:100]}...")

        if hasattr(response, "tool_calls") and response.tool_calls:
            logger.info(f"工具调用数量: {len(response.tool_calls)}")
            for tool_call in response.tool_calls:
                logger.info(f"  - 工具名称: {tool_call['name']}")
                logger.info(f"    工具参数: {tool_call['args']}")
        else:
            logger.info("无工具调用，将生成最终答案")

    except Exception as e:
        logger.error(f"LLM 调用失败: {str(e)}")
        raise

    # 5. 更新状态
    new_state = add_message(state, response)
    logger.info(f"更新后步骤: {new_state['current_step']}")
    logger.info(f"更新后消息数量: {len(new_state['messages'])}")
    logger.info("离开 Agent Node")
    logger.info("=" * 50)

    return new_state