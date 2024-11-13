# File Hub

File Hub combines various tools 

1. Download Image

	•	Enter the image URL.
	•	Specify a name: The file type (e.g., .jpg, .png) is appended automatically if not provided.
	•	Choose a folder or path: If the folder does not exist, it will be created.

2. Download YouTube Video

	•	Enter the YouTube video URL.
	•	Choose a folder or path: If the folder does not exist, it will be created.
	•	Optionally, select a time range: Download a specific portion of the video by specifying a start and end time.

3. Convert Files

	•	JPG to PNG
	•	PNG to JPG
	•	HEIC to PNG
	•	HEIC to JPG
	•	PNG to PDF (sized to 800 width, maintaining original height ratio)
	•	JPG to PDF (sized to 800 width, maintaining original height ratio)
	•	HEIC to PDF (sized to 800 width, maintaining original height ratio)

4. MP4 to MP3

	•	Specify MP4 file path.
	•	Provide a desired MP3 name: The MP3 will be saved in the same folder as the original MP4 file.

5. PDF Compression

	•	Remove images from the PDF file.
	•	Reduce image quality (recommended for file size reduction).
	•	Lossless Compression: Joins content streams and applies a Flatedecode filter, which may not result in further compression. For more information, visit pypdf file size guide.

Libraries:

	• requests
	• shutil
	• os
	• urllib
	• pillow
	• pillow_heif
	• yt_dlp
	• moviepy
	• pypdf

TO-DO:

concatenate pdf files
interface