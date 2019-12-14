from yolo import yolo

#initialize yolo instance
y = yolo()

countrycode = 1
phonenumber = 8880000000

#sends the verf code needed to login to your device
y.sendVerfCode(countrycode,phonenumber)

#you can automate this process anyway you want, but you're going to want to send pass the verf code as a string in the loginWithVerfCode() method.
#verfcode is typically six digits, texted to your device.
#this method initializes your session
i = str(input("code? "))
y.loginWithVerfCode(i)

#Prints out all avalible JSON data of your personal YOLO profile
print(y.selfInfo())

#Prints out your current session token
print(y.getSessionToken())

#Sends a message from your computer to someone's yolo profile.
#BEWARE: YOLO logs your IP! Be sure to use a proxy while sending. Can be done by editing Yolo.py in the sendMessage method.
#You can also just use a proxy/VPN on your computer to combat this.
y.sendMessage("user","message")

#Gets last 100 messages, pass a number to skip a certain amount. EX: 0 will return last 100 messages, 500 will go back 500 messages and return the last 100 starting from there
print(y.getMessages(0))

#Like selfInfo, but for other users. You can see someone's yolo code in the link they share.
print(y.getUser("user"))
