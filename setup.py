import os

# Install dependencies for Python 3 in Google Colab
os.system('apt-get update')  # Update package lists

# Install Python 3
os.system('apt-get install python3')  # Install Python 3

# Install pip for Python 3
os.system('apt-get install python3-pip')  # Install pip3 for Python 3

# Upgrade required packages using pip3
os.system('pip3 install --upgrade google-api-python-client')  # Upgrade the Google API client
os.system('pip3 install --upgrade google-auth-oauthlib google-auth-httplib2')  # Upgrade OAuth and HTTP library
