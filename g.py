def spam():
    global eggs
    eggs='spam local'
    print(eggs) #prints spam local

def bacon():
    global eggs
    eggs='bacon local'
    print(eggs)
    spam()
    print(eggs)
    return

eggs='global'
bacon()
print(eggs)


