# swaggerTestV1
django+swagger 

命令：
django-admin startproject swagger_Test
cd api/
python manage.py startapp account
python manage.py startapp api
python manage.py migrate
python manage.py createsuperuser

settings.py
修改INSTALLED_APPS:
	添加account api APP
	
修改MIDDLEWARE_CLASSES：
	注释csrf中间件：#'django.middleware.csrf.CsrfViewMiddleware',
	
修改TEMPLATES：
	'DIRS': [os.path.join(BASE_DIR,'templates')],
	
增加：
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

修改api views
修改account views

修改urls



![图片说明1](https://github.com/huangzhif/swaggerTestV1/blob/master/static/image/1.png)

![图片说明1](https://github.com/huangzhif/swaggerTestV1/blob/master/static/image/2.png)
