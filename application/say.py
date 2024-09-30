import cowsay
from datetime import datetime


def cow_saying(frase):
    cowsay.cow(frase)
    current_date = datetime.now()
    print(current_date)


def ghostbusters_saying(frase):
    cowsay.ghostbusters(frase)
    current_date = datetime.now()
    print(current_date)

if __name__ == '__main__':    
    cow_saying('Let`s milkshake!')    
    ghostbusters_saying('Who you gonna call?!')

