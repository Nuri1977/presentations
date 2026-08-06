import type { LucideIcon } from "lucide-react"

/* ---------- category color system ---------- */
export type Category = "renderer" | "providers" | "skills" | "connected" | "mcp" | "tools" | "memory"

export const CATEGORY: Record<
  Category,
  { color: string; labelBg: string; labelText: string; grad: [string, string] }
> = {
  renderer: { color: "#3b82f6", labelBg: "#dbeafe", labelText: "#1d4ed8", grad: ["#3b82f6", "#60a5fa"] },
  providers: { color: "#ec4899", labelBg: "#fce7f3", labelText: "#be185d", grad: ["#ec4899", "#f472b6"] },
  skills: { color: "#d946ef", labelBg: "#fae8ff", labelText: "#86198f", grad: ["#d946ef", "#f0abfc"] },
  connected: { color: "#64748b", labelBg: "#e2e8f0", labelText: "#475569", grad: ["#64748b", "#94a3b8"] },
  mcp: { color: "#7c3aed", labelBg: "#ede9fe", labelText: "#6d28d9", grad: ["#7c3aed", "#a78bfa"] },
  tools: { color: "#10b981", labelBg: "#d1fae5", labelText: "#047857", grad: ["#10b981", "#34d399"] },
  memory: { color: "#f59e0b", labelBg: "#fef3c7", labelText: "#b45309", grad: ["#f59e0b", "#fbbf24"] },
}

/* ---------- pill model ---------- */
export type Pill = { label: string; icon?: LucideIcon; img?: string }

/* ---------- frosted card wrapper ---------- */
export function Card({
  children,
  style,
  className,
}: {
  children: React.ReactNode
  style?: React.CSSProperties
  className?: string
}) {
  return (
    <div
      className={className}
      style={{
        background: "rgba(255,255,255,0.82)",
        backdropFilter: "blur(8px)",
        WebkitBackdropFilter: "blur(8px)",
        border: "1px solid rgba(148,163,184,0.18)",
        borderRadius: 14,
        padding: "16px 18px",
        boxShadow: "0 12px 34px rgba(15,23,42,0.09), inset 0 1px 0 rgba(255,255,255,0.9)",
        ...style,
      }}
    >
      {children}
    </div>
  )
}

/* ---------- category label pill ---------- */
export function CatLabel({
  category,
  children,
  icon: Icon,
}: {
  category: Category
  children: React.ReactNode
  icon?: LucideIcon
}) {
  const c = CATEGORY[category]
  return (
    <span
      style={{
        display: "inline-flex",
        alignItems: "center",
        gap: 7,
        padding: "6px 15px 6px 10px",
        borderRadius: 8,
        fontSize: 16,
        fontWeight: 800,
        letterSpacing: "-0.005em",
        marginBottom: 10,
        background: c.labelBg,
        color: c.labelText,
        border: "1px solid rgba(255,255,255,0.6)",
        boxShadow: "0 5px 14px rgba(15,23,42,0.07), inset 0 1px 0 rgba(255,255,255,0.8)",
      }}
    >
      {Icon ? (
        <Icon size={15} strokeWidth={2.5} color={c.labelText} />
      ) : (
        <span
          style={{
            width: 7,
            height: 7,
            borderRadius: "50%",
            background: "currentColor",
            boxShadow: "0 0 0 3px rgba(255,255,255,0.7)",
          }}
        />
      )}
      {children}
    </span>
  )
}

/* ---------- sub-group label ---------- */
export function SubLabel({ children, style }: { children: React.ReactNode; style?: React.CSSProperties }) {
  return (
    <div
      style={{
        fontSize: 12,
        fontWeight: 800,
        textTransform: "uppercase",
        letterSpacing: "0.12em",
        color: "#94a3b8",
        padding: "0 0 0 1px",
        ...style,
      }}
    >
      {children}
    </div>
  )
}

/* ---------- tech pill ---------- */
export function PillView({ pill }: { pill: Pill }) {
  const Icon = pill.icon
  return (
    <span
      style={{
        display: "inline-flex",
        alignItems: "center",
        gap: 6,
        padding: "4px 11px 4px 7px",
        borderRadius: 999,
        background: "rgba(255,255,255,0.9)",
        border: "1px solid rgba(148,163,184,0.18)",
        fontSize: 15,
        fontWeight: 600,
        color: "#0f172a",
        boxShadow: "0 1.5px 4px rgba(15,23,42,0.04)",
        whiteSpace: "nowrap",
        lineHeight: 1.25,
      }}
    >
      <span
        style={{
          width: 20,
          height: 20,
          display: "inline-flex",
          alignItems: "center",
          justifyContent: "center",
          flexShrink: 0,
        }}
      >
        {pill.img ? (
          <img
            src={pill.img || "/placeholder.svg"}
            alt=""
            style={{ width: "100%", height: "100%", objectFit: "contain", display: "block" }}
          />
        ) : Icon ? (
          <Icon size={18} strokeWidth={2.25} color="#475569" />
        ) : null}
      </span>
      {pill.label}
    </span>
  )
}

/* ---------- pill grid ---------- */
export function PillGrid({ pills, style }: { pills: Pill[]; style?: React.CSSProperties }) {
  return (
    <div style={{ display: "flex", flexWrap: "wrap", gap: "7px 8px", ...style }}>
      {pills.map((p) => (
        <PillView key={p.label} pill={p} />
      ))}
    </div>
  )
}
