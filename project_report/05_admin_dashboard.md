# 05. Admin Dashboard Frontend

The administration panel is a Single Page Application (SPA) built using **React** and **Vite**. It features a modern user interface, responsive layout, interactive data visualizations, and secure session management.

---

## 🔒 Security & Authentication Architecture

### 1. Token-Based Authentication
*   **JWT Handshake**: Upon loading `/login`, the administrator enters credentials which are validated by the FastAPI backend using a SHA256 hashed matching algorithm.
*   **Token Persistence**: A successful login returns a JWT Bearer Token, which the frontend stores in the browser's `localStorage` as `gmu_token`.
*   **Authenticated API Clients**: All outgoing analytical requests to `/admissions/stats` or `/admissions/students` append this token automatically in the `Authorization: Bearer <token>` header.

### 2. Frontend Route Guards (`ProtectedRoute`)
A react wrapper manages page authorization. If an unauthenticated user attempts to visit any dashboard sub-routes, they are automatically intercepted and redirected to `/login`.

```javascript
function ProtectedRoute({ children }) {
  const token = localStorage.getItem('gmu_token')
  if (!token) return <Navigate to="/login" replace />
  return children
}
```

---

## 📄 Application Pages & Functionality

### 1. Login Page (`LoginPage.jsx`)
*   Provides a clean form containing inputs for the administrator's username and password.
*   Features state-aware error handling, displaying error alerts if credentials are invalid or if the backend service is offline.

### 2. Overview Dashboard (`OverviewPage.jsx`)
Acts as the central analytics command center. It features key KPI metrics cards and visual charts:
*   **Stat Cards**:
    *   **Total Leads**: Aggregate count of all unique prospective students logged.
    *   **Today's Traffic**: Distinct visitor count interacting with the bot in the current calendar day.
    *   **Top Academic Interest**: Highlighting the branch receiving the most hits (e.g. *UG › CSE*).
*   **Visualizations**:
    *   **Level Distribution**: Pie/Bar representation showing the ratio of Undergraduate (UG) vs Postgraduate (PG) applicants.
    *   **Faculty & School Standings**: Identifies the top 10 Faculties and Schools drawing the highest student interest.
    *   **Activity Timeline**: Displays a 14-day chronological chart mapping student interaction spikes.

### 3. Students Ledger (`StudentsPage.jsx`)
A comprehensive, interactive search ledger for lead processing:
*   **Real-time Filters**:
    *   **Search Input**: Performs wildcard queries on names, phone numbers, or WhatsApp IDs.
    *   **Academic Level Dropdown**: Filter list by `UG`, `PG`, or `All`.
    *   **Faculty Input**: Filters records containing specific faculty keywords.
*   **Pagination Controls**: Restricts table views to batches (defaulting to 50 records per page) to optimize performance and prevent DOM rendering lag.
*   **Export trigger**: Triggers a direct file download from `/admissions/export/csv` to extract standard student details directly into Microsoft Excel.

### 4. Settings & Account Profile (`SettingsPage.jsx`)
*   Enables password rotation to comply with organizational security policies.
*   Requires confirming the old password, validation checks for new password lengths, and updates credentials on the backend JSON repository (`admin_creds.json`) securely upon success.
