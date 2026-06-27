"""创建支付工具"""
import logging
from typing import Dict, Any
from langchain_core.tools import tool

from src.mock.orders import get_order_by_id

logger = logging.getLogger(__name__)


@tool
def create_payment(order_id: int) -> Dict[str, Any]:
    """
    为指定订单创建支付链接

    Args:
        order_id: 订单 ID，整数类型

    Returns:
        支付信息字典，包含 paymentUrl
        如果订单不存在或状态不正确，返回错误信息
    """
    logger.info(f"调用工具 create_payment，参数: order_id={order_id}")

    # 检查订单是否存在
    order = get_order_by_id(order_id)

    if order is None:
        result = {"error": f"订单 {order_id} 不存在"}
        logger.warning(f"创建支付失败: {result}")
        return result

    # 检查订单状态
    if order["status"] != "UNPAID":
        result = {"error": f"订单 {order_id} 状态不是未付款，无法创建支付链接"}
        logger.warning(f"创建支付失败: {result}")
        return result

    # 创建支付链接
    payment_url = f"https://pay.demo/{order_id}"
    result = {"paymentUrl": payment_url}

    logger.info(f"创建支付成功: {result}")
    return result