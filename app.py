import numpy as np
import random
from flask import Flask, render_template, url_for, request
from form import AnswerForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '2e4d7d7f4db059a95715e1683fd6755e'

colours = ["czerwony", "czarny", "zielony", "niebieski"]
colour = random.sample(colours, 4) #losowe kolory
joinedlist = colour
all_answers = []


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
    guess = request.form.get('answer')
    form = AnswerForm()
    
    if form.validate_on_submit():
        guess = form.answer.data
        guess = guess.split()
        
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
                return render_template('winnerloser.html', title='WinnerLoser', winner=winner, form=form)

        if len(all_answers) == 10:
            winner = False
            return render_template('winnerloser.html', title='WinnerLoser', winner=winner, form=form)
        
    return render_template('game.html', title='Game', form=form, guess=guess, answer_list=answer_list, joinedlist=joinedlist, all_answers=all_answers)
    
if __name__ == '__main__':
    app.run(debug=True)   