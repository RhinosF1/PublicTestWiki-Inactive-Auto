import time
print("Welcome to the TestWiki:Inactivity Script")
print("This script is only for the use of Consuls")
print("Please now run the findInactive script")
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
#Fill out with title and template
print("Generating Community Noticeboard post")
#Fill out with CN text
print("Thanks for using!")
