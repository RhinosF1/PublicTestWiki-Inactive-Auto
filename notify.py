import time
print("Welcome to the TestWiki:Inactivity Script")
print("This script is only for the use of Consuls")
print("Please now run the findInactive script")
consul = input("What is your username? ")
removedate = input("Removal date: ")
date = input("Today's Date:" )
time.sleep(10)
users = input("How many users are being removed?")
userlist = []
count = 0
while count < len(users)-1:
  usertemp = input("User to remove:")
  userlist.append(usertemp)
  count = count + 1
print("Generating mass message list....")
count = 0
while count < len(users)-1:
  print("User Talk:" + str(userlist[count]))
  count = count + 1
print("Generating mass message text....")
print("{{subst:InactiveReminder|DATE=" + removedate + "|sig=~~~ for [[User:"+consul +"|"+consul + "]]}}")
print("Generating Community Noticeboard post")
print("==Inactive Rights Removal - "+ date + '==")
print("The rights of the following users will be removed on or after " + removedate + " if they do not return to activity:")
count = 0
while count < len(users)-1:
      print("*{{RFP/User|"+userlist[count]+"}}")
print("")      
print("Thanks,")
print(":~~~")
print(":For the Consul Team")
print(":~~~~~")
print("Thanks for using!")
