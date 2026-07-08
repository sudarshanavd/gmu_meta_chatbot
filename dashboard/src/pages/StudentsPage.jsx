import { useEffect, useState, useCallback } from 'react'
import { fetchStudents, exportCsvUrl } from '../api'

function LevelBadge({ level }) {
  const cls = level === 'UG' ? 'badge badge-ug' : level === 'PG' ? 'badge badge-pg' : 'badge badge-na'
  return <span className={cls}>{level || 'N/A'}</span>
}

function formatDate(dateStr) {
  if (!dateStr) return '—'
  try {
    return new Date(dateStr + ' UTC').toLocaleDateString('en-IN', {
      day: '2-digit', month: 'short', year: 'numeric',
      hour: '2-digit', minute: '2-digit',
    })
  } catch {
    return dateStr
  }
}

export default function StudentsPage() {
  const [data, setData] = useState(null)
  const [loading, setLoading] = useState(true)
  const [exporting, setExporting] = useState(false)
  const [search, setSearch] = useState('')
  const [level, setLevel] = useState('')
  const [page, setPage] = useState(1)
  const PAGE_SIZE = 10

  const load = useCallback(async () => {
    setLoading(true)
    try {
      const res = await fetchStudents({ search, level, page, page_size: PAGE_SIZE })
      setData(res)
    } catch (e) {
      console.error(e)
    } finally {
      setLoading(false)
    }
  }, [search, level, page])

  useEffect(() => { load() }, [load])
  useEffect(() => { setPage(1) }, [search, level])

  function handleExport() {
    setExporting(true)
    const token = localStorage.getItem('gmu_token')
    const url = `${exportCsvUrl()}?token=${token}`
    
    fetch(url)
      .then(r => {
        if (!r.ok) throw new Error('Export failed')
        return r.blob()
      })
      .then(blob => {
        const a = document.createElement('a')
        a.href = URL.createObjectURL(blob)
        a.download = 'gmu_admissions_students.csv'
        a.click()
        // Defer revocation to allow the browser to initiate download
        setTimeout(() => URL.revokeObjectURL(a.href), 150)
      })
      .catch(err => {
        console.error(err)
        alert('Failed to export CSV. Please try again.')
      })
      .finally(() => {
        setExporting(false)
      })
  }

  const students = data?.students || []
  const total = data?.total || 0
  const totalPages = Math.ceil(total / PAGE_SIZE)

  const getPageNumbers = () => {
    const pages = []
    if (totalPages <= 7) {
      for (let i = 1; i <= totalPages; i++) {
        pages.push(i)
      }
    } else {
      pages.push(1)
      if (page > 3) {
        pages.push('...')
      }
      const start = Math.max(2, page - 1)
      const end = Math.min(totalPages - 1, page + 1)
      for (let i = start; i <= end; i++) {
        pages.push(i)
      }
      if (page < totalPages - 2) {
        pages.push('...')
      }
      pages.push(totalPages)
    }
    return pages
  }

  return (
    <div className="table-card">
      <div className="table-header">
        <h2 style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" style={{ color: 'var(--gold-400)' }}>
            <path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2" />
            <circle cx="9" cy="7" r="4" />
            <path d="M23 21v-2a4 4 0 0 0-3-3.87" />
            <path d="M16 3.13a4 4 0 0 1 0 7.75" />
          </svg>
          <span>Student Records</span>
          <span style={{ fontSize: 13, color: 'var(--slate-500)', fontWeight: 400 }}>
            ({total} total)
          </span>
        </h2>
        <div className="table-controls">
          <div style={{ position: 'relative', display: 'flex', alignItems: 'center' }}>
            <input
              id="student-search"
              className="search-input"
              type="search"
              placeholder="Search name or phone..."
              value={search}
              onChange={e => setSearch(e.target.value)}
              style={{ paddingLeft: 34 }}
            />
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" style={{ position: 'absolute', left: 12, color: 'var(--slate-500)' }}>
              <circle cx="11" cy="11" r="8" />
              <line x1="21" y1="21" x2="16.65" y2="16.65" />
            </svg>
          </div>
          <select
            id="level-filter"
            className="filter-select"
            value={level}
            onChange={e => setLevel(e.target.value)}
          >
            <option value="">All Levels</option>
            <option value="UG">UG</option>
            <option value="PG">PG</option>
          </select>
          <button
            id="export-csv-btn"
            className="btn-export"
            onClick={handleExport}
            disabled={exporting}
            style={{ display: 'flex', alignItems: 'center', gap: 6 }}
          >
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
              <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4" />
              <polyline points="7 10 12 15 17 10" />
              <line x1="12" y1="15" x2="12" y2="3" />
            </svg>
            <span>{exporting ? 'Exporting...' : 'Export CSV'}</span>
          </button>
        </div>
      </div>

      {loading ? (
        <div className="spinner" />
      ) : students.length === 0 ? (
        <div className="table-empty" style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', gap: 12 }}>
          <svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5" strokeLinecap="round" strokeLinejoin="round" style={{ opacity: 0.4 }}>
            <rect x="2" y="2" width="20" height="20" rx="2.18" ry="2.18" />
            <line x1="7" y1="2" x2="7" y2="22" />
            <line x1="17" y1="2" x2="17" y2="22" />
            <line x1="2" y1="12" x2="22" y2="12" />
          </svg>
          <p>No students found yet.</p>
          <p style={{ fontSize: 12, color: 'var(--slate-600)' }}>
            Students will appear here once they interact with the WhatsApp bot.
          </p>
        </div>
      ) : (
        <>
          <div style={{ overflowX: 'auto' }}>
            <table className="data-table">
              <thead>
                <tr>
                  <th>#</th>
                  <th>Name</th>
                  <th>Phone / WA ID</th>
                  <th>Level</th>
                  <th>Faculty</th>
                  <th className="col-hide-sm">School</th>
                  <th className="col-hide-sm">Branch / Program</th>
                  <th>Visits</th>
                  <th className="col-hide-sm">Last Seen</th>
                </tr>
              </thead>
              <tbody>
                {students.map((s, i) => (
                  <tr key={s.id}>
                    <td style={{ color: 'var(--slate-600)', fontSize: 12 }}>
                      {(page - 1) * PAGE_SIZE + i + 1}
                    </td>
                    <td style={{ fontWeight: 600, color: 'var(--cream-50)' }}>
                      {s.sender_name || '—'}
                    </td>
                    <td>
                      <div style={{ fontSize: 13 }}>{s.phone || s.wa_id}</div>
                      <div style={{ fontSize: 11, color: 'var(--slate-600)' }}>{s.wa_id}</div>
                    </td>
                    <td><LevelBadge level={s.last_level} /></td>
                    <td style={{ fontSize: 12, color: 'var(--slate-300)', maxWidth: 180, overflow: 'hidden', textOverflow: 'ellipsis', whiteSpace: 'nowrap' }}>
                      {s.last_faculty ? s.last_faculty.replace(/ \(.*?\)$/, '') : '—'}
                    </td>
                    <td className="col-hide-sm" style={{ fontSize: 12, color: 'var(--slate-300)', maxWidth: 160, overflow: 'hidden', textOverflow: 'ellipsis', whiteSpace: 'nowrap' }}>
                      {s.last_school ? s.last_school.replace(/ \(.*?\)$/, '') : '—'}
                    </td>
                    <td className="col-hide-sm" style={{ fontSize: 12, maxWidth: 160, overflow: 'hidden', textOverflow: 'ellipsis', whiteSpace: 'nowrap' }}>
                      {s.last_branch || '—'}
                    </td>
                    <td style={{ textAlign: 'center', fontWeight: 700, color: 'var(--gold-400)' }}>
                      {s.visit_count}
                    </td>
                    <td className="col-hide-sm" style={{ fontSize: 11, color: 'var(--slate-500)', whiteSpace: 'nowrap' }}>
                      {formatDate(s.last_seen)}
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>

          {totalPages > 1 && (
            <div className="pagination">
              <span className="pagination-info">
                Showing {(page - 1) * PAGE_SIZE + 1}–{Math.min(page * PAGE_SIZE, total)} of {total}
              </span>
              <div className="pagination-controls">
                <button className="btn-page" onClick={() => setPage(p => p - 1)} disabled={page === 1}>
                  ← Prev
                </button>
                {getPageNumbers().map((p, idx) => (
                  p === '...' ? (
                    <span key={`dots-${idx}`} style={{ padding: '4px 8px', color: 'var(--slate-600)' }}>...</span>
                  ) : (
                    <button
                      key={p}
                      className={`btn-page ${page === p ? 'active' : ''}`}
                      onClick={() => setPage(p)}
                      style={{ padding: '6px 12px', minWidth: 36 }}
                    >
                      {p}
                    </button>
                  )
                ))}
                <button className="btn-page" onClick={() => setPage(p => p + 1)} disabled={page === totalPages}>
                  Next →
                </button>
              </div>
            </div>
          )}
        </>
      )}
    </div>
  )
}
