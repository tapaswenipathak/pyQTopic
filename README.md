![](https://img.shields.io/badge/-pyQTopic-blueviolet.svg)

# qtopic 
======
[![GitHub issues](https://img.shields.io/github/issues/tapaswenipathak/pyQTopic.svg)](https://github.com/tapaswenipathak/pyQTopic/issues)
[![GitHub forks](https://img.shields.io/github/forks/tapaswenipathak/pyQTopic.svg)](https://github.com/tapaswenipathak/pyQTopic/network)
[![GitHub stars](https://img.shields.io/github/stars/tapaswenipathak/pyQTopic.svg)](https://github.com/tapaswenipathak/pyQTopic/stargazers)
[![GitHub license](https://img.shields.io/github/license/tapaswenipathak/pyQTopic.svg)](https://github.com/tapaswenipathak/pyQTopic/blob/master/License.txt)
[![Twitter](https://img.shields.io/twitter/url/https/github.com/tapaswenipathak/pyQTopic.svg?label=pyQTopic&style=social)](https://twitter.com/intent/tweet?text=pyQTopic:&url=https%3A%2F%2Fgithub.com%2Ftapaswenipathak%2FpyQTopic)

A Python module to fetch and parse Topics related data from Quora.

### Projects built using QTopic
* [`qtopic-api`](https://github.com/tapasweni-pathak/qtopic-api) – A REST API to get topic realted data from Quora.
* [`quora`](https://github.com/tapaswenipathak/quora) - A package to parse Quora.


## Installation

* You will need [Python 2](https://www.python.org/download/). 

* [pip](http://pip.readthedocs.org/en/latest/installing.html) is recommended for installing dependencies.

Install using pip:

    pip install qtopic

## Usage

```python

from qtopic import QTopic

followers_count = QTopic.get_follower_count ('Computer-Programming')
    
#do stuff with the parsed data
followers_count['followers']
followers_count['topic']

```

## Features
### Currently implemented

* Follower Count
* Some followers name 
* Related Topics
* Top Stories
    breaked down links, title, published. 
* Open question
    breaked down links, title, published. 


### Todo
* Information to be stored in a better way.  
* Add most viewed writer

[![Bitdeli Badge](https://d2weczhvl823v0.cloudfront.net/tapasweni-pathak/pyqtopic/trend.png)](https://bitdeli.com/free "Bitdeli Badge")
