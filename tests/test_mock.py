"""
测试 Mock 数据模块
验证订单、用户、库存 Mock 数据功能是否正常
"""
from src.mock import get_order_by_id, get_user_by_id, get_inventory_by_product_id


def test_mock_data():
    """测试所有 Mock 数据获取函数"""
    # 测试订单数据
    order = get_order_by_id(10086)
    assert order is not None, "订单数据不应为 None"
    assert order["orderId"] == 10086, f"订单 ID 应为 10086，实际为 {order['orderId']}"
    assert order["status"] == "UNPAID", f"订单状态应为 UNPAID，实际为 {order['status']}"
    print(f"[PASS] 订单数据测试通过: {order}")

    # 测试用户数据
    user = get_user_by_id(1)
    assert user is not None, "用户数据不应为 None"
    assert user["userId"] == 1, f"用户 ID 应为 1，实际为 {user['userId']}"
    assert user["email"] == "tom@test.com", f"用户邮箱应为 tom@test.com，实际为 {user['email']}"
    print(f"[PASS] 用户数据测试通过: {user}")

    # 测试库存数据
    inventory = get_inventory_by_product_id(101)
    assert inventory is not None, "库存数据不应为 None"
    assert inventory["productId"] == 101, f"商品 ID 应为 101，实际为 {inventory['productId']}"
    assert inventory["stock"] == 20, f"库存应为 20，实际为 {inventory['stock']}"
    print(f"[PASS] 库存数据测试通过: {inventory}")

    # 测试不存在的数据
    assert get_order_by_id(999) is None, "不存在的订单应返回 None"
    assert get_user_by_id(999) is None, "不存在的用户应返回 None"
    assert get_inventory_by_product_id(999) is None, "不存在的商品库存应返回 None"
    print("[PASS] 不存在数据测试通过")

    print("\n所有 Mock 数据测试通过！")


if __name__ == "__main__":
    test_mock_data()