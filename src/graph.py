"""LangGraph 工作流编排模块"""
import logging
from langgraph.graph import StateGraph, END

from src.state import AgentState, has_tool_calls
from src.nodes.agent_node import agent_node
from src.nodes.tool_node import tool_node

logger = logging.getLogger(__name__)


def should_continue(state: AgentState) -> str:
    """
    判断是否需要继续调用工具

    Args:
        state: 当前 Agent 状态

    Returns:
        "tools" - 如果需要调用工具
        "end" - 如果不需要调用工具，结束执行
    """
    logger.info("=" * 50)
    logger.info("判断是否继续执行")
    logger.info(f"当前步骤: {state['current_step']}")
    logger.info(f"消息数量: {len(state['messages'])}")

    # 检查最后一条消息是否包含工具调用
    if has_tool_calls(state):
        logger.info("判断结果: 需要执行工具 → tools")
        return "tools"

    logger.info("判断结果: 不需要执行工具 → end")
    return "end"


def create_graph() -> StateGraph:
    """
    创建 Agent 工作流图

    Returns:
        编译后的 LangGraph 工作流图
    """
    logger.info("=" * 50)
    logger.info("创建 Agent 工作流图")
    logger.info("=" * 50)

    # 1. 创建 StateGraph
    workflow = StateGraph(AgentState)
    logger.info("创建 StateGraph 成功")

    # 2. 添加节点
    logger.info("添加节点...")
    workflow.add_node("agent", agent_node)
    logger.info("  - 添加 Agent Node")

    workflow.add_node("tools", tool_node)
    logger.info("  - 添加 Tool Node")

    # 3. 设置入口点
    logger.info("设置入口点: agent")
    workflow.set_entry_point("agent")

    # 4. 配置条件边（Agent Node → 判断 → Tool Node / END）
    logger.info("配置条件边...")
    workflow.add_conditional_edges(
        "agent",
        should_continue,
        {
            "tools": "tools",
            "end": END
        }
    )
    logger.info("  - Agent → 条件判断 → tools/end")

    # 5. 配置普通边（Tool Node → Agent Node）
    workflow.add_edge("tools", "agent")
    logger.info("  - tools → agent")

    # 6. 编译图
    logger.info("编译工作流图...")
    graph = workflow.compile()
    logger.info("工作流图编译成功")
    logger.info("=" * 50)

    return graph


# 创建全局 Graph 实例
graph = create_graph()
logger.info("全局 Graph 实例已创建")