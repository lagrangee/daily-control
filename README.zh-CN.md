# Daily Control

[English](README.md) | 简体中文

本页是英文 canonical README 的完整中文版本；如果两者表述不一致，以英文版为准。

**让 AI Agent 帮你运行一天，但不在你不知情时接管优先级。**

Daily Control 是一个 agent-native、local-first 的控制循环，由日常对话和持久 Markdown 构成。Agent 帮你规划、核对事实证据、复盘并恢复上下文；优先级、约束、解释、权限和重要变更仍由你决定。

四条边界保证这种协作关系保持诚实：

- **Human Authority** — Agent 会把重要决定作为草案清楚展示，由你接受或修改。
- **Control Policy** — 你可以显式维护、检查并在当天临时覆盖可复用的规划约束。
- **Evidence 不是判断** — 外部来源的事实不会被自动解释成意图、生产力、质量、完成情况或健康状态。
- **Durable truth 优先** — Daily、Weekly、Area、Project、Routine 和 Evidence 记录是 canonical truth；`context/now.md` 只是可以重建的缓存。

## 快速开始

```text
你：/daily-control

Agent：当前目录不是 Daily Control Context Root。
       建议下一条 route：/daily-control setup

你：/daily-control setup

Agent：我可以创建新的 Markdown Context Root，或采用当前目录。
       写入前，我会预览所有文件和冲突。
```

Setup 完成后，同一个 bare command 只读取已确认的 Context Root，并建议一条下一步 route，不会自动执行：

```text
help
setup
open → refresh → shutdown
weekly-review
extend
```

“用 Daily Control 开始今天”这样的自然语言请求会选择同一条 route。`/daily-control <route>` 是推荐的显式写法，不是对某一种 Agent Surface 的依赖。

## 一眼看懂控制循环

下面是一个合成示例，其中的 Control Policy 是用户自己配置的；Daily Control 不提供默认限制。

```text
你：今天我想同时推进 Atlas、Billing 和 Launch。

Agent：你配置的 Policy 只允许一个 Primary Outcome，今天的 capacity
       约为四小时。把三个项目都放进今日计划会产生冲突。哪个结果优先？

你：Atlas 作为 Primary。Billing 移到明天，Launch 留在 backlog。

Agent：Open 草案：Atlas 是 Primary Outcome；Billing 是明天的 anchor；
       Launch 保留在 backlog。不需要 policy override。是否写入？

你：确认。稍后：/daily-control shutdown

Agent：来源 Evidence 显示 Atlas 有三小时 coding activity。这能证明活动，
       不能证明 Atlas 已经交付。你认为今天实际完成了什么？

你：核心流程已经能在本地运行，但还没有完成 review。

Agent：我会把这个结果、待完成的 review，以及 Billing 作为 next anchor
       写入今天的 durable Shutdown。是否确认？
```

Policy 负责暴露取舍，用户负责决定，Evidence 保持事实性；只有经过确认的判断才会成为持久历史。

## Truth flow

```text
                        USER AUTHORITY
                 priorities · policy · judgment
                              │
                              ▼
External Sources ──▶ Evidence ──▶ Durable Records ──▶ context/now.md
   rich truth        factual       canonical history     rebuildable cache
```

Daily Control 不是一个把活动转换成分数的 AI 日记，也不是另一个应用运行时。计划、有来源的 Evidence、人类解释和派生上下文始终彼此分离。它不需要 Daily Control app、CLI、数据库、后台调度器或 Obsidian 插件。

## 安装

使用开源 [`skills`](https://github.com/vercel-labs/skills) 安装器，从 GitHub 安装 standalone Skill：

```bash
npx skills add lagrangee/daily-control -g
```

Global 安装让这个 Skill 可以跨多个 Context Root 使用。如果你明确希望它只属于一个项目、并随该仓库共享，请省略 `-g`。

也可以把完整的 [`skills/daily-control`](skills/daily-control/) 文件夹复制到 Agent Surface 使用的 skills 目录。请保持文件夹完整：其中包含自己的 license、route 指引、contracts 和 scaffold assets，不依赖本仓库的 `docs/` 或 `extensions/`。

然后打开你希望作为 Context Root 的目录并执行：

```text
/daily-control setup
```

Skill 不会扫描你的电脑寻找其他 Context Root。Setup 可以创建新的 Context Root，也可以采用已有目录，同时保留其中的内容。

## 控制循环

```text
/daily-control help
/daily-control open
/daily-control refresh
/daily-control shutdown
/daily-control weekly-review
/daily-control extend
```

- **open** 在提交计划前检查当前 capacity 和已配置的 Control Policy。
- **refresh** 把已启用 Source 的事实整理为最小、有来源的 Evidence。
- **shutdown** 记录结果、偏移、学习和下一个 anchor，不把 Evidence 自动转换为判断。
- **weekly-review** 检查一个已结束的周期；只有经过单独确认，才会提交 policy 或优先级变更。
- **extend** 通过明确的 capability、权限、预览和启用边界接入新的 Evidence Source。

完整工作方式参见英文版 [GUIDE.md](GUIDE.md)。本页已经包含理解、安装和开始使用 Daily Control 所需的信息。

## 仓库结构

- [`skills/daily-control/`](skills/daily-control/) — 可独立安装的 Skill。
- [`docs/`](docs/) — 公开的产品、隐私、验收和 extension 文档；不是 Skill 的运行时依赖。
- [`extensions/`](extensions/) — 可选的 source integration 和贡献模板。
- [`examples/`](examples/) — 合成的 Context Root 示例。

## License

[MIT](LICENSE)
