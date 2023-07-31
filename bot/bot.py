import discord
import pandas as pd
import numpy as np
import joblib
import imgkit
import random
# from bokeh.plotting import figure
# from bokeh.models import ColumnDataSource
# import csv
# from bokeh.io import output_notebook
import os
# import seaborn as sns
# from sklearn.model_selection import GridSearchCV

# Regression
# from sklearn.linear_model import LinearRegression
# from sklearn.tree import DecisionTreeRegressor
# from sklearn.model_selection import train_test_split
# output_notebook()
# import matplotlib.pyplot as plt
# from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
# import joblib
# from sklearn.ensemble import GradientBoostingRegressor, RandomForestRegressor
# from sklearn.compose import TransformedTargetRegressor
# from sklearn.preprocessing import QuantileTransformer
# import lightgbm as lgbm
# import xgboost as xg
# # IMPORT THE OS MODULE.
import os

# IMPORT LOAD_DOTENV FUNCTION FROM DOTENV MODULE.
from dotenv import load_dotenv

# LOADS THE .ENV FILE THAT RESIDES ON THE SAME LEVEL AS THE SCRIPT.
load_dotenv()

#load model
regr = joblib.load(os.getcwd().replace('bot', '/best_model.pkl'))

# GRAB THE API TOKEN FROM THE .ENV FILE.
# DISCORD_TOKEN = os.getenv("sk-EdrOSrn1ciYTp6AbwO9RT3BlbkFJcNJd2INZtRAruZRPTXtUv")

# GETS THE CLIENT OBJECT FROM DISCORD.PY. CLIENT IS SYNONYMOUS WITH BOT.
bot = discord.Client(intents=discord.Intents.all())
scores = pd.read_csv(os.getcwd().replace('bot', '/scripts/scores.csv'))
# EVENT LISTENER FOR WHEN THE BOT HAS SWITCHED FROM OFFLINE TO ONLINE.
@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith('/hello'):
        await message.channel.send('Hello!')
    
    if message.content.startswith('/predict'):
        l = []
        try:
            l = message.content.split(" ")[1:]
            
            # print(message.content)
            l = [int(x) for x in l]
            print(l)

            to_predict = pd.DataFrame(columns = scores.columns[:-3])
            app = []
            for i in range(len(l)):
                team = l[i]
                df = pd.read_csv(os.getcwd().replace('bot', '')+f'/data/team_data/{team}.csv')
                        
                app+= list(df.describe().loc['mean'])
                        
            to_predict.loc[0] = app

            score1 = regr.predict(to_predict[to_predict.columns[0:6]])
            score2 = regr.predict(to_predict[to_predict.columns[6:]])

            r = round(score1[0])
            b = round(score2[0])

            await message.channel.send(f'Prediction: \nRed Team ({l[0]} and {l[1]}): {r}\nBlue Team ({l[2]} and {l[3]}): {b}')
        except Exception as e:
            print(str(e))

            await message.channel.send("Please input four team numbers, separated by spaces!")
    
    jokes = [
        "Yo momma is so fat, when she stepped on a scale, it said 'To be continued.'",
        "Yo momma is so stupid, she got locked in a grocery store and starved.",
        "Yo momma is so old, she has a picture of Moses in her yearbook.",
        "Yo momma is so fat, she was overthrown as a small moon by the International Astronomical Union.",
        "Yo momma is so ugly, she made an onion cry.",
        "Yo momma is so poor, when I asked her what's for dinner, she pulled out a shotgun and said 'The next thing that moves.'",
        "Yo momma is so fat, when she fell, no one laughed but the ground started cracking up.",
        "Yo momma is so dumb, she thought a quarterback was a refund.",
        "Yo momma is so old, she knew Burger King when he was just a prince.",
        "Yo momma is so fat, she needs cheat codes for Wii Fit.",
        "Yo momma is so stupid, when they said it was chilly outside, she ran out with a spoon.",
        "Yo momma is so ugly, even her reflection walks away.",
        "Yo momma is so fat, she left the house in high heels and came back in flip flops.",
        "Yo momma is so poor, she waves around a popsicle stick and calls it air conditioning.",
        "Yo momma is so stupid, she put paper on the TV and called it 'paper view'.",
        "Yo momma is so old, her birth certificate says 'expired'.",
        "Yo momma is so fat, she uses Google Earth to take a selfie.",
        "Yo momma is so ugly, she scares the ghosts away.",
        "Yo momma is so poor, she can't afford to pay attention.",
        "Yo momma is so fat, when she jumps, she gets stuck in the sky.",
        "Yo momma is so old, her social security number is 1.",
        "Yo momma is so stupid, she climbed a glass wall to see what was on the other side.",
        "Yo momma is so fat, when she sat on an iPhone, it turned into an iPad.",
        "Yo momma is so ugly, when she went to the haunted house, she came out with a job application.",
        "Yo momma is so poor, she eats cereal with a fork to save milk.",
        "Yo momma is so fat, she got baptized at SeaWorld.",
        "Yo momma is so old, when she was in school, there was no history class.",
        "Yo momma is so stupid, she tried to climb Mountain Dew.",
        "Yo momma is so fat, her belly button gets home 15 minutes before she does.",
        "Yo momma is so ugly, even Hello Kitty said goodbye.",
        "Yo momma is so poor, she chases the garbage truck with a grocery list.",
        "Yo momma is so fat, she got arrested for carrying 10 pounds of crack.",
        "Yo momma is so old, she remembers when the Grand Canyon was a ditch.",
        "Yo momma is so stupid, she brought a spoon to the Super Bowl.",
        "Yo momma is so fat, her car has stretch marks.",
        "Yo momma is so ugly, when she tried to join an ugly contest, they said, 'Sorry, no professionals.'",
        "Yo momma is so poor, the ducks throw bread at her.",
        "Yo momma is so fat, when she goes camping, the bears hide their food.",
        "Yo momma is so old, she has an autographed Bible.",
        "Yo momma is so stupid, she stared at a cup of orange juice because it said 'concentrate'.",
        "Yo momma is so fat, when she wears a yellow raincoat, people yell 'Taxi!'",
        "Yo momma is so ugly, the government moved Halloween to her birthday.",
        "Yo momma is so poor, burglars break into her home and leave money.",
        "Yo momma is so fat, she stepped on a rainbow and made Skittles.",
        "Yo momma is so old, her memory is in black and white.",
        "Yo momma is so stupid, she put a ruler next to her bed to see how long she slept.",
        "Yo momma is so fat, when she sits around the house, she really sits around the house.",
        "Yo momma is so ugly, her portraits hang themselves.",
        "Yo momma is so poor, her idea of dessert is chasing the ice cream truck.",
        "Yo momma is so fat, she needs GPS to find her belly button.",
        "Yo momma is so old, she knew Captain Crunch when he was still a private.",
        "Yo momma is so stupid, she thought a lawsuit was something you wear to court.",
        "Yo momma is so fat, she sat on Walmart and lowered the prices.",
        "Yo momma is so ugly, when she looks in the mirror, her reflection ducks.",
        "Yo momma is so poor, she washes paper plates.",
        "Yo momma is so fat, her blood type is Ragu.",
        "Yo momma is so old, she owes Jesus a dollar.",
        "Yo momma is so stupid, she thinks Taco Bell is a Mexican phone company.",
        "Yo momma is so fat, when she went to the beach, the whales sang 'We are family.'",
        "Yo momma is so ugly, she made a blind kid cry."
    ]

    if message.content == "/yomama":
        await message.channel.send(jokes[random.randint(0,59)])
    
    if message.content.startswith("/progression"):
        try:
            team = message.content.split(" ")[1]
                
            team = int(team)
        
            key = message.content.split(" ")[2]

            # imgkit.from_file(os.getcwd().replace('bot', f'data/team_data/{team}_{key}.html'), 'out.jpg')
            print("done")
            await message.channel.send(f'https://ftcscout.org/teams/{team}')
            with open(os.getcwd().replace('bot', f'data/team_data/{team}_{key}.png'), 'rb') as f:
                picture = discord.File(f)
                await message.channel.send(file=picture)


        except Exception as e:
            print(str(e))
            await message.channel.send("Please use a valid team and key! Keys: \"Auto\", \"OPR\", \"CCWM\"")

    if message.content.startswith("/roast "):
        try:
            team = message.content.split("/roast")[1]
            
            team = int(team)

            roasts = [
                f"Team {team}, your bot moves so slowly, even a snail could outpace it.",
                f"Team {team}, your robot's programming is so poor, even a toaster is smarter.",
                f"I've seen more precision in a kid's finger painting than Team {team}'s bot design.",
                f"Team {team}, your AI has the processing power of a potato.",
                f"Your robot has less balance than a cat on a tightrope, Team {team}.",
                f"Team {team}'s robot is so inefficient, it would lose in a race against a Roomba.",
                f"I've seen more complex systems in a wind-up toy than in Team {team}'s bot.",
                f"Even the simplest maze would be an insurmountable challenge for Team {team}'s robot.",
                f"Team {team}, the only thing your robot masters is the art of malfunctioning.",
                f"The engineers at Team {team} must've mistaken 'off' for 'on' in the robot's programming.",
                f"Team {team}, your bot's navigation system couldn't guide it out of a paper bag.",
                f"Team {team}, your bot's sensors are as effective as a blindfold.",
                f"Team {team}'s robot has more bugs than an anthill.",
                f"Your bot's design is as outdated as dial-up, Team {team}.",
                f"Team {team}, your robot's battery life is shorter than a goldfish's memory.",
                f"Your robot has the agility of a sloth, Team {team}.",
                f"The only thing your bot excels at is gathering dust, Team {team}.",
                f"Team {team}'s robot is so noisy, it could be mistaken for a jackhammer.",
                f"Your bot's signal is weaker than a radio in a tunnel, Team {team}.",
                f"Team {team}, your robot is less responsive than a rock.",
                f"Team {team}, your robot's wiring is messier than a bowl of spaghetti.",
                f"Your robot's user interface is more confusing than quantum physics, Team {team}.",
                f"Team {team}, your robot couldn't navigate its way out of a cardboard box.",
                f"The most advanced feature of Team {team}'s robot is its power switch.",
                f"Team {team}, your robot's programming is as robust as a house of cards.",
                f"Team {team}'s robot is less reliable than weather forecasts.",
                f"The only thing predictable about Team {team}'s robot is its unpredictability.",
                f"Your robot has fewer features than a brick, Team {team}.",
                f"The only thing high-performance about Team {team}'s robot is its ability to drain batteries.",
                f"Your robot's response time is like waiting for a glacier to move, Team {team}.",
                f"Team {team}, your robot's maneuverability is on par with a boulder.",
                f"Your robot's durability is like a sandcastle facing the tide, Team {team}.",
                f"Team {team}'s robot couldn't outsmart a doorknob.",
                f"Your robot is about as stealthy as a marching band, Team {team}.",
                f"Team {team}, your robot's speed wouldn't challenge a turtle.",
                f"Your robot's accuracy is as reliable as a broken clock, Team {team}.",
                f"Team {team}, your robot's operational time is shorter than a commercial break.",
                f"Your robot's range of motion is on par with a parking lot, Team {team}.",
                f"Team {team}, your robot's problem-solving ability equates to a garden gnome's.",
                f"Your robot has a higher crash rate than a computer running on dial-up, Team {team}.",
                f"Team {team}'s robot moves like it's always on its coffee break.",
                f"Their robot's software is so outdated, even the dinosaurs wouldn't use it.",
                f"Team {team}'s robot has more downtime than a hibernating bear.",
                f"Even a compass would be a better navigator than Team {team}'s robot.",
                f"If Team {team}'s robot were any slower, it would be going backwards.",
                f"Team {team}'s robot couldn't pick up an object if it was glued to it.",
                f"Their robot has more loose screws than a second-hand furniture store.",
                f"If confusion were an asset, Team {team}'s robot would be a millionaire.",
                f"Their robot is so fragile, even a leaf could damage it.",
                f"Team {team}'s robot has a hard time differentiating between up and down.",
                f"Team {team}'s robot is as stealthy as an elephant in a china shop.",
                f"If errors were a form of art, their robot would be Picasso.",
                f"Team {team}'s robot has more 'unknown errors' than known features.",
                f"If you're in need of a paperweight, Team {team}'s robot might be of some use.",
                f"Team {team}'s robot runs out of battery faster than their fans run out of patience.",
                f"Team {team}'s robot is as useful as a chocolate teapot.",
                f"If 'system crash' was a competition, Team {team}'s robot would take the gold.",
                f"Their robot couldn't follow a line if it was a railroad track.",
                f"If shaking and rattling were scoring points, Team {team} would be champions.",
                f"Team {team}'s robot is more lost in a competition than a penguin in a desert.",
            ]

            msg = roasts[random.randint(0,59)]

            await message.channel.send(msg)

        except Exception as e:
            await message.channel.send("One valid team please!")

    if message.content == "/help":
        await message.channel.send("Here are the functions of the bot:\n/roast {team number}: Roasts a team.\n\n/progression {team} {OPR/CCWM/Auto}: Shows a graph of team progression for the whole season.\n\n/yomama: A yomama joke.")
# EXECUTES THE BOT WITH THE SPECIFIED TOKEN. TOKEN HAS BEEN REMOVED AND USED JUST AS AN EXAMPLE.
bot.run("MTEzMDM0MzI4MjgxMjE0MTYxMQ.GTBKdU.lzNPB_OUoXz2xMDHMeAl6l7cbbd2NJXbap1wdQ")