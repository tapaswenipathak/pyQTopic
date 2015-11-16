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
        html_doc = urllib2.urlopen(url)
        soup = BeautifulSoup(html_doc.read())
        raw_data = str(soup.find_all('span', class_="count"))
        soup = BeautifulSoup(raw_data)
        followers = soup.find_all('span')[0].get_text()
        dict = {
            'topic': topic,
            'followers': followers,
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
