def convert(pic):
    with open(pic, "rb") as f:
        data12 = f.read()
        UU = data12.encode("base64")
    return(UU)

#print(convert('divider.png'))
