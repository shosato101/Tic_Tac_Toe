import PySimpleGUI as sg

"""
Tic Tac Toe !

Parameters
----------
field : dict
    9マスのフィールドに相当する。マークを格納して、勝敗判定をする。

done : list
    ボタンを無効化するためのリスト。
    マークの上書き防止、およびゲーム終了後のマーク記入を無効化する。
    また、len(done) > 9 でゲーム決着、len(done) < 9 でゲーム続行中となる。

count : int
    ゲームのターン数。○と×のターンや表示など、こちらの値で判断。


"""

field = {0: "Button0", 1: "Button1", 2: "Button2",  # 結果判定のため。
         3: "Button3", 4: "Button4", 5: "Button5",
         6: "Button6", 7: "Button7", 8: "Button8"}
done = []  # 選択済みボタンのキーを格納。
count = 0  # ゲームのターン数。


def check_result():
          # 横のライン
    if (  field[0] == field[1] == field[2] or
          field[3] == field[4] == field[5] or
          field[6] == field[7] == field[8] or
          # 縦のライン
          field[0] == field[3] == field[6] or
          field[1] == field[4] == field[7] or
          field[2] == field[5] == field[8] or
          # 斜めのライン
          field[0] == field[4] == field[8] or
          field[2] == field[4] == field[6]):
        if count % 2 == 0:
            sg.popup("× won!", keep_on_top=True)
        else:
            sg.popup("○ won!", keep_on_top=True)
        window["turn"].update("Finish!")
        finish()

    elif len(done) == 9:
        sg.popup("Draw", keep_on_top=True)
        window["turn"].update("Draw....")


def finish():
    for i in range(9):  # フィールドの全てのボタンを無効化する。
        done.append(i)  # ゲーム終了後はlen(done) > 9。続行中はlen(done) < 9 。


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
                   grab_anywhere=False,
                   keep_on_top=True)


# イベントループしつつ、対話に応じてウィンドウの情報を更新する
while True:
    event, values = window.read()  # 情報更新

    if event == sg.WIN_CLOSED:  # タイトルバーの×ボタンで終了
        break

    if event in done:  # ○×マークの上書き防止のため。
        continue

    elif event in list(range(9)):
        if count % 2 == 0:
            field[event] = "circle"
            window[event].update("○")
            done.append(event)
            count += 1
            check_result()
            if len(done) < 9:  # ゲームが続行しているかを確認する。
                window["turn"].update("×'s turn")
        else:
            field[event] = "cross"
            window[event].update("×")
            done.append(event)
            count += 1
            check_result()
            if len(done) < 9:
                window["turn"].update("○'s turn")

    if event == "reset":
        for i in range(9):
            field[i] = f"Button{i}"  # 結果判定用の辞書をリセット。
            window[i].update("")  # ウィンドウの○×の表示を消す。
        done = []
        count = 0
        window["turn"].update("○'s turn")

window.close()
