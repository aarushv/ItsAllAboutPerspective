from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser
#
import urlparse, urllib, json, urllib2, urllib3
import apiclient, httplib2, oauth2client, uritemplate




# Set DEVELOPER_KEY to the API key value from the APIs & auth > Registered apps
# tab of
#   https://cloud.google.com/console
# Please ensure that you have enabled the YouTube Data API for your project.
DEVELOPER_KEY = "AIzaSyA2TPUjP0mXT6VAjNJr_5L9oWeD2v-NNyk"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"


def youtube_search(options):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                    developerKey=DEVELOPER_KEY)

    # Call the search.list method to retrieve results matching the specified
    # query term.
    search_response = youtube.search().list(
        q=options.q,
        part="id,snippet",
        maxResults=options.max_results
    ).execute()

    videos = []

    # Add each result to the appropriate list, and then display the lists of
    # matching videos, channels, and playlists.
    for search_result in search_response.get("items", []):
        if search_result["id"]["kind"] == "youtube#video":
            videos.append("%s (%s)" % (search_result["snippet"]["title"],
                                       search_result["id"]["videoId"]))

    print("Videos:\n", "\n".join(videos), "\n")

if __name__ == "__main__":
    argparser.add_argument("--q", help="Search term", default="Google")
    argparser.add_argument("--max-results", help="Max results", default=25)
    args = argparser.parse_args()
    youtube_search(args)




# newsKey = 'c93dc8ed47da4d759ad5a5183592c88e'
#
# def pretty(obj):
#     return json.dumps(obj, sort_keys=True, indent=2)
#
# def invokeAPI(topic):
#     baseurl = 'https://newsapi.org/v2/everything'
#     api_key = 'c93dc8ed47da4d759ad5a5183592c88e'
#     topic = topic
#     params = {'q': topic, 'apiKey': api_key}
#     newsRequest = baseurl + '?' + urllib.urlencode(params)
#     openURL = urllib.request.urlopen(newsRequest)
#     newsJsonStr = openURL.read()
#     newsData = json.loads(newsJsonStr)
#     return newsData
#
# def newsAPI(topic):
#     baseurl = 'https://newsapi.org/v2/everything'
#     api_key = '97d738a2d8fe4f3c960397bfe17b63d2'
#     topic = topic
#     params = {'q': topic, 'apiKey': api_key}
#     newsRequest = baseurl + '?' + urllib.urlencode(params)
#     openURL = urllib2.urlopen(newsRequest)
#     newsJsonStr = openURL.read()
#     newsData = json.loads(newsJsonStr)
#     return(newsData)
#
# print(newsAPI('huawei'))

