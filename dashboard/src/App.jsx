import { useState, useEffect } from 'react'
import { Routes, Route, Navigate, useNavigate } from 'react-router-dom'
import LoginPage from './pages/LoginPage'
import DashboardLayout from './layouts/DashboardLayout'
import OverviewPage from './pages/OverviewPage'
import StudentsPage from './pages/StudentsPage'
import SettingsPage from './pages/SettingsPage'

function ProtectedRoute({ children }) {
  const token = localStorage.getItem('gmu_token')
  if (!token) return <Navigate to="/login" replace />
  return children
}

export default function App() {
  const navigate = useNavigate()
  const [authed, setAuthed] = useState(!!localStorage.getItem('gmu_token'))

  function handleLogin() {
    setAuthed(true)
    navigate('/', { replace: true })
  }

  return (
    <Routes>
      <Route path="/login" element={
        authed ? <Navigate to="/" replace /> : <LoginPage onLogin={handleLogin} />
      } />

      <Route path="/" element={
        <ProtectedRoute>
          <DashboardLayout />
        </ProtectedRoute>
      }>
        <Route index element={<OverviewPage />} />
        <Route path="students" element={<StudentsPage />} />
        <Route path="settings" element={<SettingsPage />} />
      </Route>

      <Route path="*" element={<Navigate to="/" replace />} />
    </Routes>
  )
}
