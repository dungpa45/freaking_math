from flask import Flask, request, render_template, session, redirect, url_for
import mlab
from models.highscore import Highscore

mlab.connect()

app = Flask(__name__)


@app.route("/home",methods=["GET","POST"])
def home():
  if request.method == "GET":
    return render_template("freaking_math.html")
  elif request.method == "POST":
    print('hihi')
    form = request.form
    print(form)
    if 'easy' in form:
      return render_template("play.html", mode = 'EASY')
    elif 'normal' in form:
      return render_template("play.html", mode = 'NORMAL')
    elif 'hard' in form:
      return render_template("play.html", mode = 'HARD')
    



    

@app.route("/play")
def play():
  return render_template("play.html")



@app.route("/highscore")
def highscore():
  hs = Highscore.objects()
  return render_template("highscore.html",hs_list=hs)

if __name__ == '__main__':
  app.run(debug=True)
