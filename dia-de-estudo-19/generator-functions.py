# Introdução às Generator functions em Python
# generator = (n for n in range(1000000))

def generator(n=0, maximum=10): # Função generator
    while True:
        yield n # Pausado aqui no yield
        n += 1

        if n > maximum:
            return


gen = generator(maximum=1000000)


for n in gen:
    print(n)