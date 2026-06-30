# TicTacToe-Python V4
# Created by: NkzDev-Cyber

import random


# ==========================
# SISTEMA DE IDIOMA
# LANGUAGE SYSTEM
# ==========================

print("1 - Português 🇧🇷")
print("2 - English 🇺🇸")

lang = input("\nChoose / Escolha: ")


if lang == "2":

    txt = {
        "title": "🎮 TIC TAC TOE ULTIMATE",
        "ia": "Play against AI",
        "player": "Play against friend",
        "score": "Score",
        "exit": "Exit",
        "choose": "Choose: ",
        "diff": "Difficulty",
        "easy": "Easy",
        "medium": "Medium",
        "hard": "Hard",
        "pos": "Choose a position (1-9): ",
        "taken": "Position already taken!",
        "win": "won!",
        "draw": "Draw!",
        "bye": "Goodbye!"
    }

else:

    txt = {

        "title": "🎮 TIC TAC TOE ULTIMATE",
        "ia": "Jogar contra IA",
        "player": "Jogar contra amigo",
        "score": "Placar",
        "exit": "Sair",
        "choose": "Escolha: ",
        "diff": "Dificuldade",
        "easy": "Fácil",
        "medium": "Médio",
        "hard": "Difícil",
        "pos": "Escolha uma posição (1-9): ",
        "taken": "Posição ocupada!",
        "win": "venceu!",
        "draw": "Empate!",
        "bye": "Até mais!"
    }



placar = {
    "X":0,
    "O":0,
    "Draw":0
}



def mostrar(tab):

    print("\n")

    print(tab[0]+" | "+tab[1]+" | "+tab[2])
    print("--+---+--")
    print(tab[3]+" | "+tab[4]+" | "+tab[5])
    print("--+---+--")
    print(tab[6]+" | "+tab[7]+" | "+tab[8])



def venceu(tab):

    comb = [

        [0,1,2],
        [3,4,5],
        [6,7,8],
        [0,3,6],
        [1,4,7],
        [2,5,8],
        [0,4,8],
        [2,4,6]

    ]


    for c in comb:

        if tab[c[0]] == tab[c[1]] == tab[c[2]] != " ":

            return tab[c[0]]

    return None



def jogar_pos(tab,jogador):

    while True:

        try:

            pos = int(input(txt["pos"]))


            if tab[pos-1] == " ":

                tab[pos-1] = jogador
                break

            else:

                print(txt["taken"])


        except:

            print("Error!")



def ia(tab,nivel):

    livre=[]

    for i in range(9):

        if tab[i]==" ":

            livre.append(i)



    if nivel=="easy":

        tab[random.choice(livre)]="O"


    elif nivel=="medium":


        for p in livre:

            teste=tab.copy()

            teste[p]="O"


            if venceu(teste)=="O":

                tab[p]="O"
                return



        for p in livre:

            teste=tab.copy()

            teste[p]="X"


            if venceu(teste)=="X":

                tab[p]="O"
                return



        tab[random.choice(livre)]="O"



    else:


        if 4 in livre:

            tab[4]="O"

        else:

            tab[random.choice(livre)]="O"





def modo_ia(nivel):

    tab=[" " for i in range(9)]


    while True:

        mostrar(tab)

        jogar_pos(tab,"X")


        if venceu(tab):

            mostrar(tab)

            print("X",txt["win"])

            placar["X"]+=1

            break


        if " " not in tab:

            print(txt["draw"])

            placar["Draw"]+=1

            break



        ia(tab,nivel)



        if venceu(tab):

            mostrar(tab)

            print("O",txt["win"])

            placar["O"]+=1

            break





def modo_player():


    tab=[" " for i in range(9)]

    jogador="X"


    while True:

        mostrar(tab)

        jogar_pos(tab,jogador)


        if venceu(tab):

            mostrar(tab)

            print(jogador,txt["win"])

            placar[jogador]+=1

            break



        if " " not in tab:

            print(txt["draw"])

            placar["Draw"]+=1

            break



        if jogador=="X":

            jogador="O"

        else:

            jogador="X"




while True:


    print("\n",txt["title"])

    print("1-",txt["ia"])
    print("2-",txt["player"])
    print("3-",txt["score"])
    print("4-",txt["exit"])


    op=input(txt["choose"])



    if op=="1":

        print("\n",txt["diff"])

        print("1-",txt["easy"])
        print("2-",txt["medium"])
        print("3-",txt["hard"])


        d=input(txt["choose"])


        if d=="1":
            nivel="easy"

        elif d=="2":
            nivel="medium"

        else:
            nivel="hard"


        modo_ia(nivel)



    elif op=="2":

        modo_player()



    elif op=="3":

        print(placar)



    elif op=="4":

        print(txt["bye"])
        break
