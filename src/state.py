"""Agent 状态管理模块"""
from typing import TypedDict, List, Any, Dict
from langchain_core.messages import BaseMessage


class AgentState(TypedDict):
    """
    Agent 运行时状态

    Attributes:
        messages: 完整的聊天历史，包括 SystemMessage, HumanMessage, AIMessage, ToolMessage
        tool_results: 所有工具调用的结果记录
        current_step: 当前执行步骤计数器，用于调试和防止无限循环
    """
    messages: List[BaseMessage]
    tool_results: List[Dict[str, Any]]
    current_step: int


def create_initial_state(user_input: str) -> AgentState:
    """
    创建初始状态

    Args:
        user_input: 用户输入的内容

    Returns:
        初始化的 AgentState
    """
    from langchain_core.messages import HumanMessage

    return {
        "messages": [HumanMessage(content=user_input)],
        "tool_results": [],
        "current_step": 0
    }


def get_last_message(state: AgentState) -> BaseMessage:
    """
    获取最后一条消息

    Args:
        state: 当前状态

    Returns:
        最后一条消息
    """
    return state["messages"][-1]


def has_tool_calls(state: AgentState) -> bool:
    """
    判断最后一条消息是否包含工具调用

    Args:
        state: 当前状态

    Returns:
        是否包含工具调用
    """
    last_message = get_last_message(state)
    return hasattr(last_message, "tool_calls") and len(last_message.tool_calls) > 0


def get_tool_calls(state: AgentState) -> List[Dict[str, Any]]:
    """
    获取最后一条消息的工具调用列表

    Args:
        state: 当前状态

    Returns:
        工具调用列表
    """
    last_message = get_last_message(state)
    if hasattr(last_message, "tool_calls"):
        return last_message.tool_calls
    return []


def add_message(state: AgentState, message: BaseMessage) -> AgentState:
    """
    向状态中添加消息

    Args:
        state: 当前状态
        message: 要添加的消息

    Returns:
        更新后的状态
    """
    return {
        **state,
        "messages": state["messages"] + [message],
        "current_step": state["current_step"] + 1
    }


def add_tool_result(state: AgentState, tool_result: Dict[str, Any]) -> AgentState:
    """
    向状态中添加工具调用结果

    Args:
        state: 当前状态
        tool_result: 工具调用结果

    Returns:
        更新后的状态
    """
    return {
        **state,
        "tool_results": state["tool_results"] + [tool_result],
        "current_step": state["current_step"] + 1
    }