from flask import Flask, request, render_template_string
import os

app = Flask(__name__)

html = """
<!DOCTYPE html>
<html>
<head>
    <title>Cricket AI Predictor</title>
</head>
<body style="text-align:center; margin-top:50px;">
    <h1>🏏 Cricket AI Predictor</h1>
    <form method="POST">
        <input type="text" name="team" placeholder="Team name likho" required>
        <br><br>
        <button type="submit">Predict</button>
    </form>

    {% if result %}
        <h2>{{ result }}</h2>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""
    if request.method == "POST":
        team = request.form.get("team")

        # Simple AI logic (dummy)
        if team.lower() == "india":
            result = "🔥 India jeet sakti hai (80%)"
        else:
            result = f"🤔 {team} ka chance 50% hai"

    return render_template_string(html, result=result)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
