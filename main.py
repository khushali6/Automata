
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import tweepy
PATH="chromedriver.exe"
driver=webdriver.Chrome(PATH)


driver.get("https://todoverse.herokuapp.com/")

# task_done=driver.find_element(By.CLASS_NAME, "list-group-item todo-completed").text

task_done=driver.find_elements("xpath","//li[@class='list-group-item todo-completed']")
print("Length is ",len(task_done))
print("Printing Elements:")
for i in task_done:
    print(i.text)



#Twitter Configuration
API_KEY="iZzeSbyS27xYm5h0ucqsXOxke"
SECRET_API_KEY="joB5ZmhWHBQli1wF0h7fb1DWyzlaiUwIk7qcATnJIqurZaumhc"
BEARER_TOKEN="AAAAAAAAAAAAAAAAAAAAAAaniQEAAAAA8pfZ24PWrYV5KhQd8HorMrkC8x4%3DBvKvMCei0WVHeigP8EOaERuXAxZb2saq7LUe4TYUtl1uLFrXNi"

ACCESS_TOKEN="1583351835594616832-DmWzTzGgADI6tHng9TtvYKlwtAmR3i"
ACCESS_TOKEN_SECRET="1GZe7CBOCQscQewNH4IkKOV8N8UpU6f4ygg7DNUqHLSTa"



final_string=''
for x in task_done:
    final_string+=''+x.text+"\n"

# 
def increase_day():
    called = True

    if called:
        count_file = open("count.txt", "r") # open file in read mode
        count = count_file.read() # read data 
        count_file.close() # close file

        count_file = open("count.txt", "w") # open file again but in write mode
        count = int(count) + 1 # increase the count value by add 1
        count_file.write(str(count)) # write count to file
        count_file.close() # close file

    return count


count=increase_day()
def task():
  delete_completed=driver.find_element("xpath","//button[@name='deleteComplete']")
  delete_completed.click()
tweet_text="Day "+str(count)+" of 100\n"+final_string+" #100DaysofCode"
client = tweepy.Client(consumer_key= API_KEY,consumer_secret= SECRET_API_KEY,access_token= ACCESS_TOKEN,access_token_secret= ACCESS_TOKEN_SECRET)
response=client.create_tweet(text=tweet_text)
task()





   


   