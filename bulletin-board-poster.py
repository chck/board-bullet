#!/usr/bin/env python
# -*- coding: utf-8 -*-
import yaml
import mechanize

class BulletinBoardPoster:

  def __init__(self):
    _var = open("../API.yaml").read()
    _yaml = yaml.load(_var)
    self.url = _yaml["test_url"]

  def getBody(self):
    print("---connect start---")
    b = mechanize.Browser()
    b.open(self.url)
    return b.response().read()


bbp = BulletinBoardPoster()
print(bbp.getBody())
