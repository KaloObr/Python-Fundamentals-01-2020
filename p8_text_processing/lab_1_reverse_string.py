text = input()

while text != "end":

    # text_reversed = ''
    # for ch in reversed(text):
    #     text_reversed += ch
    # #print(text + " = " + text_reversed)

    print(f"{text} = {''.join([x for x in text[::-1]])}")

    text = input()

