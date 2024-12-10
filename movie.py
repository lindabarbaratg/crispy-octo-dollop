from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from supabase import create_client, Client
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import csv
import string
import random
import os
from tmdbv3api import TMDb
from tmdbv3api import Movie


SUPABASE_URL = "https://cqakrownxujefhtmsefa.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImNxYWtyb3dueHVqZWZodG1zZWZhIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MzIyNjMyMzMsImV4cCI6MjA0NzgzOTIzM30.E9jJxNBxFsVZsndwhsMZ_2hXaeHdDTLS7jZ50l-S72U"
SUPABASE_TABLE_NAME = "movie"
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)


def random_string(count):
    string.ascii_letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    return "".join(random.choice(string.ascii_letters) for x in range(count))


EMAIL = "sonia_levine@gdrive.or.id"
PASSWORD = "Cobasih12#"

def web_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--verbose")
    # options.add_argument('--no-sandbox')
    # options.add_argument('--headless')
    options.add_argument("--disable-gpu")
    # options.add_argument("--window-size=1920, 1200")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=options)
    return driver

driver = web_driver()
driver.maximize_window()


driver.get("https://accounts.google.com/signin")


email_field = driver.find_element(By.ID, "identifierId")
email_field.send_keys(EMAIL)
email_field.send_keys(Keys.ENTER)
time.sleep(10)


password_field = driver.find_element(By.CSS_SELECTOR, "input[name='Passwd']")
password_field.send_keys(PASSWORD)
password_field.send_keys(Keys.ENTER)
time.sleep(10)



driver.get("https://www.wikiart.org/")
time.sleep(2)


driver.find_element(By.CSS_SELECTOR, "b[class='ng-binding']").click()
time.sleep(2)   

driver.find_element(By.CSS_SELECTOR,"button[value='google']").click()
time.sleep(10)
print("Selesai Login")

with open('id.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for line in csv_reader:
        tmdb = TMDb()
        tmdb.api_key = 'ce7dc231f477c13ba0789c8de9268db4'
        tmdb.language = 'en-US'
        movie = Movie()
        kw = line[0]

        
        m = movie.details(line[0])
        poster_path = m.poster_path

        
        year = m.release_date[0:4]
        poster = 'https://image.tmdb.org/t/p/w185/'+poster_path
        link   ='https://app.geoflix.me/movie/'+line[0]+'?ref=wikiArt'
        title  =m.title
        # overview = m.overview
        original = m.original_title


        try:


            

            judul = f"**{title} ({year}) Tamil/Hindi Movie Download Free Dual Audio 1080p HD"
                        
                        
            driver.get("https://www.wikiart.org/en/edit/john-constable/new")
            time.sleep(10)

            file_input = driver.find_element(By.CSS_SELECTOR, "label.upload-button input[type='file']")

            # Path file yang akan diunggah
            file_path = "as.png"
            file_path = os.path.abspath(file_path) 

            # Kirim path file ke input file untuk mengunggahnya
            file_input.send_keys(file_path)

            time.sleep(5)



            driver.find_element(By.CSS_SELECTOR, "input[placeholder='Empty field'][name='PaintingName']").send_keys(judul)
            time.sleep(3)         

            konten = f"*Filmyzilla! {title} ({year}) .FullMovie. Free Download Full4K HINDI Dubbed Mp4moviez \n \n 33secs ago - Downloading or Watching01 ~ {title} movie download in hindi mp4moviez 480p filmyzilla \n \n [url href={link}]CLICK HERE >> {title} ({year}) FullMovie [/url] \n \n [url href={link}] CLICK HERE >> {title} - The Rule ({year}) FullMovie [/url] \n \n \n {title} The Rule Movie Release Live Updates: Three years back when Pushpa 1 hit the screens not many could predict the kind of impact it would have on Indian cinema. The film about the rise of a gutsy nobody to the top echelons of a smuggling syndicate found resonance across the country. Among its many box-office achievements Pushpa also made history by making Allu Arjun the first male Telugu actor to receive a National Award for Best Actor. In fact in an interview on Nandamuri Balakrishna’s Unstoppable with NBK Allu Arjun spoke about how it was very distressing to not see a single male Telugu actor’s name in the Best Actor list and Pushpa’s role in making history. Finally the journey that started in December 2021 will come full circle this December as {title}: The Rule is set to hit theatres on Thursday. \n \n Despite various controversies surrounding {title} including a purported tiff between director Sukumar and Allu Arjun and a public spat between composer Devi Sri Prasad and producers Mythri Movie Makers the film has been completed and is gearing up for a blockbuster opening. Major credit to the hype surrounding the film has to go to the intense promotional drive spearheaded by Allu Arjun and Rashmika Mandanna. They kept the movie in the news for the past couple of weeks by relentless promotions in cities like Patna Kochi Chennai Hyderabad and Mumbai. \n \n \n Related Search : \n \n {title} (.Tamil.) Fullmovie Filmyzilla Download Free 720p 480p HD \n {title} full movie watch online hd dailymotion \n {title} ({year}) Hindi Dubbed Hdhub4u \n {title} full movie watch online free hd dailymotion \n {title} full movie watch online hd 720p \n {title} (Free) Fullmovie Download Free 720p 480p 1080p HD \n WATCH**{title} ({year}) FuLLMovie Free Online Hindi Dubbed \n {title} hindi dubbed download filmyzilla \n {title} ({year}) Tamil Dubbed Movie Download Isaimini \n {title} movie download in english filmyzilla \n {title} movie download in hindi mp4moviez \n {title} full movie hindi dubbed download filmyzilla \n filmyzilla {title} south movie hindi dubbed \n {title} full movie in hindi download mp4moviez \n {title} movie download in hindi filmywap \n \n *Filmyzilla! {title} ({year}) .FullMovie. Free Download Full4K HINDI Dubbed Mp4moviez \n \n *!{title} - The Rule {year} FullMovie Hindi Dubbed Download Full4K HINDI Dubbed Mp4moviez \n \n"
                        
            driver.find_element(
                By.CSS_SELECTOR, "textarea[name='bbcode-area']"
            ).send_keys(konten)
            time.sleep(5)

            driver.find_element(By.CSS_SELECTOR,"span[ng-hide='$root.ajaxRequest']").click()
            time.sleep(25)


            response = (
                supabase.table(SUPABASE_TABLE_NAME)
                .insert({"result": driver.current_url})
                .execute()
            )
            time.sleep(3)
                        
           
                
        except:
            print("Terjadi Error")
