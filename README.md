# Lab07CoasterLoop
List + For loop application Lab

# Scenario
You are a theme park designer. Your latest project is Clappy’s Carnival of Fun for Family and Friends, a theme park that hopes to be known for its speedy lines and family diner. As a part of your job, you have to manipulate the lines to help keep guests entertained, as well as keeping track of what areas may be splash zones, setting up countdowns to be read out before the rollercoasters take off, and planning the randomly generated special birthday dance!

# Step 0
Before getting started, take a look at the code for Step 0 and do your best to understand what it is doing–this may help you with writing the other steps. 
*YOU DO NOT HAVE TO CODE ANYTHING FOR THIS STEP*

# Step 1: Line Management — lineManage(customers)
As at many theme parks, the rollercoasters at Clappy’s Carnival of Fun have lines. For this function, use a for-loop to fill a list with numbers from 0 to (customers-1), then add “now that’s a line!” to the end. Return this list.

   Ex: lineManage(5) should return [0, 1, 2, 3, 4, “now that’s a line!”] 

# Step 2: Line Management, the Sequel, Now With More Water! — lineSplash(customers)
Jimmy’s Tower of Fun and Not Scares is a rollercoaster whose line passes under Splashy Splashington’s Splash-a-Palooza. Because of this, there is a chance that some of the guests will get splashed when they walk under it. For this function, use a for-loop to fill a list with numbers from 0-customers. If the number is divisible by 3, add “splashed!” to the list instead of the number. Return the list.

  Ex: lineSplash(5) should return [“splashed”, 1, 2, “splashed!”, 4]

# Step 3: Connie the Carnival Animatronic’s Special Countdown! — connieCountdown(num)
Connie the Carnival Animatronic is an animatronic in charge of some of the roller coaster rides and games. When in charge of rollercoasters, they do a special countdown. Connie picks a number and then counts down from that number to 1, and then says “Happy New Years!” For connieCountdown(num), use a for-loop to make a list from num-1 and then add “Happy New Years!” to the end. Return this list.

  Ex: connieCountdown(10) should return [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, “Happy New Years!”]


# Step 4: Connie the Carnival Animatronic’s Ring Toss Spectacular! ringToss(rolls, success)
 *Note: Where rings and success are both lists*
The Ring Toss Spectacular is a rather interesting attraction at Clappy’s. To win this game, the player rolls 6 20 sided die and Connie does the same. Each roll the player has that matches one of Connie’s is considered a success. For this function, you will write a nested for-loop like the kind seen below that goes through the list of rolls and compares each roll to each of the rolls in the success list. If it is a success, append to a list “Success for [number]”. For example, if the number 3 was a success, append “Success for 3”. Return this list.


  Example of nested for-loop:
	  for i in lst1:
		  for j in lst2:
			  print(i, j)

  Ex: ringToss([10, 3, 5, 7, 20, 19], [19, 3, 18, 12, 15, 1]) should print:
  “Success for 3”
  “Success for 19”

# Step 5: Happy Clappy’s Family Diner Birthday Dosido Spectacular! — dinerDance(start, numMoves)
Clappy’s Family Diner workers like to perform a special dance for customer birthdays. What makes this dance so special? It is somewhat random. For this function, you will be building and returning a list that consists of numMoves moves. To get each dance move, take start and multiply it by 2, add 4, and divide by 3 – make sure to keep your number casted to an int. 

  1. If the number is divisible by 3, add “spin” to your dance. 
  2. Otherwise, if the number is divisible by 4, add “side step” to your dance. 
  3. Otherwise, if the number is divisible by 5, add “shake hips”
  4. Otherwise, if the number is even, add “freestyle” to your dance. 
  5. For anything else, add “hop” to your dance.


  Ex: dinerDance(50, 4) should return [“freestyle”, “spin”, “hop”, “spin”]
  
# Step 6: Turn It In!
  Turn it in to submit mode on Zybooks
