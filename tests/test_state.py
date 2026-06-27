"""测试状态管理模块"""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../src'))

from src.state import (
    create_initial_state,
    get_last_message,
    has_tool_calls,
    add_message
)
from langchain_core.messages import HumanMessage, AIMessage


def test_state():
    """测试状态管理功能"""
    print("=" * 50)
    print("测试状态管理模块")
    print("=" * 50)

    # 测试创建初始状态
    print("\n1. 测试创建初始状态")
    state = create_initial_state("查询订单10086")
    print(f"用户输入: 查询订单10086")
    print(f"消息数量: {len(state['messages'])}")
    print(f"工具结果数量: {len(state['tool_results'])}")
    print(f"当前步骤: {state['current_step']}")
    assert len(state["messages"]) == 1
    assert state["current_step"] == 0

    # 测试获取最后一条消息
    print("\n2. 测试获取最后一条消息")
    last_message = get_last_message(state)
    print(f"最后一条消息类型: {type(last_message).__name__}")
    print(f"最后一条消息内容: {last_message.content}")
    assert isinstance(last_message, HumanMessage)

    # 测试添加消息
    print("\n3. 测试添加消息")
    ai_message = AIMessage(content="我将调用 query_order 工具")
    state = add_message(state, ai_message)
    print(f"添加 AI 消息后，消息数量: {len(state['messages'])}")
    print(f"当前步骤: {state['current_step']}")
    assert len(state["messages"]) == 2
    assert state["current_step"] == 1

    # 测试工具调用判断
    print("\n4. 测试工具调用判断")
    has_calls = has_tool_calls(state)
    print(f"是否有工具调用: {has_calls}")
    assert has_calls is False

    # 测试添加带工具调用的 AI 消息
    print("\n5. 测试带工具调用的消息")
    ai_message_with_tools = AIMessage(
        content="",
        tool_calls=[{"name": "query_order", "args": {"order_id": 10086}, "id": "call_123"}]
    )
    state = add_message(state, ai_message_with_tools)
    has_calls = has_tool_calls(state)
    print(f"是否有工具调用: {has_calls}")
    assert has_calls is True

    print("\n" + "=" * 50)
    print("状态管理测试通过！")
    print("=" * 50)


if __name__ == "__main__":
    test_state()