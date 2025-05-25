from flask import Flask
from update_naukri import run_update

app = Flask(__name__)

@app.route("/")
def home():
    return "Repl is alive!"

@app.route("/update")
def update():
    run_update()
    return "Profile updated."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
