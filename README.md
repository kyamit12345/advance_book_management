# advance_book_management
Intelligent Book Management


We can manage services via Docker Compose File.
1. Build Application from the Dockerfile & expose to port 8000
2. We can use PostgreSQL image & set envrionment variables for databse.


Steps to deploy to Web App in Azure:
1. create Azure Web App
2. Create Azure Container Registry 
3. Create a github actions pipeline for Build & deployment in github.
4. Using Dockerfile create the image & push it container registry via Build Pipeline.
5. Pull the image from container registry & push it to the web app.
6. Check web app is running successfully or not via its url.


