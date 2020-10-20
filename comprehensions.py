videos = ["v1.mp4", "v2.mp4", "v3.mp4"]
links = ["https://xa.com/v1.mp4",
         "https://xa.com/v2.mp4", "https://xa.com/v3.mp4"]
ya_dict = dict()
ya_list = []
xa_list = [{idx+1: {"name": videos[idx], "link":links[idx]}}
           for idx in range(0, len(videos))]

print(xa_list)

for i in range(0, len(videos)):
  dict({i+1: {'name': videos[i], 'link': links[i]}})
  # print(ya)
  ya_list.append(dict({i+1: {'name': videos[i], 'link': links[i]}}))
  # print(ya_list)

print('\n',ya_list)
