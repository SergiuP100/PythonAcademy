text = input("Write a Text :    ")
for i in text:
    if (i == "." or i == "?" or i == "!" or i == "," or i == ";" or i == ":" or i == "—" or i == "–" or i == "-" or i == "(" or i == ")" or i == "[" or i == "]" or i == "{" or i == "}" or i == "'" or i == '"' or i == "`" or i == "..." or i == "*" or i == "^" or i == ","):
        text = text.replace(i, "")
print("This is the new Text :   ", text)