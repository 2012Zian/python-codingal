print("enter marks of each subject")

Maths=int(input("enter your math mark"))
English=int(input("enter your English mark"))
Afrikaans=int(input("enter your Afrikaans mark"))
Zulu=int(input("enter your Zulu mark"))
Computing=int(input("enter your Computing mark"))
Global_siences=int(input("enter your Global_siences mark"))

sum = Maths + English + Afrikaans + Zulu + Computing + Global_siences
percentage=(sum/420)*100
print("this is your percentage",percentage)