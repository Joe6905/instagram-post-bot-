from instagrapi import Client

# Login details
USERNAME = 'usrnme'
PASSWORD = 'passwd'

# Initialize the Client
bot = Client()

# Login to Instagram
bot.login(USERNAME, PASSWORD)

# Path to the photo
photo_path = "C:\\Users\\\\Downloads\\img"


# Caption for the post
caption = "caption "

# Upload the photo
bot.photo_upload(photo_path, caption)

# Logout after posting
bot.logout()
