spam=[1,2,3,4]

def eggs(spam):
    spam.append('Hello')
    return spam.append('hello')

for i in spam:
    eggs(spam)
    print(spam)
    if len(spam) > 50:
        break





