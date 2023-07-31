import discord
import pandas as pd
import numpy as np
import joblib
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

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
    
    if message.content.startswith('$predict'):
        l = []
        try:
            l = message.content.split(" ")[1:]
            l = [int(x) for x in l]

            to_predict = pd.DataFrame(columns = scores.columns[:-2])
            app = []
            for i in len(l):
                team = l[i]
                df = pd.read_csv(os.getcwd().replace('bot', f'/data/team_data/{team}.csv'))
            
                app+= list(df.describe().loc['mean'])
            
            to_predict[0] = app

            score1 = regr.predict(to_predict[to_predict.columns[0:6]])
            score2 = regr.predict(to_predict[to_predict.columns[6:]])

            await message.channel.send(f'{score1} {score2}')
        except Exception as e:
            print(str(e))

            print("Please input four team numbers, separated by spaces!")

# EXECUTES THE BOT WITH THE SPECIFIED TOKEN. TOKEN HAS BEEN REMOVED AND USED JUST AS AN EXAMPLE.
bot.run("MTEzMDM0MzI4MjgxMjE0MTYxMQ.GTBKdU.lzNPB_OUoXz2xMDHMeAl6l7cbbd2NJXbap1wdQ")