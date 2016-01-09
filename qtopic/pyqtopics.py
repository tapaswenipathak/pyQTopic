import urllib2
from bs4 import BeautifulSoup
import feedparser
import re


####################################################################
# API
####################################################################

class QTopic:

    @staticmethod
    def get_follower_count(topic):
        url = "https://www.quora.com/" + topic
        topic = topic.replace(" ","-")
        html_doc = urllib2.urlopen(url)
        soup = BeautifulSoup(html_doc.read())
        raw_data = soup.find('a',{'class':'TopicFollowersStatsRow StatsRow'})
        follower_count = str(raw_data.find('strong').text)
        dict = {
            'topic': topic,
            'followers': follower_count
        }
        return dict

    @staticmethod
    def get_some_followers(topic):
        url = "http://www.quora.com/" + topic + "/followers"
        html_doc = urllib2.urlopen(url)
        soup = BeautifulSoup(html_doc.read())
        raw_data = str(soup.find_all('a', class_='user'))
        soup = BeautifulSoup(raw_data)
        name = soup.get_text()
        dict = {
            'name': name,
            'topic': topic,
        }
        return dict

    @staticmethod
    def get_related_topics(topic):
        url = "https://www.quora.com/" + topic
        html_doc = urllib2.urlopen(url)
        soup = BeautifulSoup(html_doc.read())
        raw_data = str(soup.find_all(
            'div', class_='RelatedTopicFaqsSection RelatedTopicsSection'))
        soup = BeautifulSoup(raw_data)
        raw_data = str(soup.find_all('span', class_='TopicName'))
        soup = BeautifulSoup(raw_data)
        related_topics = soup.get_text()
        dict = {
            'topic': topic,
            'related_topics': related_topics,
        }
        return dict

    @staticmethod
    def get_best_questions(topic):
        url = "http://www.quora.com/" + topic + "/best_questions/rss"
        f = feedparser.parse(url)
        feed_len = len(f.entries)
        links = []
        title = []
        published = []
        for i in range(feed_len):
            links.append(f['entries'][i]['links'][0]['href'])
            title.append(f['entries'][i]['title'])
            published.append(f['entries'][i]['published'])
        dict = {
            'links': links,
            'title': title,
            'published': published
        }
        return dict

    @staticmethod
    def get_top_stories(topic):
        url = "http://www.quora.com/" + topic + "/rss"
        f = feedparser.parse(url)
        feed_len = len(f.entries)
        links = []
        title = []
        published = []
        for i in range(feed_len):
            links.append(f['entries'][i]['links'][0]['href'])
            title.append(f['entries'][i]['title'])
            published.append(f['entries'][i]['published'])
        dict = {
            'links': links,
            'title': title,
            'published': published
        }
        return dict

    @staticmethod
    def get_open_questions(topic):
        url = "http://www.quora.com/" + topic + "/questions"
        html_doc = urllib2.urlopen(url)
        soup = BeautifulSoup(html_doc.read())
        raw_data = str(soup.find_all('div', class_='QuestionText'))
        soup = BeautifulSoup(raw_data)
        title = soup.get_text()
        dict = {
            'question_titles': title,
            'topic': topic,
        }
        return dict
    @staticmethod
    def  get_top_writers (topic) :
    name = []
    view_count = []
    answer_count = []
    topic=topic.replace(" ","-")
    url = "https://www.quora.com/" + topic + "/writers"
    try:
        x = urllib2.urlopen(url).read()
        soup = BeautifulSoup(x)
        list_item = soup.find_all('div',{'class':'LeaderboardListItem'})
        for item in list_item:
            try:     
                    view_count.append(str(item.find('div',{'class':'num'}).text))
                    name.append(str(item.find('a',{'class':'answers_link'},href=True)['href']).split('/')[2].replace("-"," "))
                    answer_count.append(str(item.find('a',{'class':'answers_link'}).text.split(" ")[1]))

            except(UnicodeEncodeError,AttributeError):
                  continue
        dict={'name':name,
            'view_count':view_count,
            'answer_count':answer_count}    
        return dict      
    except urllib2.HTTPError,e:
        if e.code == 404:
           print "Top Writers info unavailable for this topic"
        else:
            print "Sorry!Unable to get the required info"    
