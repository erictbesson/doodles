#Python 2.7.6 (default, Nov 10 2013, 19:24:24) [MSC v.1500 64 bit (AMD64)] on win32
#Type "copyright", "credits" or "license()" for more information.
import random

#Some test characters as dictionaries
Kiro = {'name': 'Kiro', 'speed': 10, 'HP': 100, 'atk':10}
Slime = {'name': 'Slime', 'speed': 5, 'HP':20, 'atk':10}
Bee = {'name': 'Bee', 'speed': 20, 'HP':10, 'atk':5}

#Implement test characters as classes instead?
#class Attributes:
#   name
#   speed


class Participant:
	"""
	Base Class for enemy participants and party members.  Need another class which tokenizes the enemy participants.
	"""
	def __init__(self, name, speed=10, hp=100, atk=10):
		self.name = name
		self.speed = speed
		self.hp = hp
		self.atk = atk


class Ally_Participant(Participant):
	"""
	Derived Class for allies
	"""
	def ally_attack_enemy(self, target_choice):

		"""
		Code for a basic attack against an enemy.
		"""
		damage_dealt = self.atk #to be adjusted by a real formula later
		print self.name, "attacks", target_choice.name, ", dealing", damage_dealt, "damage."
		target_choice.hp = target_choice.hp - damage_dealt
		if target_choice.hp <= 0:
			enemy_is_defeated(target_choice.name)


class Enemy_Participant(Participant):
	"""
	Derived Class for enemies
	"""	

	
	def enemy_attack_ally(self, target_choice):
    """
    Code for a basic attack against an ally.
    """
		damage_dealt = self.atk #to be adjusted by a real formula later
		print self.name, "attacks", target_choice.name, ", dealing", damage_dealt, "damage."
		target_choice.hp = target_choice.hp - damage_dealt
		if target_choice.hp <= 0:
			party_member_is_defeated(target_choice.name)
	
	def random_ally_target(self):
   		return test_allies[random.randint(0,len(test_allies)-1)]

   	def basic_attack(self):
   		enemy_attack_ally(self, random_ally_target)









kiro = Ally_Participant('Kiro', 10, 100, 10)
slime = Participant('Slime', 5, 20, 10)
bee = Participant('Bee', 20, 10, 5)


test_Participants = [Kiro, Slime, Bee]

test_allies = [Kiro]
test_enemies = [Slime, Bee]

#Readiness Stages
#a = act
#b = backswing
#r = ready




global_participant_readiness = []

def battle_Readiness_Init(Participants):
    """
    Creates a list of list-pairs of particpants and their readiness, with their readiness taking default values.
    """
    party_names = [entry['name'] for entry in test_allies]
    # for entry in test_allies:
    #     party_names.append(entry['name'])
    enemy_names = [entry['name'] for entry in test_enemies]
    # for entry in test_enemies:
    #     enemy_names.append(entry['name'])

    print "Party:", party_names  # Need to expand this latter
    print "Enemies:", enemy_names
    for entry in Participants:
        global_participant_readiness.append([entry, [1000, 'b']])
    return global_participant_readiness





def finish_list_2nd_element(p):
    return p[1]

def battle_Orderer(Participants_Readiness):
    """
    I imagine participants to be a list of participants where participants are dictionaries with relevant stats
    Participants_Readiness would be a global variable which lists list-pairs of how close to ready each participant is (float down to 0) and whether that character is acting (and can be interrupted) or is just waiting)
    """
    finish_list = []
    #The current code does not factor in participants waiting at ready.
    for participant in Participants_Readiness:
        finish_list.append([participant[0]['name'], participant[1][0]/participant[0]['speed'], participant[1][1]])
    finish_list.sort(key=finish_list_2nd_element)
    order = []
    for entry in finish_list:
        order.append(entry[0])
    print 'Turn Order:', order
    status_screen()
    return finish_list


def status_screen():
    sum_hp_blocks = []
    names_list_maxed = []
    HP_list_maxed =[]
    char_max = 0
    for entry in global_participant_readiness:
        names_list_maxed.append(entry[0]['name'])
        HP_list_maxed.append(str(entry[0]['HP'])+'HP')
        if len(entry[0]['name']) > char_max:
            char_max = len(entry[0]['name'])
        if len(str(entry[0]['HP'])) > char_max:
            char_max = len(str(entry[0]['HP']))
    print string_space_adder(names_list_maxed, char_max)
    print string_space_adder(HP_list_maxed, char_max)


def string_space_adder(list, char_max):
    new_list = []
    for element in list:
        if len(element) < char_max:
            dif_element_char_max = char_max-len(element)
            new_element = element +' '*dif_element_char_max
            new_list.append(new_element)
        else:
            new_list.append(element)
    return new_list



def get_next_turn(finish_list):
    """
    Figures out who will be acting next (next participant to become ready, excluding those waiting at ready).  Advances time until that participant is ready 
    """
    for entry in finish_list:
        if entry[2] != 'r':#ignore waiting characters
            time_advance(entry[1])
            print entry[0], 'is ready!'
            return entry[0]





def action_turn_end_clean_up(participant, backswing_recovery=1000):
    """
    Takes the participants name as input.  Optionally takes custom backswing recovery value.
    Ends the participants turn, giving him defualt readiness and setting him in backswing.
    Switches all participants waiting at ready to backswing so they have a new opportunity to act.
    """
    #edit this code to do the first part! global_participant_readiness[0].index(participant)
    for entry in global_participant_readiness:
        if entry[0]['name'] == participant:
            entry[1] = [backswing_recovery, 'b']
        if entry[1][1] == 'r':
            entry[1][1] = 'a'
    return




def time_advance(n):
    """
    Advances time n steps.
    """
    i = 0
    while i < n :
        time_step()
        i += 1
    return

def time_step():
    """
    Advances time one step.  Add in more code for damage/healing over time eventually
    """
    for participant in global_participant_readiness:
        participant[1][0] = participant[1][0]-participant[0]['speed']#advance participants towards being ready one step
    return


def battle_run(allies, enemies):
    """
    Runs a battle until all enemies or allies are defeated.  Or will.
    I dislike how expandable this function is.  Change it eventually.
    """
    while allies:
        while enemies:
            nexts_name = get_next_turn(battle_Orderer(global_participant_readiness))
            if nexts_name == 'Bee':
                action_turn_end_clean_up(bee_turn())
            else:
                if nexts_name == 'Kiro':
                    action_turn_end_clean_up(player_turn('Kiro'))
                else:
                    if nexts_name == 'Slime':
                        action_turn_end_clean_up(slime_turn())    
        print 'Victory!'
        return
    print 'Defeat!'


def player_turn(party_member):
    """
    Lists player action choices.
    Returns party_member [the input].
    """
    made_a_choice = False
    while made_a_choice == False:
        action_choice = int(raw_input('What will you do? \n 1: Attack \n 2: Wait \n'))
        if action_choice == 1:
            enemies_string = 'Whom will you attack?'
            i = 1
            for entry in test_enemies:
                enemies_string = enemies_string+"\n "+str(i)+":"+entry['name']
                i +=1
            enemies_string = enemies_string+"\n "+str(i)+": cancel"
            target_choice_value = int(raw_input(enemies_string + '\n'))
            if target_choice_value > i-1:
                made_a_choice = False
            else:
                made_a_choice = True
                attack_enemy(target_choice(target_choice_value), party_member)
    return party_member

def target_choice(target_value):
    """
    Takes a number and returns target's name.
    """
    i = 1
    for entry in test_enemies:
        if i == target_value:
            return entry['name']
        i +=1
    print "error in target choice"

#Its stupid that I have two different functions here.  Replace with one that searches global_participant_readiness



def enemy_name_to_dict_value(name):
    """
    takes an enemies name and returns its dict value
    """
    for entry in test_enemies:
        if entry['name'] == name:
            return entry

def party_member_name_to_dict_value(name):
    """
    takes a party member's name and returns its dict value
    """
    for entry in test_allies:
        if entry['name'] == name:
            return entry


#Following function needs to be modified to consider more values eventually
def attack_enemy(target_name, agent_name=Kiro):
    """
    Code for a basic attack against an enemy.
    """
    damage_dealt = party_member_name_to_dict_value(agent_name)['atk']
    print agent_name, "attacks", target_name, ", dealing", damage_dealt, "damage."
    enemy_name_to_dict_value(target_name)['HP'] = enemy_name_to_dict_value(target_name)['HP']-damage_dealt
    if enemy_name_to_dict_value(target_name)['HP'] <= 0:
        enemy_is_defeated(target_name)



def enemy_is_defeated(target_name):
    print target_name, "is defeated" 
    for entry in global_participant_readiness:
        if entry[0] == enemy_name_to_dict_value(target_name):
            global_participant_readiness.remove(entry)
    test_enemies.remove(enemy_name_to_dict_value(target_name))


def party_member_is_defeated(target_name):
    """
    Doesn't currently allow for coding
    """
    print target_name, "is downed" 
    for entry in global_participant_readiness:
        if entry[0] == party_member_name_to_dict_value(target_name):
            global_participant_readiness.remove(entry)
    test_enemies.remove(enemy_name_to_dict_value(target_name))

#Needs finishing!!!
def attack_ally(target_name, agent_name):
    """
    Code for a basic attack against an ally.
    """
    if type(target_name) == str:
        target_of_attack = party_member_name_to_dict_value(target_name)
    else:
        target_of_attack = target_name
    damage_dealt = enemy_name_to_dict_value(agent_name)['atk']
    print agent_name, "attacks", target_name['name'], ", dealing", damage_dealt, "damage."
    target_of_attack['HP'] = target_of_attack['HP']-damage_dealt
    if target_of_attack['HP'] <= 0:
        party_member_is_defeated(target_name)


def bee_turn():
    """
    Bee does something.
    Returns the Bee's name
    """
    basic_attack_by_enemy('Bee')
    return Bee['name']


def slime_turn():
    """
    Slime does something.
    Returns the slime's name
    """
    basic_attack_by_enemy('Slime')
    return Slime['name']



def basic_attack_by_enemy(agent_name):
    target_ally = test_allies[random.randint(0,len(test_allies)-1)]
    attack_ally(target_ally, agent_name)


battle_Readiness_Init(test_Participants)
battle_run(test_allies, test_enemies)


