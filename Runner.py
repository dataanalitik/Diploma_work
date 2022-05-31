from Task import Scenario


login = 'RT'
password = 'Passw_2022'
name = 'Roman'
country = 'Ukraine'
city = 'Kyiv'
card = '1234 5678 9012 3456'
month = 'May'
year = '2024'


if __name__ == "__main__":
    s = Scenario()
    s.log_in(login, password)
    s.click_laptops()
    s.click_dell()
    s.add_to_cart()
    s.go_to_cart()
    s.place_order()
    s.filling_in_the_card_data(name, country, city, card, month, year)
    s.purchase_click()
    s.check_pop_up_window()
