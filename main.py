import random

name_1 = str(input("\033[5;31;1m Enter your name:\033[0;0m"))
name_2 = str(input("\033[5;31;1m Enter your crush name:\033[0;0m"))
a = list(name_1.lower().replace(' ', ''))
b = list(name_2.lower().replace(' ', ''))
c = []
for i in a:
    for o in b:
        if i == o:
            c += i
        else:
            continue

for i in range(len(c)):
    try:
        a.remove(c[i])
        b.remove(c[i])
    except ValueError:
        pass

d = len(a) + len(b)


def friends():
    print(f"\033[1;35;40m {name_1.title()} and {name_2.title()}, you both are friends \033[0;0m")


def love():
    e = [f'\033[1;35;40m {name_1.title()} and {name_2.title()}, you have a hidden love on eachother \033[0;0m', f'\033[1;35;40m {name_1.title()} and {name_2.title()}, you love eachother \033[0;0m', f'\033[1;35;40m {name_1.title()} and {name_2.title()}, guys you are made for eachother \033[0;0m']
    print(random.choice(e))


def affection():
    f = [f'\033[1;35;40m {name_1.title()} and {name_2.title()}, you have affection towards eachother \033[0;0m', f'\033[1;35;40m {name_1.title()} and {name_2.title()}, you both have affection on eachother \033[0;0m']
    print(random.choice(f))


def marriage():
    g = [f'\033[1;35;40m {name_1.title()} and {name_2.title()}, you both are husband and wife \033[0;0m', f'\033[1;35;40m {name_1.title()} and {name_2.title()}, you both will get married soon \033[0;0m', f'\033[1;35;40m {name_1.title()} and {name_2.title()}, you both are cute couples \033[0;0m', f'\033[1;35;40m {name_1.title()} and {name_2.title()} you both looks cute when you guys are together, you will get married soon \033[0;0m']
    print(random.choice(g))


def enemy():
    h = [f'\033[1;35;40m {name_1.title()} and {name_2.title()}, you both are snake and mongoose \033[0;0m', f'\033[1;35;40m {name_1.title()} and {name_2.title()}, you are enemies \033[0;0m']
    print(random.choice(h))


def siblings():
    j = [f'\033[1;35;40m {name_1.title()} and {name_2.title()}, you both are siblings \033[0;0m', f'\033[1;35;40m {name_1.title()} and {name_2.title()}, you guys are good brother and sister \033[0;0m']
    print(random.choice(j))

flames = ["F", "L", "A", "M", "E", "S"]

while len(flames) > 1:
    formula = d % len(flames) - 1
    if formula >= 0:
        before = flames[formula + 1:]
        after = flames[:formula]
        flames = before + after
    else:
        flames = flames[:len(flames) - 1]

if flames == ['F']:
    friends()
if flames == ['L']:
    love()
if flames == ['A']:
    affection()
if flames == ['M']:
    marriage()
if flames == ['E']:
    enemy()
if flames == ['S']:
    siblings()