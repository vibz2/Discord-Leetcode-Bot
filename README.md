# About
Dreading LeetCode? Fearing for that next mock interview? Hate suffering alone?

WELL HAVE NO FEAR! (corny intro insert)

All jokes aside, this is a simple discord leetcode bot. All it really does is connect to your leetcode account and then has commands to allow you to sync it to the last 20 problems you did
it accumulating those points and then having a leaderboard.

## Why I made it
Well, just like everyone else in CS I unfortunately (or fortunately if your a wacko like me) have to do leetcode. However, where's the fun without a bit of competition and tracking with
your friends! I looked online for other discord leetcode bots and they were either too many features and not really doing these simple tasks I wanted, or had different functionalities
like doing leetcode together inside of discord which wasn't what I wanted.

I simply wanted to track my leetcode problems, have a leaderboard with a simple point system and reduced points on repeated leetcode problems (YEAH IT TRACKS THOSE TOO!). And so here we are,
two full days worth of coding later :D.

# Tech Stack
The project is made entirely in python. It also uses SQLite as I didn't want a heavier database with more compute and setup than necessary. Please keep in mind though that since it does
use SQLite, due to the nature of the software it stores the database as a file wherever you host or run it. As a result, be wary if your hosting this bot online and there's no permanent
file system as it may get destroyed on redeployment or crashes, and you will lose all your precious points.

# How to run
First you have to have a .env containing DISCORD_TOKEN if you are trying to run it locally, or somewhere on that online hosting platform you will use. Keep the name the same and 
put the token you have in it. For instance in railway there's an option to use variables, you can add a variable, set it to DISCORD_TOKEN and put your token as the value.

Due to this, please make sure to go to https://discord.com/developers/applications and set up a new project and generate a token to then use with the bot.

after doing all of that, just make sure that whatever is trying to run the bot is doing so through python bot.py as that is the file which starts and runs the whole application.

# Commands
## Normal User Commands
/leaderboard - will generate the leaderboard for the server for you to view

/sync - will sync the last 20 leetcode problems you did (fetches it from leetcode api and compares with database for point tracking) 

/link - Simply put in your LeetCode username in this. We need this for the bot to properly get all your details or do anything with your account.

/stats - This is to view your individual stats. So should show your current points, how many problems of which difficulty you did, etc.

## Admin User Commands
/clear_user - deletes that users points and data. Their user still exists in the database, just wipes their entire point standing

/clear_all - wipes everyones point data. Thier users should still exist in the database 

# Support
If you got any questions or issues don't hesitate to reach out! Here's my linkedin: https://www.linkedin.com/in/vibhas-ramani/
