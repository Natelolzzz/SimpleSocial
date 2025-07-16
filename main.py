import NateUtils
from operator import itemgetter
import random, time
from difflib import SequenceMatcher

posts = []

def addPost(text,tags):
  post = [text,tags]
  posts.append(post)

def suggestSimilar(current):
  toSuggest = []
  for item in posts:
    if current != item:
      percent = ((SequenceMatcher(None, item[0], current[0]).ratio()) * NateUtils.listSimilarity(item[1], current[1]))/2
      similarityData = [item,percent]
      toSuggest.append(similarityData)
  toSuggest.sort(key=itemgetter(1))
  return list(reversed(toSuggest))

posts = []
postNumber = 200
iterations = 2

for i in range(postNumber):
  addPost(f"Example {i}",[f"Example Tag {random.randint(1, round(postNumber/10))}",f"Example Tag {random.randint(1, round(postNumber/10))}",f"Example Tag {random.randint(1, round(postNumber/10))}",f"Example Tag {random.randint(1, round(postNumber/10))}",f"Example Tag {random.randint(1, round(postNumber/10))}"])

times = [] # Speed test, caclulate average performance and accuracy, for posts of diffrent text
accuracy = []
  
for x in range(iterations):
  for i in range(len(posts)):
    start_time = time.time()
    similar = suggestSimilar(posts[i])
    times.append(time.time() - start_time)
    accuracy.append(similar[0][1])
    print(f"Post {i}'s best match: ")
    print(f"Body text: {similar[0][0][0]}")
    print(f"Tags of match: {similar[0][0][1]}")
    print(f"Tags of original: {posts[i][1]}")
    print(f"Percent match: {similar[0][1]}%")
    print("\n")
    time.sleep(0.1)

print(f"{NateUtils.average(times)}sec per match completed")
print(f"{NateUtils.average(accuracy)}% average accuracy")

input("Enter to Continue")

posts = []
for i in range(postNumber):
  addPost(f"Example",[f"Example Tag {random.randint(1, round(postNumber/10))}",f"Example Tag {random.randint(1, round(postNumber/10))}",f"Example Tag {random.randint(1, round(postNumber/10))}",f"Example Tag {random.randint(1, round(postNumber/10))}",f"Example Tag {random.randint(1, round(postNumber/10))}"])

times = [] # Speed test, caclulate average performance and accuracy for posts of the same text
accuracy = []
  
for x in range(iterations):
  for i in range(len(posts)):
    start_time = time.time()
    similar = suggestSimilar(posts[i])
    times.append(time.time() - start_time)
    accuracy.append(similar[0][1])
    print(f"Post {i}'s best match: ")
    print(f"Body text: {similar[0][0][0]}")
    print(f"Tags of match: {similar[0][0][1]}")
    print(f"Tags of original: {posts[i][1]}")
    print(f"Percent match: {similar[0][1]}%")
    print("\n")
    time.sleep(0.1)

print(f"{NateUtils.average(times)}sec per match completed")
print(f"{NateUtils.average(accuracy)}% average accuracy")
