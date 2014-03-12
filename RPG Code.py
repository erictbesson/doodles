#Python 2.7.6 (default, Nov 10 2013, 19:24:24) [MSC v.1500 64 bit (AMD64)] on win32
#Type "copyright", "credits" or "license()" for more information.


#Some test characters
Kiro = {'name': 'Kiro', 'speed':10}
Generic_Enemy = {'name': 'Slime', 'speed':5}

test_Participants = [[Kiro, Generic_Enemy]]
		     
test_start_readiness = [1000, 'w']
		     
def battle_Readiness_Init(Participants, Test_Start_Readiness):
		    Participant_Readiness = []
		    for entry in Participants:
			     Participant_Readiness.append([entry, Test_Start_Readiness])
		    return Participant_Readiness
	
		     

def finish_list_2nd_element(p):
	return p[1]

def battle_Orderer(Participant_Readiness):
	#I imagine participants to be a list of participants where participants are dictionaries with relevant stats
	#Participant_Readiness would be a global variable which lists list-pairs of how close to ready each participant is (float down to 0) and whether that character is acting (and can be interrupted) or is just waiting)
        finish_list = []
        for participant in Participant_Readiness:
            finish_list.append([participant[0]['name'], participant[1][0]/participant[0]['speed']])
        finish_list.sort(key=finish_list_2nd_element)
        print finish_list            


battle_Orderer(battle_Readiness_Init(test_Participants, test_start_readiness))
