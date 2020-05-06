import time
print("Welcome to the TestWiki:Inactivity Script")
print("This script is only for the use of Consuls")
print("Please now run the findInactive script")
time.sleep(10)
consul = input("What is your username? ")
removedate = input("Removal date: ")
date = input("Today's Date: " )
users = input("How many users are being removed? ")
userlist = []
count = 0
while count < int(users):
  usertemp = input("User to remove: ")
  userlist.append(usertemp)
  count = count + 1
  time.sleep(0.5)
print("Generating mass message list....")
time.sleep(2)
count = 0
while count < len(userlist):
  print("User Talk:" + str(userlist[count]))
  count = count + 1
  time.sleep(0.5)
print("Generating mass message text....")
time.sleep(2)
print("{{subst:InactiveReminder|DATE=" + removedate + "|sig=~~~ for [[User:"+consul +"|"+consul + "]]}}")
print("Generating Community Noticeboard post")
time.sleep(2)
print("==Inactive Rights Removal - "+ date + "==")
print("The rights of the following users will be removed on or after " + removedate + " if they do not return to activity:")
count = 0
while count < len(userlist):
      print("*{{RFP/User|"+userlist[count]+"}}")
      count = count + 1
print("")      
print("Thanks,")
print(":~~~")
print(":For the Consul Team")
print(":~~~~~")
time.sleep(5)
print("Thanks for using!")
