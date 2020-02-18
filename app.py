import numpy as np
import random
from flask import Flask, render_template, url_for, request
from form import AnswerForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '2e4d7d7f4db059a95715e1683fd6755e'
all_answers = []
colors = ["czerwony", "czarny", "zielony", "niebieski"]
color = random.choices(colors, k=4) #losowe kolory
joinedlist = color

@app.route("/")
@app.route("/home")
def home():
    form = AnswerForm()
    return render_template('home.html', form=form)

@app.route("/rules")
def rules():
    form = AnswerForm
    return render_template('rules.html', title='Rules', form=form)

@app.route("/game", methods=['GET', 'POST'])
def game_ready():

    guess = []
    answer_list = []
    failure = True
    guess = request.form.get('answer')
    form = AnswerForm()
    
    if form.validate_on_submit():
        guess = form.answer.data
        guess = guess.split()

        global colors
        #walidacja
        if len(guess) == 4:
            if guess[0] in colors and guess[1] in colors and guess[2] in colors and guess[3] in colors:
                    failure=False
        
        if failure == False:
            global joinedlist

            #sprawdzenie kolorów w odpowiedzi
            for i in range(4):
                if guess[i] == joinedlist[i]: #poprawny kolor i prawidłowe miejsce
                    answer_list.append("O")
                elif guess[i] in joinedlist:	
                    #poprawny kolor, ale na złym miejscu
                    answer_list.append("V")
                else: #zły kolor
                    answer_list.append("X")
            
            global all_answers
            
            if len(all_answers) < 10:
                all_answers.append([guess, answer_list])

                if guess == joinedlist:
                    winner = True
                    all_answers = guess = joinedlist = answer_list = []
                    colors = ["czerwony", "czarny", "zielony", "niebieski"]
                    color = random.choices(colors, k=4) #losowe kolory
                    joinedlist = color
                    return render_template('winnerloser.html', title='WinnerLoser', winner=winner, form=form)

            if len(all_answers) == 10:
                winner = False
                all_answers = guess = joinedlist = answer_list = []
                colors = ["czerwony", "czarny", "zielony", "niebieski"]
                color = random.choices(colors, k=4) #losowe kolory
                joinedlist = color
                return render_template('winnerloser.html', title='WinnerLoser', winner=winner, form=form)

            failure=True
        
    return render_template('game.html', title='Game', form=form, guess=guess, answer_list=answer_list, joinedlist=joinedlist, all_answers=all_answers)
    
if __name__ == '__main__':
    app.run(debug=True)   
    #app.run(host = "0.0.0.0", port = 5078, debug = "True")
