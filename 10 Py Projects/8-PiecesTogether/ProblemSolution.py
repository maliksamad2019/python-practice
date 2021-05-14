def sentance_maker(phrase):
    interogatives = ('how','what','why')
    capitalized = phrase.capitalize()
    if "phrase".lower().startswith(interogatives):
        return "{}?".format(capitalized)
    
    return "{}.".format(capitalized)

result = []

while True:
    userinput = input('Say something: ')
    if userinput == '\end':
        break
    else:
        result.append(sentance_maker(userinput))


print(" ".join(result))