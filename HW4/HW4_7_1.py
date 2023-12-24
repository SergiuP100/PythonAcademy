text = input("Write a Text :    ")
punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
for i in text:
    if i in punctuation:
        text = text.replace(i, "")
print("This is the new Text :   ", text)