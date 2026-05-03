
from flask import Flask, request, render_template, jsonify
from model import predict_match, explain_prediction

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""
    probability = ""
    explanation = ""

    if request.method == "POST":
        team = request.form["team"]
        opponent = request.form["opponent"]
        team_score = int(request.form["team_score"])
        opponent_score = int(request.form["opponent_score"])

        winner, prob = predict_match(team, opponent, team_score, opponent_score)
        explanation = explain_prediction(team, opponent, team_score, opponent_score)

        result = f"🏆 Winner: {winner}"
        probability = f"📊 Win Chance: {prob}%"

    return render_template("index.html", result=result, probability=probability, explanation=explanation)


@app.route("/api")
def api():
    team = request.args.get("team")
    opponent = request.args.get("opponent")
    team_score = int(request.args.get("team_score"))
    opponent_score = int(request.args.get("opponent_score"))

    winner, prob = predict_match(team, opponent, team_score, opponent_score)

    return jsonify({
        "winner": winner,
        "probability": prob
    })


if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
