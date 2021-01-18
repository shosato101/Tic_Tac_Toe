import PySimpleGUI as sg


field = {0:"0", 1:"1", 2:"2", 3:"3", 4:"4", 5:"5", 6:"6", 7:"7", 8:"8"}
done = []
count = 0


def check_result():
        #横のライン
        if field[0] == field[1] == field[2]:
            sg.popup(f"{field[0]}' win!")
            finish()
        elif field[3] == field[4] == field[5]:
            sg.popup(f"{field[3]}' win!")
            finish()
        elif field[6] == field[7] == field[8]:
            sg.popup(f"{field[6]}' win!")
            finish()
        #縦のライン
        elif field[0] == field[3] == field[6]:
            sg.popup(f"{field[0]}' win!")
            finish()
        elif field[1] == field[4] == field[7]:
            sg.popup(f"{field[1]}' win!")
            finish()
        elif field[2] == field[5] == field[8]:
            sg.popup(f"{field[2]}' win!")
            finish()
        #斜めのライン
        elif field[0] == field[4] == field[8]:
            sg.popup(f"{field[0]}' win!")
            finish()
        elif field[2] == field[4] == field[6]:
            sg.popup(f"{field[2]}' win!")
            finish()
        elif count == 9:
            sg.popup(f"Draw")

def finish():
    for i in range(9):
        done.append(i)
    

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
    
    if event in done:
        continue

    elif event in list(range(9)):
        if count % 2 == 0:
            field[event] = "○"
            done.append(event)
            count += 1
            check_result()
            window["turn"].update("×'s turn")
        else:
            field[event] = "×"
            done.append(event)
            count += 1
            check_result()
            window["turn"].update("○'s turn") 
        window[event].update(f"{field[event]}")

    if event == "reset":
        for i in range(9):
            field[i] = i
            event = i
            window[event].update("")
        done.clear()
        count = 0
        window["turn"].update("○'s turn")

    if len(done) > 9:
        if count % 2 == 0:
            window["turn"].update("Finish!  ×'s win!")
        else:
            window["turn"].update("Finish!  ○'s win!")
    if len(done) == 9 and count == 9:
            window["turn"].update("Draw....")


window.close()