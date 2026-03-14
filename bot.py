import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# রেন্ডারে চালানোর জন্য ড্রাইভার অটো-সেটআপ
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
