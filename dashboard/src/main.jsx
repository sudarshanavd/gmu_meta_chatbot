import React from 'react'
import ReactDOM from 'react-dom/client'
import { BrowserRouter } from 'react-router-dom'
import { Toaster } from 'react-hot-toast'
import App from './App'
import './index.css'

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <BrowserRouter basename="/dashboard">
      <App />
      <Toaster
        position="top-right"
        toastOptions={{
          style: {
            background: '#1e2a3a',
            color: '#e2e8f0',
            border: '1px solid #334155',
          },
        }}
      />
    </BrowserRouter>
  </React.StrictMode>
)
