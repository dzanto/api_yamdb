from django.contrib import admin 
from api.models import Categories, Genres, Titles, Comment, Review
 
  
class CommentAdmin(admin.ModelAdmin):  
      
    list_display = ("review", "text",  "author", "pk")   
    


class ReviewAdmin(admin.ModelAdmin):  
      
    list_display = ("title", "text", "score", "author")   
      
class CategoriesAdmin(admin.ModelAdmin):  
      
    list_display = ("name", "slug")   

class GenresAdmin(admin.ModelAdmin):  
      
    list_display = ("name", "slug")   


class TitlesAdmin(admin.ModelAdmin):  
      
    list_display = ("name", "year", "description", "category", 'pk')        
          
# при регистрации модели Post источником конфигурации для неё назначаем класс PostAdmin 

admin.site.register(Comment, CommentAdmin) 
admin.site.register(Review, ReviewAdmin) 
admin.site.register(Categories, CategoriesAdmin) 
admin.site.register(Genres,  GenresAdmin) 
admin.site.register(Titles,  TitlesAdmin) 
