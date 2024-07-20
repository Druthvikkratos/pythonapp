from django.db import models

from django.db import models

    
class Services(models.Model):
     service_name=models.CharField(max_length=50,verbose_name='Service Name')
     image = models.ImageField(upload_to='services/') 
     short_content=models.TextField(verbose_name='Short Content') 
     long_content=models.TextField(verbose_name='Long Content')
     url_name=models.CharField(max_length=50,verbose_name='URL Name',unique=True)
     
     class Meta:
            verbose_name_plural='Services' 

     def __str__(self):
            return self.service_name    
    
class Contact_Messages(models.Model):
    contact_name=models.CharField(max_length=50,verbose_name='Contact Name')
    email=models.EmailField(verbose_name='Email ID')
    subject=models.CharField(max_length=50,verbose_name='Subject')
    message=models.CharField(max_length=500,verbose_name='Message') 

    class Meta:
        verbose_name_plural='Contact Messages' 

    def __str__(self):
            return self.contact_name
 
    




    
    