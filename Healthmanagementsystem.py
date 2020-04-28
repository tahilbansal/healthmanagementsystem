#3 clients - Harry,Rohan, Hammad
def getdate():
    import datetime
    return datetime.datetime.now()
# Total 6 files
# write a function that when executed takes as input client name

print("What you want to do ?\n" "1. Lock\n" "2. Retrieve\n")
num = int(input())
if num == 1:
    num1 = "lock"
else:
    num1 = "Retrieve"
print("Which client\n" "1. Harry\n" "2. rohan\n" "3. hammad\n")
client = int(input())
print("What you want to " + num1 + "\n1. Diet\n" "2. Workout\n")
select = int(input())

if (client ==1) :
    if(select ==1):
        if(num==1):
            f = open("harry_diet.txt","a")
            a = f.write (str(getdate()) + ":" + str(input()) + "\n")
            f.close()

        if(num == 2):
            f = open("harry_diet.txt")
            a = f.read()
            print(a)
            f.close()
    elif(select ==2):
        if (num == 1):
            f = open("harry_workout.txt", "a")
            a = f.write(str(getdate()) + ":" + str(input()) + "\n")
            f.close()

        if (num == 2):
            f = open("harry_workout.txt")
            a = f.read()
            print(a)
            f.close()






