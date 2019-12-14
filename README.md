# Yolo-API

A Python API for interacting with the YOLO app.

##Security risks

While making this I discovered that all YOLO messages are sent with the sender's IP address being logged. On top of that, you can veiw all of your recieved messages along with the senders' ips. This opens the floodgates for people with malitious intent to track down people's locations that respond to their YOLOs. Also, you can view anyone's phone number with only their YOLO code; this is also dangerous. I would encourage the YOLO team to fix these issues.

## Documentation

**See examples.py for useage exmaples.**

**Make sure you have your phone number linked to your YOLO, can be done in the app**


###sendVerfCode(countrycode, phonenumber)
Sends the verification code needed to login to your device. Step one of logging in.

###loginWithVerificationCode(verfcode)
Logs into your YOLO with the provided verification code. It's reccomended that you use an input for the verification code as you need to wait for YOLO to text you the code. You are now logged into the account.

###selfInfo()
Returns a JSON structure of all data of your acccount:
**Some values have been edited for security**
```json
{
   "objectId":"my yolo code",
   "username":"username",
   "displayName":"Archer",
   "bitmojiAvatarUrl":"https://sdk.bitmoji.com/render/panel/6fd54c4f-fdd1-4283-a768-bf54dc9399ae-AS1tcjbzndEPSwy5ioL_twqocqCt-v1.png?transparent=1&palette=1",
   "createdAt":"2019-05-09T12:05:17.747Z",
   "updatedAt":"2019-12-14T04:40:55.505Z",
   "snapchatExternalId":"snapchat external ID",
   "phoneNumber":"my phone number",
   "bunchOpened":true,
   "ACL":{
      "*":{
         "read":true
      },
      "my yolo code":{
         "read":true,
         "write":true
      }
   },
   "__type":"Object",
   "className":"_User",
   "sessionToken":"current session token"
}
```

###getSessionToken()
Returns your session token. You shouldn't need to use this.

###getMessages(skip)
Returns the last 100 messages as a list. The skip arg will tell YOLO where to start at, EX if you put 10 it will show you your last 100 messages starting at the 10th message you've recieved.

Example of message JSON object:

```json
{
   "objectId":"object id",
   "createdAt":"2019-11-19T02:19:42.000Z",
   "updatedAt":"2019-11-19T02:19:42.000Z",
   "text":"hey cutie ;)",
   "_p_recipient":"_User$my yolo code",
   "seen":False,
   "replied":False,
   "deleted":False,
   "isBackUp":True,
   "cookie":"cookie",
   "wording":"Send anonymous messages",
   "ip":"The senders IP address",
   "__type":"Object",
   "className':'Message"
}
]
```

###getUser(user)
Returns avalible data about any user. You do not need to be logged in to use this. The JSON structure is identical to selfInfo() but all the info is someone else's instead of your's.

###sendMessage(user, text)
Sends an anonymous message to a specific user with the text of your choice. **BEWARE: YOLO logs your IP, so you may want to edit yolo.py to add proxies if you need to.**
