from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random
import time

def getRandomTopic():
    """
    Return a random topic from topic list

    Args:
        NONE
    Returns:
        Topic (string)
    """
    topics = ['Microsoft', 'Google', 'Yahoo', 'Cute Dogs', 'Cute Cats', 'Cheese Platter', 'Tesla', 'Elon Musk', 'Apple Tech', 'Tim Cook', 'Scooby Doo', 'Black Lives Matter']
    return topics[int(len(topics) * random.random())]

def googleSignIn(usr,pw):
    """
    Sign into gmail via Udemy

    Args:
        usr: gmail username (string)
        pw: gmail password (string)
    Returns:
        NONE
    """
    driver.get('https://www.udemy.com/join/login-popup/?locale=en_US&response_type=html&next=https%3A%2F%2Fwww.udemy.com%2F%3Futm_source%3Dadwords-brand%26utm_medium%3Dudemyads%26utm_campaign%3DBrand-Udemy_la.EN_cc.US%26utm_term%3D_._ag_78616515599_._ad_389436697904_._de_c_._dm__._pl__._ti_kwd-310556426868_._li_9004426_._pd__._%26utm_term%3D_._pd__._kw_udemy_._%26matchtype%3De%26gclid%3DEAIaIQobChMI34un_Zat6wIVga_ICh2XrwQ1EAAYASAAEgKmr_D_BwE')
    signIn = driver.find_element_by_class_name('google-auth--social-btn--google--1H6_f')
    signIn.click()
    beforeWindow = driver.window_handles[0]
    gmailWindow = driver.window_handles[1]
    # first page actions
    driver.switch_to.window(gmailWindow)
    driver.find_elements_by_id('identifierId')[0].send_keys(usr)
    driver.find_elements_by_id('identifierNext')[0].click()
    # second page actions
    time.sleep(1)
    driver.find_elements_by_tag_name('input')[2].send_keys(pw)
    driver.find_elements_by_tag_name('button')[1].click()
    time.sleep(1)
    driver.switch_to.window(beforeWindow)
    pass

def googleSearch():
    """
    Search a topic on google, open a random result on the first page, and scroll around
    Args:
        NONE
    Returns:
        NONE
    """
    driver.get('https://google.com')
    search = driver.find_element_by_name('q')
    search.send_keys(getRandomTopic())
    search.send_keys(Keys.RETURN)
    time.sleep(10)
    results = driver.find_elements_by_xpath("//div[contains(@class, 'g') and not (@class='kno-kp')]//div[@class='rc']/div[@class='r']/a")
    # remove empty links
    searchRes = list(filter(lambda x: len(x.text)!= 0, results))
    res = searchRes[int(len(searchRes) * random.random())]
    res.click()
    #scroll around
    time.sleep(3)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight/2);")
    time.sleep(3)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight/3);")
    time.sleep(3)
    driver.execute_script("window.scrollTo(0, 0);")
    time.sleep(3)
    pass 

def youtubeSearch():
    driver.get("https://youtube.com")
    # search topic
    search = driver.find_element_by_xpath("//input[@id='search']")
    search.send_keys(getRandomTopic())
    search.send_keys(Keys.RETURN)
    # select video
    results = driver.find_elements_by_id('video-title')[0:10]
    vid = results[int(len(results) * random.random())]
    vid.click()
    time.sleep(5)

def main():
    global driver
    driver = webdriver.Chrome()
    # googleSignIn('username','password')
    # googleSearch()
    youtubeSearch()
    time.sleep(20)
    driver.close()  

main()