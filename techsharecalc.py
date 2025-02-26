import math

print("Hello, and welcome to Jonnemannis Tech Share Calculator.")
print("(Copykek Jonnemanni 2021)")
print(" ")

partnernum = 0
while True:
    try:
        partnernum = int(input("How many Tech Trading Partners do you have?\n"))

        if partnernum < 1:
            raise Exception("No 0 or negative numbers.")

    except ValueError:
        print("This value is not a whole number.")

    except Exception:
        print("This value can't be below 1.")

    else:
        break

# Tech bases are identified as a number in ascending order, with the range from one number to another deciding the bonus for the lesser partner.
# No Base       = 1
# Minimal Base  = 2
# Growing Base  = 3
# Decent Base   = 4
# Modern Base   = 5
# Technocracy   = 6
# Stagnant      = 7

mytechbase = 0
while True:
    try:
        mytechbase = int(input("What is your Tech Base?\nNo Base = 1\nMinimal Base = 2\nGrowing Base = 3\nDecent Base = 4\nModern Base = 5\nTechnocracy = 6\nStagnant = 7\n"))

        if mytechbase < 1 or mytechbase > 7:
            raise Exception("Value must be between 1 and 7.")

    except ValueError:
        print("This value is not a whole number.")

    except Exception:
        print("Value must be between 1 and 7.")

    else:
        break

partners = []

for partner in range(partnernum):

    partnername = input("What is the name of partner {}?\n".format((partner+1)))

    while True:
        try:
            othertechbase = int(input("What is the Tech Base of {}?\nNo Base = 1\nMinimal Base = 2\nGrowing Base = 3\nDecent Base = 4\nModern Base = 5\nTechnocracy = 6\nStagnant = 7\n".format(partnername)))

            if othertechbase < 1 or othertechbase > 7:
                raise Exception("Value must be between 1 and 7.")

        except ValueError:
            print("This value is not a whole number.")

        except Exception:
            print("Value must be between 1 and 7.")

        else:
            break
    
    bonus = 0
    if othertechbase <= mytechbase:
        bonus = 1
    else:
        bonus = othertechbase - mytechbase + 1

    partners.append({'name':partnername, 'techbase':othertechbase, 'bonus':bonus})

def myFunc(e):
    return e['bonus']

partners.sort(reverse=True, key=myFunc)

for index, partner in enumerate(partners):

    if index == 0:
        continue

    partner['bonus'] /= 2 ** index

total = 0

print("—————————————————————————————————————————————————")
print("Your nations Tech Base level is", mytechbase)
print("Your partners are...")
for partner in partners:
    print("{name}'s Tech Base is level {level}, and they give you a total bonus of {bonus}.".format(name = partner['name'], level = partner['techbase'], bonus = partner['bonus']))
    total += partner['bonus']

total = math.floor(total)
print("Your total bonus is", total)

input("Press Enterto exit.")