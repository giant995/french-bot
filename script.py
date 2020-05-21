def print_message():
    print("Excusez-moi, répéter s'il vouis plait.")

def mood():
    while True:
        res = input("Ca va? \n[a] Ca va (Good) \n[b] Calme (Calm) \n[c] Content/Contente (happy) \n[d] Fatigue/Fatiguee (Tired) \n[e] inquiet/inquiete (worried) \n[f] stresse/stressee (stressed) \n[g] triste (sad) \n>")
        if res == "a":
            return "ça va"
        elif res == "b":
            return "calme"
        elif res == "c":
            return "content/contente"
        elif res == "d":
            return "fatigué/fatiguée"
        elif res == "e":
            return "inquiet/inquiète"
        elif res == "f":
            return "stressé/stressée"
        elif res == "g":
            return "triste"
        else:
            print_message()

def greeting():
    print("Bonjour")
    user_name = input("Je m'appelle Cyberbarbie et vous? ")
    print(f"Enchantée, {user_name}!")
    feeling = mood()
    print(f"Apparently you're feeling {feeling}")

greeting()

# What to add next? How do I expand this application?
# Integrate Twilio's autopilot API to build a more elegant and mature bot, perhaps?
# Next bot questions for user: ask about where they are from, goals, what are they learning 
# purpose of bot is to have increasingly meaningful basic conversations in French
