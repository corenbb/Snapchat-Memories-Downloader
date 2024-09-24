# Snapchat Memories Downloader
 This is a script to automate the downloading of memories from your phone to your PC. It works well with large amounts of memories and also sorts them by date.

## Guide
### Downloading your data from Snapchat
You can download your data from snapchat via the app settings:
https://help.snapchat.com/hc/en-us/articles/7012305371156-How-do-I-download-my-data-from-Snapchat

### Using the script
Requirements: Node, Python3, pip.
1. Download the .zip file containing your data from Snapchat.
2. Extract the 'memories_history.json' file.
3. Place the 'memories_history.json' file in a folder with these scripts.
4. Run the 'generate_aws.js' file to get the S3 links from the .json directory.
5. Run 'aws_links_downloader.py' to download and sort all of your memories.
6. OPTIONAL: use the 'optional_video_merge.py' script to merge videos in a specific folder into one video.