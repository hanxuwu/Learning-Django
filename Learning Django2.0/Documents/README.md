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

  
















































































