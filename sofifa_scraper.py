
# coding: utf-8

# ## Description
# The goal is to create a Database with all the weekly data of the players, scraped from sofifa (http://www.sofifa.com)
# 
# This programm scrapes all the possible data weeks from sofifa and iterates then from 100000 to 250000 and tries if there's a player. Maybe it would make sense to do that just for the found players.
# 
# Takes ages, so download it as .py file and run it on an aws instance


import requests
from bs4 import BeautifulSoup
import pandas as pd
from itertools import islice

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

with open("./sofifa/all_ids.txt") as f:
    content = f.readlines()
ids = [x.strip() for x in content]


def scrapeForLink(link, filename):
        
    csv_path = "./sofifa/{}.csv".format(filename)
    #unsuccessful_path = "./sofifa/{}_unsuccessful.txt".format(filename)
    #successful_path = "./sofifa/{}_successful.txt".format(filename)
    
    #text_file_successful = open(successful_path, "a")
    #text_file_unsuccessful = open(unsuccessful_path, "a")
    
    s = requests.Session()
    s.get("https://sofifa.com{}".format(link))
    
    crossing_index, finishing_index, heading_accuracy_index, short_passing_index, volley_index = getAttackingIndexes(filename)
    dribbling_index, curve_index, freekick_accuracy_index, long_passing_index, ball_control_index = getSkillIndexes(filename)
    acceleration_index, sprint_speed_index, agility_index, reactions_index, balance_index = getMovementIndexes(filename)
    shot_power_index, jumping_index, stamina_index, strength_index, long_shots_index = getPowerIndexes(filename)
    aggression_index, interceptions_index, positioning_index, vision_index, penalties_index, composure_index = getMentalityIndexes(filename)
    marking_index, standing_tackle_index, sliding_tackle_index = getDefendingIndexes(filename)
    gk_diving_index, gk_handling_index, gk_kicking_index, gk_positioning_index, gk_reflexes_index = getGoalkeepingIndexes(filename)
    
    try:
        df = pd.read_csv(csv_path)
    except:
        df = pd.DataFrame(columns=dataframeColumns())

    for i in ids:
#        if int(i) % 20 == 0: # nicht gleich verlässlich wie bei iteration, aber trotzem wird gelegentlich gespeichert
#            print 'Saved files'
#            df.to_csv(csv_path)
#            text_file_successful.close()
#            text_file_unsuccessful.close()
#            text_file_successful = open(successful_path, "a")
#            text_file_unsuccessful = open(unsuccessful_path, "a")

        print 'Player id {0} Filename{1}'.format(i, filename)
        page = s.get("https://sofifa.com/player/{}".format(i), allow_redirects=False)

        if page.content:
            #text_file_successful.write("%s\n" % i)
            soup = BeautifulSoup(page.content)
            player_info = soup.find('div', attrs={'class':'player'})
            meta = player_info.find('div', attrs={'class':'meta'})
            name = meta.find('span').find('a').previousSibling[:-1]

            stats = player_info.find('div', attrs={'class':'stats'})
            table_entries = stats.find_all('td')
            overall_rating = table_entries[0].span.text
            potential = table_entries[1].span.text
            value = table_entries[2].span.text
            wage = table_entries[3].span.text

            try:
                team_table = player_info.find('div', attrs={'class':'teams'}).find_all('td')[2].find_all('li')
            except:
                print "Player {0} has no team! ({1})".format(i, filename)

            team = ""
            team_rating = ""
            pos = ""
            if team_table:
                team = team_table[0].find_all('a')[1].text
                team_rating = team_table[1].span.text
                pos = team_table[2].span.text
                
            
            skill_columns = soup.find_all('section', attrs={'class': 'columns'})[1].find_all('div', attrs={'class': 'columns'})
            first_row = skill_columns[0].find_all('div')

            attacking = first_row[0].find_all('li')
            crossing = attacking[crossing_index].span.text
            finishing = attacking[finishing_index].span.text
            heading_accuracy = attacking[heading_accuracy_index].span.text
            short_passing = attacking[short_passing_index].span.text
            volleys = ""            
            try:
                volleys = attacking[volley_index].span.text
            except:
                pass

            skill = first_row[2].find_all('li')
            dribbling = skill[dribbling_index].span.text
            curve = ""
            try:
                curve = skill[curve_index].span.text
            except:
                pass
            free_kick_accuracy = skill[freekick_accuracy_index].span.text
            long_passing = skill[long_passing_index].span.text
            ball_control = ""            
            try:
                ball_control = skill[ball_control_index].span.text
            except:
                pass

            movement = first_row[4].find_all('li')
            acceleration = movement[acceleration_index].span.text
            sprint_speed = movement[sprint_speed_index].span.text
            agility = ""
            try:
                agility = movement[agility_index].span.text
            except:
                pass
            reactions = movement[reactions_index].span.text
            balance = ""
            try:
                balance = movement[balance_index].span.text
            except:
                pass
            
            power = first_row[6].find_all('li')
            shot_power = power[shot_power_index].span.text
            jumping = ""
            try:
                jumping = power[jumping_index].span.text
            except:
                pass
            stamina = power[stamina_index].span.text
            strength = power[strength_index].span.text
            long_shots = power[long_shots_index].span.text

            second_row = skill_columns[1].find_all('div')

            mentality = second_row[0].find_all('li')
            aggression = mentality[aggression_index].span.text
            interceptions = ""
            try:
                interceptions = mentality[interceptions_index].span.text
            except:
                pass
            positioning = ""
            try:
                positioning = mentality[positioning_index].span.text
            except:
                pass
            vision = ""
            try:
                vision = mentality[vision_index].span.text
            except:
                pass
            penalties = mentality[penalties_index].span.text
            composure = ""
            try:
                composure = mentality[composure_index].span.text
            except:
                composure = "12"

            defending = second_row[2].find_all('li')
            marking = defending[marking_index].span.text
            standing_tackle = defending[standing_tackle_index].span.text
            sliding_tackle = ""
            try:
                sliding_tackle = defending[sliding_tackle_index].span.text
            except:
                pass
            
            goalkeeping = second_row[4].find_all('li')
            gk_diving = goalkeeping[gk_diving_index].span.text
            gk_handling = goalkeeping[gk_handling_index].span.text
            gk_kicking = goalkeeping[gk_kicking_index].span.text
            gk_positioning = goalkeeping[gk_positioning_index].span.text
            gk_reflexes = goalkeeping[gk_reflexes_index].span.text

            new_row = [i, name, overall_rating, potential, value, wage, team, team_rating, pos, crossing, finishing, heading_accuracy, short_passing, volleys, dribbling, curve, free_kick_accuracy, long_passing, ball_control, acceleration, sprint_speed, agility, reactions, balance, shot_power, jumping, stamina, strength, long_shots, aggression, interceptions, positioning, vision, penalties, composure, marking, standing_tackle, sliding_tackle, gk_diving, gk_handling, gk_kicking, gk_positioning, gk_reflexes]
            df.loc[len(df)] = new_row
    #else:
            #text_file_unsuccessful.write("%s\n" % i)
    df.to_csv(csv_path)
    #text_file_successful.close()
    #text_file_unsuccessful.close()

def dataframeColumns():
    return ["SofifaId", "FullName", "OverallRating", "Potential", "Value", "Wage", "Team", "TeamRating", "Pos","Crossing", "Finishing", "HeadingAccuracy", "ShortPassing", "Volleys", "Dribbling", "Curve", "FreeKickAccuracy", "LongPassing", "BallControl", "Acceleration", "SprintSpeed", "Agility", "Reactions", "Balance", "ShotPower", "Jumping", "Stamina", "Strength", "LongShots", "Aggression", "Interceptions", "Positioning", "Vision", "Penalties", "Composure", "Marking", "StandingTakcle", "SlidingTackle", "GKDiving", "GKHandling", "GKKicking", "GKPositioning", "GKReflexes"]

def getAllVersionLinks():
    return_dict = {}
    page = requests.get("https://sofifa.com/")
    soup = BeautifulSoup(page.content)
    filter_body = soup.find('div', attrs={'class': 'filter-body'})
    card_headers = filter_body.find_all('div', attrs={'class' : 'card-header'})
    card_bodies = filter_body.find_all('div', attrs={'class':'card-body'})
    for card_header, card_body in zip(card_headers, card_bodies):
        links = card_body.find_all('a')
        for link in links:
            month_year = card_header.text.split('  ')
            month = month_year[0]
            year = month_year[1]
            name = "FIFA%s_%s_%s_%s" % (card_body.parent.parent['data-tag'][-2:], year, month, link.text)
            return_dict[name] = link['href']
    return return_dict

#crossing, finishing, heading_accuracy, short_passing, volleys
def getAttackingIndexes(filename):
    fifa = filename.split("_")[0]
    if "07" in fifa or "08" in fifa or "09" in fifa or "10" in fifa:
        return [0, 1, 2, 3, 10]
    else:
        return [0, 1, 2, 3, 4]
    
#dribbling, curve, free_kick_acc, long_passing, ball_control
def getSkillIndexes(filename):
    fifa = filename.split("_")[0]
    if "07" in fifa or "08" in fifa or "09" in fifa or "10" in fifa:
        return [0, 10, 1, 2, 3]
    else:
        return [0, 1, 2, 3, 4]
    
#acceleration, sprint_speed, agility, reactions, balance
def getMovementIndexes(filename):
    fifa = filename.split("_")[0]
    if "07" in fifa or "08" in fifa or "09" in fifa or "10" in fifa:
        return [0, 1, 10, 2, 10]
    else:
        return [0, 1, 2, 3, 4]
    
#shot_power, jumping, stamina, strength, long_shots
def getPowerIndexes(filename):
    fifa = filename.split("_")[0]
    if "07" in fifa or "08" in fifa or "09" in fifa or "10" in fifa:
        return [0, 10, 1, 2, 3]
    else:
        return [0, 1, 2, 3, 4]
    
#aggression, interceptions, positioning, vision, penalties, composure
def getMentalityIndexes(filename):
    fifa = filename.split("_")[0]
    if "07" in fifa:
        return [0, 10, 10, 10, 1, 10]
    elif "08" in fifa or "09" in fifa or "10" in fifa:
        return [0, 1, 2, 10, 3, 10]
    elif "11" in fifa or "12" in fifa or "13" in fifa or "14" in fifa or "15" in fifa or "16" in fifa:
        return [0, 1, 2, 3, 4, 10]
    else:
        return [0, 1, 2, 3, 4, 5]
    
#marking, standing_tackle, sliding_tackle
def getDefendingIndexes(filename):
    fifa = filename.split("_")[0]
    if "07" in fifa or "08" in fifa or "09" in fifa or "10" in fifa:
        return [0, 1, 10]
    else:
        return [0, 1, 2]
    
#gk_diving, gk_handling, gk_kicking, gk_positioning, gk_reflexes
def getGoalkeepingIndexes(filename):
    return [0, 1, 2, 3, 4]

# In[2]:

with open("./sofifa/finished.txt", "w+") as f:
    content = f.readlines()
finished_files = [x.strip() for x in content]

linkdict = getAllVersionLinks()

for filename, link in islice(reversed(linkdict.items()), len(linkdict)/2, None): #backwards to the half. Programmed as reversed and then from the half to the end is like from the half back to the beginning
#for filename, link in islice(linkdict.iteritems(), len(linkdict)/2, None): #forward from the half to the end
#for filename, link in linkdict.items():
#for filename, link in reversed(linkdict.items()): #reversed so we can let it go in parallel
    if "%s, %s" % (filename, link) in finished_files:
        continue
    scrapeForLink(link, filename)
    text_file_finished = open("./sofifa/finished.txt", "a")
    text_file_finished.write("%s, %s\n" % (filename, link))
    text_file_finished.close()
