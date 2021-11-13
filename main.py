import os
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()
drive = GoogleDrive(gauth)

folder = '1v5Dtp6m6OV1EgXB_jokyd9c0Wnj-Jsw4'

# Upload files
directory = "D:/pyGuru/Youtube/Google services/Google drive backup/data"
for f in os.listdir(directory):
	filename = os.path.join(directory, f)
	gfile = drive.CreateFile({'parents' : [{'id' : folder}], 'title' : f})
	gfile.SetContentFile(filename)
	gfile.Upload()
