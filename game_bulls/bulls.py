# 👱 🆚 🤖 (1 - player mode)
####	Bulls and Cows with AI    ####

import random
def vt (g, n): # g ➡ string and n ➡ string
    t=v=0
    for i in range(4) :
        if g[i] == n[i] :
            t+=1
        elif g[i] in n :
            v+=1
    return (str(t) + str(v))

def distinct (n) :  # n ➡ string
    test = True
    if n[0] == "0" :
        test = False
    if int(n) < 1000 or int(n) > 9999 :
        test = False
    if test == True :
        for i in range(3) :
            if (n.count(n[i]) > 1) :
                test = False

    return test

def liste (k, u, g) :# k ➡ list,  u ➡ string, g ➡ string
    r=[]
    for i in k :
        if vt(g,str(i)) == u :
            r.append(i)
    return r

def k0 () :
    s=[]
    for i in range(1000, 10000) :
        if distinct(str(i)) :
            s.append(i)
    return s


stop = False
while stop == False:
    print("""Think about a number between 1000 and 9999 💭
such as its digits are distinct
Let's start now : You 👱 Start""")

    possible = k0()  # possible is a list of integer
    num = possible[random.randint(0, len(possible) - 1)]

    while True:
        while True:
            try:
                print("\n\tYour 👱 turn")
                choice = str(int((input("Guess my number💭: "))))
                if distinct(str(choice)):
                    break
            except:
                continue
        print(vt(str(choice), str(num))[0], "bulls and", vt(str(choice), str(num))[1], "cows")
        if vt(str(choice), str(num))[0] == "4":
            print("Wow! You're amazing, you managed to beat a robot as smart as me. Respect! 🙌")
            break
        else:
            print("\n\t  My 🤖 turn")

        try:
            guess = str(possible[random.randint(0, len(possible) - 1)])
            if len(possible) == 1:
                print("HAHAHA I won 💪: ", possible[0])
                break

            print("Number 🤖 guessed: ", guess)
            v = input("How many cows   ☆: ")
            t = input("How many bulls  ★: ")

            vtt = t + v
            if t == "4":
                print("HAHAHAA! I won 💪: ", guess)
                break

            possible = liste(possible, vtt, guess)
            if len(possible) == 0:
                print("You apparently made a mistake somewhere!😤")
                break
        except:
            print("You apparently made a mistake somewhere!😤")
            break

    while True:
        haha = input("\nDo you wish to play again❓ yes/no: ")
        if "no" in haha or "No" in haha or "NO" in haha or "yes" in haha or "YES" in haha or "Yes" in haha:
            if "no" in haha or "No" in haha or "NO" in haha:
                stop = True
            break
    print("""
     """)