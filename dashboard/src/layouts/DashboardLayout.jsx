import { useState } from 'react'
import { Outlet, useLocation } from 'react-router-dom'
import Sidebar from '../components/Sidebar'

const PAGE_TITLES = {
  '/':         { title: 'Overview',         sub: 'Admissions analytics at a glance' },
  '/students': { title: 'Student Records',  sub: 'All WhatsApp leads & their program interests' },
  '/settings': { title: 'Settings',         sub: 'Account & dashboard configuration' },
}

export default function DashboardLayout() {
  const location = useLocation()
  const info = PAGE_TITLES[location.pathname] || { title: 'Dashboard', sub: '' }
  const [sidebarOpen, setSidebarOpen] = useState(false)

  return (
    <div className="layout">
      <Sidebar open={sidebarOpen} onClose={() => setSidebarOpen(false)} />

      <div className="main-area">
        <header className="topbar">
          <div className="topbar-left">
            <button
              className="hamburger"
              aria-label="Toggle menu"
              onClick={() => setSidebarOpen(o => !o)}
            >
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.5" strokeLinecap="round" strokeLinejoin="round">
                <line x1="3" y1="12" x2="21" y2="12" />
                <line x1="3" y1="6" x2="21" y2="6" />
                <line x1="3" y1="18" x2="21" y2="18" />
              </svg>
            </button>
            <div className="topbar-title">
              <h1>{info.title}</h1>
              <p>{info.sub}</p>
            </div>
          </div>
          <div className="topbar-right">
            <div className="topbar-badge" style={{ display: 'flex', alignItems: 'center', gap: 6 }}>
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
                <path d="M22 10v6M2 10l10-5 10 5-10 5z" />
                <path d="M6 12v5c0 2 2 3 6 3s6-1 6-3v-5" />
              </svg>
              <span>GM University</span>
            </div>
          </div>
        </header>

        <main className="page-content">
          <Outlet />
        </main>
      </div>
    </div>
  )
}
