from flask import Flask, render_template_string
import psutil

app = Flask(__name__)

@app.route('/')
def home():
    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory().percent
    color = "green" if cpu < 80 else "red"
    return f"""
    <html>
        <body style="text-align:center; font-family:Arial; padding-top: 50px;">
            <h1 style="color: {color};">DevOps Sentinel - Live Status</h1>
            <div style="border: 2px solid #ddd; display: inline-block; padding: 20px;">
                <h2>CPU Usage: {cpu}%</h2>
                <h2>RAM Usage: {ram}%</h2>
            </div>
            <p>Status: {"Healthy" if cpu < 80 else "Overloaded"}</p>
        </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
