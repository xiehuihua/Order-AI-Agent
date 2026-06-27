"""测试所有工具模块"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.tools import get_all_tools
from src.tools.create_payment import create_payment
from src.tools.send_email import send_email
from src.tools.cancel_order import cancel_order


def test_all_tools():
    """测试所有工具"""
    print("=" * 50)
    print("测试所有工具")
    print("=" * 50)

    tools = get_all_tools()
    print(f"\n已注册工具数量: {len(tools)}")
    assert len(tools) == 6, "应该注册 6 个工具"

    # 测试每个工具
    for tool in tools:
        print(f"\n工具名称: {tool.name}")
        print(f"工具描述: {tool.description}")

    # 测试 create_payment
    print("\n" + "=" * 50)
    print("测试 create_payment")
    print("=" * 50)

    # 测试成功场景
    result = create_payment.invoke({"order_id": 10086})
    print(f"创建支付链接成功: {result}")
    assert "paymentUrl" in result
    assert result["paymentUrl"] == "https://pay.demo/10086"

    # 测试订单不存在
    result = create_payment.invoke({"order_id": 999})
    print(f"订单不存在: {result}")
    assert "error" in result

    # 测试 send_email
    print("\n" + "=" * 50)
    print("测试 send_email")
    print("=" * 50)

    result = send_email.invoke({
        "email": "test@example.com",
        "content": "这是一封测试邮件"
    })
    print(f"发送邮件结果: {result}")
    assert result["success"] is True

    # 测试 cancel_order
    print("\n" + "=" * 50)
    print("测试 cancel_order")
    print("=" * 50)

    # 测试成功场景
    result = cancel_order.invoke({"order_id": 10086})
    print(f"取消订单成功: {result}")
    assert result["success"] is True

    # 测试订单不存在
    result = cancel_order.invoke({"order_id": 999})
    print(f"订单不存在: {result}")
    assert "error" in result

    print("\n" + "=" * 50)
    print("所有工具测试通过！")
    print("=" * 50)


if __name__ == "__main__":
    test_all_tools()