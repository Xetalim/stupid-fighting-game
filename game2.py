import random
# bunch of stats about player, needs to be organised
damage = 1
weapons = {"Moo": 1, "Moo1": 2}
player_health = 5
player_maxhealth = 5
player_defense = 2
player_attack = 1
player_xp= 0
zombie = {'name': 'the zombie', 'health': 1, 'power': 1, 'aname': 'a zombie', 'exp': 1}
skeleton = {'name': 'the skeleton', 'health': 50, 'power': 5, 'aname': 'a skeleton', 'exp': 2}
none = {'name': 0, 'health': 0}
an = {zombie['name']: 'a zombie', skeleton['name']: 'a skeleton'}
enemy = zombie
enemyname = enemy['name']
#attacks the enemy using a value that is your weapon
def attack_enemy(weapon):
	enemy['health'] -= damage * weapon
	print "You have attacked %s for %r damage! %s is at %r health now!" % (enemy['name'], damage * weapon, enemy['name'].capitalize(), enemy['health'])
#again, needs to be organised
can_run = 1

# attacks the player by subtracting amount of damage from the player health
def attack_player():
	global player_health
	damage_taken = player_defense-enemy['power']
	if damage_taken < 0:
		player_health += damage_taken
	else:
		player_health -= player_defense-enemy['power']
	print "%s has attacked you for %r damage! Your health is at %r now!" % (enemy['name'].capitalize(), abs(damage_taken), player_health)

#ignore this
def turn():
	global enemy
	global anenemy
	attack_enemy(1)
	attack_player()
	enemy = skeleton
	anenemy = skeleton
#ignore this
def next():
	attack_enemy(1)
	attack_player()
# needs to be organised
youran = 0
first = 1
# main function, does a lot of things
def an_enemy_is_still_here():
	global can_run
	global first
	global youran
	# tells what should be shown at the start
	if first == 1:
			print "You have encountered %s! What do you do?" % enemy['aname']
			first = 0
	elif first == 0:
		print "%s is still alive. What do you do?" % enemy['name'].capitalize()
# gives a bunch of options
	print "1: Attack %s!" % enemy['name']

	if can_run == 1:
		print "2: Run from %s." % enemy['name']

	elif can_run == 0:
		print "2: You can't run!"


	print "3: Wait for %s to attack." % enemy['name']

	choice = raw_input("> ")
# asks for choice
	if choice == "1":
			
		attack_enemy(player_attack)
		if enemy['health'] == 0:
			removeenemy()
			return
			# attacks enemy if 1 is chosen, if enemy health reaches 0 kill it
		attack_player()

		an_enemy_is_still_here()

		first = 0
# let's player run if chosen 2, random chance to run or not
	elif choice == "2" and can_run == 1:
		if random.randint(0, 10) < 5:
			print "You've sucessfully run from %s!" % enemyname
			youran=1
			removeenemy()

		else:
			print "You tripped and can't run anymore!"
			attack_player()

			can_run = 0

			an_enemy_is_still_here()

			first = 0

	elif choice == "2" and can_run == 0:
		print "You can't run!"

		an_enemy_is_still_here()
			
		first = 0
# most useless function, get attacked, might use this for counterattacks
	elif choice == "3":
		attack_player()

		an_enemy_is_still_here()
			
		first = 0

	elif choice != 3 and choice != 2 and choice != 1:
		print "I don't understand your input D:"
		an_enemy_is_still_here()
		first = 0


#kills the enemy
def removeenemy():
	global enemy
	if youran == 1:
		print "You ran from the %s!" % enemy['name']
		enemy = none
	elif youran == 0:
		print "You have defeated the %s. You gain %r experience!" % (enemy['name'], enemy['exp'])
		enemy = none


an_enemy_is_still_here()