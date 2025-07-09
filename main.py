import NateUtils
from operator import itemgetter
import random, time

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

for i in range(100):
  addPost(f"Example {i}",[f"Example Tag {random.randint(1, 10)}",f"Example Tag {random.randint(1, 10)}",f"Example Tag {random.randint(1, 10)}",f"Example Tag {random.randint(1, 10)}",f"Example Tag {random.randint(1, 10)}"])

times = [] # Speed test, caclulate average performance
for x in range(100):
  for i in range(100):
    start_time = time.time()
    similar = suggestSimilar(posts[i])
    times.append(time.time() - start_time)
    print(f"Post {i}'s best match: ")
    print(f"Body text: {similar[0][0][0]}")
    print(f"Tags of match: {similar[0][0][1]}")
    print(f"Tags of original: {posts[i][1]}")
    print(f"Percent match: {similar[0][1]}%")
    print("\n")

print(f"{NateUtils.average(times)}sec per match completed")
