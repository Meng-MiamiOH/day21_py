from flask import Flask, render_template
import plotly.graph_objects as go
import pandas as pd

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("page.html", title="HOME PAGE")

@app.route("/<path>")
def doc(path):
    df = pd.read_csv(path + ".csv")

    fig = go.Figure(
        data=go.Bar(
            x=df['date'],
            y=df['time'],
            name="Time",
            marker=dict(color="paleturquoise"),
        )
    )

    fig.add_trace(
        go.Scatter(
            x=df['date'],
            y=df['score'],
            yaxis="y2",
            name="Scores",
            marker=dict(color="crimson"),
        )
    )

    fig.update_layout(
        title=path,
        legend=dict(orientation="h"),
        yaxis=dict(
            title=dict(text="time"),
            side="left",
        ),
        yaxis2=dict(
            title=dict(text="scores"),
            side="right",
            overlaying="y",
        )
    )

    fig.show()
    return render_template("page.html", title=path)

@app.route("/about")
def about():
    return render_template("page.html", title="about page")

if __name__ == "__main__":
    app.run(debug=False)