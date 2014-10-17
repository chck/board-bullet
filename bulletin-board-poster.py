#!/usr/bin/env python
# -*- coding: utf-8 -*-
import yaml
import mechanize

class BulletinBoardPoster:

  def __init__(self, num=0):
    _var = open("../API.yaml").read()
    _yaml = yaml.load(_var)
    self.br = mechanize.Browser()
    if num==1:
      _url = _yaml["url_b100"]
    if num==2:
      _url = _yaml["url_41"]
    else:
      _url = _yaml["url_test"]
    self.br.open(_url)
    self.br.select_form(nr=0)
    self.num = num

  def getHtml(self):
    return self.br.response().read()

  def post(self, text):
    if self.num==1:
      self.br.select_form(id="comment-form")
      self.br["comment"] = text
    if self.num==2:
      self.br.select_form(name="comment_submit")
      self.br["posting_text"] = text
    else:
      self.br.select_form(name="fcs")
      self.br["MESSAGE"] = text
    self.br.submit()

  def main(self):
    _text = "14141"
#    print("test post")
#    BotforTest = BulletinBoardPoster()
#    BotforTest.post(_text)
#    print("prod post1")
#    BotforS7 = BulletinBoardPoster(1)
#    BotforS7.post(_text)
    print("prod post2")
    Botfor41 = BulletinBoardPoster(2)
    Botfor41.post(_text)


if __name__ == "__main__":
#  print(BulletinBoardPoster().getHtml())
  print(BulletinBoardPoster().main())
