from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class Scenario:
    def __init__(self, driver=webdriver.Chrome(executable_path='./chromedriver')):
        self.driver = driver
        self.driver.maximize_window()
        self.driver.get("https://www.demoblaze.com/")

    def log_in(self, login, password):
        login_btn = self.driver.find_element(By.XPATH, '/html/body/nav/div[1]/ul/li[5]/a')
        login_btn.click()
        time.sleep(0.5)

        login_ipt = self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/form/div[1]/input')
        login_ipt.send_keys(login)

        password_ipt = self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/form/div[2]/input')
        password_ipt.send_keys(password)
        time.sleep(0.5)

        login_btn_1 = self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[3]/button[2]')
        login_btn_1.click()

    def click_laptops(self):
        time.sleep(1)
        self.driver.refresh()
        time.sleep(1)
        laptop_btn = self.driver.find_element(By.LINK_TEXT, 'Laptops')
        laptop_btn.click()

    def click_dell(self):
        time.sleep(1)
        dell_btn = self.driver.find_element(By.XPATH, '//*[@id="tbodyid"]/div[4]/div/div/h4/a')
        dell_btn.click()

    def add_to_cart(self):
        time.sleep(1)
        add_btn = self.driver.find_element(By.XPATH, '/html/body/div[5]/div/div[2]/div[2]/div/a')
        add_btn.click()

    def go_to_cart(self):
        cart_btn = self.driver.find_element(By.XPATH, '//*[@id="navbarExample"]/ul/li[4]/a')
        cart_btn.click()
        time.sleep(1)

    def place_order(self):
        place_order_btn = self.driver.find_element(By.XPATH, '//*[@id="page-wrapper"]/div/div[2]/button')
        place_order_btn.click()

    def filling_in_the_card_data(self, name, country, city, card, month, year):
        time.sleep(2)
        name_ipt = self.driver.find_element(By.XPATH, '//*[@id="name"]')
        name_ipt.send_keys(name)
        time.sleep(0.5)

        country_ipt = self.driver.find_element(By.XPATH, '//*[@id="country"]')
        country_ipt.send_keys(country)
        time.sleep(0.5)

        city_ipt = self.driver.find_element(By.XPATH, '//*[@id="city"]')
        city_ipt.send_keys(city)
        time.sleep(0.5)

        card_ipt = self.driver.find_element(By.XPATH, '//*[@id="card"]')
        card_ipt.send_keys(card)
        time.sleep(0.5)

        month_ipt = self.driver.find_element(By.XPATH, '//*[@id="month"]')
        month_ipt.send_keys(month)
        time.sleep(0.5)

        year_ipt = self.driver.find_element(By.XPATH, '//*[@id="year"]')
        year_ipt.send_keys(year)
        time.sleep(0.5)

    def purchase_click(self):
        purchase_btn = self.driver.find_element(By.XPATH, '//*[@id="orderModal"]/div/div/div[3]/button[2]')
        purchase_btn.click()

    def check_pop_up_window(self):
        if "Thank you for your purchase!" in self.driver.page_source:
            time.sleep(3)
            self.driver.close()
            self.driver.quit()
            print('Complete')
        else:
            print("purchase not completed")