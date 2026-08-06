"use client"

import { getBezierPath, type EdgeProps, type Edge } from "@xyflow/react"
import { CATEGORY, type Category } from "./primitives"

export type FlowEdgeData = { category: Category; delay?: number }
export type FlowEdge = Edge<FlowEdgeData, "flow">

/**
 * A richly styled spoke edge:
 *  - a wide blurred glow underlay in the category color
 *  - the main gradient stroke with an animated flowing dash
 *  - a bright "data packet" that travels from the orb to the card
 *  - a pulsing ring at the arrival point on the card
 */
export function FlowEdgeView({
  sourceX,
  sourceY,
  targetX,
  targetY,
  sourcePosition,
  targetPosition,
  data,
}: EdgeProps<FlowEdge>) {
  const category = data?.category ?? "renderer"
  const delay = data?.delay ?? 0
  const color = CATEGORY[category].color

  const [path] = getBezierPath({
    sourceX,
    sourceY,
    targetX,
    targetY,
    sourcePosition,
    targetPosition,
    curvature: 0.4,
  })

  return (
    <g className="rosetta-edge">
      {/* 1. soft glow underlay */}
      <path
        d={path}
        fill="none"
        stroke={color}
        strokeWidth={10}
        strokeOpacity={0.16}
        strokeLinecap="round"
        style={{ filter: "blur(3px)" }}
      />

      {/* 2. base gradient track (faint, solid) */}
      <path d={path} fill="none" stroke={`url(#g-${category})`} strokeWidth={2} strokeOpacity={0.35} strokeLinecap="round" />

      {/* 3. animated flowing dash on top */}
      <path
        d={path}
        fill="none"
        stroke={`url(#g-${category})`}
        strokeWidth={2.75}
        strokeLinecap="round"
        strokeDasharray="7 9"
        style={{ animation: `rosetta-dash 1.1s linear infinite`, animationDelay: `${delay}s` }}
      />

      {/* 4. traveling data packet */}
      <circle r={3.4} fill="#ffffff" stroke={color} strokeWidth={1.7}>
        <animateMotion dur="2.8s" repeatCount="indefinite" path={path} rotate="auto" begin={`${delay}s`} />
      </circle>

      {/* 5. pulsing arrival ring on the card side */}
      <circle cx={targetX} cy={targetY} r={4} fill="none" stroke={color} strokeWidth={1.4}>
        <animate attributeName="r" values="4;10;4" dur="2.4s" repeatCount="indefinite" begin={`${delay}s`} />
        <animate attributeName="stroke-opacity" values="0.6;0;0.6" dur="2.4s" repeatCount="indefinite" begin={`${delay}s`} />
      </circle>
      {/* solid arrival dot */}
      <circle cx={targetX} cy={targetY} r={3.4} fill={color} stroke="#fff" strokeWidth={1.4} />
    </g>
  )
}

export const edgeTypes = { flow: FlowEdgeView }
