CMI
====

+ **Project URL**
https://github.com/hszcg/CMI

Including Content Management Tools and HTML Auto-generation Tools from JSON data files.


## Required Libs:
* Python 2.7
* PyQt4


## Content Management Tools
+ **Directory**
* CMI_ROOT/ is for CMI Lab Page
* JiaXu_ROOT/ is for JiaXu's Home Page

+ **Usage**
```
$ cd gui/
$ python window.py 
```

+ **Operations**
* On initialization, program will automatically load data from "gui/data.json".
* Use "Add/Delete" button to add/delete items.
* Use "Up/Down/Top/Bottom" button to reorder items.
* Use "Save Item" button to save current item to data memmory.
* Use "Save File" button to save current data to "gui/data.json", while the old one is backup to "gui/data.json.bak".
* Use "Make HTML" button to generate HTML files from current data to ""html/" directory.


## Data
+ **Data File**
gui/data.json 

+ **Data Format**
JSON Format, Level 1 key is in the left column, Level 2 key is in the middle column, Level 3 list is in the right column.
And for each item, the property name is the key, and the content is the value.


## Deploy
Copy the "html/" directory to host dir.


## Backup
+ **Data Backup**
Data is automatically backup from "gui/data.json" to "gui/data.json.bak"

+ **HTML Backup**
HTML is backup from "html/" to "html_bak/"
```
$ ./backup.sh 
```


## Others
* 'counter' is reserved for additional Javascript code in each HTML page

