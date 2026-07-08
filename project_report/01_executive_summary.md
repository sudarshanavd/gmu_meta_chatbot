# 01. Executive Summary

## 📌 Project Overview
The **GM University (GMU) Admissions WhatsApp Marketing Platform** is an automated, interactive chat assistant and data capture system designed to optimize the prospective student enrollment pipeline for the 2026-2027 academic year. 

By leveraging Meta's official WhatsApp Business Platform API, the system engages students directly on their preferred communication channel, enabling them to:
1. Browse Undergraduate (UG) and Postgraduate (PG) programs.
2. Drill down into specific Faculties, Schools, and Branches.
3. Access detailed course guidelines, program fees, durations, and direct website links.

Simultaneously, a secure, React-based web dashboard allows the GMU admissions helpdesk and marketing teams to monitor engagement, analyze interest trends, and export clean lead lists for telephone outreach.

---

## 🎯 Key Business Objectives
*   **Scale Lead Capture**: Automate initial student interactions and course discoveries 24/7 without requiring manual human agents.
*   **Enrich Lead Quality**: Automatically decode and capture the student's exact academic preferences (e.g., Level, Faculty, School, and Branch) based on their interactive menu choices.
*   **Identify Trends**: Provide visual insights into which faculties and branches are experiencing the highest student interest.
*   **Enable Seamless Outreach**: Provide the helpdesk team with clean, filterable student lists and CSV downloads containing validated WhatsApp IDs and names.

---

## 💎 Core Platform Features

### 1. Interactive WhatsApp Journey
*   **Interactive Controls**: Employs WhatsApp interactive buttons (up to 3 options) and list menus (up to 10 options per section) to guide students cleanly through the course tree.
*   **Frictionless Navigation**: Eliminates text entry friction by using interactive taps, which prevents typos and ensures standardized data logging.
*   **State-Aware Tracking**: Captures the exact academic program a student clicked on, maintaining a structured record of their interest journey.

### 2. Intelligent Interest Decoder
*   **Code Parsing**: Translates condensed button/list reply IDs (e.g., `AAAA` for UG CSE, `BFAB` for PG Professional MBA) into human-readable strings (e.g., `UG › Faculty of Engineering & Tech › CSE`).
*   **Transition Persistence**: Features an intelligent hierarchy-aware database update policy. If a user previously navigated to a specific branch (e.g., CSE) and subsequently restarts the bot, their detailed interest is preserved rather than overwritten by generic "Unknown" or high-level selections.

### 3. Analytics Dashboard
*   **Security First**: Features JWT-based admin authentication, session invalidation, and password rotation.
*   **Interactive Charts**: Provides visual insights including total lead count, active daily unique visitors, top interest branch, distribution by level, and daily visit timeline graphs.
*   **Filterable Lead Ledger**: Enables searching across student names, phone numbers, and WhatsApp IDs, with filtering by academic level (UG/PG) and faculty.
*   **CSV Exports**: Offers clean CSV extraction formatted correctly for Microsoft Excel import, removing raw interest codes to display clean, student-friendly labels.
