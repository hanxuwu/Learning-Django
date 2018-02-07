# Learning-Django  --TEST

## 1.Install Django2.0
`python`  
python 3.6.1  
`pip install Django==2.0`  
![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/INSTALL.PNG)  

## 2.Start project  
`django-admin startproject mysite`  
![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/STARTPROJECT.PNG)  

## 3.Create views    

## 4.Run  

`python manage.py runserver`  
![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/RUNSERVER.PNG)    
![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/OPENWEBSITE.PNG)   

## 5.Migrate  
initiall the datebase    
`python manage.py migrate`  

`python manage.py createsuperuser`  -- admin   -- wosh****1  
![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/ADMINISTRATION.PNG)   
## 6.Open the admin   

`127.0.0.1:8000/admin`  
the same effect    
`localhost:8000`  
![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/SITEADMIN.PNG)  

## 7.Django app  
`python manage.py startapp xxxxxxx`  

## 8.Add model in modelspy  

![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/ADDMODEL.PNG)  

## 9.Register in setting.py  
![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/REGISTERAPP.PNG)  

## 10.Makemigration  
`python manage.py makemigrations`  

`python manage.py migrate`  
![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/MIGRATION.PNG)  

## 11.Edit /article/admin.py  
![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/REGISTERAD.PNG)  

![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/ARTICLE.PNG)  
## 12.View and edit article  

![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/FIRST%20ARTICLE.PNG)   


## 13.Create view  
![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/CREATEVIEW.PNG) 

## 14.Addurl  
![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/MANAGEURL.PNG)  

## 15.View the page  
![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/VIEWTHEPAGE.PNG)  


## 16.Use object modify the view to get the article
  
![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/GETTHETILEANDCONTENT.PNG) 

![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/VIEWTITLEANDCONTENT.PNG)  


## 17.Add exception  
a. If Request the page doesn't exist  
![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/REQUESTNONEEXIST.PNG)  
b. Add throw exception  
![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/THROWEXCEPTION.PNG)  


c.  Request the page again  
![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/404ERROR.PNG)  

## 18.create template Folder in article  

a.newview  
![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/NEWVIEW.PNG)  
b.templates

![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/TEMPLATES.PNG)  

## 19.new simplified approach  
![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/SIMPLIFYVIEW.PNG)  


## 20.GET LIST  
a. Add list   
![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/VIEWLIST.PNG)  

b. List template  
![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/LISTTEMPLATE.PNG)  

c. Add it to path  
![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/ADDPATH.PNG)  

d.Open the website  
![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/VIEWLISTINPAGE.PNG)  

## 21 use for loop output the title  
a.template  
![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/LOOPTEMPLATE.PNG)    

b.view  
![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/VIEWLOOP.PNG)  

## 22.click title  
a. click titile  
![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/CLICKTITLE.PNG)   
b. Open article list  
![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/VIEWARTICLECLICK.PNG)  


## 23.use url's name simplify the path  
a. use url's name simplify the path  
![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/SIMPLIFYPATH.PNG)   
b.Open article list  
![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/VIEWARTICLECLICK.PNG)  


## 24.add urls.py  
a.create urls.py in article folder  
![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/ARTICLEURL.PNG)  

b.Modify the main urls  
![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/MYURL.PNG)  


## 25.modify  the back  
a.Before modify  
![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/BEFOREMODIFY.PNG)  

b. add a function  
![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/ADDFUNCTION.PNG)  

c.After modify  
![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/AFTERMODIFY.PNG)  

## 26.Add manage info  
a.Before  
![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/AFTERMODIFY.PNG)    

b.Add title   
![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/MODIFYADMIN.PNG)  

c.After  
![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/AFTER.PNG)  

## 27.Ordering  
a. add order keywords  
![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/ORDERING.PNG)  
b.After  
![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/AFTERORDERING.PNG)  

## 28.Use decorator  (same effect as 27)
![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/DECORATOR.PNG)   

## 29.Modify the datebase and update the database  
a.Backup the database  
![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/BACKUPDB.PNG)   

b.add the createtime to admin article  in models.py  
![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/ADDCREATETIME.PNG)  

c.If you don't makemigrations  
![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/IFNOTUPDATEDB.PNG)   

d.make mikegrations  
`python manage.py makemigrations`  
THERE IS NO DEFAULT VALUE  
![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/AFTERMAKEMIGRATION.PNG)    

e.There are 2 way to set the default  
__First Methon__:  timezone.now  
1.input  
`timezone.now`
2.add the column in admin.py   
![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/ADDCREATEINADMIN.PNG)  
3.migrate    

`python manage.py migrate`  

![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/AFTERADDED.PNG)    

__Second Methon__:default  
DELETE previous the 0002\_article\_created\_time.py in \_pycache\_ first   and restore the DB   
1.add default value  in admin.py  
![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/ADDDEFAULT.PNG)   

2.apply the new database  
`python manage.py migrate`  

3.After method 2  
![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/AFTERMETHOD2.PNG)  

## 30. Add last update time  
a.Add last update time  
![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/ADDLASTUPDATE.PNG)   
b.Add columnn  
![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/ADDLASTTIMECOLUMN.PNG)   

c.migrates  
`python manage.py migrate`   
![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/AFTERADDLASTUPDATE.PNG)   

## 31 Add author  
a.Add author in models.py  
![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/ADDAUTHOR.PNG)  

b.Add author column in admin.py  
![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/ADDAUTHORCOLU.PNG)  

c.Apply  
`python manage.py makemigrations`  
`python manage.py migrates`   
![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/AFTERADDAUTHOR.PNG)  

## 32 is deleted  

a.Add is_deleted  
![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/ADDISDELETE.PNG)  
b.Add it to showlist  
![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/ADDTOSHOWLIST.PNG)  

c.Mark is_deleted  
![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/DELETETRUE.PNG)  
the article list doesn't change  
![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/ARTICLEBEFORE.PNG)  


d.We need to add Filter the deleted one  in view.py  
![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/FILTERDELETED.PNG)   

then the page does not show the deleted one  
![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/NOSHOWDELETED.PNG)  



# Learning-Django  --Blog

## 1.install  environment  
a. Install virtual environment  
`pip install virtualenv`   
`pip list`  

b. create virtualenv  
`virtuallenv xxxxxxxx`  
c. start virtualenv  
`Scripts\activate`  
d.exit  
`deactivate`  

## 2.create virtualenv  
a.create virtualenv   
`virtualenv myblog_env`  
![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/myblog2a.PNG)  

b.automatically add these file  
![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/myblog2b.PNG)   

c. enter the virtualenv  
`cd myblog_env`  
`Scripts\activate`  
![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/myblog1c.PNG)  

d. install Django2.0  
![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/myblog2d.PNG)  

## 3. create the new project  
a.Start new project  
`django-admin startproject myblog`  
`cd myblog`  

b.Start app   
`python manage.py startapp blog`  
![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/myblog3b.PNG)  

c.After creation

![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/myblog3c.PNG)   


## 4. create superuser   
a. initalize the datebase  
`python manage.py migrate`  
b. create superuser   user:admin  pwd:wo* * * * * *1
`python manage.py createsuperuser`  

## 5. add new model  

a. add new model in models.py  
![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/myblog5a.PNG)  

b.register blog app in setting.py  
![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/myblog5b.PNG)  

c. make makemigrations  
`python manage.py makemigrations`  
![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/myblog5c.PNG)  

`python manage.py migrate`  
![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/myblog5c1.PNG)  

d. setting the admin  manage  in  admin.py  
![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/myblog5d.PNG)  

e. login  
`http://localhost:8000/admin/`  
![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/myblog5e.PNG)  

f.make it display the name(not <object1>),modify models.py  
![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/myblog5f.PNG)  

g. then add one blog  
![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/myblog5g.PNG) 


## 6. pip export the env name  
a. export the lib  
`pip freeze > requirements.txt`

b. install the lib  
`pip install -r requirements.txt`  

## 7. Create templates  
a.Create *template* folder in blog folder
b.Create *blog_list.html* in templates folder  
![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/myblog7b.PNG)  
c.Create *blog_detail.html* in templates folder  
![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/myblog7c.PNG)  

## 8. migrate the url  

a. creates *urls.py* in blog  
b. write the path and method  
![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/myblog8b.PNG)  
c. Add the urls in myblog  *urls.py*  
![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/myblog8c.PNG)  

## 9. modify *views.py* to create value  
![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/myblog9.PNG)    

## 10.  add urllinks
a. modify the *blog_list.html* to add links to blog  
![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/myblog10a.PNG)  

![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/myblog10a1.PNG)  



b.modify the *blog_detail.html* to add links to homepage   

![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/myblog10b.PNG)  

![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/myblog10b1.PNG)  


## 11. count the blogs in *blog_list.html*  
`<p>There are {{blogs|length}} blogs</p>`  
![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/myblog11.PNG)  

## 12a. use truncatechars in *blog_list.html*  
a.before use the truncate  
![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/myblog12a.PNG)  

b.after use the truncate  
`<p>{{blog.content|truncatechars:50}}</p>`  
![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/myblog12b.PNG)  

## 12b. use truncatechars add Date in *blog_detail.html*  

`<p>Author:{{blog.author}}</p>`  
`<p>Date:{{blog.create_time|date:"Y-m-d G:n:s"}}</p>`  
`<p>Catalog:{{blog.blog_type}}</p>`  
![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/myblog12b1.PNG)   

![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/myblog12b2.PNG)   

## 13. click the catalog it will show all the blogs in the catalog  
a. add path in *urls.py* in myblog folder  

![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/myblog13a.PNG)   

b. add function in *views.py* in myblog folder  

![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/myblog13b.PNG)   

c. add an html in templates named *blog_with_type.html*  
![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/myblog13c.PNG)  

d. add Alabel in *blog_detail.html*  
![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/myblog13d.PNG)  

f. The basic function  
![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/myblog27012018.gif)   


## 14 Create the common templates  
a.Create *base.html* in Templates folder  
`{% block title %}{% endblock %}`  
![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/myblog14a.PNG)  

b. Modify *blog_detail.html*  
`{% extends 'base.html'%}`  
![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/myblog14b.PNG)  

c. Modify *blog_list.html*  
![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/myblog14c.PNG)  

d. Modify *blog_with_type.html*  
![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/myblog14d.PNG)  

## 15.global templates  
a. Create global templates folder in myblog folder  
b. add it to *setting.py*  
![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/myblog15b.PNG)  
c. cut all the html templates to global templates  
d. create a *blog* Folder in global templates for better manage  
f. modify the path in *view.py*  
`return render_to_response('blog/blog_with_type.html',context)`  
![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/myblog15f.PNG)  

## 16.No need to use the blog list as the homepage
a. add url to homepage and bloglist in *base.html*  
![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/myblog16a.PNG)   
b. add path in *urls.py* in blog folder  
![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/myblog16b.PNG)   
c. modify the global *urls.py* in myblog folder change the home page  
![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/myblog16c.PNG)   

d.Create *view.py* in myblog folder to write the function of the home page  
![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/myblog16d.PNG)   

e.Create *home.html* in global template folder in myblog folder(the same path as*base.html*)    
![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/myblog16e.PNG)   

f. Now the blog looks like this:  
![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/myblog28012018.gif)  

## 17. Add CSS to decorate the website  
a. modify *base.html*  

use css    
`<style type="text/css">`    
name the navigator "nav"      
`<div class="nav">`    
hide the underline of the title    
`text-decoration:none;`   
make it a block and show in oneline  
`display:inline-block`  
make the navigator text black  
`color:#000000`  
dege distance
`padding: 5px 10px `  
![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/myblog17a.PNG)   
b. modify *home.html*   
![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/myblog17b.PNG)   
c. new the home page likes this:  
![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/myblog28a012018.gif)  

## 18. extract it to css  
a. Create folder *static* in myblog folder    
b. Create *base.css* in static folder     
c. Copy` <style type="text/css">` part to *base.css*   
![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/myblog18b.PNG)   
d. Modify *base.html* add  
`{% load staticfiles %}`  
`<link rel="stylesheet" href=""> `   
![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/myblog18d.PNG)   
e. add static path in *setting.py*  make Django find the css file  
![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/myblog18e.PNG)   
f. Create *home.css* in static folder   
![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/myblog18f.PNG)   
g. Modify *home.html* add  ccs style  
![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/myblog18g.PNG)   


## 19.initialize bootstrap  
a.Download bootstrap3.3.7
https://getbootstrap.com/   

b.copy it to static folder

c. delete the unnecessary files onlykeep:
*bootstrap.min.css*  
*bootstrap.min.css.map*
*bootstrap.min.js*
*font*

## 20. add bootstrap in *base.html*  
a.use basic template reference to http://getbootstrap.com/docs/3.3/getting-started/#download  
![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/myblog20a.PNG)  

`<link rel="stylesheet" href="{% static 'bootstrap-3.3.7/css/bootstrap.min.css' %}">`    
`<script type="text/javascript" src="{% static 'bootstrap-3.3.7/js/bootstrap.min.js' %}"></script>`    
`<html lang="en">`  
 ` <head>`  
   ` <meta charset="utf-8">`  
   ` <meta http-equiv="X-UA-Compatible" content="IE=edge">`  
    `<meta name="viewport" content="width=device-width, initial-scale=1">`  
b.download *jquery.min.js* from  https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js  copy to static folder  
`<script type="text/javascript" src="{% static 'jquery.min.js' %}"></script>`  
![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/myblog20b.PNG) 

c. introduce grid system  
![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/myblog20c.PNG)   

## 21.change to bootstrap's Navbar   http://getbootstrap.com/docs/3.3/components/#navbar  
a.reference of the Navbar  
![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/myblog21a.PNG)  
b. modify the *base.html*  
![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/myblog21b.PNG)   


c. delete the unnecessary in the *base.css*  
![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/myblog21c.PNG)  

d. Now we use bootstrap's Navbar it looks like  
![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/myblog29012018.gif) 


## 22.add navbutton  for the mobile devices
a. reference http://getbootstrap.com/docs/3.3/components/#nav  
![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/myblog21a.PNG)    

b. modify the *base.html*   
![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/myblog22b.PNG)  

c. Test the navbutton  
![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/MyBlog29012018.gif)


## 23. Mark The selected navbar  

a.Modify *base.html*  add  
![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/myblog23a.PNG)  
b.Modify *home.html*  add  
![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/myblog23b.PNG)  
c.Modify *blog_detail.html*  add `{% block nav_blog_active %}active{% endblock %}` 

d.Modify *blog_list.html*  add  `{% block nav_blog_active %}active{% endblock %}`

e.Modify *blog_with_type.html*  add `{% block nav_blog_active %}active{% endblock %}`  
![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/myblog23e.PNG)  

f.test:  
![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/myblog23f.PNG)  

## 24. Fix the navbar 
a.Before fix  
![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/myblog29b012018.gif)  

b. Add `navbar-fix-top` in *base.html*  
![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/myblog24b.PNG)  
c. The title was gone  
![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/myblog24c.PNG)  
d. Modify *base.css* change the margin.USE !important,otherwize it doesn't work  
![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/myblog24d.PNG)  
e. Test the navbar  
![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/myblog29c012018.gif)  

## 25. Grid system  
a. Reference to grid system  
![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/myblog25a.PNG)   

b.Modify *blog_list.html*  use container and grid system   then add content of blog catalog part  
![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/myblog25b.PNG)  
c. cut blog folder in templates to templates in myblog/blog folder     
d. Modify "views.py"  in /blog/myblog  
![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/myblog25d.PNG)  
e. Now it shold looks like  
![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/myblog25e.PNG)  

## 26. Add Panels  
a. Reference to Panel  https://getbootstrap.com/docs/3.3/components/#panels  
![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/myblog26a.PNG)  
b. modify *blog_list.html*   
c. delete the dot  
  `<ul style="list-style-type:none;">`  
d. reference to different device  
![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/myblog26d.PNG)    
e. make it fits the Small devices Tablets  
![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/myblog26e.PNG)  
f. test  panels  
![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/myblog31012018.gif)  

## 27. Extract the css  
a.Create *blog.css* in /myblog/static/  
![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/myblog27a.PNG)  

b.modify *blog_list.html*  
![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/myblog27b.PNG)  

c. migrate the *blog.css* to /blog  
Create the *static* folder in /myblog/blog  
copy the *blog.css* to static  

d.restart the server  

 
## 28. modify the margin and font  
a. Preview more words  
`<p>{{blog.content|truncatechars:200}}</p>`  
b. add new class "blog"  
![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/myblog28b.PNG)   
c.modify *blog.css*  
![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/myblog28c.PNG)   
d.There are one more line at the bottom  
![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/myblog28d.PNG)  
f. elimiate the last line  
![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/myblog28f.PNG)   
g. it should looks like  
![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/myblog28g.PNG)   

## 29. Add catalog and Data in blog list  
a. Add catalog  in  *blog_list.html*   
![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/myblog29a.PNG)  
b.  Modify *blog.css* change the margin  
![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/myblog29b.PNG)  
c. Now it looks like  
![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/myblog29c.PNG)  
d. Reference to button  https://getbootstrap.com/docs/3.3/components/#glyphicons-examples   
![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/myblog29d.PNG)  
e. Add catalog-tag,and time-tag  
`<span class="glyphicon glyphicon-star"></span>`  
![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/myblog29e.PNG)
f. Now it looks like  
![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/myblog01022018.gif)  

## 30. modify other pages  
a. Modify *blog_list.html*  
`<div class="panel-heading">{% block blog_list_title %} Blog List(There are {{blogs|length}} blogs){% endblock %} </div>`  
`<span class="glyphicon glyphicon-time"></span>{{blog.create_time|date:"Y-m-d H:n:s"}}`  
b. Modify *blog_with_type.html*  
![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/myblog30b.PNG)  

c. Modify *views.py* copy catalogs  
![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/myblog30c.PNG)  

d. Reference to Grid-offsetting https://getbootstrap.com/docs/3.3/css/#grid-offsetting   
![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/myblog30d.PNG)  
e. Modify *blog_detail.html* copy catalogs  
![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/myblog30e.PNG) 

f.Modify *blog.css*  
![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/myblog30f.PNG) 

g.test  
![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/myblog03022018.gif)  

## 31. Shell command  
a. open shell  
`python manage.py shell`  
b. check the current article  
`from blog.models import Blog`  
`dir()`    
`Blog.objects.all()`    
`Blog.objects.count()`  
![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/myblog31b.PNG)  
c. add new object  
![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/myblog31c.PNG)  
d. use loop add 30 blogs  
![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/myblog31d.PNG)   
e.now there are 35 blogs in total  
![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/myblog04022018.gif)   

## 32. add paginator  

a. open shell  
`python manage.py shell`  
b. import Paginator  but there is an warning  
`from django.core.paginator import Paginator`  
`from blog.models import Blog`   
![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/myblog32b.PNG)  

c. add meta in *models.py*  
![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/myblog32c.PNG)  

d. Migration the database  then migrate  
![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/myblog32d.PNG) 

e.now the list is in order  
f.Some command of Paginator  
![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/myblog32f.PNG)  
g. Modify *view.py* get the page num  
![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/myblog32g.PNG)  

h.modify *blog_list.html*  
![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/myblog32h.PNG)   

i.test the blog   
![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/myblog06022018.gif)  

## 33.add pagenumber button  


a.reference to bootstrap pageination https://getbootstrap.com/docs/3.3/components/#pagination    
![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/myblog33a.PNG)      

b. modify *blog_list.html*  
![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/myblog33b.PNG)

c. test  
![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/myblog06a022018.gif)  

## 34. fix the bug that blog_type doesn't show anything  
a. modify *blog_list.html*  
![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/myblog34a.PNG)  

b. modify *view.py*  
![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/myblog34b.PNG)  

## 35. highlight the button limit number of button and  add first last page
a. highlight the current page, modify *blog_list.html*   
![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/myblog35a.PNG)    
b. hide the pagenumber if there is too many pages, modify*view.py*  
![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/myblog35b.PNG)  
c. modify *blog_list.html*  
![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/myblog35c.PNG)  
d. test  
![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/myblog07022018.gif)  

## 36. add content of the pages  
a.modify *blog_list.html*  
![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/myblog36a.PNG)  

b.modify *blog.css*  align to center
![Image](https://github.com/hanxuwu/Learning-Django/blob/master/Learning%20Django2.0/Documents/SCREENSHOT/myblog36b.PNG)  



































































































  
















































































