text=input("Enter your password:")
flag=0
flag2=0
flag3=0
flag4=0
for character in text:
    if(character.isupper()):
        flag=1
    if(character.islower()):
        flag2=1
    if(character.isdigit()):
        flag3=1
    if(not character.isalnum()):
        flag4=1
if(flag==1 and flag2==1 and flag3==1 and len(text)>=8 and flag4==1):
    print("✅Strong Password!")
else:
    print("Weak Password❌")
    print("Missing:")
    if(flag==0):
     print("❌Add an uppercase letter!!")
    if(flag2==0 ):
     print("❌Add an lowercase letter!!")
    if(flag3==0):
     print("❌Add an digit!!")
    if( len(text)<8):
     print("❌Add more characters upto 8!!")
    if(flag4==0 ):
     print("❌Add an special character!!")


# text = input("Enter your password: ")

# for character in text:
#     if character.isupper():
#         print("True")
#         break
# else:
#     print("False")