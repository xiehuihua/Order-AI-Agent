"""发送邮件工具"""
import logging
from typing import Dict, Any
from langchain_core.tools import tool

logger = logging.getLogger(__name__)


@tool
def send_email(email: str, content: str) -> Dict[str, Any]:
    """
    向指定邮箱发送邮件

    Args:
        email: 收件人邮箱地址
        content: 邮件内容

    Returns:
        发送结果字典，包含 success 字段
    """
    logger.info(f"调用工具 send_email，参数: email={email}, content_length={len(content)}")

    # 模拟发送邮件
    # 实际项目中这里会调用真实的邮件发送服务
    result = {"success": True}

    logger.info(f"邮件发送成功: {email}")
    return result