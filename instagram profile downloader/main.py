import instaloader

# create an instance of Instaloader class
L = instaloader.Instaloader()

# get a profile name from user input
profile = input("Enter the profile name: ")

# download the metadata and profile picture !!

L.download_profile(profile, profile_pic_only=True)
s