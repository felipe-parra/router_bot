#!/usr/bin/env python

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

from secrets import username, password, hostname, reboot

class RouterBot():
  def __init__(self):
    self.driver = webdriver.Chrome()

  def login(self):
    self.driver.get(hostname)
    
    sleep(5)

    btn_cfg = self.driver.find_element_by_xpath('//*[@id="settings"]')
    btn_cfg.click()
    
    user_in = self.driver.find_element_by_xpath('//*[@id="username"]')
    user_in.send_keys(username)
    user_in.send_keys(Keys.ENTER)
    
    ps_in = self.driver.find_element_by_xpath('//*[@id="password"]')
    ps_in.send_keys(password)
    ps_in.send_keys(Keys.ENTER)
    
    login_btn = self.driver.find_element_by_xpath('//*[@id="pop_login"]')
    login_btn.click()
    base_window = self.driver.window_handles[0]

    self.driver.switch_to_window(base_window)
    self.driver.get(reboot)
    sleep(5)
    btn_reboot = self.driver.find_element_by_xpath('//*[@id="undefined"]')
    btn_reboot.click()

    btn_acept_reboot = self.driver.find_element_by_xpath('//*[@id="pop_confirm"]')
    btn_acept_reboot.click()


if __name__ == "__main__":
    bot = RouterBot()
    bot.login()

