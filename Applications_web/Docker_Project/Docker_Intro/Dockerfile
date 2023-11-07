FROM python:3.11.4-alpine
COPY .. /app
WORKDIR /app
LABEL authors="etixi"
RUN pip install -r requirements.txt
CMD python app.py
ENTRYPOINT ["top", "-b"]

##### Creating a docker images
# ipconfig/ ip addr show
# docker build -t welcome-app .
# docker images
# docker run -p 5000:5000 welcome-app
# docker ps
# docker stop
# docker images

#### Push Docker Image To Docker
# docker images
# docker images rm -f welcome-app
# docker build -t etixi/welcome-app .
# docker images
# docker tag etixi/welcome-app etixi/welcome-app1 (rename image)
# docker images
# docker push etixi/welcome-app:latest
# docker images
# docker pull etixi/welcome-app:latest
# docker images
# docker run -d -p 5000:5000 welcome-app:latest

