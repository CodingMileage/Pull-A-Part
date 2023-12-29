import time
import sv_ttk
import tkinter as tk
from tkinter import ttk
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

def PAP ():
	try:

		root = tk.Tk()

		sv_ttk.set_theme("dark")

		options = webdriver.ChromeOptions()
		options.page_load_strategy = 'normal'

		driver = webdriver.Chrome(options=options)
		driver.maximize_window()
		driver.get('https://www.pullapart.com/locations/alabama/birmingham/')

		time.sleep(.5)

		makeButton = driver.find_element(By.XPATH, '//*[@id="LocationPageDesktop"]/div/div/div[2]/div/div[2]/div/div/div[2]/div[2]').click()

		time.sleep(1)

		makeSearch = driver.find_element(By.CLASS_NAME, 'select2-search__field')

		makeSearch.send_keys('Infiniti')

		makeSearch.send_keys('\ue007')

		modelBox = driver.find_element(By.XPATH, '/html/body/main/div[2]/div/div[2]/div[2]/div/div/div/div[2]/div/div[2]/div/div/div[2]/div[3]/div[2]/div/span/span[1]/span/span[1]').click()

		modelSearch = driver.find_element(By.CLASS_NAME, 'select2-search__field')

		modelSearch.send_keys('G35')

		modelSearch.send_keys('\ue007')

		time.sleep(1)

		searchButton = driver.find_element(By.XPATH, '/html/body/main/div[2]/div/div[2]/div[2]/div/div/div/div[2]/div/div[2]/div/div/div[2]/div[4]/button').click()

		time.sleep(5)

		row = driver.find_element(By.XPATH, '/html/body/main/div[1]/div/div/div/div/div[3]/div/div[3]/div[3]/div/div/div[3]/div[4]/div[3]/div/div[5]/div')

		entry_label = tk.Label(root, text = f'There is a car in row {row.text}')
		entry_label.grid(row = 0, column = 0)

		root.mainloop()

	except Exception as e:
		print(e, 'Pull A Part')

PAP()