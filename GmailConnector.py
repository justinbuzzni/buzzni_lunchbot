#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.append("/home/newmoni/workspace")

from utils.src.mail import Sender
from utils.src.crawler.CrawlUtil import CrawlUtil
from datetime import date

class GmailConnector(object):
    def __init__(self):
        account = ""
        passwd = ""

        fp = open("/home/newmoni/workspace/buzzni_lunchbot/sender_account.secret", "r")
        account, passwd = fp.read().split(",")

        self.mail = Sender("gmail", account, passwd)

    def send(self, targets=[], type="", content=""):
        """ type : pre, result
        """
        title = ""
        if type == "pre":
            title = "%s 버즈니 점심 사전조사" % (date.today())
        elif type == "result":
            title = "%s 버즈니 점심 조" % (date.today())

        return self.mail.send(targets, title, content)

def get_members():
    fp = open("/home/newmoni/workspace/buzzni_lunchbot/members.secret", "r")

    member_list = []
    #이메일,이름,식사,남/여,팀장
    for line in fp.readlines():
        line = line.replace("\n","")
        if line[0] == "#":
            continue

        line = line.split(",")
        tmp = {
            "email":line[0].replace("\"",""),
            "name":line[1].replace("\"","")
        }

        if line[2] == "True":
            tmp["status"] = True
        elif line[2] == "False":
            tmp["status"] = False

        if line[3] == "True":
            tmp["gender"] = True
        elif line[3] == "False":
            tmp["gender"] = False

        if line[4] == "True":
            tmp["commander"] = True
        elif line[4] == "False":
            tmp["commander"] = False

        member_list.append(tmp)
    return member_list

def get_account():
    fp = open("/home/newmoni/workspace/buzzni_lunchbot/sender_account.secret", "r")
    return fp.read().split(",")

