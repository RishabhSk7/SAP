from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from selenium.webdriver.support.wait import WebDriverWait
from HTML_TABLE_PARSER import table_to_list

def do_do(driver):
    driver.find_element(by=By.ID, value="WD0220").click()

    def switch_tab():
        try:
            driver.switch_to.window(driver.window_handles[1])   
        except:
            print("Tab switch falied, trying again")
            switch_tab()
    switch_tab()

    check2 = WebDriverWait(driver, timeout=20).until(lambda d: d.find_element(By.ID,value="WD21-caption"))
    assert check2.text == "Navigate to Print"
    print("YUP, switched tabs")

    table = driver.find_element(by=By.ID, value="WD2B-contentTBody")
    soup=BeautifulSoup(table.get_attribute('innerHTML'), 'html.parser')
    print(table.get_attribute('innerHTML'))
    # for i in soup.find_all(["td"]):
    #     #print(i, "\n")
    #     tag=BeautifulSoup(str(i), 'html.parser')
    #     #tag = str(tag).split("\n")
    #     schedule=[]
    #     if "Module" in str(tag.get_text()) and bool(str(tag.get_text())) != False:schedule.append(str(tag.get_text()))
    #     print(len(schedule))
    #     print(schedule)