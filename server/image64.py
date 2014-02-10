def hex2htmlPicture(string):
    return '<img height="{}" src="data:image/png;base64,{}">{}'.format(str(picture_height), string, '{}')
def file2hexPicture(fil):
    return image64.convert(fil)
def file2htmlPicture(fil):
    return hex2htmlPicture(file2hexPicture(fil))
def convert(pic):
    with open(pic, "rb") as f:
        data12 = f.read()
        UU = data12.encode("base64")
    return(UU)

#print(convert('divider.png'))
