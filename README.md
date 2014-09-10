# qtopic 

A Python module to fetch and parse Topics related data from Quora.

### Projects built using QTopic
* [`qtopic-api`](https://github.com/tapasweni-pathak/qtopic-api) – A REST API to get topic realted data from Quora.


## Installation

* You will need [Python 2](https://www.python.org/download/). 

* [pip](http://pip.readthedocs.org/en/latest/installing.html) is recommended for installing dependencies.

Install using pip:

    pip install qtopic

## Usage

```python

from qtopic import QTopic

best_questions = QTopic.get_best_questions ('Computer-Programming')
    
#do stuff with the parsed data
best_questions['links']
best_questions['title']
best_questions['published']

```

## Features
### Currently implemented

* Follower Count
* Some followers name 
* Related Topics
* Feed last updated
* Best questions
* Top Stories
    breaked down links, title, published. 
* Open question
    breaked down links, title, published. 


### Todo
* Information to be stored in a better way.  