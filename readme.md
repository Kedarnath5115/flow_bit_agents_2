# 🧠 Multi-Agent Document Classifier and Router

This project is a **multi-agent AI system** that processes documents in **PDF, JSON, or Email (text)** format. It classifies both the **format** and **intent** (e.g., Invoice, RFQ, Complaint), routes the input to the appropriate **processing agent**, and logs all metadata and extracted content into a **shared memory** (Redis or SQLite).

---

## 📌 Objective

✔️ Build a multi-agent system that:
- Accepts various document formats  
- Detects document **type** and **intent**  
- Extracts relevant information  
- Maintains traceable, centralized **context/memory**

---

## 🧠 Agents Overview

### 1. 🔍 Classifier Agent
- Accepts raw input (file/email/JSON)
- Detects:
  - **Format**: PDF, JSON, Email  
  - **Intent**: RFQ, Invoice, Complaint, etc.
- Logs metadata to memory
- Routes to appropriate agent

### 2. 🧾 JSON Agent
- Accepts structured JSON
- Extracts and normalizes fields
- Flags anomalies or missing data
- Logs output to memory

### 3. 📧 Email Agent
- Accepts email content
- Extracts:
  - Sender  
  - Subject/body  
  - Urgency and intent
- Formats output for CRM usage
- Logs to memory

---

## 🗃️ Shared Memory Module

Backed by **Redis** or **SQLite**, the memory layer stores:
- Source and format
- Timestamp
- Sender info
- Intent
- Extracted fields
- Thread or conversation ID

---

## 📂 Project Structure

multi-agent-system/
├── agents/
│ ├── classifier_agent.py
│ ├── email_agent.py
│ └── json_agent.py
│
├── memory/
│ ├── redis_store.py
│ └── schema.json
│
├── inputs/
│ ├── sample_invoice.json
│ ├── sample_email.txt
│ └── sample_complaint.pdf
│
├── outputs/
│ └── logs.json
│
├── demo/
│ └── demo_video.mp4
│
├── main.py
├── requirements.txt
└── README.md
