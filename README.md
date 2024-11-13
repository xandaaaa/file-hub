# File Hub

File Hub combines various tools 

1.	Download Image
•	Enter the image URL
•	Specify a name (file type is appended automatically if not provided)
•	Choose a folder or path to save the image to, creates folder if it does not exist

2.	Download YouTube Video
•	Enter the YouTube video URL
•	Choose a folder or path to save the video to, creates folder if it does not exist
•	Optionally, select a time range to download a specific portion of the video

3.	Convert File
•	JPG to PNG
•	PNG to JPG
•   HEIC to PNG
•	HEIC to JPG
•	PNG to PDF (sized 800 width, with original height ratio)
•	JPG to PDF (sized 800 width, with original height ratio)
•	HEIC to PDF (sized 800 width, with original height ratio)


4.  MP4 to MP3
•   Specify MP4 (path)
•   Give MP3 desired name, will download to the same folder MP4 is in

5.  PDF Compression
•   Removes images from PDF file
•   Reduces image quality (recommended)
•   Lossless Compression (joins all content streams and applies a Flatedecode filter, possible to not perform anything further information: https://pypdf.readthedocs.io/en/stable/user/file-size.html)

Libraries:

	•	requests
	•	shutil
	•	os
	•	urllib
	•	pillow
	•	pillow_heif
	•	yt_dlp
	•	moviepy
	•	pypdf

TO-DO:

concatenate pdf files
interface