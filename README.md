# Order AI Agent 开发步骤总览

## 项目概述

本项目旨在开发一个基于 LangGraph 的 ReAct 单 Agent 系统，能够理解用户自然语言指令，自主决策并执行多步任务。

## 开发步骤列表

本项目采用迭代开发模式，严格按照以下 11 个步骤逐步完成：

### 第一阶段：基础设施搭建

#### [步骤 001：环境搭建与项目初始化](task/001.md)
- **目标**: 搭建 Python 开发环境，创建项目基础目录结构
- **涉及规范**: architecture.md, development-guide.md, project-overview.md
- **关键任务**:
  - 创建项目目录结构
  - 初始化 Python 项目和虚拟环境
  - 安装依赖库（langgraph, langchain, langchain-openai, pydantic, python-dotenv）
  - 配置环境变量（.env）
  - 创建配置文件（config.py）
  - 创建日志配置模块

---

### 第二阶段：数据层开发

#### [步骤 002：Mock 数据层开发](task/002.md)
- **目标**: 实现订单、用户、库存三个 Mock 数据模块
- **涉及规范**: tools-design.md, development-guide.md, architecture.md
- **关键任务**:
  - 实现 mock/orders.py（订单数据）
  - 实现 mock/users.py（用户数据）
  - 实现 mock/inventory.py（库存数据）
  - 创建 Mock 数据初始化文件

---

### 第三阶段：工具层开发

#### [步骤 003：工具层开发（第一部分 - 查询工具）](task/003.md)
- **目标**: 实现三个查询工具（query_order, query_user, query_inventory）
- **涉及规范**: tools-design.md, development-guide.md, architecture.md
- **关键任务**:
  - 使用 @tool 装饰器实现查询工具
  - 添加完整的类型注解和文档字符串
  - 正确调用 Mock 数据层
  - 处理错误情况
  - 注册工具到 get_all_tools()

#### [步骤 004：工具层开发（第二部分 - 操作工具）](task/004.md)
- **目标**: 实现三个操作工具（create_payment, send_email, cancel_order）
- **涉及规范**: tools-design.md, development-guide.md, architecture.md
- **关键任务**:
  - 实现操作工具（create_payment, send_email, cancel_order）
  - 添加业务逻辑检查（订单状态验证）
  - 处理错误情况
  - 完成工具注册（共 6 个工具）

---

### 第四阶段：核心模块开发

#### [步骤 005：状态管理层开发](task/005.md)
- **目标**: 实现 AgentState 状态管理，定义 Agent 运行时状态结构
- **涉及规范**: state-design.md, development-guide.md, architecture.md
- **关键任务**:
  - 使用 TypedDict 定义 AgentState
  - 实现状态辅助函数（创建、更新、查询）
  - 确保状态更新的不可变性

#### [步骤 006：提示词配置开发](task/006.md)
- **目标**: 实现 System Prompt，引导 LLM 进行正确的 ReAct 推理
- **涉及规范**: prompt-design.md, development-guide.md, architecture.md
- **关键任务**:
  - 设计 System Prompt（角色、能力、原则、流程、规则）
  - 实现 get_system_prompt() 和 get_user_prompt()
  - 确保 Prompt 包含停止条件和重要规则

---

### 第五阶段：节点层开发

#### [步骤 007：Agent Node 开发](task/007.md)
- **目标**: 实现 Agent Node，负责调用 LLM、处理响应、判断是否需要工具调用
- **涉及规范**: graph-design.md, development-guide.md, architecture.md
- **关键任务**:
  - 初始化 LLM（使用 config.py 配置）
  - 绑定所有工具
  - 处理 System Prompt（首次调用时添加）
  - 调用 LLM API
  - 处理响应（包含 tool_calls）
  - 更新状态

#### [步骤 008：Tool Node 开发](task/008.md)
- **目标**: 实现 Tool Node，负责执行工具、处理结果、封装 ToolMessage
- **涉及规范**: graph-design.md, development-guide.md, architecture.md
- **关键任务**:
  - 获取工具调用列表
  - 建立工具映射
  - 执行工具调用
  - 处理执行错误
  - 封装 ToolMessage
  - 更新状态

---

### 第六阶段：编排层开发

#### [步骤 009：Graph 编排层开发](task/009.md)
- **目标**: 实现 Graph，定义 Agent 工作流，配置节点和条件边
- **涉及规范**: graph-design.md, development-guide.md, architecture.md
- **关键任务**:
  - 创建 StateGraph
  - 添加节点（agent, tools）
  - 设置入口点
  - 配置条件边（agent → should_continue → tools/end）
  - 配置普通边（tools → agent）
  - 编译工作流图

---

### 第七阶段：应用层开发

#### [步骤 010：应用入口开发](task/010.md)
- **目标**: 实现 app.py，提供用户交互界面，启动 Agent 工作流
- **涉及规范**: architecture.md, development-guide.md, test-cases.md
- **关键任务**:
  - 实现 run_agent() 函数
  - 实现 display_result() 函数
  - 实现交互模式（interactive_mode）
  - 实现单次运行模式（single_run_mode）
  - 实现主函数（main）

---

### 第八阶段：测试与验收

#### [步骤 011：集成测试与验收](task/011.md)
- **目标**: 进行全面测试，验证系统功能完整性和稳定性
- **涉及规范**: test-cases.md, development-guide.md, project-overview.md
- **关键任务**:
  - 运行所有测试案例（Case 1 - Case 5）
  - 验证功能验收标准
  - 验证性能验收标准
  - 验证代码质量验收标准
  - 输出测试报告

---

## 开发原则

### 1. 严格遵循步骤顺序
- 每个步骤都是在前一步骤的基础上进行
- 不要跳过任何步骤
- 每完成一个步骤，确保代码能运行并通过测试

### 2. 遵循规范文档
- 每个步骤都明确了要参考的规范文档
- 严格按照规范要求进行开发
- 不要偏离规范定义的设计原则

### 3. 单一职责原则
- 每个模块只负责一种功能
- Agent Node 只调用 LLM
- Tool Node 只执行工具
- Graph 只定义流程

### 4. Clean Architecture
- 高内聚、低耦合
- 模块职责清晰
- 易于维护和扩展

### 5. 类型安全
- 所有函数都有类型注解
- 使用 TypedDict 定义结构
- 遵循 PEP8 编码规范

### 6. 日志规范
- 所有关键步骤都有日志输出
- 日志内容清晰易懂
- 使用中文日志内容

---

## 项目验收标准

### 功能验收
- ✅ 所有工具能正确调用
- ✅ Agent 能正确推理
- ✅ 最终答案准确
- ✅ 工具调用顺序正确
- ✅ 条件判断正确

### 性能验收
- ✅ 单个工具调用 < 1秒
- ✅ 完整流程 < 30秒
- ✅ 无无限循环
- ✅ 无内存泄漏

### 代码质量验收
- ✅ 类型注解完整
- ✅ 日志输出清晰
- ✅ 代码结构清晰
- ✅ 模块职责明确
- ✅ 遵循 PEP8 规范

---

## 测试案例（5 个）

| Case | 描述 | 工具调用次数 | 预期工具 |
|------|------|------------|---------|
| Case 1 | 查询订单 | 1 | query_order |
| Case 2 | 查询订单并生成支付链接 | 2 | query_order, create_payment |
| Case 3 | 查询订单、检查库存、取消订单 | 3 | query_order, query_inventory, cancel_order |
| Case 4 | 查询订单、检查库存、生成支付、发送邮件 | 5 | query_order, query_inventory, create_payment, query_user, send_email |
| Case 5 | 完整业务流程 | 5+ | 完整工具调用链 |

---

## 后续扩展方向

完成本项目后，可考虑扩展：

1. **Memory 持久化** - 添加对话历史记忆
2. **Checkpoint** - 添加检查点机制
3. **SQLite/Redis** - 替换 Mock 数据
4. **RAG** - 添加知识库检索
5. **Streaming** - 实现流式输出
6. **Human In The Loop** - 添加人工审核
7. **Multi-Agent** - 扩展为多智能体系统

---

## 技术栈

- Python 3.12+
- LangGraph（工作流编排）
- LangChain（LLM 应用框架）
- langchain-openai（OpenAI 集成）
- Pydantic（数据验证）
- python-dotenv（环境变量管理）
- OpenAI Compatible API

---

## 开发团队

本项目由资深 Python AI 工程师开发，遵循生产级代码质量标准。

---

**开始开发：请从 [步骤 001：环境搭建与项目初始化](task/001.md) 开始**