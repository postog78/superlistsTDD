Обеспечение работы нового сайта
===============================
## Необходимые пакеты
# nginx
# Python 3.6
# virtualenv + pip
# Git

например, в Ubuntu^
	sudo add-apt-repozitory ppa:fkrull/deadsnakes
	sudo apt-get install nginx git python36 python3.6-venv

# Конфигурация вирутального узла Nginx

# см. nginx.template.conf
# заменить SITENAME, например, на staging.my-domain.com

# Служба Systemd

# см gunicorn-systemd.template.service
# заменить SITENAME, например на staging.my-domain.com

## Структура папок:
#Если допустить, что есть учетная запись пользователя в /home/username

/home/username
___sites
   ___SITENAME
      ___database
      ___source
      ___static
      ___virtualenv

