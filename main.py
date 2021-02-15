#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2, urllib, urllib2, jinja2, json, os, webbrowser
from datetime import datetime, timedelta



JINJA_ENVIRONMENT = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
                                               extensions=['jinja2.ext.autoescape'],
                                               autoescape=True)


def newsAPI(topic, source):
    baseurl = 'https://newsapi.org/v2/everything'
    api_key = 'c93dc8ed47da4d759ad5a5183592c88e'
    params = {'q': topic, 'apiKey': api_key}
    newsRequest = baseurl + '?' + urllib.urlencode(params)
    openURL = urllib.urlopen(newsRequest)
    newsJsonStr = openURL.read()
    newsData = json.loads(newsJsonStr)
    sourceData = [data for data in newsData["articles"] if data["source"]["id"] == source]
    return sourceData


class articleData():
    def __init__(self, data):
        self.title = (data['title']).encode('ascii', 'ignore')
        self.author = str(data['author'])
        self.description = (data['description']).encode('ascii', 'ignore')

        self.published = datetime.strptime(data['publishedAt'], '%Y-%m-%dT%H:%M:%S%fZ')
        self.url = str(data['url'])
        self.source = str(data['source']['name'])



class MainHandler(webapp2.RequestHandler):
    def get(self):
        template_values = {}
        template = JINJA_ENVIRONMENT.get_template('p1.html')
        self.response.write(template.render(template_values))


class TopicHandler(webapp2.RequestHandler):
    def post(self):
        vals = {}
        source1 = self.request.get('dd1')
        source2 = self.request.get('dd2')
        topic = self.request.get('entersearch')

        data1 = newsAPI(topic, source1)
        data2 = newsAPI(topic, source2)

        articles1 = [articleData(info) for info in data1]
        articles2 = [articleData(info) for info in data2]


        vals['results1'] = articles1
        vals['results2'] = articles2

        template = JINJA_ENVIRONMENT.get_template('p2.html')
        self.response.write(template.render(vals))


application = webapp2.WSGIApplication([
    ('/p2', TopicHandler),
    ('/.*', MainHandler)
], debug=True)