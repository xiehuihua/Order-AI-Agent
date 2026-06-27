"""工具模块注册"""
from typing import List
from langchain_core.tools import Tool

from .query_order import query_order
from .query_user import query_user
from .query_inventory import query_inventory

__all__ = [
    "query_order",
    "query_user",
    "query_inventory",
    "get_all_tools"
]


def get_all_tools() -> List[Tool]:
    """
    获取所有工具列表

    Returns:
        所有注册的工具列表
    """
    return [
        query_order,
        query_user,
        query_inventory
    ]