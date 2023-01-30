#import stuff
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time
from timetable import do_do
import sys

#creating driver and assuring correct webpage
driver = webdriver.Firefox()
driver.get("https://myupes.upes.ac.in/Login")
assert "UPES" in driver.title

#Enter credentials into login site
UID = driver.find_element(by=By.ID, value="email")
UID.send_keys("Rishabh.105035@stu.upes.ac.in")
Password = driver.find_element(by=By.ID, value="Pwd")
Password.send_keys("Jul82160")
submit_button = driver.find_element(by=By.TAG_NAME, value="button")
submit_button.click()

# check if Logged in
check = driver.find_element(By.LINK_TEXT, "SAP Portal")
print(check.text == "SAP Portal")

#get current tab id
original_window = driver.current_window_handle
print(original_window)

#enter sap portal
driver.find_element(by=By.LINK_TEXT, value="SAP Portal").click()
sap = driver.find_element(by=By.ID, value="btnmySAPPortal")
driver.execute_script("window.stop();")
sap.click()

#NOTE remove previous tab
while True:
    try:
        time.sleep(1)
        new_win = driver.window_handles[1]
        driver.close()
        driver.switch_to.window(new_win)
        print(driver.current_window_handle)
        break
    except:
        pass

#wait till SAP portal is finished processing
def check_loading():
    try:
        WebDriverWait(driver, timeout=5).until(lambda d: d.find_element(By.XPATH,"//*[contains(text(), 'Timetable')]"))
        print("done!")
    except:
        print("taking some time")
        check_loading()
check_loading()

#Open timetable window
do_do(driver)

## assert "No results found." not in driver.page_source
## driver.close()

#RR = https://sappro.upes.ac.in:8443/sap/bc/webdynpro/sap/zupes_student_portal?LOGIN_PARAM=MTEyMDA1MDAxMDUwMzU=#
#KK = https://sappro.upes.ac.in:8443/sap/bc/webdynpro/sap/zupes_student_portal?LOGIN_PARAM=MTEwNDA1MDAxMDgwMjk=#