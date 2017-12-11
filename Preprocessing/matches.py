from Utils import *
import datetime
import numpy as np
import players as players
import math
import xml.etree.ElementTree as ET

def result(match_df):
  if match_df['home_team_goal'] > match_df['away_team_goal']:
    return 'HOME_WIN'
  elif match_df['home_team_goal'] == match_df['away_team_goal']:
    return 'DRAW'
  else:
    return 'AWAY_WIN'


def get_player_ratings_by_type(match_df, player_type_input, player_to_player_type_dict,
    players_ratings_label, last_date, team):
  # Away Team First
  n = 0
  ratings_sum = 0
  if team == 'away':
    PLAYER_COLUMNS = AWAY_PLAYER_COLUMNS
  else:
    PLAYER_COLUMNS = HOME_PLAYER_COLUMNS
  for PLAYER in PLAYER_COLUMNS:
    player_api_id = match_df[PLAYER]
    # TODO: Get from dict
    player_type = player_to_player_type_dict[str(int(player_api_id))]
    if player_type not in PLAYER_TYPES:
      print ("Unknown player type " + player_type)
      raise Exception
    if player_type == player_type_input:
      n =n + 1
      rating_df = players.player_rating(player_api_id = player_api_id,
                                        last_date=last_date,
                                        players_ratings_label=players_ratings_label)
      ratings_sum = ratings_sum + rating_df['overall_rating'].values[0]
      #print(ratings_sum)

  if (n == 0):
    return 0
  else:
    type_rating = ratings_sum/n
    return type_rating


def single_match_rating(match_df, players_ratings_label,
          player_to_player_type_dict, player_type_input, team_type ):
  last_date=match_df['date'].split(' ')[0]
  if match_df[0] % 1000 == 0:
    print ("Done with " + str(match_df['id']) + "samples")
  rating = (get_player_ratings_by_type(match_df = match_df , player_type_input=player_type_input,
                                              player_to_player_type_dict=player_to_player_type_dict,
                                               players_ratings_label=players_ratings_label, last_date=last_date,
                                               team=team_type))

  return rating

player_api_id_season_rating_dict = dict()

def top_players_in_team(match_df, players_ratings_label, team_type, TOP_PLAYER_THRESHOLD):
  if match_df[0] % 100 == 0:
    print ("Done with " + str(match_df['id']) + "samples")
  if team_type == 'away':
    PLAYER_COLUMNS = AWAY_PLAYER_COLUMNS
  else:
    PLAYER_COLUMNS = HOME_PLAYER_COLUMNS

  total_top_players = 0
  last_date=match_df['date'].split(' ')[0]
  current_season = match_df['season']
  for PLAYER in PLAYER_COLUMNS:
    player_api_id = match_df[PLAYER]
    if player_api_id in player_api_id_season_rating_dict:
      if current_season in player_api_id_season_rating_dict[player_api_id]:
        rating = player_api_id_season_rating_dict[player_api_id][current_season]
      else:
        rating_df = players.player_rating(player_api_id = player_api_id,
                                          last_date=last_date,
                                          players_ratings_label=players_ratings_label)
        rating = rating_df['overall_rating'].values[0]
        player_api_id_season_rating_dict[player_api_id][current_season] = rating
    else:
      rating_df = players.player_rating(player_api_id = player_api_id,
                                        last_date=last_date,
                                        players_ratings_label=players_ratings_label)
      rating = rating_df['overall_rating'].values[0]
      player_api_id_season_rating_dict[player_api_id] = dict()
      player_api_id_season_rating_dict[player_api_id][current_season] = rating
    if rating >= TOP_PLAYER_THRESHOLD:
      total_top_players = total_top_players + 1
  return total_top_players


def bottom_players_in_team(match_df, players_ratings_label, team_type, BOTTOM_PLAYER_THRESHOLD):
  if match_df[0] % 100 == 0:
    print ("Done with " + str(match_df['id']) + "samples")

  if team_type == 'away':
    PLAYER_COLUMNS = AWAY_PLAYER_COLUMNS
  else:
    PLAYER_COLUMNS = HOME_PLAYER_COLUMNS

  total_bottom_players = 0
  last_date=match_df['date'].split(' ')[0]
  current_season = match_df['season']
  for PLAYER in PLAYER_COLUMNS:
    player_api_id = match_df[PLAYER]
    if player_api_id in player_api_id_season_rating_dict:
      if current_season in player_api_id_season_rating_dict[player_api_id]:
        rating = player_api_id_season_rating_dict[player_api_id][current_season]
      else:
        rating_df = players.player_rating(player_api_id = player_api_id,
                                      last_date=last_date,
                                      players_ratings_label=players_ratings_label)
        rating = rating_df['overall_rating'].values[0]
        player_api_id_season_rating_dict[player_api_id][current_season] = rating
    else:
      rating_df = players.player_rating(player_api_id = player_api_id,
                                        last_date=last_date,
                                        players_ratings_label=players_ratings_label)
      rating = rating_df['overall_rating'].values[0]
      player_api_id_season_rating_dict[player_api_id] = dict()
      player_api_id_season_rating_dict[player_api_id][current_season] = rating
    if rating <= BOTTOM_PLAYER_THRESHOLD:
      total_bottom_players = total_bottom_players + 1
  return total_bottom_players

def player_age(match_df, players_age_label,
          player_to_player_type_dict, player_type_input, team_type):
    n=0
    age=0
    match_date=match_df['date'].split(' ')[0]
    if match_df[0] % 1000 == 0:
        print ("Done with " + str(match_df['id']) + "samples")
    # Away Team First
    if team_type == 'away':
        PLAYER_COLUMNS = AWAY_PLAYER_COLUMNS
    else:
        PLAYER_COLUMNS = HOME_PLAYER_COLUMNS
    for PLAYER in PLAYER_COLUMNS:
        player_api_id = match_df[PLAYER]
        # TODO: Get from dict
        player_type = player_to_player_type_dict[str(int(player_api_id))]
        if player_type not in PLAYER_TYPES:
            print ("Unknown player type " + player_type)
            raise Exception
        if player_type == player_type_input:
            n=n+1
            age_df = players.get_age(player_api_id = player_api_id,
                                        match_date=match_date,
                                        players_age_label=players_age_label)
            age=age+np.float(age_df)
            #print(age_df)
    if (n == 0):
        return 0
    else:
        #a=age_df
        a=age/n
        return a

    

def player_bmi(match_df, players_bmi_label,
          player_to_player_type_dict, player_type_input, team_type):
    n=0
    bmi=0
    if match_df[0] % 1000 == 0:
        print ("Done with " + str(match_df['id']) + "samples")
    # Away Team First
    if team_type == 'away':
        PLAYER_COLUMNS = AWAY_PLAYER_COLUMNS
    else:
        PLAYER_COLUMNS = HOME_PLAYER_COLUMNS
    for PLAYER in PLAYER_COLUMNS:
        player_api_id = match_df[PLAYER]
        # TODO: Get from dict
        player_type = player_to_player_type_dict[str(int(player_api_id))]
        if player_type not in PLAYER_TYPES:
            print ("Unknown player type " + player_type)
            raise Exception
        if player_type == player_type_input:
            n=n+1
            bmi_df = players.get_bmi(player_api_id = player_api_id,
                                        players_bmi_label=players_bmi_label)
            bmi=bmi+np.float(bmi_df)
            #print(age_df)
    if (n == 0):
        return 0
    else:
        #a=age_df
        a=bmi/n
        return a
    
def shots_on_home(match_df):

    #Counting home team shots on goal and away team shots on goal
    homeTeamCount = 0
    if match_df[0] % 1000 == 0:
        print ("Done with " + str(match_df['id']) + "samples")
        
    homeTeam = match_df['home_team_api_id']
    
    #Reading XML column from string
    if match_df['shoton'] == None:
        homeTeamCount=0
    else:
        tree = ET.fromstring(match_df['shoton'])    
        lst = tree.findall('value')   
        #numShoton = len(lst)
    
        #looping through values in Shoton
        for value in tree.findall("value"):
            #print(value)
            #Getting team api id for each shot on goal
            if value.find('team')==None:
                continue
            else:
                #print(value.find('team').text)
                team = value.find('team').text
                if(homeTeam==eval(team)):
                    homeTeamCount+=1
    #print(homeTeamCount,awayTeamCount)
    return homeTeamCount
        
def shots_off_home(match_df):

    #Counting home team shots on goal and away team shots on goal
    homeTeamCount = 0
    if match_df[0] % 1000 == 0:
        print ("Done with " + str(match_df['id']) + "samples")
        
    homeTeam = match_df['home_team_api_id']
    
    #Reading XML column from string
    if match_df['shotoff'] == None:
        homeTeamCount=0
    else:
        tree = ET.fromstring(match_df['shotoff'])    
        lst = tree.findall('value')   
        #numShoton = len(lst)
    
        #looping through values in Shoton
        for value in tree.findall("value"):
            #print(value)
            #Getting team api id for each shot on goal
            if value.find('team')==None:
                continue
            else:
                #print(value.find('team').text)
                team = value.find('team').text
                if(homeTeam==eval(team)):
                    homeTeamCount+=1
    #print(homeTeamCount,awayTeamCount)
    return homeTeamCount

def shots_on_away(match_df):

    #Counting home team shots on goal and away team shots on goal
    awayTeamCount = 0
    if match_df[0] % 1000 == 0:
        print ("Done with " + str(match_df['id']) + "samples")
        
    awayTeam = match_df['away_team_api_id']
    
    #Reading XML column from string
    if match_df['shoton'] == None:
        awayTeamCount=0
    else:
        tree = ET.fromstring(match_df['shoton'])    
        lst = tree.findall('value')   
        #numShoton = len(lst)
    
        #looping through values in Shoton
        for value in tree.findall("value"):
            #print(value)
            #Getting team api id for each shot on goal
            if value.find('team')==None:
                continue
            else:
                #print(value.find('team').text)
                team = value.find('team').text
                if(awayTeam==eval(team)):
                    awayTeamCount+=1
    #print(homeTeamCount,awayTeamCount)
    return awayTeamCount
        
def shots_off_away(match_df):

    #Counting home team shots on goal and away team shots on goal
    awayTeamCount = 0
    if match_df[0] % 1000 == 0:
        print ("Done with " + str(match_df['id']) + "samples")
        
    awayTeam = match_df['away_team_api_id']
    
    #Reading XML column from string
    if match_df['shotoff'] == None:
        awayTeamCount=0
    else:
        tree = ET.fromstring(match_df['shotoff'])    
        lst = tree.findall('value')   
        #numShoton = len(lst)
    
        #looping through values in Shoton
        for value in tree.findall("value"):
            #print(value)
            #Getting team api id for each shot on goal
            if value.find('team')==None:
                continue
            else:
                #print(value.find('team').text)
                team = value.find('team').text
                if(awayTeam==eval(team)):
                    awayTeamCount+=1
    #print(homeTeamCount,awayTeamCount)
    return awayTeamCount
        