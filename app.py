from flask import Flask, render_template, request
import os
import random

app = Flask(__name__)

# Simple AI logic (improved)
teams_strength = {
    "india": 90,
    "australia": 88,
    "england": 85,
    "pakistan": 83,
    "new zealand": 82,
    "south africa": 84
}

@app.route("/", methods=["GET", "POST"])
def home():
    result = None

    if request.method == "POST":
        team = request.form.get("team").lower()

        base = teams_strength.get(team, random.randint(60, 75))
        opponent = random.randint(65, 90)

        win_prob = int((base / (base + opponent)) * 100)

        if win_prob > 60:
            verdict = "🔥 Strong chance to win"
        elif win_prob > 45:
            verdict = "⚖️ Match close hai"
        else:
            verdict = "😬 Low chance"

        result = {
            "team": team.upper(),
            "prob": win_prob,
            "verdict": verdict
        }

    return render_template("index.html", result=result)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
