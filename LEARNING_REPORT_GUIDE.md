# 三海一核·智能调研 Agent（3-Sea-1-Nuclear Research Agent）：学习与报告提纲

## 项目定位

三海一核·智能调研 Agent 是基于 GPT Researcher 的场景化学习项目。它把通用网络调研流程收敛为**船海核（船舶工程 / 海洋工程 / 核能应用）领域研究**：输入一个问题、技术领域、研究对象/平台类型、规范区域和分析重点，生成带来源引用、区分事实与推断、默认中文的研究报告。

上游项目：https://github.com/assafelovic/gpt-researcher  
上游许可证：MIT（上游 GPT Researcher）。本仓库保留上游版权与许可证，并注明自己的改动。

## 本次改动

- 将首页改为中文船海核研究入口。
- 增加技术领域（综合 / 船舶工程 / 海洋工程 / 核能应用）、研究对象·平台类型、规范/法规区域、分析重点输入。
- 后端把用户上下文转为船海核研究约束（`backend/server/maritime_nuclear.py` 的 `build_maritime_nuclear_task`），要求优先引用监管机构/船级社/论文/官方文档、比较至少两个方案、逐条标注来源、区分事实/推断/不确定性、不编造安全裕度/概率、不给核安全绕过指引。
- 增加纯单元测试覆盖任务构造、三领域关键词与空问题校验。

## 推荐学习路径

1. 看 `frontend/index.html` 和 `frontend/scripts.js`：理解输入、WebSocket 请求与进度展示。
2. 看 `backend/server/server_utils.py`：理解消息解析和任务调度（`extract_command_data` / `handle_start_command`）。
3. 看 `backend/server/maritime_nuclear.py`：理解船海核领域任务构造与安全约束。
4. 看 `backend/server/websocket_manager.py` 与 `gpt_researcher/agent.py`：理解 Agent 调用、研究执行和结果回传。
5. 看 `gpt_researcher/actions/` 和 `gpt_researcher/prompts.py`：理解检索、上下文整理和报告生成。
6. 跑 `tests/test_maritime_nuclear_task.py`，再用 mock 或录制样本验证来源不足、规范冲突等边界情况。

## 可继续完成的学习实验

- 对技术方案建立明确的评估维度（如安全性、成熟度、合规性）和可配置权重，并对评估分数做单元测试。
- 增加规范/来源的证据卡片，让结论能回溯到原始规范或论文页面。
- 给报告增加 Markdown 导出与固定结构校验。
- 用一组固定船海核问题建立评测集，检查来源覆盖率、事实可追溯率和结论稳定性。

## 运行提示

在 PowerShell 中可按以下步骤启动：

```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
Copy-Item .env.example .env
# 在 .env 中填写模型和网页搜索服务密钥
python main.py
```

然后访问 `http://localhost:8000`。在线调研需要可用的模型与搜索服务密钥；依赖未安装、密钥未配置时，Agent 无法实际完成在线分析。单元测试无需密钥：`python -m pytest tests/test_maritime_nuclear_task.py -v`。
