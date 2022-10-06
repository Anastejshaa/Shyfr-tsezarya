while (True):

    alphabet = {"eng": "abcdfghijklmnopqrstuvwxyz",
                "ukr": "абвгґдеєжзиійїклмнопрстуфхцчшщьюя",
                "num": "123456789" }

    encrypt = input(" \n Enter a clear message: ").lower()
    encrypted = ""
    for letter in encrypt:
        if letter in alphabet["eng"]:
            position = alphabet["eng"].find(letter) + 1
            if letter in alphabet["eng"][-1]:
                encrypted = encrypted + alphabet["eng"][0]
            else:
                encrypted = encrypted + alphabet["eng"][position]
        elif letter in alphabet["ukr"]:
            position = alphabet["ukr"].find(letter) + 1
            if letter in alphabet["ukr"][-1]:
                encrypted = encrypted + alphabet["ukr"][0]
            else:
                encrypted = encrypted + alphabet["ukr"][position]
        elif letter in alphabet["num"]:
            position = alphabet["num"].find(letter) + 1
            if letter in alphabet["num"][-1]:
                encrypted = encrypted + alphabet["num"][0]
            else:
                encrypted = encrypted + alphabet["num"][position]
        else:
            encrypted = encrypted + letter
    print(encrypted)
