# ModernSECFootballStats-BeautifulSoup
A Python 2.7, BeautifulSoup4-based web scraper that I wrote to extract all data from CFBStats.com for the "Modern" SEC (South Eastern Conference) Football era, from 2012 - 2017, and to post all of that back into a SQL database for basic data analysis and visualizations. **This code does still needs some refactoring** (particularly in how database tables are created) as it was written purely as a one-time utility, but it works as-is following the instructions below.

## How to Use This Web Scraper (Mac OS)

1) Open your Mac terminal
2) Type `pip install BeautifulSoup`
3) Press enter/return
4) Once that is finished, type `pip install mysql-connector-python`
5) Press enter/return

### Once you've done that:

6) Download 'secstatsscraper.py'
7) Open 'secstatsscrapery.py'
8) Navigate to line 148
9) Insert all of your proper database details

### Finally, build out your database and necessary tables:

10) Open your Mac terminal
11) Type `/usr/local/mysql/bin/mysql -u root -p`
12) Press enter/return
13) Enter your machine's password
14) Type `CREATE DATABASE secstats;`
15) Type `USE DATABASE secstats;`
16) Copy/paste the entire text block below (**again, this is the aspect of code that needs refactoring...there are certainly much cleaner and more Pythonoic ways of doing this...I'll update the code and README accordingly in the future**)

```
CREATE TABLE roster (Season int, Team varchar(255), No varchar(255), Name varchar(255), Pos varchar(255), Yr varchar(255), Ht int, Wt int, Hometown varchar(255), Last_School varchar(255));
CREATE TABLE rushing (Season int, Team varchar(255), Rank_On_Team int, Name varchar(255), Yr varchar(255), Pos varchar(255), G int, Att int, Yards int, Avg DECIMAL(5,2), TD int, Att_G DECIMAL(5,2), Yards_G DECIMAL(5,2));
CREATE TABLE passing (Season int, Team varchar(255), Rank_On_Team int, Name varchar(255), Yr varchar(255), Pos varchar(255), G int, Att int, Comp int, Pct DECIMAL(5,2), Yards int, Yards_Att DECIMAL(5,2), TD int, Ints int, Rating DECIMAL(5,2), Att_G DECIMAL(5,2), Yards_G DECIMAL(5,2));
CREATE TABLE receiving (Season int, Team varchar(255), Rank_On_Team int, Name varchar(255), Yr varchar(255), Pos varchar(255), G int, Rec int, Yards int, Avg DECIMAL(5,2), TD int, Rec_G DECIMAL(5,2), Yards_G DECIMAL(5,2));
CREATE TABLE puntreturn (Season int, Team varchar(255), Rank_On_Team int, Name varchar(255), Yr varchar(255), Pos varchar(255), G int, Ret int, Yards int, Avg DECIMAL(5,2), TD int, Ret_G DECIMAL(5,2), Yards_G DECIMAL(5,2));
CREATE TABLE kickreturn (Season int, Team varchar(255), Rank_On_Team int, Name varchar(255), Yr varchar(255), Pos varchar(255), G int, Ret int, Yards int, Avg DECIMAL(5,2), TD int, Ret_G DECIMAL(5,2), Yards_G DECIMAL(5,2));
CREATE TABLE punting (Season int, Team varchar(255), Rank_On_Team int, Name varchar(255), Yr varchar(255), Pos varchar(255), G int, Punts int, Yards int, Avg DECIMAL(5,2), Punts_G DECIMAL(5,2), Yards_G DECIMAL(5,2));
CREATE TABLE kickoff (Season int, Team varchar(255), Rank_On_Team int, Name varchar(255), Yr varchar(255), Pos varchar(255), G int, Kickoffs int, Yards int, Avg DECIMAL(5,2), Touchback int, Touchback_pct DECIMAL(5,2), Out_Of_Bounds int, Onside int);
CREATE TABLE scoring (Season int, Team varchar(255), Rank_On_Team int, Name varchar(255), Yr varchar(255), Pos varchar(255), G int, TD int, FG int, 1XP int, 2XP int, Safety int, Points int, Points_G DECIMAL(5,2));
CREATE TABLE total (Season int, Team varchar(255), Rank_On_Team int, Name varchar(255), Yr varchar(255), Pos varchar(255), G int, Rush_Yards int, Pass_Yards int, Plays int, Total_Yards int, Yards_Play DECIMAL(5,2), Yards_G DECIMAL(5,2));
CREATE TABLE allpurpose (Season int, Team varchar(255), Rank_On_Team int, Name varchar(255), Yr varchar(255), Pos varchar(255), G int, Rush int, Recv int, Punt_Ret int, Kick_Ret int, Int_Ret int, Plays int, Total_Yards int, Yards_Play DECIMAL(5,2), Yards_G DECIMAL(5,2));
CREATE TABLE interception (Season int, Team varchar(255), Rank_On_Team int, Name varchar(255), Yr varchar(255), Pos varchar(255), G int, Ints int, Yards int, TD int, Int_G DECIMAL(5,2));
CREATE TABLE fumblereturn (Season int, Team varchar(255), Rank_On_Team int, Name varchar(255), Yr varchar(255), Pos varchar(255), G int, Fum_Ret int, Yards int, TD int);
CREATE TABLE tackleforloss (Season int, Team varchar(255), Rank_On_Team int, Name varchar(255), Yr varchar(255), Pos varchar(255), G int, TFL int, TFL_Yards int, TFL_G DECIMAL(5,2));
CREATE TABLE sack (Season int, Team varchar(255), Rank_On_Team int, Name varchar(255), Yr varchar(255), Pos varchar(255), G int, Sacks DECIMAL(5,2), Sack_Yards int, Sacks_G DECIMAL(5,2));
CREATE TABLE miscdefense (Season int, Team varchar(255), Rank_On_Team int, Name varchar(255), Yr varchar(255), Pos varchar(255), G int, Passes_Broken_Up int, QB_Hurries int, Fumbles_Forced int, Kicks_Punts_Blocked int);
CREATE TABLE tackle (Season int, Team varchar(255), Rank_On_Team int, Name varchar(255), Yr varchar(255), Pos varchar(255), G int, Solo int, Assisted int, Total int, Total_G DECIMAL(5,2));
```
17) Press enter/return
18) Open 'secstatsscraper.py'
19) Build/compile the code
20) On my machine and internet connection, ~1500 pages were opened, scraped, cleaned, and placed into the SQL database in ~8 minutes.
