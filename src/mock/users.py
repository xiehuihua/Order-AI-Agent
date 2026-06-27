"""
用户 Mock 数据模块
提供用户数据的模拟查询功能
"""
from typing import Dict, Any, Optional

# Mock 用户数据
MOCK_USERS: Dict[int, Dict[str, Any]] = {
    1: {
        "userId": 1,
        "name": "Tom",
        "email": "tom@test.com"
    }
}


def get_user_by_id(user_id: int) -> Optional[Dict[str, Any]]:
    """
    根据用户 ID 获取用户信息

    Args:
        user_id: 用户 ID

    Returns:
        用户信息字典，如果不存在返回 None
    """
    return MOCK_USERS.get(user_id)