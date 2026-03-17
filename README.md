# Datawhale Hello-Agents 学习打卡仓库

这是一个基于 Datawhale `Hello-Agents` 社群任务整理的非官方学习记录仓库模板。你可以直接基于它记录 `Task00 ~ Task06` 的学习过程、代码实践、问题排查、截图和心得总结，也可以把自己的大模型或 Agent 拉进来一起共学。

## 仓库定位

- 按社群任务拆分目录，降低自己重新整理结构的成本
- 提供统一的 `ToStudyList` 入口，方便持续打卡和后续复盘
- 适合作为个人学习仓库的起点，也方便后续整理成自己的学习作品集
- 重点是记录自己的理解与实践，而不是简单搬运教程正文

## 快速开始

1. 点击 GitHub 右上角的 `Use this template`
2. 新建你自己的学习仓库并 clone 到本地
3. 根据你所在期次的安排，修改 `学习计划.md` 和 `打卡总表.md`
4. 每完成一个任务，就补充对应目录下的 `ToStudyList.md` 和 `截图/`
5. 定期填写 `项目总结.md`，把阶段收获沉淀下来

## 推荐目录结构

```text
.
├── README.md
├── 学习计划.md
├── 打卡总表.md
├── 项目总结.md
├── Task00-环境配置/
│   ├── README.md
│   ├── ToStudyList.md
│   └── 截图/
├── Task01-第一章/
├── Task02-第二章/
├── Task03-第三章/
├── Task04-第四章/
├── Task05-第五章/
├── Task06-第六章/
└── hello-agents/          # 本地参考用，可不提交到自己的仓库
```

## 学习导航

| Task | 主题 | 任务说明 | ToStudyList |
|------|------|----------|-------------|
| Task00 | 环境配置与前言 | [README](./Task00-环境配置/README.md) | [ToStudyList](./Task00-环境配置/ToStudyList.md) |
| Task01 | 第一章 初识智能体 | [README](./Task01-第一章/README.md) | [ToStudyList](./Task01-第一章/ToStudyList.md) |
| Task02 | 第二章 智能体发展史 | [README](./Task02-第二章/README.md) | [ToStudyList](./Task02-第二章/ToStudyList.md) |
| Task03 | 第三章 大语言模型基础 | [README](./Task03-第三章/README.md) | [ToStudyList](./Task03-第三章/ToStudyList.md) |
| Task04 | 第四章 智能体经典范式构建 | [README](./Task04-第四章/README.md) | [ToStudyList](./Task04-第四章/ToStudyList.md) |
| Task05 | 第五章 基于低代码平台的智能体搭建 | [README](./Task05-第五章/README.md) | [ToStudyList](./Task05-第五章/ToStudyList.md) |
| Task06 | 第六章 框架应用开发实践 | [README](./Task06-第六章/README.md) | [ToStudyList](./Task06-第六章/ToStudyList.md) |

## 推荐共学方式

- 用你熟悉的大模型或 Agent 当作共学搭子，陪你一起拆解每个 Task
- 学习前，让它先帮你梳理任务顺序、关键概念和建议产出
- 学习中，让它根据 `ToStudyList` 追问你做到哪一步、卡在什么地方
- 学习后，让它帮你整理反馈、沉淀心得，并生成下一步计划
- 让模型辅助你学习，但不要跳过自己的动手实践和判断

## 建议记录内容

每个 Task 至少补齐下面几类信息：

1. `任务要求`：这一阶段需要完成什么
2. `学习输入`：读了哪些内容，看了哪些资料
3. `实践过程`：跑了什么代码，做了什么实验
4. `问题记录`：遇到了什么报错，怎么解决的
5. `学习心得`：自己的理解、收获和下一步计划

## 推荐使用方式

- 这个仓库更适合作为你的“学习仓库起点”
- 建议不要直接在公共模板仓库里写个人进度
- 更推荐新建自己的仓库后再持续填写内容
- 如果你有自己的大模型工作流，也可以把它和这个仓库配合使用
- 如果你优化了记录方式，也欢迎回到本仓库提 `issue` 或分享改进建议

## 提交建议

- 每个 Task 至少保留一次可追踪提交
- 截图建议统一放在对应任务目录下的 `截图/`
- 代码实践建议记录关键命令、运行结果和改动说明
- 不要提交 API Key、`.env`、本地虚拟环境等敏感或无关内容

## 参考资料

- 官方教程源码：<https://github.com/datawhalechina/hello-agents>
- 在线文档：<https://datawhalechina.github.io/hello-agents/>

## 可继续扩展

- 增加章节知识卡片
- 增加 demo 展示截图或录屏链接
- 增加阶段性总结和个人路线图
- 增加一个按顺序跟进学习进度、轮询追问并整理反馈的共学 skill
