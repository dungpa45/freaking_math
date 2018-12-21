from flask import Flask, request, render_template, session, redirect, url_for
import mlab
from models.highscore import Highscore

mlab.connect()

app = Flask(__name__)


@app.route("/",methods=["GET","POST"])
def home():
  if request.method == "GET":
    return render_template("freaking_math.html")
  elif request.method == "POST":
    form = request.form
    if 'easy' in form:
      return redirect(url_for('play', mode = 'EASY', name = form['name']))
      # return render_template("play.html", mode='EASY', name=form['name'])
    elif 'normal' in form:
      return redirect(url_for('play', mode = 'NORMAL', name = form['name']))
      # return render_template("play.html", mode='NORMAL', name=form['name'])
    elif 'hard' in form:
      return redirect(url_for('play', mode = 'HARD', name = form['name']))
      # return render_template("play.html", mode='HARD', name=form['name'])
    
    
    


@app.route("/play/<mode>/<name>", methods=['GET', 'POST'])
def play(mode, name):
  if request.method == 'GET':
    return render_template("play.html", mode = mode, name = name)
  elif request.method == 'POST':
    form = request.form
    point = form['point']
    h = Highscore(name=name,level=mode,diem=point)
    h.save()
    return redirect(url_for('highscore', point = point))


@app.route("/highscore/<point>", methods=['GET', 'POST'])
def highscore(point):
  # if request.method == 'GET':
  #   # return "abc"
  #   return render_template("highscore.html", diem=diem)
  # elif request.method == "POST":
  #   form = request.form
  #   diem = form['diem']

  # if request.method == 'POST':
  #   print(request.form)
  # return "abc"
  # print(request.form)
  hs = Highscore.objects()
  # print(hs)
  return render_template("highscore.html", hs_list=hs, point = point)

if __name__ == '__main__':
  app.run(debug=True)
