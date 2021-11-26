import functools
import itertools
from functools import reduce
from random import randint
def menu():
    print("1 - Exemplo S = [1, 3, 6, 9] e t = 13")
    print("2 - Exemplo S = [1, 5, 7, 9] e t = 4")
    print("3 - Inserir S e t")
    print("4 - S randomico e t randomico")
    res = int(input("Digite a opção: "))

    if res == 1:
        return [1, 3, 6, 9], 13
    elif res == 2:
        return [1, 5, 7, 9], 4
    elif res == 3:
        vals = input("Digite S (só os numeros, separados por vigula): ")
        t = int(input("Digite o valor de t: "))
        return [int(v) for v in vals.split(",")], t
    else:
        arr = [randint(0,100) for _ in range(20)]
        t = randint(0,500)
        return arr, t

def main():
    S, t = menu()

    comb = []
    for i in range(1, len(S)+1): # sem o conjunto vazio
        for subset in itertools.combinations(S, i):
            comb.append(list(subset))


    somaComb = list(map(lambda x: reduce(lambda a,b: a + b, x), comb))
    condComb = list(map(lambda x: x == t, somaComb))    
    res = list(itertools.compress(comb, condComb))
    if len(res) != 0:
        for r in res:
            vals = ", ".join([str(v) for v in r])
            print("{" + vals + "}")
    else:
        print(f"Não existe subconjunto de S cujas somas dos elementos resulta em {t}")


if __name__ == "__main__":
    main()