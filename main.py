import NateUtils
import random, time, math
from operator import itemgetter
from difflib import SequenceMatcher

adj = ("Adorable", "Clueless", "Dirty", "Odd", "Stupid", "Cool", "Smart", "Normal", "Big", "Small")
nouns = ("puppy", "car", "rabbit", "girl", "monkey", "boy", "woman", "man", "horse" ,"creature","shark")
verbs = ("runs", "hits", "jumps", "drives", "barfs", "dances", "punches", "explodes", "destroys", "hides") 
adv = ("crazily", "dutifully", "foolishly", "merrily", "occasionally", "carelessly", "fearlessly", "scaredly")
punct = ("",".","!","?",":")

def addPost(text,tags):
  post = [text,tags]
  posts.append(post)

def suggestSimilar(current):
  toSuggest = []
  for item in posts:
    if current != item:
      percent = ((SequenceMatcher(None, item[0], current[0]).ratio()*100) + NateUtils.listSimilarity(item[1], current[1]))/2
      similarityData = [item,percent]
      toSuggest.append(similarityData)
  toSuggest.sort(key=itemgetter(1))
  return list(reversed(toSuggest))

def test():
  global iterations, posts, times, accuracy
  for x in range(iterations):
    for i in range(len(posts)):
      start_time = time.time()
      similar = suggestSimilar(posts[i])
      times.append(time.time() - start_time)
      accuracy.append(similar[0][1])
      print(f"Post {i} (iter {x})'s best match: ")
      print(f"Body text of original: {posts[i][0]}")
      print(f"Body text of match: {similar[0][0][0]}")
      print(f"Tags of match: {similar[0][0][1]}")
      print(f"Tags of original: {posts[i][1]}")
      print(f"Percent match: {similar[0][1]}%")
      print("\n")
      time.sleep(0.1)

posts = []
postNumber = 200
iterations = 2

for i in range(postNumber):
  tags = []
  for x in range(round(math.log(postNumber))):
    tags.append(f"Example Tag {random.randint(1, round(math.log(postNumber))*3)}")
  addPost(f"{adj[random.randint(0, len(adj)-1)] + ' ' + nouns[random.randint(0, len(nouns)-1)] + ' ' + verbs[random.randint(0, len(verbs)-1)] + ' ' + adv[random.randint(0, len(adv)-1)] + punct[random.randint(0, len(punct)-1)]}",tags)

times = [] # Speed test, caclulate average performance and accuracy, for posts of diffrent text
accuracy = []
test()

print(f"{NateUtils.average(times)}sec per match completed")
print(f"{NateUtils.average(accuracy)}% average accuracy")
print(f"{max(accuracy)}% most accurate match")

input("Enter to Continue")

posts = []
for i in range(postNumber):
  addPost(f"Example",[f"Example Tag {random.randint(1, round(postNumber/10))}",f"Example Tag {random.randint(1, round(postNumber/10))}",f"Example Tag {random.randint(1, round(postNumber/10))}",f"Example Tag {random.randint(1, round(postNumber/10))}",f"Example Tag {random.randint(1, round(postNumber/10))}"])

times = [] # Speed test, caclulate average performance and accuracy for posts of the same text
accuracy = []
test()

print(f"{NateUtils.average(times)}sec per match completed")
print(f"{NateUtils.average(accuracy)}% average accuracy")
print(f"{max(accuracy)}% most accurate match")
