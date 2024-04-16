Django server to predict NSFW image  
Ref: https://github.com/GantMan/nsfw_model
----------
Setting your .env to use
-------------
DEBUG=True

SECRET_KEY=

ALLOWED_HOSTS=*,

CREDENTIAL=

Use postman to test in localhost:8000/api/v1/predict/nsfw/
![image](https://github.com/tranhuynhkyanh/nsfw-django/assets/56480941/6e92a565-cf67-48fb-a3c7-2e5ad5344b54)
---------------
Admin is auto create when migrate (admin, 123456)
---------------------------------
http://127.0.0.1:8000/admin/predict/historypredict/
![image](https://github.com/tranhuynhkyanh/nsfw-django/assets/56480941/f48e5c15-6dfd-4fbc-b928-a335117b14ee)
