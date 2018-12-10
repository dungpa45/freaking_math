from flask import Flask, request, render_template, session, redirect, url_for
import mlab

mlab.connect()

app = Flask(__name__)


@app.route("/home")
def profile():
    return render_template("freaking_math.html")


if __name__ == '__main__':
  app.run(debug=True)
