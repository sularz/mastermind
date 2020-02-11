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
print(joinedlist)
attempts = 0
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
    guess = []
    
    if guess == []:
        form = AnswerForm()
        guess = request.form.get('answer_form')

    else:
        guess = list(guess)
        global game
        while game:

            global attempts
            attempts += 1

            if attempts > 10:
                game = False
                    #print('Koniec gry')

            answer = []
            global joinedlist
            joinedlist = list(map(str, joinedlist)) #konwertuję do stringów, potrzebne przy sprawdzaniu cyfr

                    #sprawdzenie kolorów w odpowiedzi
            for i in range(0, 7, 2):
                if guess[i] == joinedlist[i]: #poprawny kolor i prawidłowe miejsce
                    answer.append("O")
                elif guess[i] in joinedlist:	
                        #poprawny kolor, ale na złym miejscu
                    answer.append("V")
                else: #zły kolor
                    answer.append("X")
                    
                    #sprawdzenie cyfr w odpowiedzi
            for i in range(1, 8, 2):
                if guess[i] == joinedlist[i]: #poprawna cyfra i prawidłowe miejsce
                    answer.append("O")
                elif guess[i] in joinedlist:	
                        #poprawna cyfra, ale na złym miejscu
                    answer.append("V")
                else: #zła cyfra
                    answer.append("X")
        
    return render_template('game.html', title='Game', form=form, guess=guess, joinedlist=joinedlist, numbers=numbers, colours=colours)

if __name__ == '__main__':
    app.run(debug=True)