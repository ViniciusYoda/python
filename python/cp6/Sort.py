import time

def get_time(arg):
    inicio = time.time()
    time.sleep(arg)
    fim = time.time()
    return fim-inicio

dif = get_time(1)
print(f'Dif: {dif:.2f}')