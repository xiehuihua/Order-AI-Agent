"""工具模块注册"""
from typing import List
from langchain_core.tools import Tool

from .query_order import query_order
from .query_user import query_user
from .query_inventory import query_inventory
from .create_payment import create_payment
from .send_email import send_email
from .cancel_order import cancel_order

__all__ = [
    "query_order",
    "query_user",
    "query_inventory",
    "create_payment",
    "send_email",
    "cancel_order",
    "get_all_tools"
]


def get_all_tools() -> List[Tool]:
    """
    获取所有工具列表

    Returns:
        所有注册的工具列表（查询工具 + 操作工具）
    """
    return [
        # 查询工具
        query_order,
        query_user,
        query_inventory,
        # 操作工具
        create_payment,
        send_email,
        cancel_order
    ]