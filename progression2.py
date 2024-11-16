import pickle

with open ("c:\\lab19\\list.bin", "rb") as file:
    load_list = pickle.load(file)

print("Список елементів: ", load_list)