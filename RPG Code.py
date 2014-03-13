#Python 2.7.6 (default, Nov 10 2013, 19:24:24) [MSC v.1500 64 bit (AMD64)] on win32
#Type "copyright", "credits" or "license()" for more information.


#Some test characters as dictionaries
Kiro = {'name': 'Kiro', 'speed': 10}
Generic_Enemy = {'name': 'Slime', 'speed': 5}
Bee = {'name': 'Bee', 'speed': 20}

#Implement test characters as classes instead?
#class Attributes:
#   name
#   speed



test_Participants = [Kiro, Generic_Enemy, Bee]

test_allies = [Kiro]
test_enemies = [Generic_Enemy, Bee]

#Readiness Stages
#a = act
#b = backswing
#r = ready




global_participant_readiness = []

def battle_Readiness_Init(Participants):
    """
    Creates a list of list-pairs of particpants and their readiness, with their readiness taking default values.
    """
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
    print 'order is',order
    return finish_list



def get_next_turn(finish_list):
    """
    Figures out who will be acting next (next participant to become ready, excluding those waiting at ready).  Advances time until that participant is ready 
    """
    for entry in finish_list:
        if entry[2] != 'r':#ignore waiting characters
            time_advance(entry[1])
            print entry[0], 'is ready!'
            return entry[0]





def action_turn_end_clean_up(participant):
    """
    Takes the participants name as input.
    Ends the participants turn, giving him defualt readiness and setting him in backswing.
    Switches all participants waiting at ready to backswing so they have a new opportunity to act.
    """
    #edit this code to do the first part! global_participant_readiness[0].index(participant)
    for entry in global_participant_readiness:
        if entry[0]['name'] == participant:
            entry[1] = [1000, 'b']
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
    Runs a battle until all enemies or allies are defeated.  Or will
    """
    while allies:
        while enemies:
            nexts_name = get_next_turn(battle_Orderer(global_participant_readiness))
            if nexts_name == 'Bee':
                action_turn_end_clean_up(bee_turn())
            else:
                break#temporary while turns don't do anything!
        break#temporary while turns don't do anything!
        #print 'Victory!'
        #return
    #print 'Defeat!'



def bee_turn():
    """
    Bee does something.
    Returns the Bee's name
    """
    print Bee['name'], 'buzzes around!'
    return Bee['name']

battle_Readiness_Init(test_Participants)
battle_run(test_allies, test_enemies)


