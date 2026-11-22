# Reddit Video Downloader Using Links in txtFiles

## Introduction

#### What is this?

This repo is for my scripting for my yt channel in downloading reddit videos.

#### Why?

I noticed that when I am using a free reddit video downloader that I found on the internet. I have to enter the links one by one to download. It wastes a lot of time. So I thought of making a program / script that will read a text file full of links and automatically download the next video.

#### How?

Find videos in reddit and simply copy the link and paste in a text file within the folder of the repo. Change the variable `textOne.txt` to your name of the file text. And run `py main.py` in the terminal and wait each categories with its folder to show the downloaded videos.

## Documentaion

#### Why Python?

Python is designed for making a genral-purpose scripting language and it applicable to a lot of applications. It allows developers to write scritps that can automate tasks and others.
Plus, I most used Javascript in programming and I want to explore and test some language that why I used Python.


##### Problems

    1. error encoutering in executing the reddit video downloader function `yt_dlp`
        - fixed by installing `ffmpeg` to the system and adding to the env variables
         - but encounters more error in authentication related issues
            + fixed by using other libraries the RedDownloader
    2. naming file of the videos
        + fixed by adding a string tempalte with an increment fnc
