# Learning-Django  

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


































