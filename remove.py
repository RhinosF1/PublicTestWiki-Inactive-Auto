import time
import requests
import stdiomask
print("Welcome to the TestWiki:Inactivity Script")
print("This script may only be used by consuls")
print("Please ensure notifications were sent > 7 days ago and the users are still inacitve")
time.sleep(2)
input("Press enter to continue or ctrl+c to quit")
users = input("How many users are being removed? ")
userlist = []
count = 0
while count < int(users):
  usertemp = input("User to remove: ")
  userlist.append(usertemp)
  count = count + 1
  time.sleep(0.5)
fromheader = input("Your Email: ")
headers = {
    'User-Agent': 'PublicTestWikiInactiveAuto-github/rhinosf1-fortestwikiconusls',
    'From': fromheader
}
S = requests.Session()
URL = "https://test.miraheze.org/w/api.php"
# Step 1: Retrieve a login token
PARAMS_1 = {
    "action": "query",
    "meta": "tokens",
    "type": "login",
    "format": "json"
}
R = S.get(url=URL, params=PARAMS_1, headers=headers)
DATA = R.json()
LOGIN_TOKEN = DATA["query"]["tokens"]["logintoken"]
# Step 2: Send a post request to log in. See
# https://www.mediawiki.org/wiki/Manual:Bot_passwords
time.sleep(1) #wait 1s to avoid throttling
username = input("Username: ")
password = stdiomask.getpass()
PARAMS_2 = {
    "action": "login",
    "lgname": username,
    "lgpassword": password,
    "lgtoken": LOGIN_TOKEN,
    "format": "json"
}
R = S.post(URL, data=PARAMS_2, headers=headers)
time.sleep(1) #hold for 1s to avoid throttling
# Step 3: Obtain a Userrights token
PARAMS_3 = {
    "action": "query",
    "format": "json",
    "meta": "tokens",
    "type": "userrights"
}
R = S.get(url=URL, params=PARAMS_3, headers=headers)
DATA = R.json()

USERRIGHTS_TOKEN = DATA["query"]["tokens"]["userrightstoken"]

count = 0
while count < len(userlist):
  inactiveuser = userlist[count]
    time.sleep(5) #wait 5 seconds before write api
# Step 4: Request to add or remove a user from a group
  PARAMS_4 = {
      "action": "userrights",
      "format": "json",
      "user": inactiveuser,
      "remove": "bot|sysop|bureaucrat|consul|testgroup|autopatrolled|confirmed|rollbacker|interface-admin|flow-bot|checkuser|interwiki-admin|oversight|steward",
      "reason": "per [[TestWiki:Inactivity|Inactivity report]]",
      "token": USERRIGHTS_TOKEN
  }
  count = count + 1

  R = S.post(URL, data=PARAMS_4)
  DATA = R.json()

  print(DATA)
time.sleep(2)
print('Generating mass message text..')
print('{{subst:Inactivity|user='+username+'}}')
time.sleep(5)
print("Thanks for using!")
