def print_message():
    print("Excusez-moi, répéter s'il vouis plait.")

def mood():
    while True:
        res = input("Ca va? \n[a] Ca va (Good) \n[b] Calme (Calm) \n[c] Content/Contente (happy) \n[d] Fatigue/Fatiguee (Tired) \n[e] inquiet/inquiete (worried) \n[f] stresse/stressee (stressed) \n[g] triste (sad) \n>")
        if res == "a":
            return "ca va"
        elif res == "b":
            return "calme"
        elif res == "c":
            return "content/contente"
        elif res == "d":
            return "fatigue/fatiguee"
        elif res == "e":
            return "inquiet/inquiete"
        elif res == "f":
            return "stresse/stressee"
        elif res == "g":
            return "triste"
        else:
            print_message()

def greeting():
    print("Bonjour")
    user_name = input("Je m'appelle Cyberbarbie, et vous? ")
    print(f"Enchantee, {user_name}!")
    feeling = mood()
    print(f"Apparently you're feeling {feeling}")

greeting()