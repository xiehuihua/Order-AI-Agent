"""
订单 Mock 数据模块
提供订单数据的模拟查询功能
"""
from typing import Dict, Any, Optional

# Mock 订单数据
MOCK_ORDERS: Dict[int, Dict[str, Any]] = {
    10086: {
        "orderId": 10086,
        "status": "UNPAID",
        "userId": 1,
        "productId": 101
    },
    20087: {
        "orderId": 20087,
        "status": "UNPAID",
        "userId": 1,
        "productId": 102
    }
}


def get_order_by_id(order_id: int) -> Optional[Dict[str, Any]]:
    """
    根据订单 ID 获取订单信息

    Args:
        order_id: 订单 ID

    Returns:
        订单信息字典，如果不存在返回 None
    """
    return MOCK_ORDERS.get(order_id)