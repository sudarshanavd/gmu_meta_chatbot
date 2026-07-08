import { useEffect, useState } from 'react'
import {
  AreaChart, Area, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer,
  PieChart, Pie, Cell, Legend,
  BarChart, Bar,
} from 'recharts'
import { fetchStats } from '../api'

const GMU_GOLD = '#c9971f'
const BAR_COLORS = ['#c9971f', '#9e1830', '#2dd4bf', '#a78bfa', '#fb7185', '#60a5fa', '#34d399']
const PIE_COLORS = ['#c9971f', '#9e1830', '#2dd4bf', '#a78bfa']

// SVG Icons
const Icons = {
  TotalStudents: () => (
    <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" style={{ color: 'var(--gold-400)' }}>
      <path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2" />
      <circle cx="9" cy="7" r="4" />
      <path d="M23 21v-2a4 4 0 0 0-3-3.87" />
      <path d="M16 3.13a4 4 0 0 1 0 7.75" />
    </svg>
  ),
  Today: () => (
    <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" style={{ color: 'var(--teal-400)' }}>
      <rect x="3" y="4" width="18" height="18" rx="2" ry="2" />
      <line x1="16" y1="2" x2="16" y2="6" />
      <line x1="8" y1="2" x2="8" y2="6" />
      <line x1="3" y1="10" x2="21" y2="10" />
    </svg>
  ),
  Trophy: () => (
    <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" style={{ color: '#fb7185' }}>
      <path d="M6 9H4.5a2.5 2.5 0 0 1 0-5H6" />
      <path d="M18 9h1.5a2.5 2.5 0 0 0 0-5H18" />
      <path d="M4 22h16" />
      <path d="M10 14.66V17c0 .55-.45 1-1 1H4v2h16v-2h-5c-.55 0-1-.45-1-1v-2.34" />
      <path d="M12 2a7 7 0 0 0-7 7c0 2.5 2 4.67 4.66 5.16a6.92 6.92 0 0 0 4.68 0A5.36 5.36 0 0 0 19 9a7 7 0 0 0-7-7z" />
    </svg>
  ),
  Levels: () => (
    <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" style={{ color: 'var(--purple-400)' }}>
      <path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5" />
    </svg>
  ),
  Chart: () => (
    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" style={{ color: 'var(--gold-400)', marginRight: 8 }}>
      <line x1="18" y1="20" x2="18" y2="10" />
      <line x1="12" y1="20" x2="12" y2="4" />
      <line x1="6" y1="20" x2="6" y2="14" />
    </svg>
  ),
  Pie: () => (
    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" style={{ color: 'var(--gold-400)', marginRight: 8 }}>
      <path d="M21.21 15.89A10 10 0 1 1 8 2.83" />
      <path d="M22 12A10 10 0 0 0 12 2v10z" />
    </svg>
  ),
  Building: () => (
    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" style={{ color: 'var(--gold-400)', marginRight: 8 }}>
      <rect x="4" y="2" width="16" height="20" rx="2" ry="2" />
      <line x1="9" y1="22" x2="9" y2="16" />
      <line x1="15" y1="22" x2="15" y2="16" />
      <line x1="9" y1="16" x2="15" y2="16" />
      <path d="M8 6h.01M16 6h.01M8 10h.01M16 10h.01" />
    </svg>
  )
}

function KpiCard({ icon: Icon, value, label, sub, accent }) {
  return (
    <div className="kpi-card" style={{ '--accent': accent }}>
      <div className="kpi-icon"><Icon /></div>
      <div className="kpi-value">{value}</div>
      <div className="kpi-label">{label}</div>
      {sub && <div className="kpi-sub">{sub}</div>}
    </div>
  )
}

const ChartTooltip = ({ active, payload, label }) => {
  if (!active || !payload?.length) return null
  return (
    <div style={{
      background: 'rgba(26,2,8,0.96)',
      border: '1px solid rgba(201,151,31,0.3)',
      borderRadius: 8, padding: '10px 14px', fontSize: 13,
    }}>
      <p style={{ color: '#94a3b8', marginBottom: 4 }}>{label}</p>
      <p style={{ color: GMU_GOLD, fontWeight: 700 }}>{payload[0].value} interactions</p>
    </div>
  )
}

export default function OverviewPage() {
  const [stats, setStats] = useState(null)
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    fetchStats()
      .then(setStats)
      .catch(console.error)
      .finally(() => setLoading(false))
  }, [])

  if (loading) return <div className="spinner" />
  if (!stats) return (
    <div style={{ color: 'var(--slate-500)', textAlign: 'center', padding: 60 }}>
      Failed to load stats.
    </div>
  )

  const faculties = (stats.by_faculty || []).map(f => ({
    name: f.faculty
      .replace('Faculty of ', '')
      .replace('Faculty for ', '')
      .split(' (')[0]
      .trim()
      .slice(0, 28),
    count: f.count,
  }))

  return (
    <>
      {/* KPI Cards */}
      <div className="kpi-grid">
        <KpiCard
          icon={Icons.TotalStudents}
          value={stats.total_students.toLocaleString()}
          label="Total Students"
          sub="Unique WhatsApp leads"
          accent="linear-gradient(135deg, rgba(201,151,31,0.1), transparent)"
        />
        <KpiCard
          icon={Icons.Today}
          value={stats.today_visitors.toLocaleString()}
          label="Today's Visitors"
          sub="Unique users today"
          accent="linear-gradient(135deg, rgba(20,184,166,0.08), transparent)"
        />
        <KpiCard
          icon={Icons.Trophy}
          value={(stats.top_interest?.count || 0).toLocaleString()}
          label="Top Program Interest"
          sub={stats.top_interest?.label?.split(' › ').pop() || 'N/A'}
          accent="linear-gradient(135deg, rgba(158,24,48,0.12), transparent)"
        />
        <KpiCard
          icon={Icons.Levels}
          value={(stats.by_level || []).map(l => l.level).join(' & ') || '—'}
          label="Active Levels"
          sub={(stats.by_level || []).map(l => `${l.level}: ${l.count}`).join('  ·  ')}
          accent="linear-gradient(135deg, rgba(167,139,250,0.08), transparent)"
        />
      </div>

      {/* Daily Visits + UG/PG Split */}
      <div className="charts-grid">
        <div className="chart-card">
          <h2 style={{ display: 'flex', alignItems: 'center' }}>
            <Icons.Chart />
            <span>Daily Interactions</span>
            <span className="chart-badge" style={{ marginLeft: 8 }}>Last 14 days</span>
          </h2>
          {stats.daily_visits?.length > 0 ? (
            <ResponsiveContainer width="100%" height={230}>
              <AreaChart data={stats.daily_visits}>
                <defs>
                  <linearGradient id="gmuGrad" x1="0" y1="0" x2="0" y2="1">
                    <stop offset="5%"  stopColor={GMU_GOLD} stopOpacity={0.35} />
                    <stop offset="95%" stopColor={GMU_GOLD} stopOpacity={0} />
                  </linearGradient>
                </defs>
                <CartesianGrid strokeDasharray="3 3" stroke="rgba(255,255,255,0.05)" />
                <XAxis
                  dataKey="day"
                  tick={{ fill: '#64748b', fontSize: 10 }}
                  tickLine={false}
                  tickFormatter={d => d?.slice(5) || d}
                />
                <YAxis tick={{ fill: '#64748b', fontSize: 10 }} tickLine={false} axisLine={false} />
                <Tooltip content={<ChartTooltip />} />
                <Area
                  type="monotone"
                  dataKey="count"
                  stroke={GMU_GOLD}
                  strokeWidth={2.5}
                  fill="url(#gmuGrad)"
                  dot={{ fill: GMU_GOLD, r: 3, strokeWidth: 0 }}
                  activeDot={{ r: 5, fill: GMU_GOLD }}
                />
              </AreaChart>
            </ResponsiveContainer>
          ) : (
            <NoData />
          )}
        </div>

        <div className="chart-card">
          <h2 style={{ display: 'flex', alignItems: 'center' }}>
            <Icons.Pie />
            <span>UG vs PG Split</span>
          </h2>
          {stats.by_level?.length > 0 ? (
            <ResponsiveContainer width="100%" height={230}>
              <PieChart>
                <Pie
                  data={stats.by_level}
                  dataKey="count"
                  nameKey="level"
                  cx="50%" cy="50%"
                  innerRadius={55}
                  outerRadius={85}
                  paddingAngle={5}
                >
                  {stats.by_level.map((_, i) => (
                    <Cell key={i} fill={PIE_COLORS[i % PIE_COLORS.length]} />
                  ))}
                </Pie>
                <Legend
                  formatter={v => <span style={{ color: '#94a3b8', fontSize: 12 }}>{v}</span>}
                />
                <Tooltip
                  contentStyle={{
                    background: 'rgba(26,2,8,0.96)',
                    border: '1px solid rgba(201,151,31,0.3)',
                    borderRadius: 8, fontSize: 13,
                  }}
                />
              </PieChart>
            </ResponsiveContainer>
          ) : (
            <NoData />
          )}
        </div>
      </div>

      {/* Faculty bar chart */}
      <div className="chart-card" style={{ marginBottom: 24 }}>
        <h2 style={{ display: 'flex', alignItems: 'center' }}>
          <Icons.Building />
          <span>Students by Faculty</span>
          <span className="chart-badge" style={{ marginLeft: 8 }}>Top 10</span>
        </h2>
        {faculties.length > 0 ? (
          <ResponsiveContainer width="100%" height={Math.max(220, faculties.length * 42)}>
            <BarChart data={faculties} layout="vertical" margin={{ left: 20, right: 24 }}>
              <CartesianGrid strokeDasharray="3 3" stroke="rgba(255,255,255,0.05)" horizontal={false} />
              <XAxis
                type="number"
                tick={{ fill: '#64748b', fontSize: 10 }}
                tickLine={false}
                axisLine={false}
              />
              <YAxis
                dataKey="name"
                type="category"
                width={175}
                tick={{ fill: '#94a3b8', fontSize: 11 }}
                tickLine={false}
              />
              <Tooltip content={<ChartTooltip />} />
              <Bar dataKey="count" radius={[0, 5, 5, 0]}>
                {faculties.map((_, i) => (
                  <Cell key={i} fill={BAR_COLORS[i % BAR_COLORS.length]} />
                ))}
              </Bar>
            </BarChart>
          </ResponsiveContainer>
        ) : (
          <NoData msg="No student data yet — charts will populate as students interact on WhatsApp." />
        )}
      </div>

      {/* School progress bars */}
      {stats.by_school?.length > 0 && (
        <div className="chart-card">
          <h2 style={{ display: 'flex', alignItems: 'center' }}>
            <Icons.Building />
            <span>Interest by School</span>
          </h2>
          <div className="faculty-bar">
            {stats.by_school.slice(0, 8).map((s, i) => {
              const max = stats.by_school[0]?.count || 1
              const pct = Math.round((s.count / max) * 100)
              return (
                <div key={i}>
                  <div className="faculty-bar-label">
                    <span>{s.school?.replace(/ \(.*?\)$/, '')}</span>
                    <span>{s.count} students</span>
                  </div>
                  <div className="faculty-bar-track">
                    <div
                      className="faculty-bar-fill"
                      style={{ width: `${pct}%`, background: BAR_COLORS[i % BAR_COLORS.length] }}
                    />
                  </div>
                </div>
              )
            })}
          </div>
        </div>
      )}
    </>
  )
}

function NoData({ msg }) {
  return (
    <div style={{ textAlign: 'center', padding: '48px 0', color: 'var(--slate-600)', fontSize: 13, display: 'flex', flexDirection: 'column', alignItems: 'center', gap: 12 }}>
      <svg width="36" height="36" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5" strokeLinecap="round" strokeLinejoin="round" style={{ opacity: 0.4 }}>
        <path d="M22 19a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h5l2 3h9a2 2 0 0 1 2 2z" />
      </svg>
      <span>{msg || 'No data yet'}</span>
    </div>
  )
}
