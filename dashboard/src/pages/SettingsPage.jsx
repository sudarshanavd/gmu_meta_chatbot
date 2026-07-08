import { useState } from 'react'
import toast from 'react-hot-toast'
import { changePassword } from '../api'

export default function SettingsPage() {
  const username = localStorage.getItem('gmu_username') || 'admin'
  const [form, setForm] = useState({ old_password: '', new_password: '', confirm: '' })
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState('')
  const [success, setSuccess] = useState('')

  function handleChange(e) {
    setForm(f => ({ ...f, [e.target.name]: e.target.value }))
    setError('')
    setSuccess('')
  }

  async function handleSubmit(e) {
    e.preventDefault()
    if (form.new_password !== form.confirm) { setError('New passwords do not match.'); return }
    if (form.new_password.length < 6)       { setError('New password must be at least 6 characters.'); return }
    setLoading(true)
    try {
      await changePassword(username, form.old_password, form.new_password)
      setSuccess('Password changed successfully!')
      setForm({ old_password: '', new_password: '', confirm: '' })
      toast.success('Password updated! 🎉')
    } catch (err) {
      setError(err?.response?.data?.detail || 'Failed to change password.')
    } finally {
      setLoading(false)
    }
  }

  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: 20, maxWidth: 520 }}>
      {/* Change Password */}
      <div className="settings-card">
        <h2 style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" style={{ color: 'var(--gold-400)' }}>
            <rect x="3" y="11" width="18" height="11" rx="2" ry="2" />
            <path d="M7 11V7a5 5 0 0 1 10 0v4" />
          </svg>
          <span>Change Password</span>
        </h2>
        <p>Update your admin dashboard password. Minimum 6 characters.</p>

        <form onSubmit={handleSubmit} className="login-form">
          <div className="form-group">
            <label htmlFor="old_password">Current Password</label>
            <input
              id="old_password" name="old_password" type="password"
              placeholder="••••••••" value={form.old_password}
              onChange={handleChange} required
            />
          </div>
          <div className="form-group">
            <label htmlFor="new_password">New Password</label>
            <input
              id="new_password" name="new_password" type="password"
              placeholder="Min. 6 characters" value={form.new_password}
              onChange={handleChange} required
            />
          </div>
          <div className="form-group">
            <label htmlFor="confirm_password">Confirm New Password</label>
            <input
              id="confirm_password" name="confirm" type="password"
              placeholder="Repeat new password" value={form.confirm}
              onChange={handleChange} required
            />
          </div>
          {error && (
            <div className="error-msg" style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
                <circle cx="12" cy="12" r="10" />
                <line x1="12" y1="8" x2="12" y2="12" />
                <line x1="12" y1="16" x2="12.01" y2="16" />
              </svg>
              <span>{error}</span>
            </div>
          )}
          {success && (
            <div className="success-msg" style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
                <polyline points="20 6 9 17 4 12" />
              </svg>
              <span>{success}</span>
            </div>
          )}
          <button type="submit" className="btn-primary" disabled={loading} style={{ display: 'flex', alignItems: 'center', justifyContent: 'center', gap: 8 }}>
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
              <rect x="3" y="11" width="18" height="11" rx="2" ry="2" />
              <path d="M7 11V7a5 5 0 0 1 10 0v4" />
            </svg>
            <span>{loading ? 'Updating…' : 'Update Password'}</span>
          </button>
        </form>
      </div>

      {/* DB Info */}
      <div className="settings-card">
        <h2 style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" style={{ color: 'var(--gold-400)' }}>
            <rect x="2" y="2" width="20" height="8" rx="2" ry="2" />
            <rect x="2" y="14" width="20" height="8" rx="2" ry="2" />
            <line x1="6" y1="6" x2="6.01" y2="6" />
            <line x1="6" y1="18" x2="6.01" y2="18" />
          </svg>
          <span>Database Configuration</span>
        </h2>
        <p>Current storage settings. Add env vars to switch to MySQL.</p>
        <div style={{ display: 'flex', flexDirection: 'column', gap: 0 }}>
          {[
            { label: 'Current Engine',    value: 'SQLite (local file)' },
            { label: 'Database File',     value: 'admissions/admissions.db' },
            { label: 'Switch to MySQL',   value: 'Set DB_TYPE=mysql in .env' },
            { label: 'MySQL Vars Needed', value: 'MYSQL_HOST · MYSQL_USER · MYSQL_PASSWORD · MYSQL_DATABASE' },
          ].map((r, i, arr) => (
            <div key={r.label} style={{
              display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start',
              padding: '11px 0',
              borderBottom: i < arr.length - 1 ? '1px solid rgba(255,255,255,0.05)' : 'none',
              gap: 12,
            }}>
              <span style={{ color: 'var(--slate-500)', fontSize: 12, flexShrink: 0 }}>{r.label}</span>
              <span style={{ color: 'var(--slate-200)', fontSize: 12, fontWeight: 500, textAlign: 'right' }}>
                {r.value}
              </span>
            </div>
          ))}
        </div>
      </div>

      {/* About */}
      <div className="settings-card">
        <h2 style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" style={{ color: 'var(--gold-400)' }}>
            <circle cx="12" cy="12" r="10" />
            <line x1="12" y1="16" x2="12" y2="12" />
            <line x1="12" y1="8" x2="12.01" y2="8" />
          </svg>
          <span>About</span>
        </h2>
        <p style={{ marginBottom: 0 }}>
          GM University Admissions Dashboard captures student program interests from the WhatsApp
          helpdesk bot and presents them as analytics. Each student interaction is decoded from a
          positional code (e.g. <strong style={{ color: 'var(--gold-400)' }}>abaa</strong> → UG › Faculty of Commerce & Management › School of Commerce › BCom General)
          and stored automatically.
        </p>
      </div>
    </div>
  )
}
