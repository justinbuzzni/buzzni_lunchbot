#!/usr/bin/env python
# -*- coding: utf-8 -*-

from GmailConnector import GmailConnector
from GmailConnector import get_members
from datetime import date

if __name__ == "__main__":
    members = [ a["email"] for a in get_members() ]

    content = """
    * 버즈니 점심 사전조사 * // %s
    안드실분은 시간내에 답장해주세요.
    """

    content = content % (date.today())

    gc = GmailConnector()
    #member
    gc.send(["pgonee@buzzni.com"], "pre", content)