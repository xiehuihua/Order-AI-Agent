"""
Mock 数据模块
提供订单、用户、库存的模拟数据查询功能
"""
from .orders import get_order_by_id, MOCK_ORDERS
from .users import get_user_by_id, MOCK_USERS
from .inventory import get_inventory_by_product_id, MOCK_INVENTORY

__all__ = [
    "get_order_by_id",
    "MOCK_ORDERS",
    "get_user_by_id",
    "MOCK_USERS",
    "get_inventory_by_product_id",
    "MOCK_INVENTORY"
]