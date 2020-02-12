import numpy as np
import random
from flask import Flask, render_template, url_for, request
from form import AnswerForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '2e4d7d7f4db059a95715e1683fd6755e'

#stworzenie losowego kodu dla gracza
number = random.randrange(1000, 10000) #randrange() to funkcja do generowania losowych liczb
list_from_number = [int(x) for x in str(number)] #stworzenie z liczby listy integerów
colours = ["b", "n", "z", "c"]
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
colour = random.sample(colours, 4) #losowe kolory
str(colour)
list_from_colours = list(colour) #stworzenie z napisu listy znaków
joinedlist = list_from_colours + list_from_number #stworzenie ostatecznej listy np. ['b', 4, 'z', 7, 'n', 3, 'c', 9]
joinedlist[1], joinedlist[4] = joinedlist[4], joinedlist[1]
joinedlist[3], joinedlist[6] = joinedlist [6], joinedlist[3]
attempts = 0
answer_list = []
game = True

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/rules")
def about():
    return render_template('rules.html', title='Rules')

@app.route("/game", methods=['GET', 'POST'])
def game_ready():
    global numbers, colours
    global failure1, failure2, failure3
    failure1=failure2=failure3=False
    guess = []
    guess = request.form.get('answer')

    form = AnswerForm()
    if form.validate_on_submit():
        guess = list(form.answer.data)   

        if len(guess)==8:
            #sprawdzenie poprawności odpowiedzi
            global numbers, colours
            for i in [1, 3, 5, 7]:
                if guess[i] not in numbers:
                    failure2=True
            for i in [0, 2, 4, 6]:
                if guess[i] not in colours:
                    failure3=True

            if failure2==False and failure3==False:
                global game
                while game:

                    global attempts 
                    attempts += 1

                    if attempts > 10:
                        game = False
                    #print('Koniec gry')

                    global joinedlist, answer_list
                    joinedlist = list(map(str, joinedlist)) #konwertuję do stringów, potrzebne przy sprawdzaniu cyfr

                                    #sprawdzenie kolorów w odpowiedzi
                    for i in range(0, 7, 2):
                        if guess[i] == joinedlist[i]: #poprawny kolor i prawidłowe miejsce
                            answer_list.append("O")
                        elif guess[i] in joinedlist:	
                                    #poprawny kolor, ale na złym miejscu
                            answer_list.append("V")
                        else: #zły kolor
                            answer_list.append("X")
                                        
                                    #sprawdzenie cyfr w odpowiedzi
                    for i in range(1, 8, 2):
                        if guess[i] == joinedlist[i]: #poprawna cyfra i prawidłowe miejsce
                            answer_list.append("O")
                        elif guess[i] in joinedlist:	
                                    #poprawna cyfra, ale na złym miejscu
                            answer_list.append("V")
                        else: #zła cyfra
                            answer_list.append("X")
                return render_template('table.html', title='Table', guess=guess, answer_list=answer_list, joinedlist=joinedlist,)
    else:
        #zła długość
        failure1=True
             
    return render_template('game.html', title='Game', form=form, guess=guess, answer_list=answer_list, joinedlist=joinedlist, failure1=failure1, failure2=failure2, failure3=failure3)
    
if __name__ == '__main__':
    app.run(debug=True) 