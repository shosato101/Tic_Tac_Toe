import PySimpleGUI as sg



marks = {0: "0", 1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8"}  #結果判定のため。
done = []  #選択済みボタンのキーを格納。
count = 0  #ゲームのターン数。


def check_result():
    #横のライン
    if (marks[0] == marks[1] == marks[2] or
        marks[3] == marks[4] == marks[5] or
        marks[6] == marks[7] == marks[8] or
    #縦のライン
        marks[0] == marks[3] == marks[6] or
        marks[1] == marks[4] == marks[7] or
        marks[2] == marks[5] == marks[8] or
    #斜めのライン
        marks[0] == marks[4] == marks[8] or
        marks[2] == marks[4] == marks[6]):
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
        done.append(i)  #9マスのボタンを無効化するため。
    

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
                    

#イベントループしつつ、作業に応じてウィンドウの情報を更新する
while True:
    event, values = window.read()  # 情報を更新するため
 
    if event == sg.WIN_CLOSED:  # タイトルバーの×ボタンで終了させるため
        break
    
    if event in done:  #マークの上書き防止、およびゲーム終了後のマーク記入禁止のため。
        continue

    elif event in list(range(9)):
        if count % 2 == 0:
            marks[event] = "circle"
            window[event].update("○")
            done.append(event)
            count += 1
            check_result()
            if len(done) < 9:
                window["turn"].update("×'s turn")
        else:
            marks[event] = "cross"
            window[event].update("×")
            done.append(event)
            count += 1
            check_result()
            if len(done) < 9:
                window["turn"].update("○'s turn") 
    
    if event == "reset":
        for i in range(9): 
            marks[i] = i  #結果判定用の辞書をリセット。
            window[i].update("")  #書き込んだ○×の表示を消す。
        done = []
        count = 0
        window["turn"].update("○'s turn")

window.close()