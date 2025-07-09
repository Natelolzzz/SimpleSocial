import NateUtils
from operator import itemgetter

posts = []

def addPost(text,tags):
  post = [text,tags]
  posts.append(post)

def suggestSimilar(current):
  toSuggest = []
  for item in posts:
    if current != item:
      similarityData = [item,NateUtils.listSimilarity(item[1], current[1])]
      toSuggest.append(similarityData)
  toSuggest.sort(key=itemgetter(1))
  return list(reversed(toSuggest))
  
addPost("I'm an example!",["Example Tag 1","Example Tag 2","Example Tag 3"])
addPost("I'm also an example!",["Example Tag 2","Example Tag 3","Example Tag 4"])
addPost("I'm still an example!",["Example Tag 1","Example Tag 5","Example Tag 7"])
addPost("I'm definitely an example!",["Example Tag 1","Example Tag 2","Example Tag 3"])

print(suggestSimilar(posts[0]))
