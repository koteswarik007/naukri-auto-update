from flask import Flask
from update_naukri import run_update
import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return "✅ App is running!"

@app.route("/ping")
def ping():
    # This route will be pinged every 10 minutes by cron-job.org to keep Render awake
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"✅ Ping received at {now}", 200

@app.route("/update")
def update():
    try:
        run_update()  # Your existing automation code
        return "✅ Profile updated successfully!", 200
    except Exception as e:
        return f"❌ Update failed: {str(e)}", 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
