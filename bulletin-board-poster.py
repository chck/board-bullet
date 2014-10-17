#!/usr/bin/env python
# -*- coding: utf-8 -*-
import yaml
import mechanize

class BulletinBoardPoster:

  def __init__(self):
    _var = open("../API.yaml").read()
    _yaml = yaml.load(_var)
    self.br = mechanize.Browser()
    self.br.open(_yaml["test_url"])
    self.br.select_form(nr=0)

  def getHtml(self):
    return self.br.response().read()

  def post(self, text):
    self.br.select_form(name="fcs")
    self.br["MESSAGE"] = text
    self.br.submit()

  def main(self):
    Bot = BulletinBoardPoster()
    Bot.post("test")

if __name__ == "__main__":
  print(BulletinBoardPoster().getHtml())
  print(BulletinBoardPoster().main())
