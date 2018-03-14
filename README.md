# Deployment 

1. create a secrets.py file on root directory with the contents:
```py
MAILCHIMP_USERNAME = 'mailchimp-user@email.com'
MAILCHIMP_KEY = 'key'
MAILCHIMP_LIST_ID = 'list_id'
```
2. Build the docker image from root
```sh
docker build -t met-equity .
```
3. Push the docker image to your docker hub repo
```sh
# login first
docker login

# tag the image appropriately
docker tag met-equity <docker-hub-username>/met-equity:latest

# push the image to docker hub
docker push <docker-hub-username>/met-equity:latest
```

4. Deploy the image to Azure Webapps (Linux Docker) (https://docs.microsoft.com/en-us/azure/app-service/containers/tutorial-custom-docker-image#test-the-web-app)
```sh
az webapp create --resource-group <my-resource-group> --plan <my-app-service-plan> --name met-equity --deployment-container-image-name <docker-hub-username>/met-equity:latest
```

# Redeploy

To redeploy changes:
1. Build the docker image after making your changes
2. Push the image to docker hub
3. Restart the Linux Webapp and it will automatically pull the image down to redeploy
