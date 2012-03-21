#!/usr/bin/env python
# -*- coding: utf-8 -*-

from GmailConnector import GmailConnector, CrawlUtil
from GmailConnector import get_members
from GmailConnector import get_account
import random, imaplib, datetime, time

if __name__ == "__main__":
    members = get_members()
    account, passwd = get_account()
    M = imaplib.IMAP4_SSL("imap.gmail.com", 993)
    M.login(account, passwd)
    M.select()

    typ, data = M.search(None, 'ALL')
    for num in data[0].split():
        typ, data = M.fetch(num, '(BODY[HEADER])')
        email_data = data[0][1]

        pattern_list = [  'Date:(?P<date>.*?) \+'
            , 'From:.*?<(?P<from>.*?)>'
        ]

        app_data = CrawlUtil.extractData(email_data, pattern_list)[0]
        today = datetime.date.today()
        mail_day = time.strptime(app_data['date'],"%a, %d %b %Y %H:%M:%S")
        if today.year == mail_day.tm_year:
            if today.month == mail_day.tm_mon:
                if today.day == mail_day.tm_mday:
                    ignore = app_data['from']
                    for people in members:
                        if people["email"] == ignore or people["name"].lower() == ignore.split("@")[0].lower():
                            print "ignored:",people["name"]
                            people["status"] = False

    M.close()
    M.logout()

    peoples_leader = []
    peoples_male = []
    peoples_female = []
    for temp_people in members:
        if temp_people["status"] == True:
            if temp_people["commander"] == True:
                peoples_leader.append([temp_people["email"],temp_people["name"]])
            elif temp_people["gender"] == True:
                peoples_male.append([temp_people["email"],temp_people["name"]])
            else:
                peoples_female.append([temp_people["email"],temp_people["name"]])

    random.shuffle(peoples_leader)
    random.shuffle(peoples_male)
    random.shuffle(peoples_female)

    peoples = [[],[]]

    for i in range(0, len(peoples_leader)):
        peoples[i%2].append(peoples_leader[i])

    for i in range(0, len(peoples_male)):
        peoples[i%2].append(peoples_male[i])

    for i in range(0, len(peoples_female)):
        peoples[i%2].append(peoples_female[i])

    random.shuffle(peoples[0])
    random.shuffle(peoples[1])

    content = """
            버즈니 점심 팀
    ================================\n"""
    for team in peoples:
        content += "\t%s 팀\n" % team[0][1]
        content += "\t---------\n"
        for people in team:
            content += "\t%s\n" % people[1]
        content += "\t---------\n"

    a = GmailConnector()
    #[ a["email"] for a in get_members() ]
    a.send(["pgonee@buzzni.com"], "result", content)















