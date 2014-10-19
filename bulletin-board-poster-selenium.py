#!/usr/bin/env python
# -*- coding: utf-8 -*-
import yaml
from selenium import webdriver

class BulletinBoardPoster:

  def __init__(self, num=0):
    _var = open("../API.yaml").read()
    _yaml = yaml.load(_var)
    self.dr = webdriver.Firefox()
    if num==1:
      _url = _yaml["url_b100"]
      self.form_id = "comment-form"
      self.form_name = "comment"
    if num==2:
      _url = _yaml["url_41"]
      self.form_id = "comment_submit"
      self.form_name = "posting_text"
    else:
      _url = _yaml["url_test"]
      self.form_id = "fcs"
      self.form_name = "MESSAGE"
    self.dr.get(_url)
    self.num = num

  def getHtml(self):
    return self.dr.page_source

  def post(self, text):
    form = self.dr.find_element_by_name(self.form_id)
    self.dr.find_element_by_name(self.form_name).send_keys(text)
    form.submit()

  def main(self):
    _text = "14141"
    print("test post")
    BotforTest = BulletinBoardPoster()
    BotforTest.post(_text)
#    print("prod post1")
#    BotforS7 = BulletinBoardPoster(1)
#    BotforS7.post(_text)
    print("prod post2")
    Botfor41 = BulletinBoardPoster(2)
    Botfor41.post(_text)

if __name__ == "__main__":
#  print(BulletinBoardPoster().getHtml())
  print(BulletinBoardPoster().main())
