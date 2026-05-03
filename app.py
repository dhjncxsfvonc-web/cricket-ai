from flask import Flask, request, jsonify

app = Flask(__name__)

# Simple logic (demo AI)
def predict_team(team):
    team = team.lower()
    if team == "india":
        return "🔥 India ke jeetne ke chances high hain!"
    elif team == "australia":
        return "💪 Australia strong team hai!"
    elif team == "england":
        return "⚡ England aggressive khel sakta hai!"
    else:
        return f"🤔 {team} ka match unpredictable ho sakta hai!"

# Website UI
@app.route("/", methods=["GET", "POST"])
def home():
    result = ""

    if request.method == "POST":
        team = request.form.get("team")
        result = predict_team(team)

    return f"""
    <html>
    <head>
        <title>Cricket AI Pro</title>
        <style>
            body {{
                background: linear-gradient(to right, #000428, #004e92);
                color: white;
                text-align: center;
                font-family: Arial;
                padding-top: 80px;
            }}
            input {{
                padding: 12px;
                width: 260px;
                border-radius: 10px;
                border: none;
            }}
            button {{
                padding: 12px 25px;
                border: none;
                border-radius: 10px;
                background: orange;
                font-weight: bold;
                cursor: pointer;
            }}
            button:hover {{
                background: yellow;
            }}
            .box {{
                margin-top: 20px;
                font-size: 20px;
            }}
        </style>
    </head>
    <body>
        <h1>🏏 Cricket AI Predictor PRO</h1>

        <form method="POST">
            <input type="text" name="team" placeholder="Team name likho" required>
            <br><br>
            <button type="submit">Predict</button>
        </form>

        <div class="box">{result}</div>

        <p style="margin-top:40px; font-size:12px;">
        API bhi available hai 👉 /api?team=india
        </p>
    </body>
    </html>
    """

# API endpoint (future app use)
@app.route("/api")
def api():
    team = request.args.get("team", "")
    result = predict_team(team)
    return jsonify({"team": team, "prediction": result})

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
