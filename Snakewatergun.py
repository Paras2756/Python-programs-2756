print("We are playing snake water gun, you and comp are opponents and who will score 10 points first he or she will win.\n\n")

n=0
win=0
lost=0

while  win<=10 or lost<=10:
	import random
	list=["s","w","g"]
	r=random.choice(list)

	n+=1
	if lost>win and lost==10:
		print("\n\nYou lose ! your points were "+str(win)+" and comp points were "+str(lost))
		break

	elif lost<win and win==10:
		print("\n\nYou won ! your points were "+str(win)+" and comp points were "+str(lost))
		break
	you=input("Snake (s) or Water (w) or Gun(g) : ")
	
	if r==you:
		print("Both chosen same")
		print(f"Your points are {win} and comp points are {lost}")
		continue
	elif r=="s":
		if you=="w":
			print("You lose comp chosen",r)
			lost+=1
			print(f"Your points are {win} and comp points are {lost}")
		
			continue
		elif you=="g":
			print("You won comp chosen",r)
			win+=1
			print(f"Your points are {win} and comp points are {lost}")

			continue
	elif r=="w":
		if you=="g":
			print("You lose comp chosen",r)
			lost+=1
			print(f"Your points are {win} and comp points are {lost}")

			continue
		elif you=="s":
			print("You won comp chosen",r)
			win+=1
			print(f"Your points are {win} and comp points are {lost}")
			
			continue
	elif r=="g":
		if you=="s":
			print("You lose comp chosen",r)
			lost+=1
			print(f"Your points are {win} and comp points are {lost}")
			continue
		elif you=="w":
			print("You won comp chosen",r)
			win+=1
			print(f"Your points are {win} and comp points are {lost}")
			continue
