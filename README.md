# ML_Project



Creating conda environment
``````````````
conda create -p venv
``````````````
``````````````
pip install -requirements.txt
``````````````

To add files to git
`````````````
git add . 
`````````````
or 
``````````````````
git add <fileName>
```````````````````

To check the activities in git
`````````````````````
git status
`````````````````````

To commit all changes
``````````````````````
git commit -m message
``````````````````````

to send changes to github
````````````````````
git push origin main
````````````````````

To create a CI/CD we need 3 things:
``````````````````````````````````````````
HEROKU_EMAIL = nanimca000@gmail.com
HEROKU_API_KEY = efba24ca-7fab-429c-a3f6-eea5ee0a6ca4
HEROKU_APP_NAME = house-price-detectionn
`````````````````````````````````````````````

Create a docker Image
```
docker build -t <img_name>:<Tag_name>
```

To see the docker images
```
docker images
```

Run docker Image
```
docker run -p 5000:5000 -e PORT=5000 <Img_Id>
```

To stop container 
```
docker stop <container_Id> 
```