import pickle 

N = int(input("Введіть кількість елементів прогресії: "))
b1=2.5
q=1.9

progression = []
for i in range(N):
    elem = round(b1 * q**i)
    progression.append(elem)

if len(progression) > 6:
    progression = progression[3:-3]
else:
    progression=[]

with open("c:\\lab19\\list.bin", "wb") as file:
    pickle.dump(progression, file)
