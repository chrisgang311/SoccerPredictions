import pandas as pd
import numpy as np
from functools import partial
import sys

'''
Function to get the home record (win rate) for the home team prior to the date today
'''
def home_team_all_time_home_record(match_df, full_df):
  all_team_home_matches_before_today = full_df[(match_df['date'] >
          full_df['date']) & (full_df['home_team_api_id']==match_df['home_team_api_id'])].shape[0]
  # Not enough data to go by
  if all_team_home_matches_before_today == 0:
    return np.nan

  all_team_home_wins_before_today = full_df[(match_df['date'] >
           full_df['date']) & (full_df['home_team_api_id']==
      match_df['home_team_api_id']) & (full_df['result_label'] == "HOME_WIN")].shape[0]
  return np.true_divide(all_team_home_wins_before_today, all_team_home_matches_before_today)


'''
Function to get the home record (draw rate) for the home team prior to the date today
'''
def home_team_all_time_home_draws(match_df, full_df):
  all_team_home_matches_before_today = full_df[(match_df['date'] >
                                                full_df['date']) & (full_df['home_team_api_id']==match_df['home_team_api_id'])].shape[0]
  # Not enough data to go by
  if all_team_home_matches_before_today == 0:
    return np.nan

  all_team_home_draws_before_today = full_df[(match_df['date'] >
                                             full_df['date']) & (full_df['home_team_api_id']==
                                                                 match_df['home_team_api_id']) & (full_df['result_label'] == "DRAW")].shape[0]
  return np.true_divide(all_team_home_draws_before_today, all_team_home_matches_before_today)


'''
Function to get the home record (win rate) for the home team prior to this date today; FOR THIS SEASON
'''
def home_team_this_season_home_record(match_df, full_df):
  all_team_home_matches_this_season = full_df[(match_df['date'] >
                                               full_df['date']) & (full_df['home_team_api_id']==match_df['home_team_api_id']) &
                                              (full_df['season'] == match_df['season'])].shape[0]

  # Not enough data to go by
  if all_team_home_matches_this_season == 0:
    return np.nan

  all_team_home_wins_this_season = full_df[(match_df['date'] >
                                            full_df['date']) & (full_df['home_team_api_id']==match_df['home_team_api_id']) &
                                           (full_df['result_label'] == "HOME_WIN") & (full_df['season'] == match_df['season']) ].shape[0]
  return np.true_divide(all_team_home_wins_this_season, all_team_home_matches_this_season)

'''
Function to get the home record (home draws) for the home team prior to this date today; FOR THIS SEASON
'''
def home_team_this_season_home_draws(match_df, full_df):
  all_team_home_matches_this_season = full_df[(match_df['date'] >
                                               full_df['date']) & (full_df['home_team_api_id']==match_df['home_team_api_id']) &
                                              (full_df['season'] == match_df['season'])].shape[0]

  # Not enough data to go by
  if all_team_home_matches_this_season == 0:
    return np.nan

  all_team_home_draws_this_season = full_df[(match_df['date'] >
                                             full_df['date']) & (full_df['home_team_api_id']==match_df['home_team_api_id']) &
                                            (full_df['result_label'] == "DRAW") & (full_df['season'] == match_df['season']) ].shape[0]
  return np.true_divide(all_team_home_draws_this_season, all_team_home_matches_this_season)


'''
AWAY TEAM FUNCTIONS
'''
'''
Function to get the away record (win rate) for the away team prior to the date today
'''
def away_team_all_time_away_record(match_df, full_df):
  all_team_away_matches_before_today = full_df[(match_df['date'] >
                                                full_df['date']) & (full_df['away_team_api_id']==match_df['away_team_api_id'])].shape[0]
  # Not enough data to go by
  if all_team_away_matches_before_today == 0:
    return np.nan

  all_team_away_wins_before_today = full_df[(match_df['date'] >
                                             full_df['date']) & (full_df['away_team_api_id']==
           match_df['away_team_api_id']) & (full_df['result_label'] == "AWAY_WIN")].shape[0]
  return np.true_divide(all_team_away_wins_before_today, all_team_away_matches_before_today)

'''
AWAY TEAM FUNCTIONS
'''
'''
Function to get the away record (win rate) for the away team prior to the date today
'''
def away_team_all_time_away_draws(match_df, full_df):
  all_team_away_matches_before_today = full_df[(match_df['date'] >
                                                full_df['date']) & (full_df['away_team_api_id']==match_df['away_team_api_id'])].shape[0]
  # Not enough data to go by
  if all_team_away_matches_before_today == 0:
    return np.nan

  all_team_away_draw_before_today = full_df[(match_df['date'] >
                                             full_df['date']) & (full_df['away_team_api_id']==
                                                                 match_df['away_team_api_id']) & (full_df['result_label'] == "DRAW")].shape[0]
  return np.true_divide(all_team_away_draw_before_today, all_team_away_matches_before_today)

'''
Function to get the away record (win rate) for the away team prior to this date today; FOR THIS SEASON
'''
def away_team_this_season_away_record(match_df, full_df):
  all_team_away_matches_this_season = full_df[(match_df['date'] >
      full_df['date']) & (full_df['away_team_api_id']==match_df['away_team_api_id']) &
                                 (full_df['season'] == match_df['season'])].shape[0]

  # Not enough data to go by
  if all_team_away_matches_this_season == 0:
    return np.nan

  all_team_away_wins_this_season = full_df[(match_df['date'] >
             full_df['date']) & (full_df['away_team_api_id']==match_df['away_team_api_id']) &
      (full_df['result_label'] == "AWAY_WIN") & (full_df['season'] == match_df['season']) ].shape[0]
  return np.true_divide(all_team_away_wins_this_season, all_team_away_matches_this_season)

'''
Function to get the away record (win rate) for the away team prior to this date today; FOR THIS SEASON
'''
def away_team_this_season_away_draw(match_df, full_df):
  all_team_away_matches_this_season = full_df[(match_df['date'] >
                                               full_df['date']) & (full_df['away_team_api_id']==match_df['away_team_api_id']) &
                                              (full_df['season'] == match_df['season'])].shape[0]

  # Not enough data to go by
  if all_team_away_matches_this_season == 0:
    return np.nan

  all_team_away_draw_this_season = full_df[(match_df['date'] >
                                            full_df['date']) & (full_df['away_team_api_id']==match_df['away_team_api_id']) &
                                           (full_df['result_label'] == "DRAW") & (full_df['season'] == match_df['season']) ].shape[0]
  return np.true_divide(all_team_away_draw_this_season, all_team_away_matches_this_season)


'''
Function to get the away record (win rate) for the away team prior to the date today
'''
def away_team_all_time_away_record_at_this_ground(match_df, full_df):
  all_team_away_matches_before_today_at_this_ground = full_df[(match_df['date'] >
                    full_df['date']) & (full_df['away_team_api_id']==match_df['away_team_api_id'])
                    & (match_df['home_team_api_id'] == full_df['home_team_api_id'])].shape[0]
  # Not enough data to go by
  if all_team_away_matches_before_today_at_this_ground == 0:
    return np.nan

  all_team_away_wins_before_today_at_this_ground = full_df[(match_df['date'] >
                               full_df['date']) & (full_df['away_team_api_id']== match_df['away_team_api_id']) &
                   (match_df['home_team_api_id'] == full_df['home_team_api_id']) & (full_df['result_label'] == "AWAY_WIN")].shape[0]
  return np.true_divide(all_team_away_wins_before_today_at_this_ground, all_team_away_matches_before_today_at_this_ground)


'''
Function to get the away record (win rate) for the away team prior to the date today
'''
def away_team_all_time_away_draws_at_this_ground(match_df, full_df):
  all_team_away_matches_before_today_at_this_ground = full_df[(match_df['date'] >
                                                               full_df['date']) & (full_df['away_team_api_id']==match_df['away_team_api_id'])
                                                              & (match_df['home_team_api_id'] == full_df['home_team_api_id'])].shape[0]
  # Not enough data to go by
  if all_team_away_matches_before_today_at_this_ground == 0:
    return np.nan

  all_team_away_draws_before_today_at_this_ground = full_df[(match_df['date'] >
                                                            full_df['date']) & (full_df['away_team_api_id']== match_df['away_team_api_id']) &
                                                           (match_df['home_team_api_id'] == full_df['home_team_api_id']) & (full_df['result_label'] == "DRAW")].shape[0]
  return np.true_divide(all_team_away_draws_before_today_at_this_ground, all_team_away_matches_before_today_at_this_ground)

'''
FUNCTION TO GET HEAD TO HEAD in terms of (Home team win percentage, home team lose percentage, draws)
'''
def head_to_head(match_df, full_df, value):
  # Either team can be home or away
  this_fixture_all_count = full_df[(match_df['date'] > full_df['date']) &
   ((full_df['away_team_api_id']==match_df['away_team_api_id']) & (full_df['home_team_api_id']==match_df['home_team_api_id']))].shape[0]
  this_fixture_all_home_team_wins = full_df[(match_df['date'] > full_df['date']) &
          ((full_df['away_team_api_id']==match_df['away_team_api_id']) & (full_df['home_team_api_id']==match_df['home_team_api_id']))
                                            & (full_df['result_label'] == 'HOME_WIN')].shape[0]
  this_fixture_all_home_team_losses = full_df[(match_df['date'] > full_df['date']) &
                                            ((full_df['away_team_api_id']==match_df['away_team_api_id']) & (full_df['home_team_api_id']==match_df['home_team_api_id']))
                                            & (full_df['result_label'] == 'AWAY_WIN')].shape[0]
  this_fixture_all_draws = full_df[(match_df['date'] > full_df['date']) &
                                            ((full_df['away_team_api_id']==match_df['away_team_api_id']) & (full_df['home_team_api_id']==match_df['home_team_api_id']))
                                            & (full_df['result_label'] == 'DRAW')].shape[0]

  return_fixture_all_count = full_df[(match_df['date'] > full_df['date']) &
   ((full_df['away_team_api_id']==match_df['home_team_api_id']) & (full_df['home_team_api_id']==match_df['away_team_api_id']))].shape[0]
  return_fixture_all_home_team_wins = full_df[(match_df['date'] > full_df['date']) &
       ((full_df['away_team_api_id']==match_df['home_team_api_id']) & (full_df['home_team_api_id']==match_df['away_team_api_id']))
                                              & (full_df['result_label'] == 'AWAY_WIN')].shape[0]
  return_fixture_all_home_team_losses = full_df[(match_df['date'] > full_df['date']) &
                                              ((full_df['away_team_api_id']==match_df['home_team_api_id']) & (full_df['home_team_api_id']==match_df['away_team_api_id']))
                                              & (full_df['result_label'] == 'HOME_WIN')].shape[0]
  return_fixture_all_draws = full_df[(match_df['date'] > full_df['date']) &
                                              ((full_df['away_team_api_id']==match_df['home_team_api_id']) & (full_df['home_team_api_id']==match_df['away_team_api_id']))
                                              & (full_df['result_label'] == 'DRAW')].shape[0]

  total_home_wins = this_fixture_all_home_team_wins + return_fixture_all_home_team_wins
  total_home_losses = this_fixture_all_home_team_losses + return_fixture_all_home_team_losses
  total_draws = this_fixture_all_draws+ return_fixture_all_draws
  total_head_to_head = this_fixture_all_count + return_fixture_all_count
  # No history
  if total_head_to_head == 0:
    return np.nan
  if (total_home_wins + total_home_losses + total_draws != total_head_to_head):
    raise Exception

  home_win_ratio = np.true_divide(total_home_wins, total_head_to_head)
  home_loss_ratio = np.true_divide(total_home_losses, total_head_to_head)
  draw_ratio = np.true_divide(total_draws, total_head_to_head)
  if value == "Home Win":
    return home_win_ratio
  elif value == "Home Loss":
    return home_loss_ratio
  else:
    return draw_ratio


def form_guide_this_season(match_df, full_df, team_type, LOOKBACK_DAYS = 5):
  if team_type == 'home':
    team_api_id = match_df['home_team_api_id']
  else:
    team_api_id = match_df['away_team_api_id']

  # Matches that contain this team
  this_team_matches_this_season_before_today = full_df[(full_df['season'] == match_df['season']) &
                                           ( (full_df['home_team_api_id'] == team_api_id) |
                                             (full_df['away_team_api_id'] == team_api_id)) &
                                           (match_df['date'] > full_df['date']) ]

  # Sort in descending
  this_team_matches_this_season_before_today = this_team_matches_this_season_before_today.sort_values('date', ascending=False)
  # Not enough history
  if this_team_matches_this_season_before_today.shape[0] < LOOKBACK_DAYS:
    return np.nan
  else:
    form_guide_string = ""
    this_team_last_five_matches = this_team_matches_this_season_before_today.head(n=LOOKBACK_DAYS)
    for index,row in this_team_last_five_matches.iterrows():
      # Draw-does not matter
      if row['result_label'] == 'DRAW':
        form_guide_string = form_guide_string + 'D'
      # Playing at home
      elif row['home_team_api_id'] == team_api_id:
        if row['result_label'] == 'HOME_WIN':
          form_guide_string = form_guide_string + 'W'
        else:
          form_guide_string = form_guide_string + 'L'
      # Playing away
      elif row['away_team_api_id'] == team_api_id:
        if row['result_label'] == 'HOME_WIN':
          form_guide_string = form_guide_string + 'L'
        else:
          form_guide_string = form_guide_string + 'W'
      else:
        print ("Something went horribly wrong :(, check logic")
        raise Exception

    return form_guide_string


if __name__ == '__main__':
  all_features_df = pd.read_csv('Data_Structures/ALL_MATCH_FEATURES.csv')
  FORM_STATS_FEATURES = ['match_api_id', 'home_team_api_id', 'away_team_api_id',
                       'season', 'date', 'result_label']
  all_features_df['date'] = pd.to_datetime(all_features_df['date'])
  match_sample = all_features_df

  print ("Getting home team's form guide for the last five matches of the season")
  home_team_form_guide_this_season = partial(form_guide_this_season, full_df=all_features_df, team_type = "home", LOOKBACK_DAYS = 5)
  match_sample['HOME_TEAM_FORM_GUIDE'] = match_sample.apply(home_team_form_guide_this_season, axis = 1)

  print ("Getting away team's form guide for the last five matches of the season")
  away_team_form_guide_this_season = partial(form_guide_this_season, full_df=all_features_df, team_type = "away", LOOKBACK_DAYS = 5)
  match_sample['AWAY_TEAM_FORM_GUIDE'] = match_sample.apply(away_team_form_guide_this_season, axis = 1)
  match_sample.to_csv('ALL_MATCH_FEATURES_2.csv')
