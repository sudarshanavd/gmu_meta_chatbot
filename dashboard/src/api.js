import axios from 'axios'

const BASE = '/admissions'

function getToken() {
  return localStorage.getItem('gmu_token')
}

function authHeaders() {
  return { Authorization: `Bearer ${getToken()}` }
}

export async function login(username, password) {
  const res = await axios.post(`${BASE}/login`, { username, password })
  return res.data
}

export async function fetchStudents(params = {}) {
  const res = await axios.get(`${BASE}/students`, {
    headers: authHeaders(),
    params,
  })
  return res.data
}

export async function fetchStats() {
  const res = await axios.get(`${BASE}/stats`, { headers: authHeaders() })
  return res.data
}

export function exportCsvUrl() {
  return `${BASE}/export/csv`
}

export async function changePassword(username, old_password, new_password) {
  const res = await axios.post(
    `${BASE}/change-password`,
    { username, old_password, new_password },
    { headers: authHeaders() }
  )
  return res.data
}
