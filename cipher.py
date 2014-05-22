text=raw_input("Enter TEXT : ")
text=list(text)
factor=input("Enter Cipher Factor : ")
factor=factor%26
dict_conv={}
for i in range(26):
    ascii=i+65
    new_ascii=(ascii)+factor
    if new_ascii > 90:
        new_ascii = 65+(new_ascii-91)
    dict_conv[chr(ascii)]=chr(new_ascii)
    dict_conv[chr(ascii+32)]=chr(new_ascii+32)
for index in range(len(text)):
    small = (ord(text[index]) >= 65) and (ord(text[index]) <= 90)
    caps = (ord(text[index]) >= 97) and (ord(text[index]) <= 122)
    if(small or caps):
        text[index]=dict_conv[text[index]]
print ''.join(text)
