from time import sleep
from requests import Session
from stdiomask import getpass
from sys import argv, exit
from random import getrandbits

# Define the functions here


def remove():
    sleep(2)
    input("Press enter to continue or ctrl+c to quit")
    file = open('userinfo.cfg', 'r')
    userdata = file.read()
    file.close()
    try:
        if userdata == '-':
            opusername = input("Operator Username: ")
            fromheader = input("Bot Email: ")
        else:
            userdata.split(',')
            opusername = userdata[1]
            fromheader = userdata[2]
            username = userdata[3]
            log = input("Logged in to: " + str(userdata) + " - Confirm? Y/N: ")
            if log == "N":
                opusername = input("Operator Username: ")
                fromheader = input("Bot Email: ")
                username = input("Bot Username: ")
    except IndexError:
        opusername = input("Operator Username: ")
        fromheader = input("Bot Email: ")
    headers = {
        'User-Agent': 'BOT: ' + opusername + '@TestWikiAutoInactive-v1rc1',
        'From': fromheader
    }
    S = Session()
    URL = "https://publictestwiki.com/w/api.php"
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
    sleep(5)  # wait 5s to avoid throttling
    password = getpass()
    PARAMS_2 = {
        "action": "login",
        "lgname": username,
        "lgpassword": password,
        "lgtoken": LOGIN_TOKEN,
        "format": "json"
    }
    # destroy the password + replace with random hash
    password = getrandbits(125)
    R = S.post(URL, data=PARAMS_2, headers=headers)
    PARAMS_AUTH = {
        "action": "query",
        "format": "json",
        "meta": "userinfo",
        "uiprop": "email"
    }
    authres = S.post(URL, data=PARAMS_AUTH, headers=headers)
    EMAIL = authres.json()
    EMAIL = EMAIL["query"]["userinfo"]["email"]
    if fromheader == EMAIL:
        print("Email Authenticated!")
    else:
        fromheader = EMAIL
        print("Your email was replaced with " + fromheader)
        headers = {
            'User-Agent': 'BOT: ' + opusername + '@TestWikiAutoInactive-v1rc1',
            'From': fromheader  # rewrite header to user email
        }
    configfile = open('userinfo.cfg', 'w+')
    configfile.write(
        ',' +
        opusername +
        ',' +
        fromheader +
        ',' +
        username +
        ',')
    configfile.close()
    sleep(5)  # hold for 5s to avoid throttling
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
    users = input("How many users are being removed? ")
    userlist = []
    count = 0
    while count < int(users):
        usertemp = input("User to remove: ")
        userlist.append(usertemp)
        count = count + 1
        sleep(0.5)
    count = 0
    while count < len(userlist):
        inactiveuser = userlist[count]
        sleep(10)  # wait 10 seconds before write api
    # Step 4: Request to add or remove a user from a group
        PARAMS_4 = {
            "action": "userrights",
            "format": "json",
            "user": inactiveuser,
            "remove": "bot|sysop|bureaucrat|consul|testgroup|autopatrolled|confirmed|rollbacker|interface-admin|flow-bot|checkuser|interwiki-admin|oversight|steward",
            "reason": "per [[TestWiki:Inactivity|Inactivity report]]",
            "token": USERRIGHTS_TOKEN}
        count = count + 1
        R = S.post(URL, data=PARAMS_4, headers=headers)
        DATA = R.json()
        print(DATA)
    sleep(2)
    print('Generating mass message text..')
    print('{{subst:Inactivity|user=' + opusername + '}}')
    sleep(5)
    print("Thanks for using! Good bye.")
    exit()


def notify():
    sleep(10)
    consul = input("What is your username? ")
    removedate = input("Removal date: ")
    date = input("Today's Date: ")
    users = input("How many users are being removed? ")
    userlist = []
    count = 0
    while count < int(users):
        usertemp = input("User to remove: ")
        userlist.append(usertemp)
        count = count + 1
        sleep(0.5)
    print("Generating mass message list....")
    sleep(2)
    count = 0
    while count < len(userlist):
        print("User Talk:" + str(userlist[count]))
        count = count + 1
        sleep(0.5)
    print("Generating mass message text....")
    sleep(2)
    print("{{subst:InactiveReminder|DATE=" + removedate +
          "|sig=~~~ for [[User:" + consul + "|" + consul + "]]}}")
    print("Generating Community Noticeboard post")
    sleep(2)
    print("==Inactive Rights Removal - " + date + "==")
    print(
        "The rights of the following users will be removed on or after " +
        removedate +
        " if they do not return to activity:")
    count = 0
    while count < len(userlist):
        print("*{{RFP/User|" + userlist[count] + "}}")
        count = count + 1
    print("")
    print("Thanks,")
    print(":~~~")
    print(":For the Consul Team")
    print(":~~~~~")
    sleep(5)
    print("Thanks for using! Good bye.")


try:
    if argv[1] == 'remove':
        print("Running Script in Remove Mode")
        print("Welcome to the TestWiki:Inactivity Script")
        print("This script may only be used by consuls")
        print("Please ensure notifications were sent > 7 days ago and the users are still inacitve")
        remove()
    elif argv[1] == 'notify':
        print("Running Script in Notify Mode")
        print("Before we begin, please run the findInactive script on https://publictestwiki.com")
        print("The notification process will begin in 10 seconds")
        notify()
    elif argv[1] == 'help':
        print("Commands are:")
        print("remove - Removes rights from inactive users")
        print("notify - Generates messages for inactive users")
        print("help - Displays this help page")
    else:
        print("Unknown command. For help use 'main.py help'.")
except IndexError as e:
    print(e)
    print("Please specify an action (remove, notify)")
    exit()
