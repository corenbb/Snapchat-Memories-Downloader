import json
import requests
import os

# Load the JSON file with the AWS links
json_file_path = 'path/to/aws_links.json'
download_folder = 'path/to/download/folder'

# Create directories based on date (year/month/day)
def create_directories(date):
    date_parts = date.split(' ')
    year, month, day = date_parts[0].split('-')
    dir_path = os.path.join(download_folder, year, month, day)
    os.makedirs(dir_path, exist_ok=True)
    return dir_path

# Download and save each memory
def download_memories():
    # Load AWS links from JSON
    with open(json_file_path, 'r') as f:
        aws_links = json.load(f)
    
    for memory in aws_links:
        aws_link = memory['awsLink']
        file_type = memory['fileType']
        date = memory['date']  # Format: YYYY-MM-DD HH:MM:SS

        # Create directories based on the date
        save_directory = create_directories(date)
        
        # Use the 24hr time for the file name
        time_part = date.split(' ')[1].replace(':', '-')
        file_name = f"{time_part}.{file_type}"
        file_path = os.path.join(save_directory, file_name)

        # Download the memory from AWS link
        try:
            print(f"Downloading {file_name}...")
            response = requests.get(aws_link, stream=True)
            response.raise_for_status()
            
            # Save the file
            with open(file_path, 'wb') as output_file:
                for chunk in response.iter_content(chunk_size=1024):
                    if chunk:
                        output_file.write(chunk)
            print(f"Saved: {file_path}")
        except Exception as e:
            print(f"Failed to download {aws_link}: {e}")

if __name__ == "__main__":
    download_memories()
