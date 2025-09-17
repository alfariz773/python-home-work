blog_views = [150,800,2500,600,1200,450,3000]
for view in blog_views:
    if view > 1000:
        print(view, "Trending")
    elif view >= 500 and view <= 1000:
         print(view, "Average")
    else:
         print(view, "low traffic")

#the total number of views
blog =0
for a in blog_views:
        blog+=a
print(f"total viewrs {blog}")

#Count how many posts were “Trending”

posts =0
for b in blog_views:
    if b >1000:
        posts= posts + 1
print(f"number of trending posts {posts}")
    