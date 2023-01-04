numbers = list(range(1, 10))

wins_comb = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)]


def field_numbers():
    print("-------------")
    for i in range(3):
        print("|", numbers[0 + i * 3], "|", numbers[1 + i * 3], "|", numbers[2 + i * 3], "|")
    print("-------------")


def value_input(player_sing):
    while True:
        value = input("В какую ячейку поставить:  " + player_sing + "?")
        if not (value in "123456789"):
            print("Вы ввели неверную ячейку. Повторите ввод. ")
            continue
        value = int(value)
        if str(numbers[value - 1]) in "XO":
            print("эта клетка занята")
            continue
        numbers[value - 1] = player_sing
        break


def game_check():
    for j in wins_comb:
        if (numbers[j[0] - 1]) == (numbers[j[1] - 1]) == (numbers[j[2] - 1]):
            return numbers[j[1] - 1]
    return False


def main():
    counter = 0
    while True:
        field_numbers()
        if counter % 2 == 0:
            value_input("X")
        else:
            value_input("O")
        if counter > 3:
            victory = game_check()
            if victory:
                field_numbers()
                print(victory, " победил!")
                break
        counter = counter + 1
        if counter > 8:
            field_numbers()
            print("Победила дружба. Ничья!")
            break


main()








