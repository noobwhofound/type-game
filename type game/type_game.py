import time
import random
import os
import keyboard
import re



def load_words(filename):
    with open(filename, 'r', encoding='ANSI') as f:
        text = f.read()
        
    words = re.findall(r"[a-zA-Z']+", text)
    
    words = [word.lower() for word in words if len(word) >= 5] 
    return words


def normal() :
    random_words = load_words('en.txt')

    holdon = input("press any key to continue...")
    while True :
        word = random.choice(random_words)
        
        os.system("cls")
        print(word + "\n\n\n")

        time.sleep(0.1)
        while True :
            if keyboard.get_hotkey_name() in ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']:
                break
                
        start = time.time()
        user = input().lower()
        end = time.time()
        elapsed = round(end - start, 3)


        passed = len(word)
        for i, n in enumerate(user):
            if i > len(word) - 1:
                passed -= 1
            elif n != word[i]:
                passed -= 1
        less = len(user) - len(word)
        if less < 0:
            passed += less

        percentege = round((passed / len(word)) * 100, 3) if passed >= 0 else 0

        print(f"it took you {elapsed} seconds\nyou got {percentege} accuracy")
        holdon = input()





def rush() :
    random_words = load_words('en.txt')

    times = []
    perces = []
    rush = False
    
    while True:
        try :
            n_words = int(input("how many words do you want to go through ? "))
            if not(n_words > 0):
                raise TypeError
            break
        except :
            print("numbers only")
    holdon = input("press any key to continue...")
    while True :
        word = random.choice(random_words)
        
        os.system("cls")
        print(word + "\n\n\n")

        time.sleep(0.1)
        while True :
            if keyboard.get_hotkey_name() in ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']:
                break
                
        start = time.time()
        user = input().lower()
        end = time.time()
        elapsed = round(end - start, 3)
        passed = len(word)

        for i, n in enumerate(user):
            if i > len(word) - 1:
                passed -= 1
            elif n != word[i]:
                passed -= 1
        less = len(user) - len(word)
        if less < 0:
            passed += less

        percentege = round((passed / len(word)) * 100, 3) if passed >= 0 else 0
        times.append(elapsed); perces.append(percentege)

        if len(times) == n_words :
            break

            
    print(f"avreage time : {round(sum(times) / len(times), 3)}\navreage accurcy : {round(sum(perces) / len(perces), 3)}")
    ghigeh = input()



if __name__ == "__main__":

    while True:
        gamemode = int(input("1.rush or 2.normal ?"))
        
        if gamemode == 1:
            os.system('cls')
            rush()
        elif gamemode == 2:
            os.system('cls')
            normal()
        else :
            print("invalid input")