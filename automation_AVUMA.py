import sh
import os

app_name = input("New app name：")
get_urls_url = input("copy which folder urls.py：")
get_base_url = input("Where is the file base.html or no：")

# new app
os.system("python manage.py startapp {}".format(app_name))

# copy urls.py
os.system('cp {}/urls.py {}'.format(get_urls_url, app_name))

# mkdir folderå
sh.cd(app_name)
sh.mkdir("templates")
sh.mkdir("static")
# sh.mkdir("media")

# skeleton.html
sh.cd("templates")
sh.mkdir(app_name)
sh.cd(app_name)

if get_base_url.lower() != "no" and get_base_url.lower() != "n":
    os.system('cp ../../../{}/templates/{}/default/base.html ./skeleton.html'.format(get_base_url, get_base_url))