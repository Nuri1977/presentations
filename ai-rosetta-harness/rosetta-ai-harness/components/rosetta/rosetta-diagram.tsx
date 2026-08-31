"use client"

import { useCallback, useEffect } from "react"
import { ReactFlow, ReactFlowProvider, useReactFlow, type Node } from "@xyflow/react"
import "@xyflow/react/dist/style.css"
import { nodeTypes } from "./nodes"
import { CATEGORY, type Category } from "./primitives"
import { edgeTypes, type FlowEdge } from "./flow-edge"

// ─── 3-column grid, no overlaps ───────────────────────────────────────────────
//
//  Col A  x=0    w=430   Memory(~290px)   gap=20   Tools(~480px)
//  Col B  x=470  w=780   Renderer(~160px) gap=20   Orb(170px) gap=20  MCP(~120px)
//  Col C  x=1280 w=440   Providers(~220px) gap=20  Skills(~220px) gap=20 Connected(~150px)
//
//  Orb top-left (470 + (780-170)/2 , 200) = (775, 200)  → orb center ≈ (860, 285)
//
//  Total canvas: ~1720 × 870 — fitView at 1440 wide = ~0.82 zoom (readable)
// ─────────────────────────────────────────────────────────────────────────────

const COL_A = 0
const COL_B = 470
const COL_C = 1290

const nodes: Node[] = [
  // ── Col A ──
  { id: "memory",    type: "memory",    position: { x: COL_A, y: 20  }, data: {} },
  { id: "tools",     type: "tools",     position: { x: COL_A, y: 355 }, data: {} },

  // ── Col B ──
  { id: "renderer",  type: "renderer",  position: { x: COL_B + 110, y: 20  }, data: {} },
  { id: "orb",       type: "orb",       position: { x: COL_B + 305, y: 380 }, data: {} },
  { id: "mcp",       type: "mcp",       position: { x: COL_B + 120, y: 720 }, data: {} },

  // ── Col C ──
  { id: "providers", type: "providers", position: { x: COL_C, y: 10  }, data: {} },
  { id: "skills",    type: "skills",    position: { x: COL_C, y: 320 }, data: {} },
  { id: "connected", type: "connected", position: { x: COL_C, y: 620 }, data: {} },
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
  const refit = useCallback(
    () => fitView({ padding: 0.03, duration: 0 }),
    [fitView],
  )

  useEffect(() => {
    window.addEventListener("resize", refit)
    return () => window.removeEventListener("resize", refit)
  }, [refit])

  return (
    <ReactFlow
      nodes={nodes}
      edges={edges}
      nodeTypes={nodeTypes}
      edgeTypes={edgeTypes}
      fitView
      fitViewOptions={{ padding: 0.03 }}
      minZoom={0.3}
      maxZoom={2}
      nodesDraggable={false}
      nodesConnectable={false}
      nodesFocusable={false}
      edgesFocusable={false}
      elementsSelectable={false}
      panOnDrag={false}
      panOnScroll={false}
      zoomOnScroll={false}
      zoomOnPinch={false}
      zoomOnDoubleClick={false}
      preventScrolling={false}
      proOptions={{ hideAttribution: true }}
      onInit={() => refit()}
    />
  )
}

export function RosettaDiagram() {
  return (
    <div
      style={{
        width: "100%",
        height: "100dvh",
        overflow: "hidden",
        background:
          "radial-gradient(circle at top left, rgba(249,115,22,0.10), transparent 28%)," +
          "radial-gradient(circle at top right, rgba(59,130,246,0.08), transparent 30%)," +
          "radial-gradient(circle at bottom center, rgba(236,72,153,0.07), transparent 36%)," +
          "linear-gradient(180deg, #fefbf7 0%, #f8fafc 50%, #eef2ff 100%)",
      }}
    >
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
      <ReactFlowProvider>
        <Canvas />
      </ReactFlowProvider>
    </div>
  )
}
