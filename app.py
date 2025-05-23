from flask import Flask, request, render_template
import random

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    error = None
    if request.method == "POST":
        try:
            start = int(request.form["start"])
            end = int(request.form["end"])
            if start > end:
                raise ValueError("Start should not be greater than End.")
            result = random.randint(start, end)
        except Exception as e:
            error = str(e)
    return render_template("index.html", result=result, error=error)

if __name__ == "__main__":
    app.run(debug=True)
