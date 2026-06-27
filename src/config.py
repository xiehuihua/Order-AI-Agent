"""
配置管理模块
负责读取和管理环境变量配置
"""
import os
from dotenv import load_dotenv

# 加载 .env 文件
load_dotenv()

# API 配置
OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")
OPENAI_API_BASE: str = os.getenv("OPENAI_API_BASE", "https://api.openai.com/v1")
MODEL_NAME: str = os.getenv("MODEL_NAME", "gpt-4")


def validate_config() -> None:
    """
    验证配置是否正确

    Raises:
        ValueError: 当必需的配置项缺失时抛出
    """
    if not OPENAI_API_KEY:
        raise ValueError("OPENAI_API_KEY 未配置，请在 .env 文件中设置")