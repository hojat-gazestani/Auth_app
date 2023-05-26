# Auth_app
* Microservice project

```bash
git clone https://github.com/hojat-gazestani/Auth_app.git && cd Auth_app
source auth/bin/activate

cd auth_project 
docker build  -t auth_app .
docker run -d --hostname AuthAPP20 -p 8020:8002 auth_app
docker run -d --hostname AuthAPP21 -p 8021:8002 auth_app
docker run -d --hostname AuthAPP22 -p 8022:8002 auth_app
```
