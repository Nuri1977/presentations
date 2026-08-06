"use client"

import { Handle, Position } from "@xyflow/react"
import {
  MessageSquare,
  Zap,
  RefreshCw,
  MessagesSquare,
  PenLine,
  BarChart3,
  NotebookPen,
  Brain,
  FlaskConical,
  Search,
  KeyRound,
  Puzzle,
  Lightbulb,
  Target,
  Package,
  Link2,
  Pencil,
  Compass,
  ClipboardList,
  Terminal,
  Globe,
  Monitor,
  Cpu,
  Wrench,
  Database,
  Server,
  BookOpen,
  Layers,
  BrainCircuit,
  Hammer,
  PieChart,
} from "lucide-react"
import { Card, CatLabel, SubLabel, PillGrid, PillView, CATEGORY, type Category, type Pill } from "./primitives"

const ICON = "/assets/icons"
const CONN = "/assets/connection"

/* target handle that doubles as the colored connection dot */
function TargetDot({ category, position, style }: { category: Category; position: Position; style?: React.CSSProperties }) {
  const c = CATEGORY[category]
  return (
    <Handle
      type="target"
      id="in"
      position={position}
      isConnectable={false}
      style={{
        width: 11,
        height: 11,
        background: c.color,
        border: "2px solid #fff",
        boxShadow: `0 0 0 3px ${c.color}40`,
        ...style,
      }}
    />
  )
}

/* ============ ORB (hub) ============ */
export function OrbNode() {
  const src = (id: string, position: Position, style: React.CSSProperties) => (
    <Handle
      key={id}
      type="source"
      id={id}
      position={position}
      isConnectable={false}
      style={{
        width: 8,
        height: 8,
        background: "rgba(255,255,255,0.9)",
        border: "1.5px solid #ea580c",
        ...style,
      }}
    />
  )
  return (
    <div style={{ position: "relative", width: 170, height: 170 }}>
      {/* animated orbit rings */}
      <div className="rosetta-rings" aria-hidden style={{ position: "absolute", inset: 0 }}>
        <span className="rosetta-ring r1" />
        <span className="rosetta-ring r2" />
        <span className="rosetta-ring r3" />
      </div>

      <div
        style={{
          position: "absolute",
          inset: 0,
          borderRadius: "50%",
          background:
            "radial-gradient(circle at 35% 30%, #fed7aa 0%, #fb923c 18%, #ea580c 48%, #c2410c 82%, #9a3412 100%)",
          boxShadow:
            "0 0 0 1px rgba(255,255,255,0.35) inset, 0 0 44px rgba(234,88,12,0.5), 0 0 90px rgba(234,88,12,0.25), 0 22px 55px rgba(154,52,18,0.4)",
          display: "flex",
          alignItems: "center",
          justifyContent: "center",
        }}
      >
        <div
          style={{
            width: 70,
            height: 70,
            borderRadius: 14,
            background: "linear-gradient(145deg, #fff 0%, #fff7ed 60%, #fed7aa 100%)",
            display: "flex",
            alignItems: "center",
            justifyContent: "center",
            boxShadow: "0 8px 24px rgba(154,52,18,0.3), inset 0 1px 0 rgba(255,255,255,0.9)",
          }}
        >
          <img
            src={`${ICON}/bot.svg`}
            alt="AI Agent"
            style={{
              width: 46,
              height: 46,
              filter:
                "invert(40%) sepia(90%) saturate(600%) hue-rotate(10deg) brightness(1.1)",
            }}
          />
        </div>
      </div>

      {/* label */}
      <div
        style={{
          position: "absolute",
          bottom: -62,
          left: "50%",
          transform: "translateX(-50%)",
          whiteSpace: "nowrap",
          textAlign: "center",
        }}
      >
        <span style={{ fontSize: 28, fontWeight: 900, color: "#9a3412", display: "block", lineHeight: 1 }}>
          AI Agent
        </span>
        <span
          style={{
            fontSize: 13,
            fontWeight: 700,
            letterSpacing: "0.14em",
            textTransform: "uppercase",
            color: "#ea580c",
            marginTop: 5,
            display: "block",
          }}
        >
          Orchestrator · Vercel AI SDK v6
        </span>
      </div>

      {/* 7 source handles around the orb.
          renderer (top) & mcp (bottom) are offset off-center on purpose: a
          perfectly vertical edge has a zero-width bounding box, which makes an
          objectBoundingBox linearGradient stroke render as invisible. The
          slight horizontal offset gives the gradient a box to paint. */}
      {src("renderer",  Position.Top,    { left: "35%" })}
      {src("providers", Position.Right,  { top: "22%" })}
      {src("skills",    Position.Right,  { top: "62%" })}
      {src("connected", Position.Bottom, { left: "72%" })}
      {src("mcp",       Position.Bottom, { left: "48%" })}
      {src("tools",     Position.Left,   { top: "62%" })}
      {src("memory",    Position.Left,   { top: "28%" })}
    </div>
  )
}

/* ============ RENDERER (top, 2 equal columns) ============ */
function SubBox({ title, dot, pills }: { title: string; dot: string; pills: Pill[] }) {
  return (
    <div
      style={{
        background: "rgba(255,255,255,0.55)",
        border: "1px solid rgba(148,163,184,0.14)",
        borderRadius: 8,
        padding: "5px 8px",
      }}
    >
      <div style={{ fontSize: 11, fontWeight: 800, color: "#1e293b", marginBottom: 5, display: "flex", alignItems: "center", gap: 5 }}>
        <span style={{ width: 6, height: 6, borderRadius: "50%", flexShrink: 0, background: dot, boxShadow: `0 0 0 2px ${dot}33` }} />
        {title}
      </div>
      <PillGrid pills={pills} />
    </div>
  )
}

export function RendererNode() {
  return (
    <Card style={{ width: 560 }}>
      <TargetDot category="renderer" position={Position.Bottom} style={{ left: "42%" }} />
      <CatLabel category="renderer" icon={Monitor}>Renderer Process</CatLabel>
      <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: 6 }}>
        <SubBox
          title="Chat UI"
          dot="#3b82f6"
          pills={[
            { label: "Interleaved streaming", icon: MessageSquare },
            { label: "Context ring", icon: Zap },
            { label: "Auto-compaction", icon: RefreshCw },
            { label: "Chat & Code modes", icon: MessagesSquare },
          ]}
        />
        <SubBox
          title="Live Editors"
          dot="#2563eb"
          pills={[
            { label: "Monaco", icon: PenLine },
            { label: "Analytics", icon: BarChart3 },
            { label: "Notebooks", icon: NotebookPen },
            { label: "Pipelines", img: `${ICON}/flow.svg` },
            { label: "SQL Editor", img: `${ICON}/duckdb.svg` },
          ]}
        />
      </div>
    </Card>
  )
}

/* ============ AI PROVIDERS ============ */
export function ProvidersNode() {
  return (
    <Card style={{ width: 440 }}>
      <TargetDot category="providers" position={Position.Left} style={{ top: "50%" }} />
      <CatLabel category="providers" icon={Cpu}>AI Providers</CatLabel>
      <SubLabel>Manager &amp; Secure</SubLabel>
      <PillGrid
        style={{ marginTop: 4 }}
        pills={[
          { label: "CRUD", icon: Package },
          { label: "Test connect", icon: FlaskConical },
          { label: "Model discovery", icon: Search },
          { label: "Keytar", icon: KeyRound },
        ]}
      />
      <SubLabel style={{ marginTop: 8 }}>Cloud · Local</SubLabel>
      <PillGrid
        style={{ marginTop: 4 }}
        pills={[
          { label: "OpenAI", img: `${CONN}/openai.svg` },
          { label: "Anthropic", img: `${CONN}/anthropic.svg` },
          { label: "Gemini", img: `${CONN}/google.svg` },
          { label: "Ollama", img: `${CONN}/ollama.svg` },
          { label: "LM Studio", img: `${CONN}/lmstudio.svg` },
          { label: "OpenAI Compat", img: `${CONN}/openai_compatible.svg` },
        ]}
      />
    </Card>
  )
}

/* ============ SKILLS ============ */
export function SkillsNode() {
  return (
    <Card style={{ width: 430 }}>
      <TargetDot category="skills" position={Position.Left} style={{ top: "50%" }} />
      <CatLabel category="skills" icon={Layers}>Skills</CatLabel>
      <SubLabel>Skill Discovery</SubLabel>
      <PillGrid
        style={{ marginTop: 4 }}
        pills={[
          { label: "skill-ls", icon: Brain },
          { label: "skill-install", icon: Package },
          { label: "skill-search", icon: Search },
          { label: "loadSkill tool", icon: Puzzle },
        ]}
      />
      <SubLabel style={{ marginTop: 8 }}>Skill Sources · Shell</SubLabel>
      <PillGrid
        style={{ marginTop: 4 }}
        pills={[
          { label: "SKILL.md", icon: ClipboardList },
          { label: "skills.sh", icon: Lightbulb },
          { label: "Project scoped", icon: Target },
          { label: "Skill registry", icon: Package },
          { label: "Skill deps", icon: Link2 },
        ]}
      />
    </Card>
  )
}

/* ============ CONNECTED SYSTEMS ============ */
export function ConnectedNode() {
  return (
    <Card style={{ width: 440 }}>
      <TargetDot category="connected" position={Position.Left} style={{ top: "50%" }} />
      <CatLabel category="connected" icon={Database}>Connected Systems</CatLabel>
      <PillGrid
        pills={[
          { label: "Postgres", img: `${CONN}/postgresql.svg` },
          { label: "Snowflake", img: `${CONN}/snowflake.svg` },
          { label: "BigQuery", img: `${CONN}/bigquery.svg` },
          { label: "Redshift", img: `${CONN}/redshift.svg` },
          { label: "DuckDB", img: `${CONN}/duckdb.svg` },
          { label: "S3", img: `${CONN}/s3_bucket.svg` },
          { label: "GCS", img: `${CONN}/googlecloud.svg` },
          { label: "Azure Blob", img: `${CONN}/azure_blob.svg` },
        ]}
      />
    </Card>
  )
}

/* ============ MCP SERVERS ============ */
export function McpNode() {
  return (
    <Card style={{ width: 420 }}>
      <TargetDot category="mcp" position={Position.Top} style={{ left: "50%" }} />
      <CatLabel category="mcp" icon={Server}>MCP Servers</CatLabel>
      <PillGrid
        pills={[
          { label: "DuckDB MCP", img: `${CONN}/duckdb.svg` },
          { label: "dbt Core", img: `${ICON}/dbt-bit_tm.svg` },
          { label: "Rosetta CLI", icon: Compass },
          { label: "DuckLake", img: `${ICON}/duck-lake.svg` },
          { label: "User servers", icon: Puzzle },
        ]}
      />
    </Card>
  )
}

/* ============ NATIVE TOOLING ============ */
export function ToolsNode() {
  return (
    <Card style={{ width: 380 }}>
      <TargetDot category="tools" position={Position.Right} style={{ top: "50%" }} />
      <CatLabel category="tools" icon={Hammer}>Native Tooling</CatLabel>
      <SubLabel>DBT &amp; Filesystem</SubLabel>
      <PillGrid
        style={{ marginTop: 4 }}
        pills={[
          { label: "Run / Test / Compile", img: `${ICON}/dbt-bit_tm.svg` },
          { label: "Read / Write Model", img: `${ICON}/dbt-black.svg` },
          { label: "List Models & Logs", img: `${ICON}/dbt-bit_tm.svg` },
          { label: "Read / Write File", img: `${ICON}/folder.svg` },
          { label: "List Directory", img: `${ICON}/collection.svg` },
        ]}
      />
      <SubLabel style={{ marginTop: 8 }}>Analytics Reports</SubLabel>
      <PillGrid
        style={{ marginTop: 4 }}
        pills={[
          { label: "Read / Write Page", icon: BarChart3 },
          { label: "Run Page", icon: Zap },
          { label: "Tables · Charts · Pies", icon: PieChart },
        ]}
      />
      <SubLabel style={{ marginTop: 8 }}>Studio-Native</SubLabel>
      <PillGrid
        style={{ marginTop: 4 }}
        pills={[
          { label: "SQL Query", img: `${ICON}/duckdb.svg` },
          { label: "Schema Extract", img: `${ICON}/duckdb.svg` },
          { label: "DuckLake Query", img: `${ICON}/duck-lake.svg` },
          { label: "Cloud Objects", img: `${CONN}/s3_bucket.svg` },
          { label: "Monaco Editor", icon: PenLine },
          { label: "CLI · dbt run", icon: Terminal },
          { label: "Connections", img: `${ICON}/flow.svg` },
          { label: "Notebooks", icon: NotebookPen },
          { label: "HTTP / SSE · stdio", icon: Globe },
        ]}
      />
    </Card>
  )
}

/* ============ AGENT MEMORY ============ */
export function MemoryNode() {
  return (
    <Card style={{ width: 430 }}>
      <TargetDot category="memory" position={Position.Right} style={{ top: "50%" }} />
      <CatLabel category="memory" icon={BrainCircuit}>Agent Memory</CatLabel>
      <SubLabel>Agent Memory (OKF v0.2)</SubLabel>
      <PillGrid
        style={{ marginTop: 4 }}
        pills={[
          { label: "MEMORY.md", icon: Brain },
          { label: "wiki_search/read", icon: Search },
          { label: "wiki_update", icon: Pencil },
          { label: "archive", img: `${ICON}/collection.svg` },
          { label: "Refresh pipeline", img: `${ICON}/flow.svg` },
        ]}
      />
      <SubLabel style={{ marginTop: 8 }}>Project Memory</SubLabel>
      <PillGrid
        style={{ marginTop: 4 }}
        pills={[
          { label: "AGENTS.md", img: `${ICON}/git-branch.svg` },
          { label: "Project scoped", icon: Target },
          { label: "Persona", img: `${ICON}/bot.svg` },
          { label: "Rules", icon: ClipboardList },
          { label: "Context", icon: Compass },
        ]}
      />
    </Card>
  )
}

export const nodeTypes = {
  orb: OrbNode,
  renderer: RendererNode,
  providers: ProvidersNode,
  skills: SkillsNode,
  connected: ConnectedNode,
  mcp: McpNode,
  tools: ToolsNode,
  memory: MemoryNode,
}
