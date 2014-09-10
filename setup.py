from setuptools import setup

setup(
    name='qtopic',
    version='0.1.0',
    description='Fetches and parses topic related data from Quora.',
    author='Tapasweni Pathak',
    author_email='tapaswenipathak@gmail.com',
    url='https://github.com/tapasweni-pathak/pyQTopic',
    packages=['qtopic'],
    install_requires=[
        "beautifulsoup4 == 4.3.2",
		"feedparser == 5.1.3"
    ]
    )
