import os
from moviepy.editor import VideoFileClip, concatenate_videoclips

# Path where the Snapchat video files are saved
video_folder = r'C:\Users\Coren\snapchat-link-generator\memories'  # Update this path

# Output path for the merged video
output_file = 'merged_snapchat_video.mp4'

def get_video_files(directory):
    """
    Retrieves all video files from the specified directory, assuming they are in correct order.
    You can modify this to sort by filename if needed.
    """
    video_files = [os.path.join(directory, f) for f in os.listdir(directory) if f.endswith(('.mp4', '.mov'))]
    video_files.sort()  # Sort the video files by filename
    return video_files

def merge_videos(video_files, output_path):
    """
    Merges a list of video files into one video.
    """
    clips = []
    for video_file in video_files:
        print(f"Loading video: {video_file}")
        clip = VideoFileClip(video_file)
        clips.append(clip)
    
    # Concatenate the video clips
    final_clip = concatenate_videoclips(clips)
    
    # Write the output to a file
    final_clip.write_videofile(output_path, codec='libx264', fps=24)

if __name__ == "__main__":
    # Get the list of video files
    video_files = get_video_files(video_folder)
    
    if not video_files:
        print("No video files found in the directory.")
    else:
        print(f"Found {len(video_files)} video(s) to merge.")
        
        # Merge the videos and save the output
        merge_videos(video_files, output_file)
        print(f"Videos merged successfully! Saved as {output_file}.")
