import { useEffect, useMemo, useState } from "react";
import {
  ArrowsSplit,
  BracketsCurly,
  ChartLineUp,
  CheckCircle,
  ClipboardText,
  Compass,
  Database,
  FileMagnifyingGlass,
  FlowArrow,
  Graph,
  HouseLine,
  MapTrifold,
  Package,
  Path,
  PuzzlePiece,
  RocketLaunch,
  SealCheck,
  ShieldCheck,
  Stack,
  Target,
  UsersThree,
  WarningDiamond,
} from "@phosphor-icons/react";
import blueprintImage from "./assets/project-launch-blueprint.png";

const repositoryUrl = "https://github.com/chuanqi210-creator/complex-project-continuous-governance";

const pages = [
  { id: "overview", label: "开始", icon: HouseLine },
  { id: "capabilities", label: "理解", icon: Stack },
  { id: "mechanism", label: "运行", icon: FlowArrow },
  { id: "maturity", label: "评测", icon: SealCheck },
  { id: "scenarios", label: "参考", icon: MapTrifold },
  { id: "advantages", label: "贡献", icon: ChartLineUp },
];

const coreOutcomes = [
  {
    title: "强自治连续推进",
    text: "AI 默认按 7 个行为推进：恢复状态、判断项目性质、划清担责边界、建立最低充分的运行环境、执行与评价、按对象交付、留下下一路线。复杂组织只在确有多模块或重复职责时启用。",
    icon: Target,
  },
  {
    title: "守住证据边界",
    text: "先分清模型发现、证据填充、混合推进或执行交付；每个主张都要知道证据能支撑到哪一层，不能把材料存在写成结论成立。",
    icon: ShieldCheck,
  },
  {
    title: "抗人工与上下文漂移",
    text: "问人前先证明必要性；能读的材料自己读，清楚的下一步直接走。同 session 自评只算 diagnostic，真正独立评审用事实账本和清上下文。",
    icon: PuzzlePiece,
  },
  {
    title: "可审查恢复链",
    text: "项目状态、行为筛查、结构化评测和填好样例使推进可恢复、可复核、可继续；只有出现真实上下文压力时才启用 Hot/Warm/Cold 分层。",
    icon: UsersThree,
  },
];

const engineeringLayers = [
  {
    title: "Prompt Contract",
    text: "保存跨多拍稳定的 Goal、完成标准、担责边界和交付契约；动态事实不塞进 master prompt。",
    signal: "intent contract",
  },
  {
    title: "Context Working Set",
    text: "按当前判断装配最小充分、可溯源的事实，记录新鲜度、排除项和压缩后的语义恢复。",
    signal: "attention allocation",
  },
  {
    title: "Runtime Harness",
    text: "让工具、环境、副作用、日志、检查点、重试和降级路线可以被 agent 直接检查和执行。",
    signal: "execution infrastructure",
  },
  {
    title: "Progress Loop",
    text: "根据环境结果评价、路由、重试、回滚或停止；固定拍数和 agent 自述都不是完成证明。",
    signal: "outcome control",
  },
];

const assets = [
  {
    name: "快速入口",
    role: "面向目标项目的任务指南：从已安装 skill、目标仓库指令和目标恢复锚点开始。",
    file: "docs/quickstart.md",
  },
  {
    name: "核心参考",
    role: "定义稳定行为、四层诊断、Codex 平台边界、担责边界和完成语义。",
    file: "protocol/core.md",
  },
  {
    name: "维护状态",
    role: "只供维护 Complex 本身使用；目标项目不得把它装入自己的当前上下文。",
    file: "protocol/current-state.md",
  },
  {
    name: "机制成熟度",
    role: "区分核心、已测试和条件候选；当前没有机制仅凭结构检查被称为已验证。",
    file: "docs/mechanism-maturity.json",
  },
  {
    name: "架构重基线",
    role: "记录运行架构、公开语言、更新治理和评测系统的外部实现、保留/合并决定与下一验证。",
    file: "docs/active-architecture-rebaseline.md",
  },
  {
    name: "自优化循环",
    role: "区分日常小修与实质性变更，让候选改动在稳定基线旁逐级获得证据、晋级或回滚。",
    file: "docs/self-optimization.md",
  },
  {
    name: "评测契约",
    role: "把案例、运行、评分和人类结论分开；marker 只筛查，锁定的同题运行才比较。",
    file: "docs/evals/README.md",
  },
  {
    name: "填好样例",
    role: "展示不同项目形态的最小运行现场；样例用于说明，不自动证明机制有效。",
    file: "docs/examples/",
  },
];

const capabilityGroups = [
  {
    title: "四层运行架构",
    summary: "Prompt、Context、Harness、Loop 分工明确，但在每拍共同运行。",
    detail:
      "Prompt Contract 保存稳定意图；Context Working Set 分配当前注意力；Runtime Harness 提供可执行环境和恢复控制；Progress Loop 从真实结果判断继续、重试、回滚或停止。发生问题时先诊断失效层，不把所有故障都修成更长的提示词。",
    icon: Stack,
  },
  {
    title: "Codex 平台对齐",
    summary: "区分平台原语和 Complex 约定。",
    detail:
      "Thread、Turn、Item、Goal、审批、skill、subagent、worktree 和 automation 是 Codex 平台能力；thread_goal、phase_goal、beat_objective 和 standing lane 是 Complex 的使用约定。不能把约定写成平台 API，也不能承诺当前界面没有的能力。",
    icon: Compass,
  },
  {
    title: "行为内核",
    summary: "一套内核承担通用运行，不再为每个缺陷新增 gate。",
    detail:
      "内核负责恢复、项目性质、责任、最低充分运行环境、执行与评价、交付和恢复。提示词重水化、连续推进、来源解析、结果验收和四层诊断都属于同一个运行内核。",
    icon: FileMagnifyingGlass,
  },
  {
    title: "顶层框架质询",
    summary: "只校准会改变项目目的地的分叉，不把启动变成问卷。",
    detail:
      "项目开始或战略重构时，先读事实和外部依据。只有多个合理答案会实质改变 Goal、目标函数、总体架构、担责边界或评价方法时，才一次问一个问题，并给出推荐、依据、最强备选和后果。事实、工具、拓扑、实现顺序、可逆选择和可试验问题由 AI 自行处理；没有合格问题就直接继续。",
    icon: Compass,
  },
  {
    title: "项目性质与连续性",
    summary: "不同任务用不同权重，但都保留顶层目标。",
    detail:
      "模型发现型保护候选框架和区分性探针，证据填充型减少无谓发散。每拍从稳定目标和最新事实装配工作上下文，下一步明确时继续执行，不以固定拍数或模型自述结束。",
    icon: Graph,
  },
  {
    title: "时间收敛与阶段成果",
    summary: "长期推进必须在明确时点交付可用增量，而不是只证明仍在工作。",
    detail:
      "项目为下一阶段结果设定时间胃口、成果时点、最小可用成果和质量证据底线。Harness 观察实际耗时与工件推进；如果原范围无法收敛，Loop 会完成高价值薄切片、停放外围分支或调整路线。时间到期触发交付和重规划，不等于项目完成。",
    icon: Path,
  },
  {
    title: "担责边界",
    summary: "项目内部决策由 AI 处理，真实外部承诺才问人。",
    detail:
      "目标或公开口径变化、账号付款、发布外写、不可逆共享状态和高影响承诺需要人承担；读取、验证、规划、拓扑选择、上下文整理和下一路线属于 AI。暂停与恢复还要保证副作用可重试、可回滚或有补偿。",
    icon: PuzzlePiece,
  },
  {
    title: "条件化组织",
    summary: "只有多模块或重复职责出现时，才建立长期组织和组合控制。",
    detail:
      "普通项目停留在内核；复杂项目才增加总控、反复使用的责任 lane、独立评审、模块组合和分支停放。lane 是责任，subagent 是短期 worker，平台线程是否创建由可用能力和任务形状决定。",
    icon: ArrowsSplit,
  },
  {
    title: "跨边界状态对账",
    summary: "局部状态各自负责，总控在关键事件上恢复一份统一的全局控制视图。",
    detail:
      "模块、仓库、线程、工作流或长期职责保留局部权威记录；总控只接收带来源版本和工件指针的紧凑状态胶囊，在恢复、阶段切换、交接、依赖变化、冲突或阶段交付时更新全局路线。它不每拍复制全部账本，不用最新文件覆盖权威事实；局部冲突只冻结真正依赖它的路线。",
    icon: Database,
  },
  {
    title: "证据与上下文",
    summary: "当前工作集保持最小充分；重要主张明确依据和反证线索。",
    detail:
      "只装载当前判断需要的指令、状态、模块和即时材料，记录排除项与新鲜度。外部依据、当前依据、推断、未支持主张和可证伪线索在高影响节点分开；没有上下文压力时不机械维护大型冷热分层。",
    icon: Database,
  },
  {
    title: "外部借鉴与更新",
    summary: "借鉴落实到固定实现、可逆变更单元和渐进证据发布。",
    detail:
      "高星和文章只负责发现候选；真正借鉴要固定版本、检查目标与非目标、代码配置测试、运行限制和失败边界。普通修复走轻路径；有界或重大更新保留稳定基线，让一个候选依次经过契约筛查、复现、同题比较、有限真实使用和重复结果审查，再决定晋级、保留、降级或回滚。",
    icon: WarningDiamond,
  },
  {
    title: "独立评审与评测",
    summary: "说明、筛查、复现、比较和验证是五种不同证据。",
    detail:
      "填好样例用于说明，marker 用于筛查，固定版本 fixture 用于复现，锁定案例的 baseline/candidate 用于比较，重复真实结果才叫验证。重要评审使用清上下文；私人原始对话留在仓库外。",
    icon: ClipboardText,
  },
];

const mechanismSteps = [
  {
    k: "01",
    title: "恢复真实状态",
    text: "先区分 current_basis、not_current_basis、用户最新请求、旧草稿和当前依据。",
    output: "current_basis",
  },
  {
    k: "02",
    title: "分层判断工作性质",
    text: "项目性质是长期先验；当前阶段、模块或工作单元可以采用更窄的路线。判断不确定性、程序稳定性、可并行性和评审独立性。",
    output: "project_nature_router",
  },
  {
    k: "03",
    title: "划清担责边界",
    text: "默认强自治：AI 处理项目内部计划、读取、验证、运行资源和下一拍推进；主目标、账号/API、付款、外部写入、发布、不可逆和高风险主张回问。",
    output: "decision_rights_matrix",
  },
  {
    k: "04",
    title: "先定工件，再编排",
    text: "先写清输入、动作或判断、预期工件、验收、失败恢复和状态回写；再选择主线程、确定性 Harness、临时并行、长期职责或清上下文评审。",
    output: "artifact contract / work topology",
  },
  {
    k: "05",
    title: "目标函数 Loop",
    text: "每拍说明 target function、当前工作单元和 outcome predicate。稳定判断可下沉为 checker 或状态机；机械流程若因前提变化反复失败，则回流到模型发现或战略判断。",
    output: "target-function loop",
  },
  {
    k: "06",
    title: "按对象交付",
    text: "人看版、机器恢复版、老师/专家/第三方版分开，不把机器字段直接包装成人话。",
    output: "delivery_contract",
  },
  {
    k: "07",
    title: "留下恢复线索",
    text: "写清 next_route、route_reason、未决问题、能力/拓扑状态和必要回滚路线。",
    output: "next_route",
  },
];

const gateTypes = [
  {
    name: "always minimum",
    zh: "常驻最小",
    examples: "current_basis、project_nature、responsibility_boundary、beat_objective、next_route",
  },
  {
    name: "nature based",
    zh: "性质触发",
    examples: "evidence_fill、model_discovery、mixed、execution_delivery",
  },
  {
    name: "boundary based",
    zh: "边界触发",
    examples: "账号、API、付款、发布、外部写入、不可逆动作、高风险主张",
  },
  {
    name: "review based",
    zh: "评审触发",
    examples: "fact-ledger、清上下文评审、read-only audit、transcript review",
  },
];

const scenarios = [
  {
    id: "evidence",
    label: "证据填充型",
    icon: Database,
    claim: "模型、指标或判断框架已经确定，现在要用证据把结论填实。",
    lenses: ["project_nature_router", "evidence_matrix", "claim_readiness_ladder", "delivery_contract"],
    outputs: ["证据分层", "缺口与可声明边界", "检索/获取升级路径", "人看版交付"],
    downgrade: "证据不足时只写到对应层级，不能把材料存在、引用存在或局部验证写成结论成立。",
  },
  {
    id: "discovery",
    label: "模型发现型",
    icon: Graph,
    claim: "问题定义、研究框架、解释路径或故事线还没定，不能过早证据填表。",
    lenses: ["project_nature_router", "candidate frameworks", "argument map", "discriminating probe"],
    outputs: ["候选框架", "issue / position / pro / con", "可区分探针", "收敛条件"],
    downgrade: "没有比较候选框架和反例之前，不能把一个局部证据缺口升级成主目标。",
  },
  {
    id: "execution",
    label: "执行交付型",
    icon: BracketsCurly,
    claim: "主要任务是实现、包装、交付、验证或说明当前成果。",
    lenses: ["beat_objective", "Progress Loop", "delivery_contract", "next_route"],
    outputs: ["窄目标", "最小验证", "交付边界", "下一轮恢复线索"],
    downgrade: "验证未覆盖的部分不能当作已完成；人看版和机器恢复记录要分开。",
  },
  {
    id: "review",
    label: "独立评审型",
    icon: UsersThree,
    claim: "需要客观检查某个输出或流程是否真的符合标准。",
    lenses: ["independent_review_context_separation", "clean reviewer", "fact ledger", "decision log"],
    outputs: ["事实账本", "清上下文评审说明", "问题/证据/结论分离", "整改建议"],
    downgrade: "同 session 角色扮演只能算诊断，不应包装成真正独立评审。",
  },
  {
    id: "boundary",
    label: "高风险边界",
    icon: ShieldCheck,
    claim: "主目标、账号/API、外部写入、公开口径、高风险主张或现实责任发生变化。",
    lenses: ["responsibility_boundary", "external side effects", "human responsibility", "rollback route"],
    outputs: ["必须回问事项", "AI 可自主事项", "人工操作边界", "回滚/降级路线"],
    downgrade: "没有授权时只能做只读分析、计划或担责边界内小验证，不能替用户执行外部影响动作。",
  },
];

const comparisonRows = [
  ["推进方式", "先讨论方案或直接执行", "先跑 7 步行为内核，再按项目性质推进"],
  ["项目性质", "容易把所有任务都变成证据审计", "先判断 evidence_fill / model_discovery / mixed / execution_delivery"],
  ["人工介入", "安全起见频繁问是否继续", "问人前证明必要性；清楚担责边界内下一步自动推进"],
  ["材料处理", "要求用户整理、搬运、摘要", "用户给路径或文件时优先自行读取和归纳"],
  ["评审独立性", "同 session 扮演评审", "区分 diagnostic 自评和清上下文 independent review"],
  ["复杂度控制", "要么过度表格化，要么完全黑箱", "行为内核给主线，模板和案例按需启用"],
  ["恢复能力", "依赖聊天记忆", "用目标项目自己的恢复锚点、下一路线和可检查产物恢复"],
];

const maturityLevels = [
  ["core", "架构角色：核心", "每次运行都要尊重的行为主轴或担责/交付边界；这不等于效果已经验证。"],
  ["supporting_practice", "架构角色：支持实践", "可复用但不是每次运行都要展开的做法。"],
  ["conditional_extension", "架构角色：条件扩展", "只有匹配规模或失败模式时才启用。"],
  ["screened", "证据状态：已筛查", "契约和外部依据已经审查，尚无有效结果比较。"],
  ["tested", "证据状态：已测试", "存在行为筛查、样例、有限实验或项目观察，真实比较仍不完整。"],
  ["validated", "证据状态：已验证", "不同真实项目的重复比较改善结果，并通过独立人工评审。"],
];

function useHashRoute() {
  const normalize = () => {
    const id = window.location.hash.replace("#", "");
    return pages.some((page) => page.id === id) ? id : "overview";
  };
  const [route, setRoute] = useState(normalize);

  useEffect(() => {
    const onHashChange = () => setRoute(normalize());
    window.addEventListener("hashchange", onHashChange);
    return () => window.removeEventListener("hashchange", onHashChange);
  }, []);

  const go = (id) => {
    window.location.hash = id;
    setRoute(id);
    window.scrollTo({ top: 0, behavior: "smooth" });
  };

  return [route, go];
}

function IconBadge({ icon: Icon, tone = "green" }) {
  return (
    <span className={`icon-badge ${tone}`} aria-hidden="true">
      <Icon size={22} weight="duotone" />
    </span>
  );
}

function Header({ route, go }) {
  return (
    <header className="site-header">
      <button className="brand" type="button" onClick={() => go("overview")}>
        <span className="brand-mark" aria-hidden="true">
          <RocketLaunch size={24} weight="fill" />
        </span>
        <span>
          <strong>Complex 项目持续治理</strong>
          <small>Complex Project Continuous Governance</small>
        </span>
      </button>
      <nav className="main-nav" aria-label="页面导航">
        {pages.map((page) => {
          const Icon = page.icon;
          return (
            <button
              className={route === page.id ? "nav-item active" : "nav-item"}
              type="button"
              key={page.id}
              onClick={() => go(page.id)}
            >
              <Icon size={18} weight="duotone" />
              <span>{page.label}</span>
            </button>
          );
        })}
      </nav>
    </header>
  );
}

function Overview({ go }) {
  return (
    <div className="page-stack">
      <section className="hero-section">
        <img className="hero-image" src={blueprintImage} alt="项目治理蓝图视觉图，展示证据地图、风险边界和持续治理流程" />
        <div className="hero-overlay">
          <p className="eyebrow">适用于复杂项目持续推进</p>
          <h1>让复杂项目在正确上下文和运行环境里持续完成</h1>
          <p className="hero-copy">
            Complex 用七步行为内核组织项目，同时让 Prompt Contract、Context Working Set、Runtime Harness 和 Progress Loop 在每拍共同工作。它先诊断失效层，再修改指令、上下文、工具环境或循环控制，而不是把所有问题都塞回提示词。
          </p>
          <div className="hero-actions">
            <button className="primary-action" type="button" onClick={() => go("mechanism")}>
              看它如何运行
            </button>
            <button className="secondary-action" type="button" onClick={() => go("capabilities")}>
              查看治理能力
            </button>
          </div>
        </div>
      </section>

      <section className="intro-grid">
        <div className="intro-panel">
          <p className="section-kicker">它解决的问题</p>
          <h2>复杂项目最大的风险，往往来自“规则很多，但本轮行为不稳”。</h2>
          <p>
            项目推进中最容易把目标说大、把证据看轻、把工具当能力、把局部资料缺口当主线。Complex 现在先用行为内核压缩复杂度，再按项目性质选择模型发现、证据填充、执行交付或混合路线。
          </p>
        </div>
        <div className="signal-list">
          {coreOutcomes.map((item) => (
            <article className="signal-card" key={item.title}>
              <IconBadge icon={item.icon} />
              <div>
                <h3>{item.title}</h3>
                <p>{item.text}</p>
              </div>
            </article>
          ))}
        </div>
      </section>

      <section className="deliverables-section">
        <div className="section-heading">
          <p className="section-kicker">四层不是四个阶段</p>
          <h2>稳定意图、当前注意力、执行基础和结果控制同时存在。</h2>
        </div>
        <div className="deliverable-grid">
          {engineeringLayers.map((layer) => (
            <article className="deliverable-card" key={layer.title}>
              <code>{layer.signal}</code>
              <h3>{layer.title}</h3>
              <p>{layer.text}</p>
            </article>
          ))}
        </div>
      </section>

      <section className="deliverables-section">
        <div className="section-heading">
          <p className="section-kicker">最终交付给项目的东西</p>
          <h2>不是更多流程，而是更清楚的行动条件。</h2>
        </div>
        <div className="deliverable-grid">
          {[
            ["问题与价值主张", "项目到底要解决什么，成功主张如何被验证。"],
            ["证据地图", "已有材料、可信来源、现场证据和未知缺口分别在哪里。"],
            ["能力与工具计划", "当前应使用哪些 skill、工具、API、子代理，哪些不该用。"],
            ["小题验证方案", "用最低成本先验证最危险假设或最高杠杆链路。"],
            ["风险边界说明", "哪些话不能说满，哪些动作要授权，哪些结论要降级。"],
            ["执行与恢复看版", "下一步路线、交付物、验证命令和机器可恢复状态。"],
          ].map(([title, text]) => (
            <article className="deliverable-card" key={title}>
              <h3>{title}</h3>
              <p>{text}</p>
            </article>
          ))}
        </div>
      </section>

      <section className="asset-section">
        <div className="section-heading">
          <p className="section-kicker">我们已经把它做成了什么</p>
          <h2>一套可维护的协议系统，而不是一句提示词。</h2>
        </div>
        <div className="asset-table">
          {assets.map((asset) => (
            <article className="asset-row" key={asset.name}>
              <div>
                <strong>{asset.name}</strong>
                <p>{asset.role}</p>
              </div>
              <a
                href={`${repositoryUrl}/${asset.file.endsWith("/") ? "tree" : "blob"}/main/${asset.file.replace(/\/$/, "")}`}
                target="_blank"
                rel="noreferrer"
              >
                <code>{asset.file}</code>
              </a>
            </article>
          ))}
        </div>
      </section>
    </div>
  );
}

function Capabilities() {
  const [open, setOpen] = useState(capabilityGroups[0].title);
  return (
    <div className="content-page">
      <PageTitle
        label="协议能做什么"
        title="它把复杂项目推进，压缩成少数稳定行为。"
        copy="这些能力不是每次全量展开。协议先判断项目性质和自治边界，再按不确定性、风险和交付对象动态激活需要的能力。"
      />
      <div className="capability-layout">
        <div className="capability-list">
          {capabilityGroups.map((item) => (
            <button
              className={open === item.title ? "capability-item open" : "capability-item"}
              type="button"
              key={item.title}
              onClick={() => setOpen(item.title)}
            >
              <IconBadge icon={item.icon} tone="soft" />
              <span>
                <strong>{item.title}</strong>
                <small>{item.summary}</small>
              </span>
            </button>
          ))}
        </div>
        <div className="capability-detail">
          {capabilityGroups
            .filter((item) => item.title === open)
            .map((item) => (
              <article key={item.title}>
                <IconBadge icon={item.icon} />
                <h2>{item.title}</h2>
                <p className="large-copy">{item.summary}</p>
                <p>{item.detail}</p>
                <div className="detail-note">
                  <strong>项目作用</strong>
                  <span>让行动方案更可追踪、可验证、可降级，不靠一次性判断赌方向。</span>
                </div>
              </article>
            ))}
        </div>
      </div>
    </div>
  );
}

function Mechanism() {
  return (
    <div className="content-page">
      <PageTitle
        label="实现方法"
        title="七步主轴负责推进，四层工程负责把推进做对。"
        copy="行为内核决定项目怎样前进；Prompt、Context、Harness 和 Loop 分别管理稳定意图、当前工作集、可执行基础和结果控制。先定位失效层，再修对应接口。"
      />

      <section className="deliverable-grid">
        {engineeringLayers.map((layer) => (
          <article className="deliverable-card" key={layer.title}>
            <code>{layer.signal}</code>
            <h3>{layer.title}</h3>
            <p>{layer.text}</p>
          </article>
        ))}
      </section>

      <section className="timeline">
        {mechanismSteps.map((step) => (
          <article className="timeline-step" key={step.k}>
            <div className="step-index">{step.k}</div>
            <div className="step-body">
              <h3>{step.title}</h3>
              <p>{step.text}</p>
            </div>
            <code>{step.output}</code>
          </article>
        ))}
      </section>

      <section className="mechanism-grid">
        <article className="mechanism-panel">
          <h2>动态激活，而不是全量硬跑</h2>
          <p>
            `complex_behavior_kernel` 是执行主轴，不是四层中的第一层。四层共同支持每个行为；候选机制只在匹配失败模式时启用，避免普通推进变成流程负担。
          </p>
          <div className="gate-grid">
            {gateTypes.map((gate) => (
              <div className="gate-card" key={gate.name}>
                <strong>{gate.zh}</strong>
                <span>{gate.name}</span>
                <p>{gate.examples}</p>
              </div>
            ))}
          </div>
        </article>

        <article className="mechanism-panel">
          <h2>主张就绪阶梯</h2>
          <p>
            每个结论都必须绑定证据层级。证据不足时，协议不让语言越级，从而防止把来源存在、测试通过、PR 合并或活动完成写成真实影响成立。
          </p>
          <div className="ladder">
            {["idea_or_candidate", "source_backed", "locally_verified", "bounded_result_observed", "pilot_ready", "production_or_public_claim_ready"].map(
              (level, index) => (
                <div className="ladder-row" key={level}>
                  <span>{index + 1}</span>
                  <strong>{level}</strong>
                </div>
              ),
            )}
          </div>
        </article>
      </section>
    </div>
  );
}

function Maturity() {
  return (
    <div className="content-page">
      <PageTitle
        label="机制成熟度"
        title="架构角色和实证强度是两回事。"
        copy="Complex 分开记录一条规则在系统中是否普遍适用，以及它目前有什么结果证据。核心规则也可以仍处于 tested；条件扩展也不能因为外部项目优秀就被称为 validated。"
      />

      <section className="mechanism-grid">
        <article className="mechanism-panel">
          <h2>两个独立轴</h2>
          <p>
            `docs/mechanism-maturity.json` 同时记录 normative_role 与 evidence_status，以及所属工程层、外部依据、内部证据、行为用例、样例、升级规则和降级触发。角色不能替代证据，marker 通过也不能等同于真实项目表现优良。
          </p>
          <div className="gate-grid">
            {maturityLevels.map(([id, title, text]) => (
              <div className="gate-card" key={id}>
                <strong>{title}</strong>
                <span>{id}</span>
                <p>{text}</p>
              </div>
            ))}
          </div>
        </article>

        <article className="mechanism-panel">
          <h2>真实行为验证</h2>
          <p>
            `tools/review_behavior_transcript.py` 只做轻量 marker 筛查；结构化评测把 eval case、baseline/candidate run 和 score record 分开。当前全量套件有 84/84 个有效可写 trial、4 次恢复重试和 0 个终止错误，但七项双臂均到达环境评分上限，因此只能说明合成契约可执行。
          </p>
          <div className="ladder">
            {[
              "behavior case",
              "writable environment screen",
              "independent trajectory review",
              "blind human preference",
              "repeated real-project outcome",
            ].map((level, index) => (
              <div className="ladder-row" key={level}>
                <span>{index + 1}</span>
                <strong>{level}</strong>
              </div>
            ))}
          </div>
        </article>
      </section>

      <section className="comparison-card">
        <div className="comparison-header">
          <span>对象</span>
          <span>不能说明什么</span>
          <span>真正说明什么</span>
        </div>
        {[
          ["当前状态", "不代表机制优于 native baseline", "3 项 core 为 tested；4 项条件扩展为 screened；0 项 validated"],
          ["候选机制", "不代表已经解决真实项目问题", "说明有外部依据和可测试 micro-contract"],
          ["填好样例", "不代表已被认证为最佳实践", "说明新代理有可模仿的最小运行现场"],
          ["Marker 通过", "不代表回复质量优秀", "说明没有明显漏掉关键行为或触发禁忌行为"],
          ["核心协议", "不应该容纳每次新失败的补丁", "只保留跨项目稳定、低摩擦、高价值的行为骨架"],
        ].map(([a, b, c]) => (
          <div className="comparison-row" key={a}>
            <strong>{a}</strong>
            <p>{b}</p>
            <p>{c}</p>
          </div>
        ))}
      </section>
    </div>
  );
}

function Scenarios() {
  const [activeId, setActiveId] = useState("software");
  const active = useMemo(() => scenarios.find((item) => item.id === activeId), [activeId]);
  const ActiveIcon = active.icon;

  return (
    <div className="content-page">
      <PageTitle
        label="适用场景"
        title="它不是单一领域模板，而是复杂项目推进的通用治理方式。"
        copy="协议默认按最终主张选择主类，再叠加高风险标签。下面每个场景都展示它会优先检查什么、输出什么、以及不能外推到哪里。"
      />

      <section className="scenario-shell">
        <div className="scenario-tabs" role="tablist" aria-label="项目场景">
          {scenarios.map((scenario) => {
            const Icon = scenario.icon;
            return (
              <button
                type="button"
                role="tab"
                aria-selected={scenario.id === activeId}
                className={scenario.id === activeId ? "scenario-tab active" : "scenario-tab"}
                key={scenario.id}
                onClick={() => setActiveId(scenario.id)}
              >
                <Icon size={20} weight="duotone" />
                <span>{scenario.label}</span>
              </button>
            );
          })}
        </div>

        <article className="scenario-detail">
          <IconBadge icon={ActiveIcon} />
          <h2>{active.label}</h2>
          <div className="scenario-block">
            <strong>要证明的核心主张</strong>
            <p>{active.claim}</p>
          </div>
          <div className="scenario-block">
            <strong>优先启用镜头</strong>
            <div className="chip-row">
              {active.lenses.map((lens) => (
                <span className="chip" key={lens}>{lens}</span>
              ))}
            </div>
          </div>
          <div className="scenario-block">
            <strong>典型输出</strong>
            <ul className="clean-list">
              {active.outputs.map((output) => (
                <li key={output}>{output}</li>
              ))}
            </ul>
          </div>
          <div className="downgrade-box">
            <WarningDiamond size={22} weight="duotone" />
            <span>{active.downgrade}</span>
          </div>
        </article>
      </section>
    </div>
  );
}

function Advantages() {
  return (
    <div className="content-page">
      <PageTitle
        label="对比优势"
        title="它比一般项目推进更稳，也比厚重流程更轻。"
        copy="持续治理协议的优势不在于字段多，而在于它把常见误判压缩成可执行行为，并用行为回归、transcript 审查、结果记录、填好样例和恢复链防止下一轮重新迷路。"
      />

      <section className="comparison-card">
        <div className="comparison-header">
          <span>对比维度</span>
          <span>普通推进</span>
          <span>持续治理协议</span>
        </div>
        {comparisonRows.map(([dimension, ordinary, governed]) => (
          <div className="comparison-row" key={dimension}>
            <strong>{dimension}</strong>
            <p>{ordinary}</p>
            <p>{governed}</p>
          </div>
        ))}
      </section>

      <section className="advantage-grid">
        {[
          {
            title: "比提示词更强",
            text: "它要求目标项目维护自己的恢复锚点、下一路线和可检查产物。下一次继续时不是靠聊天记忆，也不会读取 Complex 的维护状态。",
            icon: Path,
          },
          {
            title: "比项目管理清单更重证据",
            text: "它不只问任务拆分和时间线，还持续判断项目是在发现模型、填充证据、混合推进还是执行交付。",
            icon: ArrowsSplit,
          },
          {
            title: "比一次性咨询更可迭代",
            text: "真实小题和反膨胀机制让协议能继续学习。维护不会停在文档改完，而会扫描剩余证据债务；只有目标完成且没有仍会改变决策的内部验证时才停止。",
            icon: SealCheck,
          },
          {
            title: "比全量治理更低摩擦",
            text: "用户只需要说目标和材料，复杂字段由 AI 维护；可逆细节和运行资源由 AI 自行判断，账号/API、外部写入、不可逆和高风险边界再回问。",
            icon: RocketLaunch,
          },
        ].map((item) => (
          <article className="advantage-card" key={item.title}>
            <IconBadge icon={item.icon} />
            <h3>{item.title}</h3>
            <p>{item.text}</p>
          </article>
        ))}
      </section>
    </div>
  );
}

function PageTitle({ label, title, copy }) {
  return (
    <section className="page-title">
      <p className="section-kicker">{label}</p>
      <h1>{title}</h1>
      <p>{copy}</p>
    </section>
  );
}

export function App() {
  const [route, go] = useHashRoute();

  const page = {
    overview: <Overview go={go} />,
    capabilities: <Capabilities />,
    mechanism: <Mechanism />,
    maturity: <Maturity />,
    scenarios: <Scenarios />,
    advantages: <Advantages />,
  }[route];

  return (
    <>
      <Header route={route} go={go} />
      <main>{page}</main>
      <footer className="site-footer">
        <div>
          <strong>Complex 项目持续治理协议</strong>
          <p>当前页面用于解释协议价值与实现方法，不替代核心协议、当前状态和完整性验证。</p>
        </div>
        <button className="secondary-action compact" type="button" onClick={() => go("overview")}>
          回到概览
        </button>
      </footer>
    </>
  );
}
