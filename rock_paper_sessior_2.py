import random as rnd
ps=0
cs=0
#-----------------------------------------------------------------Header Section
for i in range(40):
	print("-",end="")
print("Welcome To Rock Paper Sessior Game ",end="")
for i in range(40):
	print("-",end="")

def invalid():
	print("\nPlease Chosse Your Option From Below : ")
	print('''1)    rock  : r
2)    paper : p 
3)   sessior : s
4 ) quit : q
''')
invalid()	
def hr():
	for i in range(50) :
		print("-",end="")
	return ' '	
hr()
#-----------------------------------------------------------------Header Section End
	
#-----------------------------------------------------------------Computer Choise  Section
def computer_choise():
	choise=rnd.choice(['r','p','s'])
	return choise
#-----------------------------------------------------------------Winner Choise  Section
def Winner(comp,player):
	global ps,cs
	if comp==player:
		choise={
		"r":"rock",
		"p":"paper",
		"s":"sessior"
		}
		print(f"""
				{hr()}
		       It's Tie You and Computer Both Choose :{choise[comp]}
			   {hr()}
			   """)
	elif ((comp=='r' and (player=='paper' or player=='p')) or
	(comp=='p' and (player=='rock' or player=='r' )) or
	(comp=='s' and(player=='paper' or player=='p'))
	) :
		cs+=1
		print(f'''{hr()}
___________________Computer Win___________________
										
You : {player}                        Your Score : {ps}
Computer :  {comp}            Computer Score : {cs}	
___________________________________________________
			{hr()}
					
		''')
		
	else:
		ps+=1
		print(f'''{hr()}
___________________You  Win___________________
		
You : {player}                        Your Score : {ps}
Computer :  {comp}            Computer Score : {cs}
___________________________________________________
{hr()}					
''')
		
#-----------------------------------------------------------------Winner  Section End

#-----------------------------------------------------------------Start From Here		
def Start(player):
		data=['rock','paper','sessior','r','p','s']
		if player in data:
			Winner(computer_choise().lower(),player.lower())
		else:
			invalid()
	
##----------------------------------------------------------------Player Choise
while True :
	player=input("\nEnter Your Turn :")
	
	if player != "quit" and player != "q" :
		Start(player.lower())
	else:
		print(f"--------------Thanks For Playing Game-------------- ")
		print(f'Your Score : {ps}')
		print(f'Computer  Score : {cs}')
		break
		