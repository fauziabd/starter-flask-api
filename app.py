# Import the packages
from flask import Flask, request, send_file, render_template, url_for
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from io import BytesIO
import urllib.parse
import time
import os

# Create a Flask app
app = Flask(__name__)


# Define a route for taking screenshots
@app.route("/screenshot")
def screenshot():
  # Get the query parameters
  url = request.args.get("url") or 'https://google.com'
  width = int(request.args.get("width") or 1200)
  height = int(request.args.get("height") or 630)

  # Validate the parameters
  if not url:
    return "Invalid parameters"

  # Create a webdriver instance with headless option
  chrome_options = Options()
  chrome_options.add_argument('--headless')
  chrome_options.add_argument('--no-sandbox')
  chrome_options.add_argument('--disable-dev-shm-usage')

  driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

  driver.set_window_size(width, height)

  # Navigate to the URL
  driver.get(urllib.parse.unquote(url))
  time.sleep(2)
  screenshot = driver.get_screenshot_as_png()
  driver.quit()
  return send_file(BytesIO(screenshot), mimetype='image/png')

@app.route('/')
def hello_world():
    return 'Hello, world!'