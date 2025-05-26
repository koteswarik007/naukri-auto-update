from flask import Flask
from update_naukri import run_update

app = Flask(__name__)

@app.route('/')
def home():
    return "Naukri Auto Update is running!"

@app.route('/update')
def update_profile():
    print("🔁 Triggered update route...")
    success = run_update()
    if success:
        print("✅ Profile updated successfully!")
        return "✅ Profile updated successfully"
    else:
        print("❌ Failed to update profile!")
        return "❌ Failed to update profile"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
