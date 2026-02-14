# DevOps Sentinel - Live Status Dashboard

### Project Overview
This project is a real-time system monitoring dashboard built for the Git and GitHub CI/CD Task. It provides a live view of CPU and RAM usage.

* **Primary Language:** Python.
* **Framework:** Flask.
* **Containerization:** Docker & Docker Compose.

---

### Branching Strategy
We followed the mandatory branching strategy:
* **feature/maryam-logic:** Individual branch for feature development.
* **dev:** The stable development branch.
* **main/master:** The production-ready branch.

---

### CI/CD Pipeline Stages
Our GitHub Actions pipeline includes the 3 mandatory stages:
1. **Build Stage:** Code checkout and environment setup.
2. **Deploy Stage:** Deployment simulation using Docker with logs.
3. **Test Stage:** Automated endpoint verification.

---

### How to Run Locally
1. Clone the repository.
2. Activate virtual environment: `source venv/bin/activate`.
3. Run: `python3 app.py`.

---

### How to Run via Docker Compose
The application is fully containerized:
```bash
docker compose up -d
