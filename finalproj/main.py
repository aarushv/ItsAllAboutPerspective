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


JINJA_ENVIRONMENT = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
                                               extensions=['jinja2.ext.autoescape'],
                                               autoescape=True)


class MainHandler(webapp2.RequestHandler):
    def get(self):
        template_values = {}
        template = JINJA_ENVIRONMENT.get_template('finalproject.html')
        self.response.write(template.render(template_values))

class TopicHandler(webapp2.RequestHandler):
    # def get(self):
    #     vals = {}
    #     vals['page_title']="landing"
    #     template = JINJA_ENVIRONMENT.get_template('p2.html')
    #     self.response.out.write(template.render(vals))
    def post(self):
        vals = {}
        vals['title']="results"
        # topic = self.request.get('entersearch')
        # go = self.request.get('searchbutton')
        # dataFromNews(topic)
        template = JINJA_ENVIRONMENT.get_template('p2.html')
        self.response.write(template.render(vals))


def newsAPI(topic):
    baseurl = 'https://newsapi.org/v2/everything'
    api_key = 'c93dc8ed47da4d759ad5a5183592c88e'
    topic = topic
    params = {'q': topic, 'apiKey': api_key}
    newsRequest = baseurl + '?' + urllib.urlencode(params)
    openURL = urllib2.urlopen(newsRequest)
    newsJsonStr = openURL.read()
    newsData = json.loads(newsJsonStr)
    return(newsData)

def dataFromNews(topic):

    dict = newsAPI(topic)
    print(topic.upper())
    print('Top Result: ' + str(dict['articles'][0]['title']))
    print('Author: ' + str(dict['articles'][0]['author']))
    print('Article Description: ' + (dict['articles'][0]['description']).encode('ascii', 'ignore'))
    print('Article URL: ' + str(dict['articles'][0]['url']) + '\n')

    print('Additional Results')
    print('1. ' + str(dict['articles'][1]['title']))
    print('Author: ' + str(dict['articles'][1]['author']))
    print('Article Description: ' + (dict['articles'][1]['description']).encode('ascii', 'ignore'))
    print('Article URL: ' + str(dict['articles'][1]['url']) + '\n')
    print('2. ' + str(dict['articles'][2]['title']))
    print('Author: ' + str(dict['articles'][2]['author']))
    print('Article Description: ' + (dict['articles'][2]['description']).encode('ascii', 'ignore'))
    print('Article URL: ' + str(dict['articles'][2]['url']) + '\n')
    print('3. ' + str(dict['articles'][3]['title']))
    print('Author: ' + str(dict['articles'][3]['author']))
    print('Article Description: ' + (dict['articles'][3]['description']).encode('ascii', 'ignore'))
    print('Article URL: ' + str(dict['articles'][3]['url']) + '\n')
    print('4. ' + (dict['articles'][4]['title']).encode('ascii', 'ignore'))
    print('Author: ' + str(dict['articles'][4]['author']))
    print('Article Description: ' + (dict['articles'][4]['description']).encode('ascii', 'ignore'))
    print('Article URL: ' + str(dict['articles'][4]['url']) + '\n')



application = webapp2.WSGIApplication([
    ('/p2', TopicHandler),
    ('/.*', MainHandler)
], debug=True)












