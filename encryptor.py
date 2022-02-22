import keygenerator

Text = input("input:")
NewText = Text
LongMax = len(Text)

for i in range(LongMax):
    if Text[i] == "a" or Text[i] == "e" or Text[i] == "y" or Text[i] == "u" or Text[i] == "i" or Text[i] == "o" or Text[i] == "j":
        NewText = Text.replace(NewText[i],"1")
        Text = NewText
    else:
        NewText = Text.replace(NewText[i],"0")
        Text = NewText

NewText =+ keygenerator.GenerateKey(LongMax)
print(NewText)
