import time


def count_sym(line):
    for sym in set(line):
        counter = 0
        for sub_sym in line:
            if sym == sub_sym:
                counter += 1
        print(sym, counter)


data = 'abcdefg' * 1000000

start = time.time()
count_sym(data)
end = time.time()

print('Время выполнения программы:', end - start)
