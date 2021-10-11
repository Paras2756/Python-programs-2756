def time():
	import datetime
	return datetime.datetime.now()
w=input("What you want, to read the data(r) or to log the data(l) ")

def rde():
	cl=int(input("Whose record you want Harry(1) or Rohan(2) or Hamad(3) "))

	wh=int(input("What you want diet(1) or exercise(2) "))
	if wh==1:
		if cl==1:
			with open("harrydiet.txt","r") as f:
				f1=f.read()
				print(f1)
		elif cl==2:
			with open("rohandiet.txt","r") as f:
				f2=f.read()
				print(f2)
		elif cl==3:
			with open("hamaddiet.txt","r") as f:
				f3=f.read()	
				print(f3)
	elif wh==2:
		if cl==1:
			with open("harryexer.txt","r") as f:
				f1=f.read()
				print(f1)
		elif cl==2:
			with open("rohanexer.txt","r") as f:
				f2=f.read()
				print(f2)
		elif cl==3:
			with open("hamadexer.txt","r") as f:
				f3=f.read()	
				print(f3)
def de():
	cl=int(input("Who are you Harry(1) or Rohan(2) or Hamad(3) "))

	wh=int(input("What you will take diet(1) or exercise(2) "))
	if wh==1:
		d=input("What you will eat ? ")
		if cl==1:
			with open("harrydiet.txt","a") as f:
				f.write("["+str(t)+"] "+d+"\n")
				print("\nSuccessfully written your record")
		elif cl==2:
			with open("rohandiet.txt","a") as f:
				f.write("["+str(t)+"] "+d+"\n")
				print("\nSuccessfully written your record")
		elif cl==3:
			with open("hamaddiet.txt","a") as f:
				f.write("["+str(t)+"] "+d+"\n")
				print("\nSuccessfully written your record")
	if wh==2:
		e=input("Which exercise you will do ? ")
		if cl==1:
			with open("harryexer.txt","a") as f:
				f.write("["+str(t)+"] "+e+"\n")
				print("\nSuccessfully written your record")
		elif cl==2:
			with open("rohanexer.txt","a") as f:
				f.write("["+str (t)+"] "+e+"\n")
				print("\nSuccessfully written your record")
		elif cl==3:
			with open("hamadexer.txt","a") as f:
				f.write("["+str(t)+"] "+e+"\n")
				print("\nSuccessfully written your record")

			
t=time()
if w=="l":
	de()
elif w=="r":
	rde()	
else:
	print("It was not defined")



