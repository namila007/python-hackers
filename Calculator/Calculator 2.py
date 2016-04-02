import sys
import ctypes
first=None     #global variables
second=None
op=None
box=ctypes.windll.user32.MessageBoxW #win error box assigning

def start():

	global first  #assigning global var to local var
	global second
	global op
	first=input(" |Enter First Number:")
	op=input(" |Math functions available \n |1. '+'  addition       | \n |2.'-'  subtraction     | \n |3. '*'  multiplication | \n |4. '/'  division       | \n |Insert Math function number:")
	#if op=="None":
	#	box(None,"Enter a fucntion","Error",0)
	#	op=input(" |Insert Math function number:")
	#else:	
	second=input(" |Enter Second Number:")
	
	
	return (first,second,op) 

def cal(fi,se):
	ans=None
	#calculation
	
	# _,_,op=start() old way to assign var for return fucntion
	
	if op == "1":
		ans=int(fi)+int(se)
		
	elif op == "2":
		ans=int(fi)-int(se)
	elif op == "3":
		ans=int(fi)*int(se)	
	elif op=="4":
		if se=="0":
			box(None, "Cant divide by Zero(0)","Error!", 0) #error box
			run()
		else:
			ans=int(fi)/int(se)
	print(" |Answer=",ans)	
	print("******************")		
		
	
def run():
	print("----------------------")	
	print(" |||CALCULATOR V2.0|||")
	print("----------------------")	
	start()
	
	
	cal(first,second)
	again=input("Do you need to calculate again? Y/N:") #recalculation
	if again=="y":
		print("----------------------")	
		print(" |||CALCULATOR V2.0|||")
		print("----------------------")	
		run()	
		
	else:
		sys.exit(0) #exit the program
	
#programme	

run()	
