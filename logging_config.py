"""
日志配置模块
提供统一的日志配置功能
"""
import logging
import sys
from typing import Optional


def setup_logging(level: Optional[int] = logging.INFO) -> None:
    """
    配置日志系统

    Args:
        level: 日志级别，默认为 INFO
    """
    logging.basicConfig(
        level=level,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.StreamHandler(sys.stdout)
        ]
    )


def get_logger(name: str) -> logging.Logger:
    """
    获取日志记录器

    Args:
        name: 日志记录器名称

    Returns:
        Logger 实例
    """
    return logging.getLogger(name)