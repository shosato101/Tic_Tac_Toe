#3*3のマスを用意する
#マスの状態は[○,× , 未入力]
#プレイヤー1、CPUが交互にマスにマークを記入する
#同じマークが三つ揃ったら勝敗の文を表示

field = {0:, 1:, 2: 3:, 4:, 5:, 6:, 7:, 8:}
done = []
count = 0

def marking(selected):
    if selected not in done and count % 2 ==0:
        field[selected] = "×"
        done,append(selected)
        count += 1
    elif selected not in done:
        field[selected] = "○"
        done,append(selected)
        count += 1
    return field, done, count

def check_result():
    #横のライン
    if field[0] == field[1] == field[2]:
        print(f"{field[0]} is win!")
    elif field[4] == field[5] == field[6]:
        print(f"{field[4]} is win!")
    elif field[7] == field[8] == field[9]:
        print(f"{field[7]} is win!")
    #縦のライン
    elif field[0] == field[3] == field[6]:
        print(f"{field[0]} is win!")
    elif field[1] == field[4] == field[7]:
        print(f"{field[1]} is win!")
    elif field[2] == field[5] == field[8]:
        print(f"{field[2]} is win!")
    #斜めのライン
    elif field[0] == field[4] == field[8]:
        print(f"{field[0]} is win!")
    elif field[2] == field[4] == field[6]:
        print(f"{field[2]} is win!")

def player_turn():
     marking()
