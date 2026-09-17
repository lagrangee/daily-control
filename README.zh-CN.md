# Daily Control

[English](README.md) | 简体中文

中英文内容如有出入，以英文 README 为准。

**让 Agent 真正帮你推进一天，但不替你决定什么重要。**

Daily Control 不是一个新的日程 App，而是一套让 Agent 围绕你自己的 Markdown 文件工作的日常控制方法。在你明确调用后，它先观察已有上下文，和你讨论判断与方向，需要时再做计划，并在收工时留下能继续接手的上下文；优先级怎么排、证据意味着什么、哪些内容可以写入，始终由你决定。

它刻意守住四条边界：

- **人来做主**：重要决定先作为草案摆出来，由你确认或修改。
- **约束写在明处**：Control Policy 保存你长期采用的工作边界；当天可以破例，但必须说清楚。
- **证据只讲事实**：Evidence 可以说明发生了什么，不能替你判断是否有效、是否完成、做得好不好。
- **长期记录才是事实源**：Daily、Weekly、Area、Project、Routine 和 Evidence 是可追溯的长期记录；`context/now.md` 只是随时可以重建的当前摘要。

## 一分钟看懂它的价值

下面只是一个示例。里面“一天只保留一个主目标”的规则来自用户自己的 Control Policy，不是 Daily Control 的默认设置。

```text
你：/daily-control open，今天想同时推进 Atlas、Billing 和 Launch。

Agent：你给自己定的规则是一天只保留一个 Primary Outcome，
       今天大约有四小时。三个项目一起排会超出这个边界。
       你想把哪个放在最前面？

你：Atlas。Billing 放到明天，Launch 先留在 backlog。

Agent：那今天的主目标是 Atlas；Billing 是明天的起点；Launch 暂不进入计划。
       这次不需要临时 override。你已经明确选择，我会据此写入今天的 Open。

你：到了晚上：/daily-control shutdown

Agent：收尾草案：今天的方向是 Atlas；已存 Evidence 记录了三小时 coding
       activity，但交付状态未知。Billing 仍是已定的下一步起点。
       有没有需要补充的重要结果？

你：核心流程已经能在本地跑通，但还没完成 review。

Agent：我会记录你报告的本地结果和待完成的 review，保留已定的 Billing 起点，
       写进今天的 Shutdown。
```

这就是 Daily Control 的核心：Policy 负责暴露取舍，你负责决定；Evidence 保持诚实，经过确认的判断才进入长期记录。

Open 也可以停在判断或方向，不必产出任务：

```text
你：/daily-control open，旅行回来后，我还没想清楚 Atlas 是否该继续。

Agent：上次 Shutdown 留下了验收标准分歧。所读两份记录中的阅读 Evidence
       增加了，但项目活动的覆盖缺失，不能据此判断原因。
       验收分歧现在仍是让下一步不明确的关键吗？

你：是的。今天先重新理解这些标准，不承诺执行任务。

Agent：我会把这个选择和仍未解决的问题写进 Open。
```

稳定的一天可以沿用已有方向，不需要重新填写签到表或改写记录；中断后从现状接上，不补写错过的日记。Context Root 的 `AGENTS.md` 可选配置 Controller Style，表达讨论和挑战偏好；它与 Control Policy 中的计划约束分开。

## 快速开始

先把 Skill 安装到全局位置，这样可以在不同的 Context Root 中使用：

```bash
npx skills add lagrangee/daily-control -g
```

如果你希望它只属于当前项目，并随项目仓库一起共享，可以省略 `-g`。

你也可以直接把完整的 [`skills/daily-control`](skills/daily-control/) 文件夹复制到 Agent 使用的 skills 目录。不要只复制 `SKILL.md`：route、contract、scaffold 和 license 都包含在这个文件夹里，安装后的 Skill 不依赖本仓库的 `docs/` 或 `extensions/`。

接着，打开你准备用来保存 Daily Control 内容的目录：

```text
/daily-control setup
```

Setup 可以创建一个新的 Context Root，也可以采用已有目录。真正写入前，Agent 会先展示将要新增的文件和可能发生的冲突；已有内容不会被静默覆盖。

Setup 成功后，默认 Context Root 会保存在 `~/.daily-control/config.md`。以后换到其他工作目录，也可以直接调用。Agent 依次使用本次明确指定的路径、保存的默认路径；没有配置时，才检查当前目录。路径有效就直接使用，无需再次确认；路径或配置失效时会提示修复，不会悄悄换目录。临时指定另一处路径不会改变默认值；想更换默认值，直接要求 Agent 记住新的 Context Root 即可。

不同 Agent 只要能加载 Skill，并能访问同一个用户主目录和 Context Root，就能共享这个默认值。云端或隔离环境仍需要配置可访问的路径或挂载目录，保存路径本身不会授予访问权限。

如果你还没有 Context Root，直接输入 `/daily-control` 也可以：

```text
你：/daily-control

Agent：还没有保存默认 Context Root，当前目录也不是。
       建议下一步：/daily-control setup
```

普通项目讨论不会自动启动 Daily Control。Setup 完成后，`/daily-control` 会根据当天的长期记录给出一条下一步建议，但不会替你执行。自然语言也可以，例如“用 Daily Control 帮我开始今天”。`/daily-control <route>` 只是推荐的明确写法，不绑定某一种 Agent。

## 日常怎么用

```text
/daily-control open
/daily-control refresh
/daily-control shutdown
/daily-control weekly-review
/daily-control extend
```

- **open**：先读已有上下文，再讨论当前判断与方向；计划有用时才做计划，并检查 Control Policy。没有新的长期信息，可以不写记录。
- **refresh**：从已经启用的 Source 获取事实，写成带来源的最小 Evidence。
- **shutdown**：先从已有记录起草收尾，只问重要缺口或修正；判断或恢复也能收尾，不必交出任务结果。新提出的重要解释或后续承诺需要确认。
- **weekly-review**：回看一个已经结束的周期，有依据时也讨论控制循环本身是否有用；长期 Policy、优先级或 Controller Style 变更需要单独确认。
- **extend**：接入新的 Evidence Source；先确认用途和权限，再验证样本、预览写入，最后决定是否启用。

`/daily-control help` 或单独输入 `/daily-control` 可以查看 route 摘要。Agent 最多建议一条下一步 route，不会自动运行。

## 信息是怎么流动的

```text
                         HUMAN AUTHORITY
                     优先级 · Policy · 判断
                                │
                                ▼
外部 Source ──▶ Evidence ──▶ 长期记录 ──▶ context/now.md
  丰富事实       只陈述事实       事实源          可重建摘要
```

计划、外部事实、人的解释和当前摘要各有自己的位置。Daily Control 不需要专用 App、CLI、数据库、后台任务或 Obsidian 插件；同步与备份方式也由你自己选择。

## Source 怎么变成 Evidence

Daily Control 会先问“做判断需要什么事实”，再问“去哪里拿这个事实”。这两件事不会混在一起：

- **Evidence Capability** 说明需要哪一类事实，例如活动记录、设备使用时间或阅读记录。
- **Source Adapter** 是获取这类事实的具体办法，可以是人工观察、Agent 已有的工具、外部 Skill，或单独安装的配套 Skill。
- **Source Contract** 是这条接入路径的边界说明。它用普通 Markdown 写清权限、读取范围、允许写入的位置、来源、已知限制，以及当前是否启用。

```text
需要的事实 ──▶ Capability ──▶ Adapter ──▶ 尚未启用的 Source Contract
                                                │
                                      验证样本 · 预览写入 · 用户接受
                                                │
                                                ▼
                                        refresh ──▶ Daily Evidence
```

`/daily-control extend` 会先建立一个禁用状态的 Source Contract，再验证代表性结果、展示准备写入的最小内容，最后由你决定是否启用。`/daily-control refresh` 只读取已经启用的 Source，并如实保留 `complete`、`partial`、`unavailable` 或 `failed` 状态。

凭据、原始 API 响应、完整历史和高频数据继续留在原来的 Source。Context Root 只保存当前决策真正需要的少量事实和出处。

### 仓库已经提供的 Extensions

| Extension | Capability | 接入方式 | 当前状态 |
| --- | --- | --- | --- |
| [Codex Computer History](extensions/codex-computer-history/) | `activity-history` | 外部 Skill | Reference-only |
| [macOS Screen Time](extensions/mac-screen-time/) | `device-usage` | 人工观察或 Agent 已有工具 | Reference-only |
| [WeRead](extensions/weread/) | `reading-history` | 外部 Skill | Reference-only |

这里的 `Reference-only` 表示仓库已经给出接入边界、Evidence 写法和验收步骤，但它不是一个已经自动启用、在所有 Agent 上都验证过的 connector。核心 `extend` route 不依赖这份目录，也可以接入用户指定的其他 Source。详细说明和贡献规则见 [Extension 文档](docs/extensions.md)。

## 仓库里有什么

- [`skills/daily-control/`](skills/daily-control/)：可以独立安装的 Skill。
- [`docs/`](docs/)：产品、隐私、验收和 extension 文档；不是 Skill 的运行时依赖。
- [`extensions/`](extensions/)：可选的 Source 接入示例和贡献模板。
- [`examples/`](examples/)：使用合成内容制作的 Context Root 示例。

更多细节见英文版 [GUIDE.md](GUIDE.md)。本页已经包含理解、安装和开始使用 Daily Control 所需的全部信息。

## License

[MIT](LICENSE)
