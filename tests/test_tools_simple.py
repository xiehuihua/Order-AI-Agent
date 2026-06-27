"""简单验证工具功能"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))

from src.tools import query_order, query_user, query_inventory

# 直接调用工具函数
print("=" * 60)
print("直接测试工具功能")
print("=" * 60)

# 测试1：查询存在的订单
print("\n[测试1] 查询订单 10086")
result = query_order.invoke({"order_id": 10086})
print(f"结果: {result}")
assert result["orderId"] == 10086
print("PASS")

# 测试2：查询不存在的订单
print("\n[测试2] 查询不存在的订单 999")
result = query_order.invoke({"order_id": 999})
print(f"结果: {result}")
assert "error" in result
print("PASS")

# 测试3：查询存在的用户
print("\n[测试3] 查询用户 1")
result = query_user.invoke({"user_id": 1})
print(f"结果: {result}")
assert result["userId"] == 1
print("PASS")

# 测试4：查询不存在的用户
print("\n[测试4] 查询不存在的用户 999")
result = query_user.invoke({"user_id": 999})
print(f"结果: {result}")
assert "error" in result
print("PASS")

# 测试5：查询存在的库存
print("\n[测试5] 查询商品 101")
result = query_inventory.invoke({"product_id": 101})
print(f"结果: {result}")
assert result["productId"] == 101
print("PASS")

# 测试6：查询不存在的库存
print("\n[测试6] 查询不存在的商品 999")
result = query_inventory.invoke({"product_id": 999})
print(f"结果: {result}")
assert "error" in result
print("PASS")

print("\n" + "=" * 60)
print("所有功能测试通过！")
print("=" * 60)