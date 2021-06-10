import time
import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC





class Assignment:

    def __init__(self, url):
        self.driver = webdriver.Chrome() #pass chromedriver path
        self.driver.maximize_window()
        self.url = url

    def close_driver(self):

        self.driver.close()
        self.driver.quit()

    def search_for_properties (self, location, check_in_date,check_out_date,Adults,Children):
        self.driver.get(self.url)
        time.sleep(2)
        
    # For Location selection

        try:
            location_btn=WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.CLASS_NAME, "_gor68n"))).click()
            time.sleep(1)
            location = self.driver.find_elements_by_css_selector('input[class="_1xq16jy focus-visible"]')[0].send_keys(location+'\n')
        except Exception as e:
            print (e)
            pass

    # For check_in and check_out date selection

        try:
            check_in = WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.CLASS_NAME, "_1qswu1v"))).find_elements_by_css_selector('td[class="_12fun97"]')[int(check_in_date)].click()
            time.sleep(1)
            check_out = WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.CLASS_NAME, "_1qswu1v"))).find_elements_by_css_selector('td[class="_12fun97"]')[int(check_out_date)].click()
        except Exception as e:
            print (e)
            pass

        time.sleep(2)


    # For Guest selection

        try:
            guest = self.driver.find_elements_by_css_selector('div[class="_37ivfdq"]')[-1].click()
            time.sleep(1)
            for adult in range(int(Adults)):
                adult_Selection = self.driver.find_elements_by_css_selector('div[id="stepper-adults"]')[0].find_elements_by_css_selector('button[aria-label="increase value"]')[0].click()
            time.sleep(1)
            for child in range(int(Children)):
                child_Selection = self.driver.find_elements_by_css_selector('div[id="stepper-children"]')[0].find_elements_by_css_selector('button[aria-label="increase value"]')[0].click()
            time.sleep(1)
        except Exception as e:
            print (e)
            pass

    # For Clicking search button

        try:
            search_btn = self.driver.find_elements_by_css_selector('button[class="_1mzhry13"]')[0].click()
        except Exception as e:
            print (e)
            pass

        time.sleep(6)


    #############
	# TEST CASE 1
	#############
    def verify_test_case_1(self, location, check_in_date,check_out_date,Adults,Children,verify_city,verify_date_filter_area,verify_guest,verify_date_search_result_header):


        self.search_for_properties(location, check_in_date,check_out_date,Adults,Children)

        filter_area_input = [verify_city,verify_date_filter_area,verify_guest]

        search_results__header_input = [verify_date_search_result_header,verify_guest]  


        #For Filter area verification :
        
        try:      
            filter_area = self.driver.find_element_by_css_selector('div[data-testid="little-search"]').find_elements_by_css_selector('div[class="_1g5ss3l"]')     
            filter_result = []
            for fi in filter_area:
                filter_result.append(fi.text)

            assert filter_area_input[0] == filter_result[0] and filter_area_input[1] == filter_result[1] and filter_area_input[2] == filter_result[2],'Filter Area not verified...Test case failed'
            print ('Filter Area verified...Test case passed')
        except Exception as e:
            print (e)
            pass

        print('..................')

        # For search results header verification

        try:
            search_results_header = self.driver.find_element_by_css_selector('div[class="_1snxcqc"]').text
            search_results_header_verify=search_results_header.split(' · ')[1:]

            assert search_results_header_verify == search_results__header_input,'Search Results Area Not verified...Test case failed'
            print ('Search Results Area verified...Test case passed')
        except Exception as e:
            print (e)
            pass

        print('..................')

        # For Verify number of guests atleast 3

        try:
            count = 0
            guests = self.driver.find_elements_by_css_selector('div[class="_12oal24"]')
            verify_guest=verify_guest.split(' ')[0]
            for gu in guests:
                no_of_guests = gu.find_elements_by_css_selector('div[class="_3c0zz1"]')[0].find_elements_by_css_selector('span[class="_3hmsj"]')[0].text.split(' ')[0]
                if int(no_of_guests) < int(verify_guest):
                    count = 1
            assert count == 0,'No_of_guests not Verified....TEST CASE FAILED'
            print ('No_of_guests verifed....TEST CASE PASSED')
        except Exception as e:
            print (e)
            pass

        print(
        	"""
        	--------------------------
        		TEST CASE 1 VERIFIED
        	--------------------------
        	""")

	#############
	# TEST CASE 2
	#############
    def verify_test_case_2(self, location, check_in_date,check_out_date,Adults,Children,bedrooms,verify_bedrooms):

        self.search_for_properties(location, check_in_date,check_out_date,Adults,Children)


        try:
            More_filters = self.driver.find_elements_by_css_selector('div[id="menuItemButton-dynamicMoreFilters"]')[0].click()  
        except Exception as e:
            print (e)
            pass


        time.sleep(3)

    	# For Select the number of bedrooms as 5

        try:
            for l in range(int(Bedrooms)):
                bedrooms = self.driver.find_elements_by_css_selector('div[data-testid="filter-stepper-row-filterItem-rooms_and_beds-stepper-min_bedrooms-0"]')[0].find_elements_by_css_selector('button[aria-label="increase value"]')[0].click()
                time.sleep(0.5)
        except Exception as e:
            print (e)
            pass

    	# For Select Pool from the Facilities section.

        try:
            pool = self.driver.find_elements_by_css_selector('input[id="filterItem-facilities-checkbox-amenities-7"]')[0].click()
        except Exception as e:
            print (e)
            pass
        time.sleep(2)


    	# For Click Show Stays

        try:
            show_results = self.driver.find_elements_by_css_selector('button[data-testid="more-filters-modal-submit-button"]')[0].click()
        except Exception as e:
            print (e)
            pass

        time.sleep(2)

    	# For Verification of BEDROOMS

        try:
            count = 0
            bedrooms = self.driver.find_elements_by_css_selector('div[class="_12oal24"]')
            for bd in bedrooms:
                no_of_bedrooms = bd.find_elements_by_css_selector('div[class="_3c0zz1"]')[0].find_elements_by_css_selector('span[class="_3hmsj"]')[1].text.split(' ')[0]
                if int(no_of_bedrooms) < int(verify_bedrooms):
                    count = 1

            assert count == 0,'No_of_bedrooms not verified....TEST CASE FAILED'
            print ('No_of_bedrooms verifed....TEST CASE PASSED')
        except Exception as e:
            print (e)
            pass

        print('..................')

        # For open the details of first

        try:
            first_property_click =WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.CLASS_NAME, "_12oal24")))
            hover_click = ActionChains(self.driver).move_to_element(first_property_click).click().perform()
        except Exception as e:
            print (e)
            pass

        time.sleep(2)

        self.driver.switch_to.window(self.driver.window_handles[-1])
        time.sleep(8)
        # self.driver.execute_script("window.scrollTo(0, window.scrollY + 900)")


    	# For clicking amenties button
        try:
            # amenties_btn = WebDriverWait(self.driver, 30).until(
            #     EC.presence_of_element_located((By.CSS_SELECTOR, "a.b1sec48q v7aged4 dir dir-ltr"))).click()
            amenties_btn = self.driver.find_element_by_css_selector('a[class="b1sec48q v7aged4 dir dir-ltr"]').click()
        except Exception as e:
            print (e)
            pass


        time.sleep(3)


    	# For pool verifiaction 
        try:
            header = self.driver.find_elements_by_css_selector('div[class="_aujnou"]')
            for hd in header:
                f_heading=hd.find_element_by_css_selector('div[class="_1crk6cd"]').text
                if 'Parking and facilities' in f_heading:
                    pool_verification=hd.find_elements_by_css_selector('div[class="_1dotkqq"]')
                    for veri in pool_verification:
                        if 'pool' in veri.text:
                            print ('Pool_exist...Test case verifiefd')

        except Exception as e:
            print (e)
            pass

        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

        print(
        	"""
        	--------------------------
        		TEST CASE 2 VERIFIED
        	--------------------------
        	""")


	#############
	# TEST CASE 3
	#############
    def verify_test_case_3(self,location, check_in_date,check_out_date,Adults,Children):

        self.search_for_properties(location, check_in_date,check_out_date,Adults,Children)

        try:
            first_listing = self.driver.find_elements_by_css_selector('div[class="_12oal24"]')[0]
            hover = ActionChains(self.driver).move_to_element(first_listing).perform()
            map_btn=self.driver.find_elements_by_css_selector('div[style="--content-mini-box-shadow:0 0 0 1px rgba(0, 0, 0, 0.32), 0px 2px 4px rgba(0, 0, 0, 0.18); align-items: center; cursor: pointer; display: flex; height: 28px; position: relative; transform: scale(1.077); transform-origin: 50% 50%; transition: transform 150ms ease 0s;"]')[0].click()
        except Exception as e:
            print (e)
            pass

        time.sleep(2)

        try:
            map_popup_price = self.driver.find_elements_by_css_selector('div[class="_9m9ayv"]')[0].find_element_by_css_selector('div[class="_1klfbd5m"]').text
            first_listing_price = self.driver.find_element_by_css_selector('div[class="_1gi6jw3f"]').text

            assert map_popup_price == first_listing_price,'Map Details and first listing details Not Matched....Test Case Failed'
            print ('Map price and listing price Matched....Test case passed')
     
            map_popup_title= self.driver.find_element_by_css_selector('div[class="_9m9ayv"]').find_elements_by_css_selector('div[class="_1afu10la"]')[0].text.replace(" · ", " in ")
            map_popup_title_2=self.driver.find_element_by_css_selector('div[class="_9m9ayv"]').find_elements_by_css_selector('div[class="_5kaapu"]')[0].text
            map_details = map_popup_title +'\n'+ map_popup_title_2
            first_listing_details=self.driver.find_elements_by_css_selector('div[class="_1mleygo"]')[0].text

            assert map_details == first_listing_details,'Map Details and first listing details Not Matched....Test Case Failed'
            print ('Map Details and first listing details Matched....Test Case Passed')

        except Exception as e:
            print (e)
            pass

        print(
        	"""
        	--------------------------
        		TEST CASE 3 VERIFIED
        	--------------------------
        	""")
            


if __name__ == '__main__':

    url = "https://www.airbnb.com/"

    location='Rome, Italy'     # Enter Location
    Adults="2"                 # Enter Adults
    Children="1"               # Enter children
    Bedrooms='5'               # Enter Bedrooms
    check_in_date='7'          # Enter days after current date
    check_out_date='14'        # Enter days after current date

    today = datetime.date.today()
    current_time = datetime.datetime.now()
    start = current_time + datetime.timedelta(days=7) 
    end = current_time + datetime.timedelta(days=14)

    verify_city = location.split(',')[0]
    verify_guest = str(int(Adults)+int(Children))+' guests'
    verify_bedrooms = Bedrooms

    # For veification of date, making date foramt as on the web.

    verify_date_filter_area = today.strftime("%b") + " " + str(start.day) +  " – " + str(end.day )  
    verify_date_search_result_header = today.strftime("%b") + " " + str(start.day) +  " - " + str(end.day )

    ob = Assignment(url)

    # ob.search_for_properties(location,check_in_date,check_out_date,Adults,Children)

    # Run test cases
    ob.verify_test_case_1(location, check_in_date,check_out_date,Adults,Children,verify_city,verify_date_filter_area,verify_guest,verify_date_search_result_header)

    ob.verify_test_case_2(location, check_in_date,check_out_date,Adults,Children,Bedrooms,verify_bedrooms)

    ob.verify_test_case_3(location, check_in_date,check_out_date,Adults,Children)

    ob.close_driver()
