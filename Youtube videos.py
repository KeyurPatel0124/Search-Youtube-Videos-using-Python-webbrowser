#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Enter name of video here
video  = input("Enter the name of the movie here:")


# In[2]:


# URL that you want to search in
youtube_url="https://www.youtube.com/results?search_query={}"
youtube_url


# In[3]:


#Form URL
search_url = youtube_url.format(video)
search_url


# In[4]:


#import webbrowser
import webbrowser
Video = webbrowser.open(search_url)


# In[5]:


#Looking for multiple videos
video=[x for x in input("").split(' ')]


video_search


# URL that you want to search in
youtube_url="https://www.youtube.com/results?search_query={}"



# creating multiple urls to be searched 
search_url=[]
i=0
for i in range(0,len(video_search)):
    search_url.append(youtube_url.format(video_search[i]))


search_url


# Import webbrowser package

import webbrowser


for i in range(0,len(search_url)):
    webbrowser.open(search_url[i])


# In[ ]:




