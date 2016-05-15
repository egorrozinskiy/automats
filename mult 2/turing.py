# функция для считывания правил машины тьюринга из файла
def read_rules():
    rules = {}
    with open('rules.txt', 'r') as f:
        for line in f: # берем построчно из файла
            vals = line.split() # разделяем строку на части(разделитель пробел)
            rules[(int(vals[0]), vals[1])] = int(vals[2]), vals[3], vals[4] # запоминаем наши правила из файла в словарь
    return rules

# функция для считывания ленты из файла
def read_tape(spec_symbol='X'):
    with open('tape.txt', 'r') as f:
        res = [spec_symbol]
        res.extend(f.readline().split())
        res.append(spec_symbol)
        return res


def main(spec_symbol='X'):
    rules = read_rules()
    tape = read_tape()

    cur_pos = 1
    cur_state = 0

    #пока у нас есть состояние, в которое мы можем перейти
    while (cur_state, tape[cur_pos]) in rules:
        new_state, new_val, dir = rules[(cur_state, tape[cur_pos])]
        tape[cur_pos] = new_val
        cur_state = new_state # переходим в новое состояние
        if dir == 'L': # сдвигаем головку по направлению влево
            if cur_pos != 0:
                cur_pos -= 1
            else:
                tape.insert(0, spec_symbol)
        elif dir == 'R':# вправо
            if cur_pos == len(tape) - 1: #если это край ленты, то добавляем еще один специальный символ справа
                tape.append(spec_symbol)
            cur_pos += 1
    print(tape)


if __name__ == '__main__':
    main()
