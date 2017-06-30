#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Module Information
__author__ = "Daniel Barker"
__copyright__ = "Copyright 2017"
__credits__ = ["Daniel Barker"]
__license__ = "GPL"
__version__ = "1.0.0a"
__date__ = "29 June 2017"
__maintainer__ = "Daniel Barker"
__email__ = "dcbark01@gmail.com"
__status__ = "Prototype"

#Global formatting variables
HEADER = '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
SPACER = '===================================================================='
FOOTER = '********************************************************************'

# 1. Import built-in modules
import pandas as pd
import re
import string
import time

# 2. Import third-party modules
from selenium import webdriver

# 3. Import my custom modules


def get_location(driver, row):
    """ Gets the nth row of the HCTRA toll rate schedule. """
    xpath = '//*[@id="travel-tools-rates"]/div/div[3]/div/div/div/table/tbody/tr[' + str(row) + ']/td'
    location = driver.find_elements_by_xpath(xpath)
    loc = location[0].text
    return loc

def get_types(driver, row):
    """ Gets the nth row of the HCTRA toll rate schedule. """
    xpath = '//*[@id="travel-tools-rates"]/div/div[3]/div/div/div/table/tbody/tr[' + str(row) + ']/td'
    t = driver.find_elements_by_xpath(xpath)
    types = t[1].text
    return types

def get_ax2_nontag(driver, row):
    """ Gets the nth row of the HCTRA toll rate schedule. """
    xpath = '//*[@id="travel-tools-rates"]/div/div[3]/div/div/div/table/tbody/tr[' + str(row) + ']/th'
    c = driver.find_elements_by_xpath(xpath)
    costs = c[0].text
    return costs

def get_ax2_eztag(driver, row):
    """ Gets the nth row of the HCTRA toll rate schedule. """
    xpath = '//*[@id="travel-tools-rates"]/div/div[3]/div/div/div/table/tbody/tr[' + str(row) + ']/th'
    cez = driver.find_elements_by_xpath(xpath)
    costs = cez[1].text
    return costs

def get_ax3(driver, row):
    """ Gets the nth row of the HCTRA toll rate schedule. """
    xpath = '//*[@id="travel-tools-rates"]/div/div[3]/div/div/div/table/tbody/tr[' + str(row) + ']/th'
    cez = driver.find_elements_by_xpath(xpath)
    costs = cez[2].text
    return costs

def get_ax4(driver, row):
    """ Gets the nth row of the HCTRA toll rate schedule. """
    xpath = '//*[@id="travel-tools-rates"]/div/div[3]/div/div/div/table/tbody/tr[' + str(row) + ']/th'
    cez = driver.find_elements_by_xpath(xpath)
    costs = cez[3].text
    return costs

def get_ax5(driver, row):
    """ Gets the nth row of the HCTRA toll rate schedule. """
    xpath = '//*[@id="travel-tools-rates"]/div/div[3]/div/div/div/table/tbody/tr[' + str(row) + ']/th'
    cez = driver.find_elements_by_xpath(xpath)
    costs = cez[4].text
    return costs

def get_ax6(driver, row):
    """ Gets the nth row of the HCTRA toll rate schedule. """
    xpath = '//*[@id="travel-tools-rates"]/div/div[3]/div/div/div/table/tbody/tr[' + str(row) + ']/th'
    cez = driver.find_elements_by_xpath(xpath)
    costs = cez[5].text
    return costs

def roadurl_to_string(url):
    """ Converts the HCTRA URL for the toll table to a concatenated string of the road name (for CSV filename). """
    url = url
    u = re.split("=", url)
    u = u[1]
    u = re.split("%20", u)
    clean = []
    for item in u:
        s = item.strip(string.punctuation)
        clean.append(s)
    road_name = ""
    for k in clean:
        road_name += k
    return road_name

def direction_to_string(direction):
    """ Converts the direction to a concatenated string (for CSV filename). """
    direction = re.split(" ", direction)
    direct_str = ""
    for d in direction:
        direct_str += d
    return direct_str


if __name__ == "__main__":
    """
    ---------------------------- USER INPUTS -----------------------
    """
    # Input URL and direction here. Comment out undesired roads
    # TO DO: Loop through a dictionary of URLs and directions

    # Sam Houston Tollway
    url = "https://www.hctra.org/TollRates?tollRoad=Sam%20Houston%20Tollway"
    direction = "Clockwise"
    # direction = "Counter Clockwise"

    # Hardy Toll Road
    # url = "https://www.hctra.org/TollRates?tollRoad=Hardy%20Toll%20Road"
    # direction = "North"
    # direction = "South"

    # Westpark Tollway
    # url = "https://www.hctra.org/TollRates?tollRoad=Westpark%20Tollway"
    # direction = "East"
    # direction = "West"

    # Ft. Bend Extension
    # url = "https://www.hctra.org/TollRates?tollRoad=Ft.%20Bend%20Extension"
    # direction = "North"
    # direction = "South"

    # Tomball Tollway
    # url = "https://www.hctra.org/TollRates?tollRoad=Tomball%20Tollway"
    # direction = "North"
    # direction = "South"

    # SH 242
    # url = "https://www.hctra.org/TollRates?tollRoad=SH%20242"
    # direction = "Off Peak hours"
    # direction = "Peak hours"

    """
    --------------------------- END USER INPUTS --------------------
    """
    print(HEADER)
    print('HCTRA Toll Rate Web Scraper')
    print(__author__)
    print(__copyright__)
    print(__license__)
    print(__version__)
    print(HEADER)
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="directionSelect"]').click()
    time.sleep(1)
    dxp1 = "//*[contains(text(), '"
    dxp2 = "')]"
    direction_xpath = dxp1 + direction + dxp2
    driver.find_element_by_xpath(direction_xpath).click()
    time.sleep(1)
    #driver.find_element_by_xpath("//*[contains(text(), 'Clockwise')]").click()
    table = driver.find_elements_by_xpath('//*[@id="travel-tools-rates"]/div/div[3]/div/div/div/table/tbody/tr')

    # Get the number of rows in the table
    tolls = []
    for i in table:
        row = i.text
        print(row)
        tolls.append(row)
    row_count = len(tolls)
    print('Number of rows = ' + str(row_count) + '\n')

    # Now scrape each row of data into lists
    locations = []
    types = []
    ax2_nontags = []
    ax2_eztags = []
    ax3_list = []
    ax4_list = []
    ax5_list = []
    ax6_list = []
    for j in range(row_count):
        j = j + 1
        loc = get_location(driver=driver, row=j)
        locations.append(loc)

        tp = get_types(driver=driver, row=j)
        types.append(tp)

        ax2_nontag = get_ax2_nontag(driver=driver, row=j)
        ax2_nontags.append(ax2_nontag)

        ax2_eztag = get_ax2_eztag(driver=driver, row=j)
        ax2_eztags.append(ax2_eztag)

        ax3 = get_ax3(driver=driver, row=j)
        ax3_list.append(ax3)

        ax4 = get_ax4(driver=driver, row=j)
        ax4_list.append(ax4)

        ax5 = get_ax5(driver=driver, row=j)
        ax5_list.append(ax5)

        ax6 = get_ax6(driver=driver, row=j)
        ax6_list.append(ax6)

    loc_df = pd.DataFrame(locations)
    loc_df.columns = ['Location']
    tp_df = pd.DataFrame(types)
    tp_df.columns = ['Type']
    ax2_nontag_df = pd.DataFrame(ax2_nontags)
    ax2_nontag_df.columns = ['2 Axles Cash / Non-Tag']
    ax2_eztags_df = pd.DataFrame(ax2_eztags)
    ax2_eztags_df.columns = ['2 Axles EZ TAG']
    ax3_df = pd.DataFrame(ax3_list)
    ax3_df.columns = ['3 Axles']
    ax4_df = pd.DataFrame(ax4_list)
    ax4_df.columns = ['4 Axles']
    ax5_df = pd.DataFrame(ax5_list)
    ax5_df.columns = ['5 Axles']
    ax6_df = pd.DataFrame(ax6_list)
    ax6_df.columns = ['6 Axles']

    results = pd.concat([loc_df,
                         tp_df,
                         ax2_nontag_df,
                         ax2_eztags_df,
                         ax3_df,
                         ax4_df,
                         ax5_df,
                         ax6_df], axis=1)
    # Create filename for CSV file
    filename_road = roadurl_to_string(url)
    filename_direction = direction_to_string(direction)
    filename = "Tolls_" + filename_road + "_" + filename_direction + ".csv"
    results.to_csv(filename)
    print(FOOTER)
    print('Program complete and results printed to .csv file!')
    print(FOOTER)


