import numpy as np
import pandas as pd
'''
Function to fill nan for the teams' head to head home team win rate
'''

def fill_nan_head_2_head_home_team_win_rate(match_df, full_df):
  value = match_df['HEAD_2_HEAD_HOME_TEAM_WINS']
  if not np.isnan(value):
    return value
  else:
    # Find average
    all_head_to_head_avg = full_df[(full_df['home_team_api_id']==
      match_df['home_team_api_id']) & (full_df['away_team_api_id']==
                                     match_df['away_team_api_id'])]
    mean_home_win_rate = all_head_to_head_avg['HEAD_2_HEAD_HOME_TEAM_WINS'].mean(skipna=True)
    # If still Na, i.e. no history
    if np.isnan(mean_home_win_rate):
      mean_home_win_rate = 0.33
    return mean_home_win_rate


'''
Function to fill nan for the teams' head to head home team loss rate
'''

def fill_nan_head_2_head_home_team_loss_rate(match_df, full_df):
  value = match_df['HEAD_2_HEAD_HOME_TEAM_LOSS']
  if not np.isnan(value):
    return value
  else:
    # Find average
    all_head_to_head_avg = full_df[(full_df['home_team_api_id']==
                                    match_df['home_team_api_id']) & (full_df['away_team_api_id']==
                                               match_df['away_team_api_id'])]
    mean_home_loss_rate = all_head_to_head_avg['HEAD_2_HEAD_HOME_TEAM_LOSS'].mean(skipna=True)
    # If still Na, i.e. no history
    if np.isnan(mean_home_loss_rate):
      mean_home_loss_rate = 0.33
    return mean_home_loss_rate


'''
Function to fill nan for the teams' head to head draw rate
'''

def fill_nan_head_2_head_draw(match_df, full_df):
  value = match_df['HEAD_2_HEAD_DRAW']
  if not np.isnan(value):
    return value
  else:
    # Find average
    all_head_to_head_avg = full_df[(full_df['home_team_api_id']==
                                    match_df['home_team_api_id']) & (full_df['away_team_api_id']==
                                           match_df['away_team_api_id'])]
    mean_draw_rate = all_head_to_head_avg['HEAD_2_HEAD_DRAW'].mean(skipna=True)
    if np.isnan(mean_draw_rate):
      mean_draw_rate = 0.33
    return mean_draw_rate


'''
Function to fill nan for the home team's ALL TIME HOME RECORD
'''

def fill_nan_home_team_win_rate_all_time(match_df, full_df):
  value = match_df['HOME_WIN_RATE']
  if not np.isnan(value):
    return value
  else:
    # Find average
    all_home_matches = full_df[(full_df['home_team_api_id']==
                                    match_df['home_team_api_id'])]
    mean_home_win_rate = all_home_matches['HOME_WIN_RATE'].mean(skipna=True)
    return mean_home_win_rate

'''
Function to fill nan for the home team's ALL TIME HOME DRAWS
'''

def fill_nan_home_team_draw_rate_all_time(match_df, full_df):
  value = match_df['HOME_DRAW_RATE']
  if not np.isnan(value):
    return value
  else:
    # Find average
    all_home_matches = full_df[(full_df['home_team_api_id']==
                                match_df['home_team_api_id'])]
    mean_draw_rate = all_home_matches['HOME_DRAW_RATE'].mean(skipna=True)
    return mean_draw_rate

'''
Function to fill nan for the away team's ALL TIME AWAY RECORD
'''

def fill_nan_away_team_win_rate_all_time(match_df, full_df):
  value = match_df['AWAY_WIN_RATE']
  if not np.isnan(value):
    return value
  else:
    # Find average
    all_away_matches = full_df[(full_df['away_team_api_id']==
                                    match_df['away_team_api_id'])]
    mean_away_win_rate = all_away_matches['AWAY_WIN_RATE'].mean(skipna=True)
    return mean_away_win_rate


'''
Function to fill nan for the away team's ALL TIME AWAY DRAWS
'''

def fill_nan_away_team_draw_rate_all_time(match_df, full_df):
  value = match_df['AWAY_DRAW_RATE']
  if not np.isnan(value):
    return value
  else:
    # Find average
    all_away_matches = full_df[(full_df['away_team_api_id']==
                                match_df['away_team_api_id'])]
    mean_away_draw_rate = all_away_matches['AWAY_DRAW_RATE'].mean(skipna=True)
    return mean_away_draw_rate


'''
Function to fill nan for the away team's away record THIS SEASON
'''

def fill_nan_away_team_win_rate_this_season(match_df, full_df):
  value = match_df['AWAY_WIN_RATE_THIS_SEASON']
  if not np.isnan(value):
    return value
  else:
    # Find average
    all_away_matches_this_season = full_df[(full_df['away_team_api_id']==
                                match_df['away_team_api_id']) &
                               (full_df['season']==
                                match_df['season'])]
    mean_away_win_rate = all_away_matches_this_season['AWAY_WIN_RATE_THIS_SEASON'].mean(skipna=True)
    if np.isnan(mean_away_win_rate):
      all_away_matches = full_df[(full_df['away_team_api_id']==
                                  match_df['away_team_api_id'])]
      mean_away_win_rate = all_away_matches['AWAY_WIN_RATE'].mean(skipna=True)
    return mean_away_win_rate


'''
Function to fill nan for the away team's draw record THIS SEASON
'''

def fill_nan_away_team_draw_rate_this_season(match_df, full_df):
  value = match_df['AWAY_DRAW_RATE_THIS_SEASON']
  if not np.isnan(value):
    return value
  else:
    # Find average
    all_away_matches_this_season = full_df[(full_df['away_team_api_id']==
                                            match_df['away_team_api_id']) &
                                           (full_df['season']==
                                            match_df['season'])]
    mean_away_draw_rate = all_away_matches_this_season['AWAY_WIN_RATE_THIS_SEASON'].mean(skipna=True)
    if np.isnan(mean_away_draw_rate):
      all_away_matches = full_df[(full_df['away_team_api_id']==
                                  match_df['away_team_api_id'])]
      mean_away_draw_rate = all_away_matches['AWAY_DRAW_RATE_THIS_SEASON'].mean(skipna=True)
    return mean_away_draw_rate


'''
Function to fill nan for the home team's home record THIS SEASON
'''

def fill_nan_home_team_win_rate_this_season(match_df, full_df):
  value = match_df['HOME_WIN_RATE_THIS_SEASON']
  if not np.isnan(value):
    return value
  else:
    # Find average
    all_home_matches_this_season = full_df[(full_df['home_team_api_id']==
                                            match_df['home_team_api_id']) &
                                           (full_df['season']==
                                            match_df['season'])]
    mean_home_win_rate = all_home_matches_this_season['HOME_WIN_RATE_THIS_SEASON'].mean(skipna=True)
    return mean_home_win_rate



'''
Function to fill nan for the home team's draw record THIS SEASON
'''

def fill_nan_home_team_draw_rate_this_season(match_df, full_df):
  value = match_df['HOME_DRAW_RATE_THIS_SEASON']
  if not np.isnan(value):
    return value
  else:
    # Find average
    all_home_matches_this_season = full_df[(full_df['home_team_api_id']==
                                            match_df['home_team_api_id']) &
                                           (full_df['season']==
                                            match_df['season'])]
    mean_home_draw_rate = all_home_matches_this_season['HOME_DRAW_RATE_THIS_SEASON'].mean(skipna=True)
    return mean_home_draw_rate


'''
Function to fill nan for the away team's ALL TIME AWAY RECORD at this ground
'''

def fill_nan_away_team_win_rate_all_time_at_this_ground(match_df, full_df):
  value = match_df['AWAY_WIN_RATE_AT_THIS_GROUND']
  if not np.isnan(value):
    return value
  else:
    # Find average
    all_away_matches_at_this_ground = full_df[(full_df['away_team_api_id']==
                                    match_df['away_team_api_id']) &
                                   (full_df['home_team_api_id']==
                                    match_df['home_team_api_id'])]

    mean_away_win_rate = all_away_matches_at_this_ground['AWAY_WIN_RATE_AT_THIS_GROUND'].mean(skipna=True)
    if np.isnan(mean_away_win_rate):
      all_away_matches = full_df[(full_df['away_team_api_id']==
                                  match_df['away_team_api_id'])]
      mean_away_win_rate = all_away_matches['AWAY_WIN_RATE'].mean(skipna=True)
    return mean_away_win_rate


'''
Function to fill nan for the away team's ALL TIME AWAY RECORD at this ground
'''

def fill_nan_away_team_draw_rate_all_time_at_this_ground(match_df, full_df):
  value = match_df['AWAY_DRAW_RATE_AT_THIS_GROUND']
  if not np.isnan(value):
    return value
  else:
    # Find average
    all_away_matches_at_this_ground = full_df[(full_df['away_team_api_id']==
                                               match_df['away_team_api_id']) &
                                              (full_df['home_team_api_id']==
                                               match_df['home_team_api_id'])]

    mean_away_win_rate = all_away_matches_at_this_ground['AWAY_DRAW_RATE_AT_THIS_GROUND'].mean(skipna=True)
    if np.isnan(mean_away_win_rate):
      all_away_matches = full_df[(full_df['away_team_api_id']==
                                  match_df['away_team_api_id'])]
      mean_away_win_rate = all_away_matches['AWAY_DRAW_RATE'].mean(skipna=True)
    return mean_away_win_rate

'''
Function to fill nan for the a team's form guide. We just get the most common form guide
and replace np.nan with it
'''
def fill_nan_form_guide(match_df, full_df, team_type, all_possibility):
  if team_type == 'home':
    value = match_df['HOME_TEAM_FORM_GUIDE']
  else:
    value = match_df['AWAY_TEAM_FORM_GUIDE']
  if not pd.isnull((value)):
    return value
  else:
    if team_type == 'home':
      team_api_id = match_df['home_team_api_id']
    else:
      team_api_id = match_df['away_team_api_id']

    # Matches that contain this team
    this_team_all_matches_this_season_before_today = full_df[(full_df['season'] == match_df['season']) &
                                                       ( (full_df['home_team_api_id'] == team_api_id) |
                                                         (full_df['away_team_api_id'] == team_api_id))]
    form_guide_list_this_team = list()
    for index, row in this_team_all_matches_this_season_before_today.iterrows():
      if row['home_team_api_id'] == team_api_id:
        if not pd.isnull(row['HOME_TEAM_FORM_GUIDE']):
          form_guide_list_this_team.append(row['HOME_TEAM_FORM_GUIDE'])
      else:
        if not pd.isnull(row['AWAY_TEAM_FORM_GUIDE']):
          form_guide_list_this_team.append(row['AWAY_TEAM_FORM_GUIDE'])
    if len(form_guide_list_this_team) == 0:
      import random
      return random.choice(all_possibility)
    from collections import Counter
    c = Counter(form_guide_list_this_team)
    #print c
    #print c.most_common(1)[0][0]
    return (c.most_common(1)[0][0])