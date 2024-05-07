from selenium import webdriver
import time
from datetime import date

# Setup options
options = webdriver.ChromeOptions()
options.add_argument('--headless')

# Locating and Opening ChromeWebDriver
driver = webdriver.Chrome(options=options)

#, https://fltr.com.au/contact-us/, 'https://fltr.com.au/product/000-983-9010-gueldner-filter-replacement/', 'https://tankvent.com.au/contact-us/', https://tankvent.com.au/product/2800i-high-accuracy-tank-servo-level-gauge/, 'https://pipestand.com.au/contact-us/', https://pipestand.com.au/product/82-nm-bench-top-pipe-welding-positioner/, 'https://prpl.com.au/contact-us/', 'https://wa-aed.com.au/contact-us/'
urls = ['https://pipestand.com.au/contact-us/', 'https://pipestand.com.au/product/82-nm-bench-top-pipe-welding-positioner/','https://prpl.com.au/contact-us/', 'https://fltr.com.au/contact-us/', 'https://fltr.com.au/product/msg-manual-bernoulli-filter/',]
#urls =['https://wa-aed.com.au/contact-us/', 'https://prpl.com.au/contact-us/', 'https://fltr.com.au/contact-us/', 'https://fltr.com.au/product/000-983-9010-gueldner-filter-replacement/']
for url in urls:
    # Getting relevant start page
    driver.get(url)
    time.sleep(2)
    contact_block = driver.find_element("xpath", "//*[@id='fl-post-6'] | //div[contains(@class,'fl-module fl-module-pp-gravity-form fl-node-ayb09xcoq2s3 dark-form')] | //div[contains(@class,'pp-gf-inner')]")

    if contact_block:
        print("contact_block found for: ", url)
        text = contact_block.find_element("xpath", "//textarea[@name='input_1'][contains(@id,'1')] | //textarea[contains(@tabindex,'204')] | //textarea[@name='input_1'][contains(@id,'1')]")
        text.send_keys('Automated Testing on '+ str(date.today()) + " : "+ url)

        name = contact_block.find_element("xpath", "//input[@name='input_2'][contains(@id,'2')] | //input[contains(@tabindex,'200')] | //input[@name='input_2'][contains(@id,'2')]")
        name.send_keys('PRPL Test Bot v1.0')

        company = contact_block.find_element("xpath", "//input[@name='input_9'][contains(@id,'9')] | //input[contains(@tabindex,'201')] | //input[@name='input_9'][contains(@id,'9')]")
        company.send_keys('Purple Engineering')

        email = contact_block.find_element("xpath", "//input[@name='input_4'][contains(@id,'4')] | //input[contains(@tabindex,'202')] | //input[@name='input_4'][contains(@id,'4')]")
        email.send_keys('info@prpl.com.au')

        phone = contact_block.find_element("xpath", "//input[@name='input_3'][contains(@id,'3')] | //input[contains(@tabindex,'203')] | //input[@name='input_3'][contains(@id,'3')]")
        phone.send_keys('1300 62 4020')

        contact_block.find_element("xpath", "//input[@type='submit'][contains(@id,'3')] | //input[@type='submit'][contains(@id,'1')]").click()
        time.sleep(5)
        #driver.close()

    else:
        print("contact_block NOT_found for: ", url)

driver.close()
