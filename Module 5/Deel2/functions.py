import time
import math
from termcolor import colored
from data import JOURNEY_IN_DAYS
from data import COST_FOOD_HORSE_COPPER_PER_DAY
from data import COST_FOOD_HUMAN_COPPER_PER_DAY
from data import COST_HORSE_SILVER_PER_DAY
from data import COST_TENT_GOLD_PER_WEEK
from data import COST_INN_HORSE_COPPER_PER_NIGHT
from data import COST_INN_HUMAN_SILVER_PER_NIGHT

##################### M04.D02.O2 #####################

def copper2silver(amount:int) -> float:
    return amount / 10

def silver2gold(amount:int) -> float:
    return amount / 5

def copper2gold(amount:int) -> float:
    return amount / 50

def platinum2gold(amount:int) -> float:
    return amount * 25

def getPersonCashInGold(personCash:dict) -> float:
    gold = silver2gold(personCash.get('silver')) + copper2gold(personCash.get('copper')) + platinum2gold(personCash.get('platinum')) 
    gold +=personCash.get('gold')
    return gold

##################### M04.D02.O4 #####################

def getJourneyFoodCostsInGold(people:int, horses:int) -> float:
    human = copper2gold(COST_FOOD_HUMAN_COPPER_PER_DAY * people) * JOURNEY_IN_DAYS
    horse = copper2gold(COST_FOOD_HORSE_COPPER_PER_DAY * horses) * JOURNEY_IN_DAYS
    return  round(human + horse,2)

##################### M04.D02.O5 #####################

def getFromListByKeyIs(list:list, key:str, value:any) -> list:
    lijst = []
    for x in range(len(list)):
        if list[x][key] == value:
            lijst.append(list[x])
    return lijst

def getAdventuringPeople(people:list) -> list:
    return getFromListByKeyIs(people, "adventuring", True)

def getShareWithFriends(friends:list) -> list:
    return getFromListByKeyIs(friends, "shareWith", True)

def getAdventuringFriends(friends:list) -> list:
    adventurefriends = []
    adventure = getAdventuringPeople(friends)
    share = getShareWithFriends(friends)

    for x in range(len(adventure)):

        if share[x] in adventure:
            adventurefriends.append(share[x])
    return adventurefriends

##################### M04.D02.O6 #####################

def getNumberOfHorsesNeeded(people:int) -> int:
    return math.ceil(people / 2)
def getNumberOfTentsNeeded(people:int) -> int:
    return math.ceil(people / 3)

def getTotalRentalCost(horses:int, tents:int) -> float:
    return (horses * silver2gold(COST_HORSE_SILVER_PER_DAY) * JOURNEY_IN_DAYS) + (tents * (COST_TENT_GOLD_PER_WEEK * math.ceil(JOURNEY_IN_DAYS / 7)) )

##################### M04.D02.O7 #####################

def getItemsAsText(items:list) -> str:
    converted= ""
    for key in range (len(items)):
        amount = str(items[key]['amount'])
        converted += amount + items[key]['unit'] + " " + items[key]['name']
        if key < len(items) -1:
            converted += ', '
    return(converted)

def getItemsValueInGold(items:list) -> float:
    value= 0
    for key in range (len(items)):
        if items[key]['price']['type'] =='gold':
            amount = items[key]['price']['amount'] * items[key]['amount']
            value += amount
        elif items[key]['price']['type'] =='copper':
            amount = copper2gold( items[key]['price']['amount']) * items[key]['amount']
            value += amount
        elif items[key]['price']['type'] =='silver':
            amount = silver2gold (items[key]['price']['amount']) * items[key]['amount']
            value += amount
        elif items[key]['price']['type'] =='platinum':
            amount =  platinum2gold(items[key]['price']['amount']) * items[key]['amount']
            value += amount
        totaal = round(value,2)
    return totaal
##################### M04.D02.O8 #####################

def getCashInGoldFromPeople(people:list) -> float:
    value= 0
    for key in range (len(people)):
        amount = people[key]['cash']['gold']
        value += amount
        amount = copper2gold( people[key]['cash']['copper']) 
        value += amount
        amount = silver2gold (people[key]['cash']['silver']) 
        value += amount
        amount =  platinum2gold(people[key]['cash']['platinum'])
        value += amount
    totaal = round(value,2)
    return totaal

##################### M04.D02.O9 #####################

def getInterestingInvestors(investors:list) -> list:
    InterestingInvestors = []
    for index in range(0,len(investors)):    
        if investors[index]['profitReturn'] <= 10:
            InterestingInvestors.append(investors[index])
    return InterestingInvestors

def getAdventuringInvestors(investors:list) -> list:
    adventuringInvestors= []
    for index in range (len(getInterestingInvestors(investors))):
        if getInterestingInvestors(investors)[index]['adventuring'] == True :
            adventuringInvestors.append(getInterestingInvestors(investors)[index])
    return adventuringInvestors

def getTotalInvestorsCosts(investors:list, gear:list) -> float:
    people= getAdventuringInvestors(investors)
    rentalCost = getTotalRentalCost(1,1)
    foodCost = getJourneyFoodCostsInGold(1,1)
    totaal = (getItemsValueInGold(gear)  + rentalCost + foodCost) * len(people)
    return totaal

##################### M04.D02.O10 #####################

def getMaxAmountOfNightsInInn(leftoverGold:float, people:int, horses:int) -> int:
    people_cost = silver2gold(COST_INN_HUMAN_SILVER_PER_NIGHT) * people
    horses_cost  = copper2gold(COST_INN_HORSE_COPPER_PER_NIGHT) * horses
    herberg_cost = people_cost  + horses_cost
    maxNachten = math.floor(leftoverGold / herberg_cost)
    return maxNachten

def getJourneyInnCostsInGold(nightsInInn:int, people:int, horses:int) -> float:
    people_cost = silver2gold(COST_INN_HUMAN_SILVER_PER_NIGHT) * people
    horses_cost  = copper2gold(COST_INN_HORSE_COPPER_PER_NIGHT) * horses
    herberg_cost = round(nightsInInn * (people_cost + horses_cost) , 2)
    return herberg_cost

##################### M04.D02.O12 #####################

def getInvestorsCuts(profitGold:float, investors:list) -> list:
    goldList = []
    AdventuringInvestors = getInterestingInvestors(investors)
    for teller in range (len(AdventuringInvestors)):
        investorsCuts = round(profitGold / 100 * AdventuringInvestors[teller][ 'profitReturn'] , 2)
        goldList.append(investorsCuts)
    return goldList

def getAdventurerCut(profitGold:float, investorsCuts:list, fellowship:list) -> float:
    for gold in investorsCuts:
        profitGold -= gold
    adventurCut = round(profitGold / fellowship ,2)
    return adventurCut

##################### M04.D02.O13 #####################

def getEarnigs(profitGold:float, mainCharacter:dict, friends:list, investors:list) -> list:
    pass

##################### view functions #####################
def print_colorvars(txt:str='{}', vars:list=[], color:str='yellow') -> None:
    vars = map(lambda string, color=color: colored(str(string), color, attrs=['bold']) ,vars)
    print(txt.format(*vars))

def print_title(name:str) -> None:
    print_colorvars(vars=['=== [ {} ] ==='.format(name)], color='green')

def print_chapter(number:int, name:str) -> None:
    nextStep(2)
    print_colorvars(vars=['- CHAPTER {}: {} -'.format(number, name)], color='magenta')

def nextStep(secwait:int=1) -> None:
    print('')
    time.sleep(secwait)

def ifOne(amount:int, yes:str, no:str, single='een') -> str:
    text = yes if amount == 1 else no
    amount = single if amount == 1 else amount
    return '{} {}'.format(amount, text).lstrip()