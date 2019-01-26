import urllib3
from bs4 import BeautifulSoup


class QTopic:

    @staticmethod
    def get_follower_count(topic):
        topic = topic.replace(" ","-")
        http = urllib3.PoolManager()
        topic = topic.replace(" ","-")
        url = "https://www.quora.com/topic/" + topic
        res = http.request('GET', url)
        sun = (res.data)
        soup = BeautifulSoup(sun, "html.parser")
        des = soup.find("a", {"class" : "TopicFollowersStatsRow"})
        follower_count = des.strong
        dict = {
            'topic': topic,
            'followers': follower_count.string.encode("utf-8")
        }
        return(dict)

    @staticmethod
    def get_some_followers(topic):
        http = urllib3.PoolManager()
        topic = topic.replace(" ","-")
        url = "http://www.quora.com/topic/" + topic + "/followers"
        html_doc= http.request('GET', url)
        res = (html_doc.data)
        soup = BeautifulSoup(res, "html.parser")
        data = str(soup.find_all('a', class_='user'))
        soup = BeautifulSoup(data)
        name = soup.get_text()
        dict = {
            'topic': topic,
            'name':  name.encode("utf-8"),
        }
        return(dict)

    @staticmethod
    def get_related_topics(topic):
        http = urllib3.PoolManager()
        topic = topic.replace(" ","-")
        url = "http://www.quora.com/topic/" + topic
        html_doc= http.request('GET', url)
        res = (html_doc.data)
        soup = BeautifulSoup(res, "html.parser")
        data = str(soup.find_all('div', class_='section_wrapper'))
        soup = BeautifulSoup(data)
        data = str(soup.find_all('span', class_='TopicName'))
        soup = BeautifulSoup(data)
        name = soup.get_text()
        dict = {
            'topic': topic,
            'name':  name,#.encode("utf-8"),
        }
        return dict

    """@staticmethod
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
        return dict"""

    @staticmethod
    def get_open_questions(topic):
        http = urllib3.PoolManager()
        topic = topic.replace(" ","-")
        url = "http://www.quora.com/topic/" + topic + "/top_questions"
        html_doc= http.request('GET', url)
        res = (html_doc.data)
        soup = BeautifulSoup(res, "html.parser")
        data = str(soup.find_all('span', class_='ui_qtext_rendered_qtext'))
        soup = BeautifulSoup(data)
        name = soup.get_text()
        dict = {
            'topic': topic,
            'name':  name,
        }
        return dict

        
    @staticmethod
    def get_top_writers(topic):
        name = []
        view_count = []
        answer_count = []
        links = []
        http = urllib3.PoolManager()
        topic = topic.replace(" ","-")
        url = "http://www.quora.com/topic/" + topic + "/writers"
        html_doc= http.request('GET', url)
        res = (html_doc.data)
        soup = BeautifulSoup(res, "html.parser")
        data = (str(soup.find_all('a', class_='Leaderboard')))
        user_data = str(soup.find_all('a', class_='user'))
        view = str(soup.find_all('div', class_='num'))
        link = str(soup.find_all('a', class_='answers_link', href=True))
        name.append((BeautifulSoup(user_data)).get_text())
        view_count.append((BeautifulSoup(view)).get_text())
        links.append((BeautifulSoup(link)))
        answer_count.append((BeautifulSoup(link)).get_text())
    
        dict = {
            'topic': topic,
            'name':  name,
            'view_count': view_count,
            'links': links,
            'answer_count': answer_count
        }
        return dict
