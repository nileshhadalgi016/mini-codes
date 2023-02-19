# pip install insta-scrape

from instascrape import Reel
import os
import time

sample_reel = Reel('https://www.instagram.com/reel/Cccgd2MFCs4/')
sample_reel.scrape()
reeldir = os.getcwd()
sample_reel.download(fp=f"{reeldir}\\reel{int(time.time())}.mp4")
print(dir)
print(f"This reel has {sample_reel.video_view_count:,} views.")