# docker images and layers

as we saw from the below, 

![imgandlayers](/reference-notes/docker-images-and-layers.jpg)

the layer is efficient in a way that if that layer exists already on the local image repo, it wont pull it again.


PS C:\Users\hafil\OneDrive\Documents\GitHub\docker\hands-on\docker-compose> docker pull acantril/containerofcats:latest \
latest: Pulling from acantril/containerofcats \
**0fa65fe5c23e: Already exists** \
216230e43a42: Pull complete \
8412c7539744: Pull complete \
64eb819ed8bb: Pull complete 
