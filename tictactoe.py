#!/usr/bin/env python
import PySimpleGUI as sg



# Demonstrates a number of PySimpleGUI features including:
#   Default element size
#   auto_size_buttons
#   Button
#   Dictionary return values
#   update of elements in form (Text, Input)


layout = [[sg.Text('')],
          [sg.Button(f'{field[0]}', key=0,), sg.Button(f'{field[1]}', key=1), sg.Button(f'{field[2]}', key=2)],
          [sg.Button(f'{field[3]}', key=3), sg.Button(f'{field[4]}', key=4), sg.Button(f'{field[5]}', key=5)],
          [sg.Button(f'{field[6]}', key=6), sg.Button(f'{field[7]}', key=7), sg.Button(f'{field[8]}', key=8)],
          [sg.Button(f'Reset')]
          ]

window = sg.Window('Tic Tac Toe', layout,
                   default_button_element_size=(5, 5),
                   auto_size_buttons=False,
                   grab_anywhere=False)

# Loop forever reading the form's values, updating the Input field
while True:
    event, values = window.read()  # read the form
    if event == sg.WIN_CLOSED:  # if the X button clicked, just exit
        break

    if event in '012345678':

        marking()

         = values['']  
     
    elif event == 'Submit':
        keys_entered = values['input']
        window['out'].update(keys_entered)  # output the final string

    # change the form to reflect current key string
    window['input'].update(keys_entered)
window.close()


#3*3=9マスのフィールドを用意する
    #二重リストfield[[1, 2, 3,], [4, 5, 6], [7, 8, 9]]を用意する
#マスの状態は、[○, ×, 無表示]
#プレイヤー、CPUが交互にマスを埋めていく
#同じマークが三つ並んだら勝ちのテキストを表示。並ばなければ引き分けを表示

#勝ちの判定
    #横のライン
        #field[:3]
        #field[3:6]
        #field[6:9]
            
    #縦のライン
        #field[0][0] and field[1][0] and field[2][0]
        #field[0][1] and field[1][1] and field[2][1]
        #field[0][2] and field[1][2] and field[2][2]
    #斜めのライン
        #field[0][0] and field[1][1] and field[2][2]
        #field[0][2] and field[1][1] and field[2][0]

#count 1 =