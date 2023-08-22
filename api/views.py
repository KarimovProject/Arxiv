from django.shortcuts import render
from telegram.ext import Updater, CommandHandler
from telegram import Bot
from django.http import HttpResponse,JsonResponse
from django.views import View
from telegram.ext import CommandHandler, CallbackQueryHandler, CallbackContext, Updater
from .bot import Personal_bot

TOKEN = "5777160491:AAGZYNh3NjYcen93fdkDbTCkAz7cRW7HLcc"
updater = Updater(TOKEN)


class BotView(View):
    def get(self, request):
        return JsonResponse({"status_code": 200})
    def post(self, request):
        return JsonResponse({"status_code": 200, "message": "ok"})
    
    
    updater.dispatcher.add_handler(CommandHandler("start", Personal_bot.start))
    updater.dispatcher.add_handler(CallbackQueryHandler(Personal_bot.query))

    updater.start_polling()
    updater.idle()

    