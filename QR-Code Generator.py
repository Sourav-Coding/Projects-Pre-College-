import qrcode as qr
a=int(input("1:- Link to QR Code\n2:- Text to QR Code\n3:- Number to QR Code\nEnter your choice :- "))
if a==1:
    link=input("Enter Your Link : ")
    img=qr.make(link)
    img.save("Link.png")
elif a==2:
    text=input("Enter Your Text : ")
    img=qr.make(text)
    img.save("Text.png")
elif a==3:
    num_=input("Enter Your Number : ")
    img=qr.make(num_)
    img.save("Number.png")
print("The QR Code has been saved where this program is saved")
print("THANK YOU")



