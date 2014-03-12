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

#Readiness Stages
#a = act
#b = backswing
#r = ready

test_start_readiness = [1000, 'b']


global_participant_readiness = []

def battle_Readiness_Init(Participants, Test_Start_Readiness):
    for entry in Participants:
        global_participant_readiness.append([entry, Test_Start_Readiness])
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
    for entry in finish_list:
        if entry[2] != 'r':#ignore waiting characters
            time_advance = entry[1]
            for participant in global_participant_readiness:
                participant[1][0] = participant[1][0]-time_advance*participant[0]['speed']#advance participants towards being ready
            print entry[0], 'is ready!'
            return






get_next_turn(battle_Orderer(battle_Readiness_Init(test_Participants, test_start_readiness)))
