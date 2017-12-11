# Feature Generation

## Players' based features

These are the features based on the players’ attributes (skills) and FIFA ratings. Each match contains the information about the line up of both the home and the away team; listing the eleven players that played for each team. These player ids’ are used to extract information from the players’ attributes table and used to generate
relevant features.

### Clustering the players based on their position in their teams 

The positions in a team are:
- Attacker
- Defender
- Midfielder
- GoalKeeper

The players were classified into their positions using a naive algorithm based on the following skills:
- finishing
- sliding_tackle
- gk_reflexes
- short passing

Thus, depending on a player's maximum skill, he will be classified into the respective position. For example, if the max skill is finishing, then the player is an attacker; if the max skill is sliding_tackle, then he is a defender etc.

### Player Features Added 

- **Average Ratings for team's players in attack, defense, midfielder, and goalkeeping**

  - away_Defender_rating
  - home_Defender_rating
  - away_Attacker_rating
  - home_Attacker_rating
  - away_Goalkeeper_rating
  - home_Goalkeeper_rating
  - away_Midfielder_rating
  - home_Midfielder_rating
  
  To get the rating of a player, we get his closest rating to the match date, as every player has yearly entries for his rating.

- **Top and Bottom players in a team** 

  We defined a top player in a team as any player with a rating greater than 80, and similarly defined the bottom players as the ones  
  with rating below 50. For both teams, the number of top and bottom players was calculated.
  
  - num_top_players_home
  - num_top_players_away
  - num_bottom_players_home
  - num_bottom_players_away
  
- **Average Age for team's players in attack, defense, midfielder, and goalkeeping**

  Using the birthday date attribute of every player, we calculated the player's age when a certain match was played. Since the players
  are clustered into 4 positions, we took the average of the ages of all players in a position for both teams.

  - away_Defender_age
  - home_Defender_age
  - away_Attacker_age
  - home_Attacker_age
  - away_Goalkeeper_age
  - home_Goalkeeper_age
  - away_Midfielder_age
  - home_Midfielder_age
  
- **Average BMI for team's players in attack, defense, midfielder, and goalkeeping**

  Using the height and weight attributes of every player, we calculated the player's body mass index (BMI). Since the players are
  clustered into 4 positions, we took the average of the bmi's of all players in a position for both teams.

  - away_Defender_bmi
  - home_Defender_bmi
  - away_Attacker_bmi
  - home_Attacker_bmi
  - away_Goalkeeper_bmi
  - home_Goalkeeper_bmi
  - away_Midfielder_bmi
  - home_Midfielder_bmi

### Form Stats Features

A team’s current form in this season, its historic home record, its away record, head to head with the team it's playing against affect players’ confidence; and have a significance in that it tells us the trend of a stronger club between the two. Thus, we generated the following features:

- **All time home record** - The percentage of home matches that the home team wins historically
- **This season home record** - The percentage of home matches that the home team has won this season
- **All time away record** - The percentage of away matches that the away team wins historically
- **This season away record** - The percentage of away matches that the away team has won this season
- **Away record at this ground** - The percentage of away matches that the away team has won at this particular home team
- **Head to head draws** - The percentage of head to head matches between the two teams that have resulted in draws
– **Head to head home wins** - The percentage of head to head matches between the two teams that have resulted in the home team winning
- **Head to head home loss** - The percentage of head to head matches between the two teams that have resulted in the home team losing/away team winning

### Form Guide Features

The form guide for a team is an aggregation of its last five results. So if a team has won the last two matches, lost the two before that and won
the one before those; its form guide will be **WWLLD**. A win corresponds to the letter W, loss to the letter L and draw to the letter D.

# Filling Missing Values

- **Head to head wins/draw/loss** - Take all head to head matches, and replace np.nan with the mean of all non nan values. It is possible that some teams have NEVER played before, in which case I will just randomly assign a value of 0.33 to each of the three events (equal probability of happening)

- **Away team’s win rate at this ground** - Find all samples where this team played away at this home team’s ground; and take average. If this team has never played here; just take the average of its all time away record. (If this case is encountered)

- **Form guide** - Replace the NaN values with the most common form guide for that team during that season

- **Player's age/bmi** - Replace the NaN values with  the average of player's age/bmi corresponding to the same position. 






