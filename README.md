##DevOps Sentinel - System Health Monitor

"DevOps Sentinel" is a lightweight system monitoring tool designed to track live server metrics within a Dockerized environment.

## 🚀 Core Features
- **Live Metrics Dashboard**: Real-time tracking of CPU and RAM usage via a web interface (Powered by Flask & psutil).
- **Dockerization**: The application is fully containerized using Docker and Docker Compose for easy deployment across any system.
- **CI/CD Pipeline**: Automated code testing and build verification integrated via GitHub Actions (Verified with Green Ticks ✅).

## 👥 Team & Contributions
- **Novera**: Flask Backend development, Dockerfile creation, System Metrics Logic, and Project Management.
- **Maryam**: Unit Testing (test_app.py) and GitHub Actions Pipeline configuration.

## 🛠️ How to Run Locally
1. Clone this repository.
2. Run the following command in your terminal:
   ```bash
   docker compose up --build
3. Access the dashboard in your browser at: http://localhost:5000
