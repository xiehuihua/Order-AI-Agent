"""查询库存工具"""
import logging
from typing import Dict, Any
from langchain_core.tools import tool

from src.mock.inventory import get_inventory_by_product_id

logger = logging.getLogger(__name__)


@tool
def query_inventory(product_id: int) -> Dict[str, Any]:
    """
    根据商品 ID 查询库存信息

    Args:
        product_id: 商品 ID，整数类型

    Returns:
        库存信息字典，包含 productId, stock
        如果商品不存在，返回错误信息
    """
    logger.info(f"调用工具 query_inventory，参数: product_id={product_id}")

    inventory = get_inventory_by_product_id(product_id)

    if inventory is None:
        result = {"error": f"商品 {product_id} 不存在"}
        logger.warning(f"查询结果: {result}")
        return result

    logger.info(f"查询成功: {inventory}")
    return inventory