MIN = 0
MAX = 49

import random

def main():
    
    stateDict = {'Alabama': 'Montgomery',
              'Alaska': 'Juneau',
              'Arizona': 'Phoenix',
              'Arkansas': 'Little Rock',
              'California': 'Sacramento',
              'Colorado': 'Denver',
              'Connecticut': 'Hartford',
              'Delaware': 'Dover',
              'Florida': 'Tallahassee',
              'Georgia': 'Atlanta',
              'Hawaii': 'Honolulu',
              'Idaho': 'Boise',
              'Illinois': 'Springfield',
              'Indiana': 'Indianapolis',
              'Iowa': 'Des Moines',
              'Kansas': 'Topeka',
              'Kentucky': 'Frankfort',
              'Louisiana': 'Baton Rouge',
              'Maine': 'Augusta',
              'Maryland': 'Annapolis',
              'Massachusetts': 'Boston',
              'Michigan': 'Lansing',
              'Minnesota': 'Saint Paul',
              'Mississippi': 'Jackson',
              'Missouri': 'Jefferson City',
              'Montana': 'Helena',
              'Nebraska': 'Lincoln',
              'Nevada': 'Carson City',
              'New Hampshire': 'Concord',
              'New Jersey': 'Trenton',
              'New Mexico': 'Santa Fe',
              'New York': 'Albany',
              'North Carolina': 'Raleigh',
              'North Dakota': 'Bismarck',
              'Ohio': 'Columbus',
              'Oklahoma': 'Oklahoma City',
              'Oregon': 'Salem',
              'Pennsylvania': 'Harrisburg',
              'Rhode Island': 'Providence',
              'South Carolina': 'Columbia',
              'South Dakota': 'Pierre',
              'Tennessee': 'Nashville',
              'Texas': 'Austin',
              'Utah': 'Salt Lake City',
              'Vermont': 'Montpelier',
              'Virginia': 'Richmond',
              'Washington': 'Olympia',
              'West Virginia': 'Charleston',
              'Wisconsin': 'Madison',
              'Wyoming': 'Cheyenne'}
              
    statesList = list(stateDict)

    correct = 0
    incorrect = 0

    again = 'y'
    
    while (again == 'y'):
        num = random.randint(MIN,MAX)
        state = statesList[num]
        print('\n' + state)
        ans = input("\nEnter the capital of this state: ")
        if (ans == stateDict[state]):
            correct += 1
            print("Correct")
            again = input("Type y to play again, anything else to stop: ")
        else:
            incorrect += 1
            print("Incorrect")
            again = input("Type y to play again, anything else to stop: ")

    print("\nYou have",correct,"correct answers")
    print("\nYou have",incorrect,"incorrect answers")
                  

main()