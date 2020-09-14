# Backend
> BaseURL = "http://localhost:8000/"
## 1. Account
### 1) Sign Up
```
POST rest-auth/signup/
```
- Request
```json
{
    "email": "", 
    "password1": "",
    "password2": "",
}
```
- Response
```json
{
    "token": "jwt token",
    "user": {
        "pk": 1,
        "username": "",
        "email": "",
        "first_name": "",
        "last_name": ""
    }
}
```
### 2) Login
```
POST rest-auth/login/
```
- Request
```json
{
    "email": "", 
    "password": ""
}
```
- Response
```json
{
    "token": "jwt token",
    "user": {
        "pk": 1,
        "username": "",
        "email": "",
        "first_name": "",
        "last_name": ""
    }
}
```
### 3) Logout
```
POST rest-auth/logout/
```
- Request
```json
{
}
```
- Response
```json
{
    "detail": "로그아웃되었습니다."
}
```


   
    


