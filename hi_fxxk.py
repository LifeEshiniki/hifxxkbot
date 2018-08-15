#!/usr/bin/python
# -*- coding: utf-8 -*-
# coding by yamatch

import janome
from janome.tokenizer import Tokenizer

import json
import numpy as np
import tweepy

import datetime

fuck_count = 0


def tweet_fuck():
    now = datetime.datetime.now()
    api.update_status("{0}現在、Fuckツイートは{1}ツイートありました。はい、fuck".format(now, fuck_count))


f_words = ["君", "みつは", "三葉", "たき", "前", "瀧", "スパークル", "彼氏", "彼女", "新海", "彗星", "運命だとか", "シド#ファ#", "口噛み"]

f_bigrams = {"": "", "運命": "", "口": "咬み", "ド": "#", "の": "名", "は": "。", "やっと": "目", "探し": "始め"}
# アプリのキー、アクセストークン
CONSUMER_KEY = ""
CONSUMER_SECRET = ""
ACCESS_TOKEN = ""
ACCESS_SECRET = ""

# ハンドラー
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)

# セット
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

# 変数apiから各々の処理を行う
api = tweepy.API(auth)

public_tweets = api.home_timeline()

tweet_words = []

for tweets in public_tweets:
    tweet_words.clear()
    t = Tokenizer()
    tokens = t.tokenize(tweets.text, wakati=True)
    is_fuck = False
    first_word = ""
    for word in tokens:
        # print(word)
        second_word = word
        if word in f_words:
            is_fuck = True
        else:
            try:
                if f_bigrams[first_word] == second_word:
                    is_fuck = True
            except KeyError:
                continue

        first_word = word

    if is_fuck == True:
        print("{} はい fuck.".format(tweets.text))
        fuck_count += 1
        try:
            reply = "@" + str(tweets.author.screen_name) + " はい、fuck"
            print("はい、Fuck")
            api.update_status(status=reply, in_reply_to_status_id=tweets.id)
        except tweepy.error.TweepError:
            pass
    else:
        print("{} is not fxxk tweet.".format(tweets.text))

tweet_fuck()


