import random

alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
             'v', 'w', 'x', 'y', 'z']


def username():
    word = ""
    for a in range(0,30):
        word += random.choice(alphabets)
    return word


def firstName():
    with open("fName.txt", 'r') as file :
        data = file.readlines()
        name = random.choice(data).split()[0].lower()
        return name


def year():
    return random.randint(1990,2000)


def day():
    return random.randint(1,28)


def month():
    return random.randint(1,12)



