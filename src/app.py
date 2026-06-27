"""应用启动入口"""
import logging
import sys

from src.state import create_initial_state
from src.graph import graph
from logging_config import setup_logging

# 配置日志
setup_logging()
logger = logging.getLogger(__name__)


def run_agent(user_input: str) -> dict:
    """
    运行 Agent 处理用户请求

    Args:
        user_input: 用户输入的请求内容

    Returns:
        Agent 执行结果,包含最终状态和答案
    """
    logger.info("=" * 80)
    logger.info("启动 Agent")
    logger.info("=" * 80)
    logger.info(f"用户输入: {user_input}")

    # 1. 创建初始状态
    initial_state = create_initial_state(user_input)
    logger.info("创建初始状态成功")

    # 2. 启动工作流
    logger.info("启动 LangGraph 工作流...")
    result = graph.invoke(initial_state)

    # 3. 提取最终答案
    final_message = result["messages"][-1]
    final_answer = final_message.content if hasattr(final_message, "content") else str(final_message)

    logger.info("=" * 80)
    logger.info("Agent 执行完成")
    logger.info("=" * 80)
    logger.info(f"最终步骤: {result['current_step']}")
    logger.info(f"工具调用次数: {len(result['tool_results'])}")
    logger.info(f"最终答案: {final_answer}")

    return {
        "result": result,
        "final_answer": final_answer,
        "tool_results": result["tool_results"]
    }


def display_result(execution_result: dict) -> None:
    """
    展示执行结果

    Args:
        execution_result: Agent 执行结果
    """
    print("\n" + "=" * 80)
    print("执行结果")
    print("=" * 80)

    # 展示工具调用记录
    if execution_result["tool_results"]:
        print("\n工具调用记录:")
        for i, tool_result in enumerate(execution_result["tool_results"], 1):
            print(f"{i}. {tool_result['tool_name']}")
            print(f"   参数: {tool_result['tool_args']}")
            print(f"   结果: {tool_result['result']}")

    # 展示最终答案
    print("\n最终答案:")
    print(execution_result["final_answer"])
    print("=" * 80)


def interactive_mode() -> None:
    """
    交互模式：持续接收用户输入并处理
    """
    print("=" * 80)
    print("Order AI Agent - 交互模式")
    print("=" * 80)
    print("可用工具:")
    print("  - query_order: 查询订单")
    print("  - query_user: 查询用户")
    print("  - query_inventory: 查询库存")
    print("  - create_payment: 创建支付链接")
    print("  - send_email: 发送邮件")
    print("  - cancel_order: 取消订单")
    print("\n输入 'exit' 或 'quit' 退出")
    print("=" * 80)

    while True:
        try:
            user_input = input("\n请输入您的请求: ").strip()

            if user_input.lower() in ["exit", "quit", "q"]:
                print("\n感谢使用,再见!")
                break

            if not user_input:
                print("请输入有效的请求")
                continue

            # 运行 Agent
            execution_result = run_agent(user_input)

            # 展示结果
            display_result(execution_result)

        except KeyboardInterrupt:
            print("\n\n程序已中断")
            break
        except Exception as e:
            logger.error(f"执行出错: {str(e)}")
            print(f"\n错误: {str(e)}")


def single_run_mode(user_input: str) -> None:
    """
    单次运行模式：处理一次请求并退出

    Args:
        user_input: 用户请求内容
    """
    execution_result = run_agent(user_input)
    display_result(execution_result)


def main():
    """
    主函数：启动应用
    """
    if len(sys.argv) > 1:
        # 单次运行模式
        user_input = sys.argv[1]
        single_run_mode(user_input)
    else:
        # 交互模式
        interactive_mode()


if __name__ == "__main__":
    main()