from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from discord.ext import commands

from .. import models
engine = create_engine("sqlite:///data.db")
models.create(engine)

sess = Session(engine)
class AnswerCog(commands.Cog):
    def __init__(self , bot, ask):
        self.bot = bot
        self.ask = ask

    # @commands.Cog.listener()
    # async def on_message(self , message):
        # print("someone sent something")


    @commands.Cog.listener()
    async def on_connect(self):
        print("Connected!")

    @commands.command()
    async def answer(self , ctx , * , arg):
        current_guild = sess.query(models.Guild).filter_by(id = int(ctx.guild.id)).first()
        if current_guild:
            await ctx.send(self.ask(arg , current_guild.context ))
        else:
            await ctx.send("register the guild first")

    @commands.command()
    async def canswer(self , ctx , * , arg):
        current_guild = sess.query(models.Guild).filter_by(id = int(ctx.guild.id)).first()
        if current_guild:
            channel_context = sess.query(models.Context).filter_by(channel_id = ctx.channel.id).first()
            if channel_context:
                await ctx.send(self.ask(arg , channel_context.para ))
            else:
                await ctx.send("No context for this channel")
        else:
            await ctx.send("register the guild first")
