"""查询订单工具"""
import logging
from typing import Dict, Any
from langchain_core.tools import tool

from src.mock.orders import get_order_by_id

logger = logging.getLogger(__name__)


@tool
def query_order(order_id: int) -> Dict[str, Any]:
    """
    根据订单 ID 查询订单详细信息

    Args:
        order_id: 订单 ID，整数类型

    Returns:
        订单信息字典，包含 orderId, status, userId, productId
        如果订单不存在，返回错误信息
    """
    logger.info(f"调用工具 query_order，参数: order_id={order_id}")

    order = get_order_by_id(order_id)

    if order is None:
        result = {"error": f"订单 {order_id} 不存在"}
        logger.warning(f"查询结果: {result}")
        return result

    logger.info(f"查询成功: {order}")
    return order