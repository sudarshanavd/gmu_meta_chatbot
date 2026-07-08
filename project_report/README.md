# GM University Admissions WhatsApp Platform & Dashboard
## Project Documentation & Report Index

Welcome to the official technical documentation and project report for the **GM University (GMU) Admissions WhatsApp Marketing Platform and Admin Dashboard**.

This report is compiled to provide the Team Leader, stakeholders, and developers with a comprehensive understanding of the platform's architecture, data models, integration pipelines, and user interfaces.

---

### 📂 Report Structure & Modules

Please navigate through the following modules for detailed insights into the project:

| Module | Document | Description |
| :--- | :--- | :--- |
| **01** | [**Executive Summary**](./01_executive_summary.md) | High-level business goals, core features, value proposition, and technological choices. |
| **02** | [**System Architecture**](./02_system_architecture.md) | Asynchronous webhook pipeline, request lifecycles, and component interactions with a sequence diagram. |
| **03** | [**Database Design**](./03_database_design.md) | SQLite/MySQL database schemas, state preservation logic for prospective students, and visit histories. |
| **04** | [**WhatsApp API Integration**](./04_whatsapp_integration.md) | Technical payload structures, interactive list/button configurations, and the hierarchical interest-code decoder. |
| **05** | [**Admin Dashboard Frontend**](./05_admin_dashboard.md) | React-based Single Page Application (SPA), security protocols, analytical charts, filtering mechanics, and data exports. |

---

### 🛠️ Technology Stack at a Glance

*   **Backend Framework**: FastAPI (Python 3) - for high-performance, asynchronous REST and Webhook processing.
*   **Frontend Framework**: React + Vite (JavaScript) - for a responsive, premium Single Page Application dashboard.
*   **Database Engine**: SQLite (default for development/local storage) and fully compatible with MySQL (configured via `.env` for production scale).
*   **Messaging Interface**: Meta WhatsApp Business Platform API v25.0.
*   **Authentication**: JSON Web Tokens (JWT) with HS256 algorithm and SHA256 hashed credentials.

---

### 🚀 Getting Started (Quick Run)
To run the server locally:
1. Ensure the `.env` file is set up with valid Meta API credentials, verify tokens, and database configs.
2. Run backend: `uvicorn main:app --reload`
3. Run dashboard frontend: `cd dashboard && npm run dev`
4. The dashboard is automatically mounted and served by FastAPI at `http://localhost:8000/dashboard`.
