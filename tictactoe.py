import PySimpleGUI as sg



field = {0: "0", 1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8"}  #○×表示と結果判定のため。
done = []  #選択したボタンのキーを格納して、選択済みボタンを無効化するため。
count = 0  #ゲームのターン数を調べて、○と×どちらのターンかを判定するため。


def check_result():
    #横のライン
    if (field[0] == field[1] == field[2] or
        field[3] == field[4] == field[5] or
        field[6] == field[7] == field[8] or
    #縦のライン
        field[0] == field[3] == field[6] or
        field[1] == field[4] == field[7] or
        field[2] == field[5] == field[8] or
    #斜めのライン
        field[0] == field[4] == field[8] or
        field[2] == field[4] == field[6]):
        if count % 2 == 0:
            sg.popup("×' win!")
            window["turn"].update("Finish!  ×'s win!")
            finish()
        else:
            sg.popup("○'s win!")
            window["turn"].update("Finish!  ○'s win!")
            finish()
        
    elif len(done) == 9 and count == 9:
        sg.popup("Draw")
        window["turn"].update("Draw....")

def finish():
    for i in range(9):
        done.append(i)  #全てのボタンを無効化するため(resetボタン以外を除く)。
    

layout = [[sg.Text("○'s turn", key="turn", font=('Helvetica', 19), size=(15, 1)),
           sg.Button("Reset", key="reset", size=(5, 1), font=('Helvetica', 9))],
          [sg.Button(key=0), sg.Button(key=1), sg.Button(key=2)],
          [sg.Button(key=3), sg.Button(key=4), sg.Button(key=5)],
          [sg.Button(key=6), sg.Button(key=7), sg.Button(key=8)],
          ]

window = sg.Window('Tic Tac Toe', layout,
                   default_button_element_size=(2, 1),
                   font=('Helvetica', 50),
                   auto_size_buttons=False,
                   grab_anywhere=False)
                    

# Loop forever reading the form's values, updating the Input field
while True:
    event, values = window.read()  # read the form
 
    if event == sg.WIN_CLOSED:  # if the X button clicked, just exit
        break
    
    if event in done:  #マークの上書き防止、またゲーム終了後にマーク記入を受けつけないようにするため。
        continue

    elif event in list(range(9)):
        if count % 2 == 0:
            field[event] = "○"
            done.append(event)
            count += 1
            window["turn"].update("×'s turn")
            check_result()
        else:
            field[event] = "×"
            done.append(event)
            count += 1
            window["turn"].update("○'s turn") 
            check_result()
        window[event].update(f"{field[event]}")

    if event == "reset":
        for i in range(9):  #フィールド上のボタン全てに適用するため。
            field[i] = i  #結果判定用の○×のvalueをリセット。
            window[i].update("")  #書き込んだ○×の表示を消すため。
        done = []
        count = 0
        window["turn"].update("○'s turn")

window.close()