from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""

    if request.method == "POST":
        team = request.form.get("team")
        
        # simple AI logic (demo)
        if team.lower() == "india":
            result = "🔥 India ke jeetne ke chances high hain!"
        else:
            result = f"🤔 {team} ka match tough ho sakta hai!"

    return f"""
    <html>
    <head>
        <title>Cricket AI</title>
    </head>
    <body style="text-align:center; font-family:sans-serif;">
        <h1>🏏 Cricket AI Predictor</h1>

        <form method="POST">
            <input type="text" name="team" placeholder="Team name likho" required>
            <br><br>
            <button type="submit">Predict</button>
        </form>

        <h2>{result}</h2>
    </body>
    </html>
    """

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
