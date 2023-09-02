To run this file unzip the papers.zip

Store this into a directory of your choice then in the papers.py file change "PATH_TO_PAPERS" to this directory

On line 44, You can change the amount of papers to be read by adjusting the "PAGES" value to any number less than "MAX_PAGES"

The program will attempt to read all pages as on line 44 the "MAX PAGES" value is set inside the range function

To install packages required to run
```
pip install -r requirements.txt
```
To run the program
```
python papers.py
```

You will also need the papers.zip from this link
[https://courses.maine.edu/d2l/le/content/294668/viewContent/8338635/View](url)


Once the program is finished a file named "papers.csv" will contain all the extracted data.

There is a function designed to read this data which will output everything in the terminal once the reading and writing has completed.
