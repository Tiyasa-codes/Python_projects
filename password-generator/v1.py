text=input("Enter your password:")
has_upper_case=False
has_lower_case=False
has_digit=False
has_special_Char=False
for character in text:
    if(character.isupper()):
        has_upper_case=True
    if(character.islower()):
        has_lower_case=True
    if(character.isdigit()):
        has_digit=True
    if(not character.isalnum()):
        has_special_Char=True
if(has_upper_case and has_lower_case and has_digit and len(text)>=8 and has_special_Char):
    print("✅Strong Password!")
else:
    print("Weak Password❌")
    print("Missing:")
    if(not has_upper_case):
     print("❌Add an uppercase letter!!")
    if(not has_lower_case):
     print("❌Add an lowercase letter!!")
    if(not has_digit):
     print("❌Add an digit!!")
    if( len(text)<8):
     print("❌Add more characters upto 8!!")
    if(not has_special_Char):
     print("❌Add an special character!!")
