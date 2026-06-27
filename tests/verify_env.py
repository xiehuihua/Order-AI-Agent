"""
环境验证脚本
验证所有依赖是否正确安装
"""
import sys
import io

# 设置 UTF-8 编码输出
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def test_imports() -> None:
    """测试所有必要的库是否能正确导入"""
    print("开始验证依赖安装...")
    print("-" * 50)
    
    libraries = [
        ("langgraph", "LangGraph"),
        ("langchain", "LangChain"),
        ("langchain_openai", "LangChain OpenAI"),
        ("pydantic", "Pydantic"),
        ("dotenv", "Python Dotenv")
    ]
    
    failed = []
    
    for module_name, display_name in libraries:
        try:
            __import__(module_name)
            print(f"✓ {display_name:<20} 导入成功")
        except ImportError as e:
            print(f"✗ {display_name:<20} 导入失败: {e}")
            failed.append(display_name)
    
    print("-" * 50)
    
    if failed:
        print(f"\n❌ 验证失败，以下库未能正确导入: {', '.join(failed)}")
        sys.exit(1)
    else:
        print("\n✅ 所有依赖安装成功！")


def test_config() -> None:
    """测试配置模块"""
    print("\n开始验证配置模块...")
    print("-" * 50)
    
    try:
        from src.config import OPENAI_API_KEY, OPENAI_API_BASE, MODEL_NAME, validate_config
        print(f"✓ 配置模块加载成功")
        print(f"  - OPENAI_API_BASE: {OPENAI_API_BASE}")
        print(f"  - MODEL_NAME: {MODEL_NAME}")
        
        if OPENAI_API_KEY and OPENAI_API_KEY != "your_api_key_here":
            print(f"  - OPENAI_API_KEY: {'*' * 10}{OPENAI_API_KEY[-5:]}")
        else:
            print(f"  - OPENAI_API_KEY: 未配置（需要在 .env 文件中设置）")
        
        print("-" * 50)
        print("✅ 配置模块验证成功！")
        
    except Exception as e:
        print(f"❌ 配置模块验证失败: {e}")
        sys.exit(1)


def test_logging() -> None:
    """测试日志模块"""
    print("\n开始验证日志模块...")
    print("-" * 50)
    
    try:
        from logging_config import setup_logging, get_logger
        setup_logging()
        logger = get_logger(__name__)
        logger.info("日志系统测试成功")
        print("-" * 50)
        print("✅ 日志模块验证成功！")
        
    except Exception as e:
        print(f"❌ 日志模块验证失败: {e}")
        sys.exit(1)


if __name__ == "__main__":
    print("=" * 50)
    print("Order AI Agent 环境验证")
    print("=" * 50)
    
    test_imports()
    test_config()
    test_logging()
    
    print("\n" + "=" * 50)
    print("🎉 所有验证通过！环境配置完成。")
    print("=" * 50)