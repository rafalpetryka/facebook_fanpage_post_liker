import facebook
with open('tokens.txt') as f:
    tokens = f.readlines()

for token in tokens:
  graph = facebook.GraphAPI(token)
  profile = graph.get_object("page_id_or_unique_name")
  posts = graph.get_connections(profile['id'], "posts")
  for post in posts['data']:
    try:
      graph.put_object(post['id'], "likes")
      print "Liking the topic: "
    except:
      print "Exception for topic : "
      continue
