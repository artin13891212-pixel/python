def char(text):
    count=0
    for char in text:
        if char !=" ":
            count=count+1
    return count
text="hello python"
print(char(text))
