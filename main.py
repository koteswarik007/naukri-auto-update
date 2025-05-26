from flask import Flask
from update_naukri import run_update
import datetime
import logging

# Configure logging
logging.basicConfig(filename="update.log", level=logging.INFO, format="%(asctime)s - %(message)s")

app = Flask(__name__)

@app.route("/")
def home():
    return "✅ App is running!", 200

@app.route("/ping")
def ping():
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    logging.info("Ping received at %s", now)
    return "✅ Ping OK", 200

@app.route("/update")
def update():
    try:
        logging.info("🔁 Starting Naukri profile update...")
        run_update()
        logging.info("✅ Profile updated successfully.")
        return "✅ Profile updated successfully", 200
    except Exception as e:
        logging.error("❌ Error during update: %s", str(e))
        return "❌ Failed to update profile", 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
