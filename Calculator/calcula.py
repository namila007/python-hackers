print(" |||CALCULATOR|||")
print("_________________")


first= input("Enter First Number : ")
second=input("Enter Second Number:")
func=input("Math functions available \n |'+' for addition       | \n |'-' for subtraction    | \n |'*' for multiplication | \n |'/' for division       | \n Insert Math function:")

if func == "+":

	ans=int(first) + int(second)
	print("------------")
	print("Answer=",ans)
	print("------------")
elif func== "-":
	ans=int(first) - int(second)
	print("------------")
	print("Answer=",ans)
	print("------------")
elif func== "*":
	ans=int(first) * int(second)
	print("------------")
	print("Answer=",ans)
	print("------------")
else :
	ans=int(first) / int(second)
	print("------------")
	print("Answer=",ans)
	print("------------")