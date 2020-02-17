def commaCode(spam):
    str1=' '
    str2='and '
    if spam[0:-2]:
        return (str1.join(spam))
    if spam[-2]:
        return (str2.join(spam))


spam= ['apples', 'bananas', 'tofu', 'cats']
print(commaCode(spam))


