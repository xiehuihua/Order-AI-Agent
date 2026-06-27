"""测试查询工具模块"""
import sys
from pathlib import Path

# 添加项目根目录到 Python 路径
sys.path.insert(0, str(Path(__file__).parent))

from src.tools import query_order, query_user, query_inventory, get_all_tools

def test_query_tools():
    """测试所有查询工具"""
    print("=" * 50)
    print("测试查询工具")
    print("=" * 50)

    # 测试 query_order
    print("\n1. 测试 query_order")
    result = query_order.invoke({"order_id": 10086})
    print(f"结果: {result}")
    assert "orderId" in result
    assert result["orderId"] == 10086

    result_error = query_order.invoke({"order_id": 999})
    print(f"错误测试结果: {result_error}")
    assert "error" in result_error

    # 测试 query_user
    print("\n2. 测试 query_user")
    result = query_user.invoke({"user_id": 1})
    print(f"结果: {result}")
    assert "userId" in result
    assert result["userId"] == 1

    result_error = query_user.invoke({"user_id": 999})
    print(f"错误测试结果: {result_error}")
    assert "error" in result_error

    # 测试 query_inventory
    print("\n3. 测试 query_inventory")
    result = query_inventory.invoke({"product_id": 101})
    print(f"结果: {result}")
    assert "productId" in result
    assert result["productId"] == 101

    result_error = query_inventory.invoke({"product_id": 999})
    print(f"错误测试结果: {result_error}")
    assert "error" in result_error

    # 测试工具注册
    print("\n4. 测试工具注册")
    tools = get_all_tools()
    print(f"已注册工具数量: {len(tools)}")
    assert len(tools) == 3

    for tool in tools:
        print(f"  - {tool.name}: {tool.description}")

    print("\n" + "=" * 50)
    print("所有测试通过！")
    print("=" * 50)

if __name__ == "__main__":
    test_query_tools()