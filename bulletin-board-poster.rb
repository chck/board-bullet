#!/usr/bin/ruby
# -*- coding: utf-8 -*-

require 'rainbow'
require 'mechanize'
require 'yaml'

class BulletinBoardPoster
  def initialize(num=0)
    conf = YAML::load(open("../API.yaml"))
    if num==1
      @url = conf["url_72"]
      @form_id = "comment_submit"
      @form_field = "js_comment_body"
    elsif num==2
      @url = conf["url_b100"]
      @form_id = "comment-form"
      @form_field = "comment"
    else
      @url = conf["url_test"]
      @form_id = "fcs"
      @form_field = "MESSAGE"
    end
    @agent = Mechanize.new
    @num = num
  end

  def post(text)
    @agent.get(@url) do |page|
      response = page.form_with(:id => @form_id) do |form|
        form.field_with(:id => @form_field).value = text
      end.submit
      puts Rainbow(response).magenta.bright
    end
  end

#  def main
#    text = "14141"
#    bot_for_b100 = BulletinBoardPoster.new(2)
#    bot_for_b100.post(text)
#  end
end

bot_for_b100 = BulletinBoardPoster.new(2)
bot_for_b100.post("14141")
