import pandas as pd
from sklearn.ensemble import RandomForestClassifier

data = pd.read_csv("data.csv")

data["team"] = data["team"].astype("category").cat.codes
data["opponent"] = data["opponent"].astype("category").cat.codes

X = data[["team", "opponent", "team_score", "opponent_score"]]
y = data["result"]

model = RandomForestClassifier(n_estimators=200)
model.fit(X, y)

def predict_match(team, opponent, team_score, opponent_score):
    team_code = hash(team) % 100
    opponent_code = hash(opponent) % 100

    proba = model.predict_proba([[team_code, opponent_code, team_score, opponent_score]])[0]
    win_prob = round(proba[1] * 100, 2)

    if proba[1] > 0.5:
        winner = team.upper()
    else:
        winner = opponent.upper()

    return winner, win_prob
def explain_prediction(team, opponent, team_score, opponent_score):
    if team_score > opponent_score:
        return f"{team.upper()} ka score zyada hai, isliye winning chances high hain."
    else:
        return f"{opponent.upper()} ne better perform kiya hai."
