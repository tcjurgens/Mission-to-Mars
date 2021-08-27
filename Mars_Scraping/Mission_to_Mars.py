#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager

import pandas as pd


# In[2]:


executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[3]:


# Visit the mars nasa news site
url = 'https://redplanetscience.com'
browser.visit(url)
# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


# In[4]:


html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('div.list_text')


# In[5]:


slide_elem.find('div', class_='content_title')


# In[6]:


# Use the parent element to find the first `a` tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# In[7]:


# .find( , ).get_text() will only return the text of the element


# In[8]:


news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# In[9]:


# IMPORTANT:
# find() is used to find the first class and attribute we've specified
# find_all() will retrieve all such tags and attributes


# In[ ]:





# ### FEATURED IMAGES 

# In[10]:


# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)


# In[11]:


full_image_elem = browser.find_by_tag('button')[1]  # [1] stipulates we want our browser to click the second button
full_image_elem.click()


# In[12]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')


# In[13]:


# Find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# In[14]:


# img tag is nested within the HTML , so we include it her
# get('src') pulls the link to the image

# here, we are telling BeautifulSoup to look inside the <img /> tag for an image with a class of fancybox-image


# In[15]:


# Use the base URL to create an absolute URL
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# In[16]:


df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.columns=['description', 'Mars', 'Earth']
df.set_index('description', inplace=True)   # sets the 'description' column as the df index
df


# In[17]:


df.to_html()


# In[18]:


browser.quit()   # ends the automated broser session


# In[ ]:




