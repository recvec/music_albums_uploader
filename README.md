
# MusicAlbumsUploader
Utility helps you to upload your audio albums as the channels in telegram

## What is it?

Imagine you have an album you bought, or created by yourself. 
Sometimes you want to hear it online in different devices, or share it with your friends (if you have the rights).
This utility helps you to create private channels for every music album in a folder with the name of the album + your own prefix. 

Input:
1) Path to the artist folder 

![Screenshot with a base folder with music albums inside](https://i.ibb.co/d5mPrY4/Deepin-20191124103918.png "Screenshot with base folder with music albums inside")
![Music inside](https://i.ibb.co/G3dbKZp/Deepin-20191124103941.png "Music inside")

2) Some text prefix which will help you to find all your created albums-channels beetwen others in telegram.
I'm using "recpl" - recvec playlist

Output:

![Created channel](https://i.ibb.co/C2sQQNQ/Deepin-20191124104720.png )
![Inside](https://i.ibb.co/fFrjZ0Q/Deepin-20191124114120.png)

The number of albums can be more than one.
(This album was just an example. Donate and help your favourite artists)


## How to use?
1) Install requirements by using:
```
pip install -r requirement.txt
```
**or** 
create a virtual environment

in python 3.6

```
virtualenv --python=/usr/bin/python3.6 <path/to/new/virtualenv/>
```

in python 2.7

```
virtualenv --python=/usr/bin/python2.7 <path/to/new/virtualenv/>
```

then install all the packages available in the requirement.txt file.

```
pip install -r <path/to/the/> requirement.txt
```

2)  Inside **uploader.py** put your API id and API hash. You can get new ones here https://my.telegram.org/apps

    api_id = 4815162342  
    api_hash = 'hash'
    
3)  Inside **uploader.py** enter your channel name prefix (for fast search) and the path of albums

    prefix = "recpl"  
    path = r"/media/recvec/DE3C1FD03C1FA317/The Left Banke"
    
4) Start script and enjoy

![process](https://i.ibb.co/Hq8Dvrr/ezgif-com-video-to-gif.gif)
![process](https://i.ibb.co/X4csPGf/ezgif-com-video-to-gif-1.gif)
