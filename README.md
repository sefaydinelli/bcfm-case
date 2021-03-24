# BestCloud Academy Study Case

## Sefa AYDINELLİ

### Setting Up Environment Variables

- For set your custom webhook url to /alert endpoint, create new file called ".env" in project directory.
In command promt :
```
nano .env
```
- Then add "WEBHOOK_URL" variable :
```
WEBHOOK_URL = "Your url at here!"
```
- Then save and close. (CTRL+X)


### Containerization

- We can build Docker images.

- In project directory : 
```
docker-compose build
```

- We can run that image with following command :
```
docker-compose up
```

- After that, project will be launching at https://localhost:80 .

### Azure Pipeline
- Project is building with Azure Pipelines and deploying to Azure Web Site : https://bcfmcase.azurewebsites.net/
