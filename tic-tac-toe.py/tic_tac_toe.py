from tkinter import *
import random, time


def stop_game():
    global game_left
    for item in game_left:
        buttons[item].config(bg='white', state='disabled')


def win(n):
    global game
    if (game[0] == n and game[1] == n and game[2] == n) \
            or (game[3] == n and game[4] == n and game[5] == n) \
            or (game[6] == n and game[7] == n and game[8] == n) \
            or (game[0] == n and game[3] == n and game[6] == n) \
            or (game[1] == n and game[4] == n and game[7] == n) \
            or (game[2] == n and game[5] == n and game[8] == n) \
            or (game[0] == n and game[4] == n and game[8] == n) \
            or (game[2] == n and game[4] == n and game[6] == n):
        return True


def push_button(push):
    global game
    global game_left
    global turn
    game[push] = 'X'
    buttons[push].config(text='X', bg='white', state='disabled')
    game_left.remove(push)
    if push == 4 and turn == 0:
        bot_turn = random.choice(game_left)
    elif push != 4 and turn == 0:
        bot_turn = 4
    if turn > 0:
        bot_turn = 8 - push
    if bot_turn not in game_left:
        try:
            bot_turn = random.choice(game_left)
        except IndexError:
            label['text'] = 'game is end!'
            stop_game()
    game[bot_turn] = 'O'
    time.sleep(0.2)
    buttons[bot_turn].config(text='O', bg='white', state='disabled')
    if win('X'):
        label['text'] = 'user Win!'
        stop_game()
    elif win('O'):
        label['text'] = 'Game over, bot win!'
        stop_game()
    else:
        if len(game_left) > 1:
            game_left.remove(bot_turn)
        else:
            label['text'] = 'game is end!'
            stop_game()
        turn += 1


game = [None] * 9
game_left = list(range(9))
turn = 0

root = Tk()
label = Label(width=20, text='Game in tic-tac-toe', font=('Arial', 20, 'bold'))

buttons = [Button(width=5, height=2, font=('Arial', 28, 'bold'), bg='green', command=lambda x=i: push_button(x)) for i
           in range(9)]

label.grid(row=0, column=0, columnspan=3)

row = 1
col = 0
for i in range(9):
    buttons[i].grid(row=row, column=col)
    col += 1
    if col == 3:
        row += 1
        col = 0

root.mainloop()
