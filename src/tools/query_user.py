"""查询用户工具"""
import logging
from typing import Dict, Any
from langchain_core.tools import tool

from src.mock.users import get_user_by_id

logger = logging.getLogger(__name__)


@tool
def query_user(user_id: int) -> Dict[str, Any]:
    """
    根据用户 ID 查询用户详细信息

    Args:
        user_id: 用户 ID，整数类型

    Returns:
        用户信息字典，包含 userId, name, email
        如果用户不存在，返回错误信息
    """
    logger.info(f"调用工具 query_user，参数: user_id={user_id}")

    user = get_user_by_id(user_id)

    if user is None:
        result = {"error": f"用户 {user_id} 不存在"}
        logger.warning(f"查询结果: {result}")
        return result

    logger.info(f"查询成功: {user}")
    return user