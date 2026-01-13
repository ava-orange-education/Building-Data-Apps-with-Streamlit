from flask import Flask, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def hello():
    form = """
        <form method="POST">
            <label for="name">Enter your name:</label>
            <input type="text" id="name" name="name">
            <input type="submit" value="Submit">
        </form>
    """

    if request.method == "POST":
        name = request.form.get("name")
        if name:
            return f"{form} Hello, {name}!"

    return form


if __name__ == "__main__":
    app.run(debug=True)
