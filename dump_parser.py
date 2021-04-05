import pickle

phone_numbers = []
with open("data.txt", "r") as file:
    for line in file:
        number = line[:13][2:]
        try:
            _number = int(number)
            phone_numbers.append(number)
        except ValueError:
            print("gege")

with open("data.pickle", "wb") as file:
    pickle.dump(phone_numbers, file)
