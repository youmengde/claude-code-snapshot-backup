# Claude Code Source Snapshot - TypeScript Version

> **⚠️ 注意**：本仓库是从 [instructkr/claude-code](https://github.com/instructkr/claude-code) 备份的 **TypeScript 源码版本**。
> 
> 原始仓库在 2026-03-31 之后已变更为 Python 移植版本，本仓库保留了 **原始 TypeScript 源码快照**。

---

## 仓库来源

- **原始仓库**: [instructkr/claude-code](https://github.com/instructkr/claude-code)
- **备份时间**: 2026-03-31
- **源码类型**: TypeScript (Bun 运行时)
- **文件数量**: 1,902 个文件
- **代码行数**: 513,517 行

## 来源说明

> This repository mirrors a **publicly exposed Claude Code source snapshot** that became accessible on **March 31, 2026** through a source map exposure in the npm distribution. It is maintained for **educational, defensive security research, and software supply-chain analysis**.

## 源码概述

本备份包含 Claude Code 的完整 TypeScript 源码，涵盖：

| 目录 | 说明 |
|------|------|
| `src/assistant/` | AI助手核心模块 |
| `src/bootstrap/` | 启动引导模块 |
| `src/bridge/` | 桥接模块 |
| `src/cli/` | 命令行接口 |
| `src/commands/` | 101个斜杠命令 |
| `src/components/` | React组件 |
| `src/coordinator/` | 多Agent协调器 |
| `src/hooks/` | React钩子 |
| `src/ink/` | Ink CLI框架 |
| `src/server/` | 服务器模块 |
| `src/services/` | 服务模块 |
| `src/skills/` | 技能系统 |
| `src/state/` | 状态管理 |
| `src/tasks/` | 任务管理 |
| `src/tools/` | 工具注册表 |
| `src/types/` | TypeScript类型定义 |
| `src/utils/` | 工具函数 |
| `src/voice/` | 语音模块 |

## 关键文件

- `src/main.tsx` - 主入口文件 (803KB)
- `src/QueryEngine.ts` - 查询引擎
- `src/query.ts` - 查询模块 (68KB)
- `src/Tool.ts` - 工具基类
- `src/Task.ts` - 任务基类
- `src/commands.ts` - 命令定义 (25KB)
- `src/tools.ts` - 工具定义

## 重要说明

1. **本仓库仅用于研究和学习目的**
2. **Claude Code 是 Anthropic 的商业产品**，本源码是通过非正常渠道获取的泄露版本
3. **请勿用于商业目的或侵犯版权**

## 研究价值

通过分析此源码，可以了解：

- AI Agent 的架构设计
- 多Agent协调机制 (Coordinator + Worker Pool)
- 工具注册和调用系统
- 斜杠命令的实现方式
- 与大语言模型的交互方式

---

**备份日期**: 2026-03-31  
**备份工具**: OpenClaw AI Agent
