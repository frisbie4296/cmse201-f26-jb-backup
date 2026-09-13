#!/usr/bin/env python
# coding: utf-8

# # Day 12 Pre-Class Assignment: Overview of data and file formats

# ### <p style="text-align: right;"> &#9989; Put your name here</p>

# ![file-formats.jpg](attachment:file-formats.jpg)

# ## Goals for today's pre-class assignment
# 
# - Review some basics of file formats
# - Identify whether files are text or binary files
# - For text files, identify key components such as *field delimiter* and *character encoding*
# 
# 
# 
# ## Assignment instructions
# 
# **This assignment is due by 11:59 p.m. the day before class,** and should be uploaded into the "Pre-class assignments" submission folder.  If you run into issues with your code, make sure to use Slack to help each other out and receive some assistance from the instructors. Submission instructions can be found at the end of the notebook.

# ---
# ## File Formats and File Systems Review

# There are thousands of accepted file formats.  For an abbreviated list, see this [summary on wikipedia](https://en.wikipedia.org/wiki/List_of_file_formats).
# 
# In general, all computer files store information as a series of bits (binary 1's and 0's).  Typically 8 bits are combined into a single byte.  All files can be categorized as:
# - **Text files**: where the bytes represent characters. 
# - **Binary files**: where the bytes represent a custom organization of information.  A single binary file can include information encoded as strings, floats, and/or ints.  Common files formats (such as * .mp3, * .bmp, * .jpeg) follow standards for how the data is organized and typically include a header with metadata and then data.  
# 
# 
# Watch the following video to learn the basics of files and file systems. If the YouTube video doesn't work, try this [MediaSpace link](https://mediaspace.msu.edu/media/Files+%26+File+SystemsA+Crash+Course+Computer+Science+20/1_lupsdt5f). 

# In[ ]:


# Video on file formats and file systems
from IPython.display import YouTubeVideo  
YouTubeVideo("KN8YgJnShPM",width=640,height=340)


# ### For additional details on how text files are stored, watch the following video
# If the YouTube video doesn't work, try this [MediaSpace link](https://mediaspace.msu.edu/media/Understanding+ASCII+and+Unicode+%28GCSE%29/1_u47mghq6).

# In[ ]:


# Video on ASCII and UNICODE
from IPython.display import YouTubeVideo  
YouTubeVideo("5aJKKgSEUnY",width=640,height=340)


# ### Tips for dealing with files
# 
# When dealing with files or file formats you're not familiar with, considering the following tips:
# 
# 1. First, determine if the file is a text file or binary file
# 
#     - Try opening the file with a simple text editor (on a mac: *TextEdit*; on a windows pc: *Notepad*; or open file with *Jupyter Notebook*).  If the file has visible, meaningful characters (e.g., numbers and letters), it is a text file.
#   
#      - **Filename Extensions:** The characters at the end of a file name after the period are the file extension.  File extensions offer a convenient way to mark a file as a certain file format.  For example, `my_text_file.txt`, has the extension `txt`.  Typically, `txt` is the accepted file extension for text files.  That said, files can be renamed to have any file extension.  When analyzing data for this course, you should insure that the file extension matches the anticipated file type. 
#      
#      - **Filename Extension Caveat:** To be clear, someone can rename a file to have any file extension.  You can encounter a file with the extension `txt` and it is not a text file.  Likewise, you can find a file with the extension `docx` and find it is not a MS Word file.  And, you can find a file with the extension `bin`, and find it is a text file. **Don't be fooled by the extension.**  
#      
#      - **Tip on Extensions**: Some file browsers on some operating systems are defaulted to hide file extensions (Windows10, we are talking to you).  *We strongly recommend that you change your default settings to show file extensions.*  As a data scientist, you need to see the entirety of your file names.  To display file extensions in your file browser visit: [Windows](https://helpx.adobe.com/x-productkb/global/show-hidden-files-folders-extensions.html) or [Mac](https://support.apple.com/en-au/guide/mac-help/mchlp2304/mac). If you don't use a Windows or Mac computer, hopefully you're familiar enough with your operating system to know how to do this.
#     
# 
# 2. If a file is a text file, determine the structure (for example, does it have rows and columns?).  
# 
#     - **Determine the delimiter between the fields** (are there commas, semicolons, tabs, or some other delimiter between each column?).
# 
#     - **Line Feed:** Text files created on DOS/Windows machines have different line endings than files created on Unix/Linux/Mac. DOS uses carriage return and line feed ("\r\n") as a line ending, which Unix uses just line feed ("\n")
#     
#     - **Encoding:** Text files can be stored with one of many different character encodings (for more information, see [summary on wikipedia](https://en.wikipedia.org/wiki/Character_encoding).  A very common encoding is UTF-8 (8-bit Unicode Transformation Format, this is the default for `pandas.read_csv()`).   Additional encodings available [here](https://docs.python.org/3/library/codecs.html#standard-encodings).
#     
#     - Most modern text editors can auto-detect the line feed and character encoding when opening a new text file.  So, you usually do not need to worry about these things, but *when loading data into python, we usually need to prescribe the encoding*!
#     
# 
# 3. If a file is a binary file, you will need to know the file format.  Unless it is a very simple organization, it will be difficult to guess the way the data is organized in the file.

# ----
# 
# ## Part 1. Identify characteristics of basic data files

# &#9989;&nbsp; **Question 1.1.** From the course website, download all of the files that start with `us_pop_by_state*`.  Open each file with a text editor on your computer and using the above tips, try to determine if these files are text or binary. And, fill in the remaining unknown fields marked with a `?` in the following markdown table. If you've not worked with a markdown table before, this should serve as a nice bit of practice!

# ---
# **COMPLETE THIS TABLE:**
# 
# | File Name | File Extension | Text or Binary | Delimiter (if text) | Number Header Rows (if text) |
# | :--- | :---: | :---: | :---: | :---: |
# us_pop_by_state_2010_2011 | ? | ? | ? | ? |
# us_pop_by_state_2012_2013_encoding_utf-16be | ? | ? | ? | ? | 
# us_pop_by_state_2014_2015_windows_linefeed | ? | ? | ? | ? | 
# us_pop_by_state_2016a | ? | ? | ? | ? | 
# us_pop_by_state_2017a | ? | ? | ? | ? | 

# &#9989;&nbsp; **Question 1.2.**  What are at least two things that are different between the data storage in files: `us_pop_by_state_2010_2011.csv` and `us_pop_by_state_2012_2013_encoding_utf-16be.csv`?
# 

# <font size=+3>&#9998;</font> *Put your answer here.*

# ----
# 
# ## Part 2.  Load text files with Pandas and Practice Plotting

# &#9989;&nbsp; **Question 2.1.**  Load in the contents from the file `us_pop_by_state_2010_2011.csv` using a Pandas load command.  *Tip:* Pay special attention to `pandas.read_csv()` flags to ensure this loads correctly.  Look at the basics of this data frame using the `.describe()` function.

# In[ ]:


# Put your code here


# &#9989;&nbsp; **Question 2.2.**  Load in the contents from the file `us_pop_by_state_2012_2013_encoding_utf-16be.csv` using pandas load command. *Tip:* Pay special attention to the `encoding` option in `pandas.read_csv()`. Look at the basics of this data frame using the `.describe()` function. If you run into issues with loading this file, read the "Additional Tip" below to see if it help solve your problems.

# In[ ]:


# Put your code here


# *Additional Tip:* One of the issues with the text file `us_pop_by_state_2012_2013_encoding_utf-16be.csv` is that the numbers are stored as strings with commas at the thousands place.  This makes large numbers more readable to the human eye, but is not helpful for a computer.  The `pandas.read_csv()` comes to the rescue again and has an optional argument for this very issue.  **Add the `thousands=','` argument to your read function.**

# &#9989;&nbsp; **Question 2.3.**  Make a list that contains the total population (sum across all states) for each year, 2010 through 2013.  Plot the total US population versus year.  Be sure to label all axes.

# In[ ]:


# Put your code here

year = [2010, 2011, 2012,2013]
# us_pop = ?????????


# ---
# 

# ---
# ## Assignment wrap-up
# 
# Please fill out the form that appears when you run the code below.  **You must completely fill this out in order to receive credit for the assignment!**

# In[ ]:


from IPython.display import HTML
HTML(
"""
<iframe 
	src="https://cmse.msu.edu/cmse201-pc-survey" 
	width="800px" 
	height="600px" 
	frameborder="0" 
	marginheight="0" 
	marginwidth="0">
	Loading...
</iframe>
"""
)


# ### Congratulations, you're done!
# 
# Submit this assignment by uploading it to the course Desire2Learn web page.  Go to the "Pre-class assignments" folder, find the appropriate submission link, and upload it there.
# 
# See you in class!

# Copyright &#169; 2021, [Department of Computational Mathematics, Science and Engineering](https://cmse.msu.edu/) at Michigan State University, All rights reserved.

# In[ ]:




