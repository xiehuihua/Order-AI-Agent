"""
库存 Mock 数据模块
提供库存数据的模拟查询功能
"""
from typing import Dict, Any, Optional

# Mock 库存数据
MOCK_INVENTORY: Dict[int, Dict[str, Any]] = {
    101: {
        "productId": 101,
        "stock": 20
    }
}


def get_inventory_by_product_id(product_id: int) -> Optional[Dict[str, Any]]:
    """
    根据商品 ID 获取库存信息

    Args:
        product_id: 商品 ID

    Returns:
        库存信息字典，如果不存在返回 None
    """
    return MOCK_INVENTORY.get(product_id)