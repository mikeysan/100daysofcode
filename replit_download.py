"""
#### THIS IS AN IDEA I HAD AFTER TRYING SEVERAL TIMES BUT FAILING TO LINK MY REPLIT ACCOUNT TO GITHUB. So I asked ChatGPT for an example. #####
To download the contents of your Replit account and upload them to GitHub, you can use the GitHub API and the Replit API in your Python script.
Here's an example of how you could do this:

First, you'll need to obtain an access token for the GitHub API. 
You can do this by visiting the Settings page of your GitHub account, going to the Developer Settings section, and clicking on "Personal access tokens".
Click on "Generate new token", give your token a name, select the appropriate permissions, and click on "Generate token".
Make sure to save the token somewhere safe, as you won't be able to see it again once you leave the page.

Next, you'll need to install the requests library in your Replit project.
You can do this by going to the "Libraries" tab in your Replit project and searching for "requests". 
Click on "Install" next to the requests library.

Now you can use the following Python code to download the contents of your Replit account and upload them to a new repository on GitHub:
"""
import requests

# Replace YOUR_ACCESS_TOKEN with your GitHub access token
# Replace YOUR_USERNAME with your GitHub username
# Replace YOUR_REPO_NAME with the name of your repository
GITHUB_API_URL = "https://api.github.com/repos/YOUR_USERNAME/YOUR_REPO_NAME"
ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"

# Set the authorization header for the GitHub API
headers = {
    "Authorization": f"Token {ACCESS_TOKEN}",
}

# Create a new repository on GitHub
response = requests.post(GITHUB_API_URL, headers=headers)

# Check if the repository was created successfully
if response.status_code == 201:
    print("Repository created successfully!")
else:
    print("Failed to create repository.")

# Get the list of files in your Replit account
replit_url = "https://replit.com/api/v0/user/files"
response = requests.get(replit_url)

# Check if the request was successful
if response.status_code == 200:
    # Iterate over the list of files and upload them to the repository
    for file in response.json():
        file_url = file["url"]
        file_path = file["path"]

        # Download the file from Replit
        file_content = requests.get(file_url).text

        # Create a new file in the repository
        create_file_url = f"{GITHUB_API_URL}/contents/{file_path}"
        data = {
            "message": "Add file",
            "content": file_content,
        }
        response = requests.put(create_file_url, json=data, headers=headers)

        # Check if the file was created successfully
        if response.status_code == 201:
            print(f"File {file_path} added to repository.")
        else:
            print(f"Failed to add file {file_path} to repository.")
else:
    print("Failed to get list of files from Replit.")
