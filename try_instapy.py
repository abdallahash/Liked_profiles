from instapy_cli import client
from textwrap import dedent 
from datetime import datetime
#This is just a comment: 

#Don't forget to put the pictures on the same folder so it's much easier for you
#The post list could be like this for example.
image_list = ["picture_1.jpg","Picture_2.jpg"]

#Here is another exmple 
text_list = ["caption1","caption2","Cool post","And a better one here","..." ]

day = datetime.now().day
day = day - 1 

username = 'your_Instagram_user_name' 
password = 'your_password'
image = image_list[day]

#Here you can add your caption text with the hashtags
text = dedent("""{}""".format(text_list[day]))


with client(username, password) as cli:
    cli.upload(image, text)
