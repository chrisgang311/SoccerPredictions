'''
FORMATTING CONSTANTS
'''
SEPARATOR = "***********************************************"

'''

'''

'''
INPUT DATA Constants
'''
INPUTFILE_DIR = "../Data/"
INPUTZIPFILE = "soccer.zip"
DATABASENAME = "database.sqlite"

'''
SQL STATEMENTS
'''
SHOW_TABLES_SQL = "SELECT name FROM sqlite_master WHERE type='table' " \
                  "ORDER BY name;"
DESC_TABLES_SQL = "DESC"

AWAY_PLAYER_COLUMNS = ["away_player_1", "away_player_2", "away_player_3",
                       "away_player_4", "away_player_5", "away_player_6",
                       "away_player_7", "away_player_8", "away_player_9",
                       "away_player_10", "away_player_11"]

HOME_PLAYER_COLUMNS = ['home_player_1', 'home_player_2', 'home_player_3',
                       "home_player_4", "home_player_5", "home_player_6",
                       "home_player_7", "home_player_8", "home_player_9",
                       "home_player_10", "home_player_11"]

PLAYER_TYPES = ['Attacker', 'Defender', 'Goalkeeper', 'Midfielder']

# TODO: Move SKILL COLUMNS to Utils.py
SKILL_COLUMNS = ['finishing', 'sliding_tackle',
                 'gk_reflexes', 'short_passing']

import pandas as pd

def select_all_query_table(table_name):
  return "SELECT * from " + table_name

def sql_to_dataframe(conn, sql):
  df = pd.read_sql_query(sql, conn)
  return df


def map_country_to_name(countries_df, country_id):
  return countries_df.loc[countries_df['id'] == country_id, 'name']


