"use client"

import { useCallback, useEffect } from "react"
import { ReactFlow, ReactFlowProvider, useReactFlow, type Node, Handle, Position } from "@xyflow/react"
import "@xyflow/react/dist/style.css"
import { nodeTypes as desktopNodeTypes } from "./nodes"
import { CATEGORY, Card, CatLabel, SubLabel, PillGrid, type Category } from "./primitives"
import { edgeTypes, type FlowEdge } from "./flow-edge"
import {
  MessageSquare, Zap, RefreshCw, MessagesSquare, PenLine, BarChart3,
  NotebookPen, Brain, FlaskConical, Search, KeyRound, Puzzle,
  Lightbulb, Target, Package, Link2, Pencil, Compass, ClipboardList,
  Terminal, Globe, Cpu, Layers, Database, Server, BrainCircuit, Hammer, PieChart,
} from "lucide-react"

const ICON = "/assets/icons"
const CONN = "/assets/connection"

// Target dot on TOP of card (for cards below the orb)
function TopDot({ category }: { category: Category }) {
  const c = CATEGORY[category]
  return (
    <Handle type="target" id="in" position={Position.Top} isConnectable={false}
      style={{ width: 11, height: 11, background: c.color, border: "2px solid #fff",
        boxShadow: `0 0 0 3px ${c.color}40`, top: -6, left: "50%" }} />
  )
}

// Target dot on BOTTOM of card (for cards above the orb)
function BottomDot({ category, style }: { category: Category; style?: React.CSSProperties }) {
  const c = CATEGORY[category]
  return (
    <Handle type="target" id="in" position={Position.Bottom} isConnectable={false}
      style={{ width: 11, height: 11, background: c.color, border: "2px solid #fff",
        boxShadow: `0 0 0 3px ${c.color}40`, bottom: -6, left: "50%", ...style }} />
  )
}

function MobileRenderer() {
  return (
    <Card style={{ width: 440 }}>
      <BottomDot category="renderer" />
      <CatLabel category="renderer">Renderer Process</CatLabel>
      <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: 6 }}>
        <div style={{ background: "rgba(255,255,255,0.55)", border: "1px solid rgba(148,163,184,0.14)", borderRadius: 8, padding: "5px 8px" }}>
          <div style={{ fontSize: 11, fontWeight: 800, color: "#1e293b", marginBottom: 5, display: "flex", alignItems: "center", gap: 5 }}>
            <span style={{ width: 6, height: 6, borderRadius: "50%", flexShrink: 0, background: "#3b82f6" }} />Chat UI
          </div>
          <PillGrid pills={[
            { label: "Interleaved streaming", icon: MessageSquare }, { label: "Context ring", icon: Zap },
            { label: "Auto-compaction", icon: RefreshCw }, { label: "Chat & Code modes", icon: MessagesSquare },
          ]} />
        </div>
        <div style={{ background: "rgba(255,255,255,0.55)", border: "1px solid rgba(148,163,184,0.14)", borderRadius: 8, padding: "5px 8px" }}>
          <div style={{ fontSize: 11, fontWeight: 800, color: "#1e293b", marginBottom: 5, display: "flex", alignItems: "center", gap: 5 }}>
            <span style={{ width: 6, height: 6, borderRadius: "50%", flexShrink: 0, background: "#2563eb" }} />Live Editors
          </div>
          <PillGrid pills={[
            { label: "Monaco", icon: PenLine }, { label: "Analytics", icon: BarChart3 },
            { label: "Notebooks", icon: NotebookPen }, { label: "Pipelines", img: `${ICON}/flow.svg` },
            { label: "SQL Editor", img: `${ICON}/duckdb.svg` },
          ]} />
        </div>
      </div>
    </Card>
  )
}

function MobileConnected() {
  return (
    <Card style={{ width: 440 }}>
      <BottomDot category="connected" />
      <CatLabel category="connected" icon={Database}>Connected Systems</CatLabel>
      <PillGrid pills={[
        { label: "Postgres", img: `${CONN}/postgresql.svg` }, { label: "Snowflake", img: `${CONN}/snowflake.svg` },
        { label: "BigQuery", img: `${CONN}/bigquery.svg` }, { label: "Redshift", img: `${CONN}/redshift.svg` },
        { label: "DuckDB", img: `${CONN}/duckdb.svg` }, { label: "S3", img: `${CONN}/s3_bucket.svg` },
        { label: "GCS", img: `${CONN}/googlecloud.svg` }, { label: "Azure Blob", img: `${CONN}/azure_blob.svg` },
      ]} />
    </Card>
  )
}

function MobileProviders() {
  return (
    <Card style={{ width: 440 }}>
      <TopDot category="providers" />
      <CatLabel category="providers" icon={Cpu}>AI Providers</CatLabel>
      <SubLabel>Manager &amp; Secure</SubLabel>
      <PillGrid style={{ marginTop: 4 }} pills={[
        { label: "CRUD", icon: Package }, { label: "Test connect", icon: FlaskConical },
        { label: "Model discovery", icon: Search }, { label: "Keytar", icon: KeyRound },
      ]} />
      <SubLabel style={{ marginTop: 8 }}>Cloud · Local</SubLabel>
      <PillGrid style={{ marginTop: 4 }} pills={[
        { label: "OpenAI", img: `${CONN}/openai.svg` }, { label: "Anthropic", img: `${CONN}/anthropic.svg` },
        { label: "Gemini", img: `${CONN}/google.svg` }, { label: "Ollama", img: `${CONN}/ollama.svg` },
        { label: "LM Studio", img: `${CONN}/lmstudio.svg` }, { label: "OpenAI Compat", img: `${CONN}/openai_compatible.svg` },
      ]} />
    </Card>
  )
}

function MobileMemory() {
  return (
    <Card style={{ width: 440 }}>
      <TopDot category="memory" />
      <CatLabel category="memory" icon={BrainCircuit}>Agent Memory</CatLabel>
      <SubLabel>Agent Memory (OKF v0.2)</SubLabel>
      <PillGrid style={{ marginTop: 4 }} pills={[
        { label: "MEMORY.md", icon: Brain }, { label: "wiki_search/read", icon: Search },
        { label: "wiki_update", icon: Pencil }, { label: "archive", img: `${ICON}/collection.svg` },
        { label: "Refresh pipeline", img: `${ICON}/flow.svg` },
      ]} />
      <SubLabel style={{ marginTop: 8 }}>Project Memory</SubLabel>
      <PillGrid style={{ marginTop: 4 }} pills={[
        { label: "AGENTS.md", img: `${ICON}/git-branch.svg` }, { label: "Project scoped", icon: Target },
        { label: "Persona", img: `${ICON}/bot.svg` }, { label: "Rules", icon: ClipboardList },
        { label: "Context", icon: Compass },
      ]} />
    </Card>
  )
}

function MobileSkills() {
  return (
    <Card style={{ width: 440 }}>
      <TopDot category="skills" />
      <CatLabel category="skills" icon={Layers}>Skills</CatLabel>
      <SubLabel>Skill Discovery</SubLabel>
      <PillGrid style={{ marginTop: 4 }} pills={[
        { label: "skill-ls", icon: Brain }, { label: "skill-install", icon: Package },
        { label: "skill-search", icon: Search }, { label: "loadSkill tool", icon: Puzzle },
      ]} />
      <SubLabel style={{ marginTop: 8 }}>Skill Sources · Shell</SubLabel>
      <PillGrid style={{ marginTop: 4 }} pills={[
        { label: "SKILL.md", icon: ClipboardList }, { label: "skills.sh", icon: Lightbulb },
        { label: "Project scoped", icon: Target }, { label: "Skill registry", icon: Package },
        { label: "Skill deps", icon: Link2 },
      ]} />
    </Card>
  )
}

function MobileTools() {
  return (
    <Card style={{ width: 440 }}>
      <TopDot category="tools" />
      <CatLabel category="tools" icon={Hammer}>Native Tooling</CatLabel>
      <SubLabel>DBT &amp; Filesystem</SubLabel>
      <PillGrid style={{ marginTop: 4 }} pills={[
        { label: "Run / Test / Compile", img: `${ICON}/dbt-bit_tm.svg` },
        { label: "Read / Write Model", img: `${ICON}/dbt-black.svg` },
        { label: "List Models & Logs", img: `${ICON}/dbt-bit_tm.svg` },
        { label: "Read / Write File", img: `${ICON}/folder.svg` },
        { label: "List Directory", img: `${ICON}/collection.svg` },
      ]} />
      <SubLabel style={{ marginTop: 8 }}>Analytics Reports</SubLabel>
      <PillGrid style={{ marginTop: 4 }} pills={[
        { label: "Read / Write Page", icon: BarChart3 }, { label: "Run Page", icon: Zap },
        { label: "Tables · Charts · Pies", icon: PieChart },
      ]} />
      <SubLabel style={{ marginTop: 8 }}>Studio-Native</SubLabel>
      <PillGrid style={{ marginTop: 4 }} pills={[
        { label: "SQL Query", img: `${ICON}/duckdb.svg` }, { label: "Schema Extract", img: `${ICON}/duckdb.svg` },
        { label: "DuckLake Query", img: `${ICON}/duck-lake.svg` }, { label: "Cloud Objects", img: `${CONN}/s3_bucket.svg` },
        { label: "Monaco Editor", icon: PenLine }, { label: "CLI · dbt run", icon: Terminal },
        { label: "Connections", img: `${ICON}/flow.svg` }, { label: "Notebooks", icon: NotebookPen },
        { label: "HTTP / SSE · stdio", icon: Globe },
      ]} />
    </Card>
  )
}

function MobileMcp() {
  return (
    <Card style={{ width: 440 }}>
      <TopDot category="mcp" />
      <CatLabel category="mcp" icon={Server}>MCP Servers</CatLabel>
      <PillGrid pills={[
        { label: "DuckDB MCP", img: `${CONN}/duckdb.svg` }, { label: "dbt Core", img: `${ICON}/dbt-bit_tm.svg` },
        { label: "Rosetta CLI", icon: Compass }, { label: "DuckLake", img: `${ICON}/duck-lake.svg` },
        { label: "User servers", icon: Puzzle },
      ]} />
    </Card>
  )
}

const mobileNodeTypes = {
  ...desktopNodeTypes,
  renderer: MobileRenderer,
  providers: MobileProviders,
  memory: MobileMemory,
  skills: MobileSkills,
  tools: MobileTools,
  connected: MobileConnected,
  mcp: MobileMcp,
}

// ─── Layout ───────────────────────────────────────────────────────────────────
// Canvas: 920px wide
// Center = 460
// Renderer (560px): x = 460 - 280 = 180
// Orb (170px):      x = 460 - 85  = 375
// Col L (440px):    x = 10
// Col R (440px):    x = 470  (10 + 440 + 20)
// Row gaps: renderer bottom ~170px, orb at y=190, orb bottom ~430
// Cards rows start at y=470 with ~290px row height
// ─────────────────────────────────────────────────────────────────────────────
const L = 10
const R = 470

const nodes: Node[] = [
  // Top row — 2 cards side by side, centered
  { id: "renderer",  type: "renderer",  position: { x: 10,  y: 10   }, data: {} },
  { id: "connected", type: "connected", position: { x: 470, y: 10   }, data: {} },
  // Orb centered below top row
  { id: "orb",       type: "orb",       position: { x: 375, y: 260  }, data: {} },
  // Left col — 3 cards
  { id: "providers", type: "providers", position: { x: L,   y: 520  }, data: {} },
  { id: "skills",    type: "skills",    position: { x: L,   y: 820  }, data: {} },
  { id: "mcp",       type: "mcp",       position: { x: L,   y: 1110 }, data: {} },
  // Right col — 2 cards
  { id: "memory",    type: "memory",    position: { x: R,   y: 520  }, data: {} },
  { id: "tools",     type: "tools",     position: { x: R,   y: 830  }, data: {} },
]

const spokes: Category[] = ["renderer", "providers", "skills", "connected", "mcp", "tools", "memory"]

const edges: FlowEdge[] = spokes.map((cat, i) => ({
  id: `orb-${cat}`,
  source: "orb",
  sourceHandle: cat,
  target: cat,
  targetHandle: "in",
  type: "flow",
  data: { category: cat, delay: (i * 0.4) % 2.8 },
}))

function Defs() {
  return (
    <svg width="0" height="0" style={{ position: "absolute" }} aria-hidden>
      <defs>
        {spokes.map((cat) => {
          const [a, b] = CATEGORY[cat].grad
          return (
            <linearGradient key={cat} id={`g-${cat}`} x1="0" y1="0" x2="1" y2="0">
              <stop offset="0%" stopColor={a} />
              <stop offset="100%" stopColor={b} />
            </linearGradient>
          )
        })}
      </defs>
    </svg>
  )
}

function Canvas() {
  const { fitView } = useReactFlow()
  const refit = useCallback(() => fitView({ padding: 0.03, duration: 0 }), [fitView])
  useEffect(() => {
    window.addEventListener("resize", refit)
    return () => window.removeEventListener("resize", refit)
  }, [refit])

  return (
    <ReactFlow
      nodes={nodes} edges={edges}
      nodeTypes={mobileNodeTypes} edgeTypes={edgeTypes}
      fitView fitViewOptions={{ padding: 0.03 }}
      minZoom={0.1} maxZoom={2}
      nodesDraggable={false} nodesConnectable={false} nodesFocusable={false}
      edgesFocusable={false} elementsSelectable={false}
      panOnDrag={false} panOnScroll={false}
      zoomOnScroll={false} zoomOnPinch={false} zoomOnDoubleClick={false}
      preventScrolling={false} proOptions={{ hideAttribution: true }}
      onInit={() => refit()}
    />
  )
}

export function MobileDiagram() {
  return (
    <div style={{
      width: "min(100vw, calc(100vh * 9 / 16))",
      height: "min(100vh, calc(100vw * 16 / 9))",
      margin: "0 auto",
      position: "relative",
      overflow: "hidden",
      background:
        "radial-gradient(circle at top center, rgba(249,115,22,0.12), transparent 40%)," +
        "radial-gradient(circle at bottom center, rgba(59,130,246,0.08), transparent 40%)," +
        "linear-gradient(180deg, #fefbf7 0%, #f8fafc 60%, #eef2ff 100%)",
    }}>
      <style>{`
        .rosetta-rings .rosetta-ring{position:absolute;border-radius:50%;border:1.5px solid transparent;transform-origin:center}
        .rosetta-rings .r1{inset:-24px;border-top-color:rgba(234,88,12,0.6);border-right-color:rgba(251,146,60,0.4);border-bottom-color:rgba(217,119,6,0.5);border-left-color:rgba(234,88,12,0.4);animation:rosetta-spin 18s linear infinite}
        .rosetta-rings .r2{inset:-48px;border-top-color:rgba(251,146,60,0.45);border-left-color:rgba(245,158,11,0.4);border-bottom-color:rgba(234,88,12,0.3);animation:rosetta-spin 26s linear infinite reverse}
        .rosetta-rings .r3{inset:-76px;border-top-color:rgba(234,88,12,0.3);border-right-color:rgba(217,119,6,0.35);opacity:.8;animation:rosetta-spin 36s linear infinite}
        @keyframes rosetta-spin{to{transform:rotate(360deg)}}
        @keyframes rosetta-dash{to{stroke-dashoffset:-32}}
        .react-flow__renderer,.react-flow__pane{cursor:default!important}
        .react-flow__handle{opacity:1!important}
        .react-flow__edge{pointer-events:none}
      `}</style>
      <Defs />
      <ReactFlowProvider><Canvas /></ReactFlowProvider>
    </div>
  )
}
