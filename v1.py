text=input("Enter your password:")
has_upper_case=0
has_lower_case=0
has_digit=0
has_special_Char=0
for character in text:
    if(character.isupper()):
        has_upper_case=1
    if(character.islower()):
        has_lower_case=1
    if(character.isdigit()):
        has_digit=1
    if(not character.isalnum()):
        has_special_Char=1
if(has_upper_case==1 and has_lower_case==1 and has_digit==1 and len(text)>=8 and has_special_Char==1):
    print("✅Strong Password!")
else:
    print("Weak Password❌")
    print("Missing:")
    if(has_upper_case==0):
     print("❌Add an uppercase letter!!")
    if(has_lower_case==0 ):
     print("❌Add an lowercase letter!!")
    if(has_digit==0):
     print("❌Add an digit!!")
    if( len(text)<8):
     print("❌Add more characters upto 8!!")
    if(has_special_Char==0 ):
     print("❌Add an special character!!")
