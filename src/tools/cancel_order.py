"""取消订单工具"""
import logging
from typing import Dict, Any
from langchain_core.tools import tool

from src.mock.orders import get_order_by_id

logger = logging.getLogger(__name__)


@tool
def cancel_order(order_id: int) -> Dict[str, Any]:
    """
    取消指定订单

    Args:
        order_id: 订单 ID，整数类型

    Returns:
        取消结果字典，包含 success 字段
    """
    logger.info(f"调用工具 cancel_order，参数: order_id={order_id}")

    # 检查订单是否存在
    order = get_order_by_id(order_id)

    if order is None:
        result = {"error": f"订单 {order_id} 不存在"}
        logger.warning(f"取消订单失败: {result}")
        return result

    # 模拟取消订单
    result = {"success": True}

    logger.info(f"订单取消成功: order_id={order_id}")
    return result