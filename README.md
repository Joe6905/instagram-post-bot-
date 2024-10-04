# Instagram Photo Upload Automation

This Python script allows you to automate the process of logging into Instagram, uploading a photo with a caption, and logging out. The script uses the `instagrapi` library to interact with Instagram.

## Features

- Log in to Instagram using your credentials.
- Upload a photo to your Instagram account with a caption.
- Automatically log out after posting.

## Requirements

Before running this script, ensure you have the following installed:

- **Python 3.x**
- **instagrapi** library

You can install the required libraries using:

```bash
pip install instagrapi
Usage
Step 1: Clone or download this repository.
bash
Copy code
git clone https://github.com/your-repo-url
Step 2: Set up the script.
Edit the Python script with your Instagram login details and the path to the image you want to upload. Here's the part you need to modify:

python
Copy code
USERNAME = 'your_username'
PASSWORD = 'your_password'
photo_path = "C:\\Users\\YourName\\path_to_photo\\image.jpg"
caption = "Your caption here"
Step 3: Run the script.
For Windows (CMD):
Open the Command Prompt.
Navigate to the directory where your script is saved:
bash
Copy code
cd path\to\your\script
Run the script:
bash
Copy code
python your_script.py
For Linux/Mac (Terminal):
Open the Terminal.
Navigate to the directory where your script is located:
bash
Copy code
cd /path/to/your/script
Run the script:
bash
Copy code
python3 your_script.py
Step 4: Script Output
Upon running the script, it will:

Log in to Instagram using the provided username and password.
Upload the specified photo with the provided caption.
Log out after the upload is complete.
