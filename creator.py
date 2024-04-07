from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select
import generator as gen


def find_otp(mail):
    numbers = ["0","1","2","3","4","5","6","7","8","9"]
    otp = ""
    for a in mail:
        if a in numbers:
            otp += a
    return otp
#
with open("prox.txt", "r") as file:
     prox = file.readlines()
     proxies = [ip.split("\n")[0] for ip in prox]
#
  for proxyIP_PORT in proxies:
           # Define proxy settings
    chrome_options = webdriver.ChromeOptions()
  #         # Set proxy options
    proxy = proxyIP_PORT
    chrome_options.add_argument(f"--proxy-server={proxy}")
    run = True
    while run:
    
        # Instantiate Chrome WebDriver with ChromeOptions
        DRIVER1 = webdriver.Chrome()
        DRIVER1.set_window_size(300, 900)
        DRIVER1.set_window_position(750,0,"current")
        DRIVER2 = webdriver.Chrome()
        DRIVER2.set_window_size(300, 900)
        DRIVER2.set_window_position(300, 0, "current")
        # variables sets
        USERNAME = gen.username()
        NAME = gen.firstName()
        PASSWORD = "#############" # use your own password
        DAY = str(gen.day())
        MONTH = str(gen.month())
        YEAR = str(gen.year())
        EMAIL = USERNAME + "@outlook.com"
            ################
            # Open Hotmail sign-up page
        DRIVER2.get("https://signup.live.com")
                # Fill in the registration form
                ############# E_MAIL ############################
        email_found = False
        while not email_found:
            try:
                switch = DRIVER2.find_element(By.ID, "liveSwitch")
                switch.click()
                email_input = DRIVER2.find_element(By.TAG_NAME, "input")
                email_input.send_keys(USERNAME)
                f_next = DRIVER2.find_element(By.ID, "iSignupAction")
                email_found = True
            except:
                pass
            else:
                time.sleep(1)
                f_next.click()
                ################ PASSWORD ##########################
        password_found = False
        while not password_found:
            try:
                pass_input = DRIVER2.find_element(By.ID, "PasswordInput")
                pass_input.send_keys(PASSWORD)
                s_next = DRIVER2.find_element(By.ID, "iSignupAction")
                password_found = True
            except:
                pass
            else:
                time.sleep(1)
                s_next.click()
                ############## NAME ################################
        names_found = False
        while not names_found:
            try:
                first_name_input = DRIVER2.find_element(By.ID, "FirstName")
                first_name_input.send_keys(gen.firstName())
                last_name_input = DRIVER2.find_element(By.ID, "LastName")
                last_name_input.send_keys(gen.firstName())
                t_next = DRIVER2.find_element(By.ID, "iSignupAction")
                time.sleep(1)
                t_next.click()
                names_found = True
            except:
                pass
                ############## DATE OF BIRTH ##########################
        date_found = False
        while not date_found:
            try:
                day_select = Select(DRIVER2.find_element(By.ID, 'BirthDay'))
                day_select.select_by_value(DAY)
                month_select = Select(DRIVER2.find_element(By.ID, 'BirthMonth'))
                month_select.select_by_value(MONTH)
                year_select = DRIVER2.find_element(By.ID, 'BirthYear')
                year_select.send_keys(YEAR)
                x_next = DRIVER2.find_element(By.ID, "iSignupAction")
                time.sleep(1)
                x_next.click()
                time.sleep(2)
                date_found = True
            except:
                pass
                ###################### until captcha ##############################
        captcha_done = False
                ###################### after captch ###############################
        while not captcha_done:
            try:
                okButtom = DRIVER2.find_element(By.ID, "id__0")
                okButtom.click()
                time.sleep(1)
                okButtom.click()
                captcha_done = True
            except:
                pass
        email_done = False
        while not email_done:
            try:
                yesBottom = DRIVER2.find_element(By.ID, "acceptButton")
                time.sleep(1)
                yesBottom.click()
                email_done = True
            except:
                pass
                ###################################################################
            # Navigate to Instagram signup page
        DRIVER1.get('https://www.instagram.com/accounts/emailsignup/')
        instagram_open = False
        while not instagram_open:
            try:
                        # Locate and fill in the signup fields
                time.sleep(5)
                email_input = DRIVER1.find_element(By.NAME, 'emailOrPhone')
                fullname_input = DRIVER1.find_element(By.NAME, 'fullName')
                username_input = DRIVER1.find_element(By.NAME, 'username')
                password_input = DRIVER1.find_element(By.NAME, 'password')
                submit_button = DRIVER1.find_element(By.CSS_SELECTOR, 'button[type="submit"]')   # Submit the form
            except:
                pass
            else:
                email_input.send_keys(EMAIL)
                fullname_input.send_keys(NAME)
                username_input.send_keys(USERNAME)
                password_input.send_keys(PASSWORD)
                time.sleep(1)
                submit_button.click()
                instagram_open = True
        birth_found = False  # Wait for signup process to complete
        while not birth_found:
            try:
                        # Handle age verification page using title attribute
                day_select = Select(DRIVER1.find_element(By.XPATH, '//*[@title="Day:"]'))
                day_select.select_by_value(DAY)
                month_select = Select(DRIVER1.find_element(By.XPATH, '//*[@title="Month:"]'))
                month_select.select_by_value(MONTH)
                year_select = Select(DRIVER1.find_element(By.XPATH, '//*[@title="Year:"]'))
                year_select.select_by_value(YEAR)
                next_button = DRIVER1.find_element(By.XPATH, "//button[contains(text(), 'Next')]")   # Submit age verification
                time.sleep(1)
                next_button.click()
                birth_found = True
            except:
                pass
                # Wait for verification process to complete
            ######################## open mailbox #############################
        DRIVER2.get("https://outlook.live.com/mail/0/")
        find = False
        otp = ""
        while not find:
            try:
                instaMail = DRIVER2.find_element(By.XPATH, "//*[contains(text(), 'Instagram code')]")
            except:
                pass
            else:
                otp = find_otp(instaMail.text)
                find = True
                print(otp)
        verify = False
        while not verify:
            try:
                otpIN = DRIVER1.find_element(By.NAME, "email_confirmation_code")
            except:
                pass
            else:
                time.sleep(2)
                otpIN.send_keys(otp)
                nextButton = DRIVER1.find_element(By.XPATH, "//*[contains(text(), 'Next')]")
                time.sleep(1)
                nextButton.click()
                time.sleep(20)
                verify = True
                DRIVER2.quit()
                DRIVER1.quit()
    
            ################### account append in text file ##############
        with open("accounts.txt", "a") as file:
            account = f"{USERNAME}:{PASSWORD}:{EMAIL}:{PASSWORD}\n"
            file.write(account)
            ######################### END ################################
    
