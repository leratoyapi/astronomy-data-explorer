# alwasy put the import at the top of the file don forget.
import requests

from flask import Flask


app = Flask(__name__)

@app.route("/")
def light_positive():
    return "<p>I am building something as part of my learning challenge</p>"

# i will fetch the days apod the out shoukd print the title , having some difficluty dont know how to start and do? felling frusttrated but im getting there want to keep the usage of ai to the mimimum

# here is the syntax :

# requests.get(url, params={key: value}, args)

# args means zero or more of the named arguments in the parameter table below.

# Example:
# define your url =...
# requests.get(url, timeout=2.50)

# creating a route that will call the apod data

@app.route("/apod")
def get_apod():
    url = "https://api.nasa.gov/planetary/apod"

    params = { 
        "api_key":"PpbxFB6KmrffTQPTZuGyqJnwRdhU3ILs8Sw3QY2r"
    } 

# added a timeout.
    day = requests.get(url,params=params, timeout=10)

# here is some error handeling 
    if day.status_code == 200:
    
      data = day.json() # turns the data into apython dictionary 


      apod_title = data.get("title", "no title found!")

      # using f strings instead of printing and brackets 
      return f"<h1>Today's APOD Title is:</h1><p>{apod_title}</p>"

    else:
        return f"<p>Error fetching data: {day.status_code}</p>"
   
# also note you routers a  are differnt  just add the /something at the end of the url and it will start.


