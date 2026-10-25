# this will have all my sript 
# guideline 
# 1. Fetch data from NASA
# 2. If successful, extract variables
# 3. Connect to DB
# 4. Check if date exists
# 5. If not, insert into DB
# 6. Close connection
import  datetime 
import requests 
from conn import conn
import os
from dotenv import load_dotenv, dotenv_values
load_dotenv()


# here i'm fetching : 
def get_apod():
  url = "https://api.nasa.gov/planetary/apod"

  today = datetime.date.today()
  thirty_days_ago = today -datetime.timedelta(days=30)

  params = { 
    "api_key":os.getenv('api_key'),
    "start_date": str(thirty_days_ago),
    "end_date": str(today)
  } 

  print("--- Checkpoint 1: About to ask NASA for data ---")
  

  try:

    day = requests.get(url,params=params)

    print (f"--- Checkpoint 2: NASA responded with status code: {day.status_code} ---")

  
    if day.status_code == 200:
      data = day.json() 
      # will now be a list of dictionaires since we are fetching myultiple days of data.

      for entry in data:
        apod_date =entry.get("date")
        apod_title = entry.get("title")
        apod_explanation = entry.get("explanation")
        apod_url = entry.get("url")
        apod_media_type= entry.get("media_type")
        print(f"{apod_title} ,{apod_date}")

        cursor = conn.cursor()
        sql = "INSERT IGNORE INTO apod (`date`, `title`, `explanation`, `url`, `media_type`) VALUES (%s, %s, %s, %s, %s)"
        values = (apod_date, apod_title, apod_explanation, apod_url, apod_media_type)
        cursor.execute(sql, values)
        conn.commit()
        print("yasss finally inserted into the database!!!")

        print(f"--- Checkpoint 3: Data received from NASA: {data} ---")

      
    else:
      print(f"--- Checkpoint 4: Error fetching data: {day.status_code} ---")

  except requests.exceptions.RequestException as e:
    # 3. Handle network errors
    print(f"--- Network error occurred: {e} ---")

get_apod()