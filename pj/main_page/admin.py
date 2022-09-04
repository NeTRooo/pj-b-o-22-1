from django.contrib import admin
from .models import Disciplines, DisciplinesActual, DisciplineHomeWork

#  
#  configuring the display
#  

# discipline, eng_discipline
class DisciplinesAdmin(admin.ModelAdmin):
    list_display = ('discipline', 'eng_discipline')
    list_display_links = ('discipline', 'eng_discipline')
    search_fields = ('discipline', 'eng_discipline')

# discipline, eng_discipline, actual_homework, actual_file
class DisciplinesActualAdmin(admin.ModelAdmin):
    list_display = ('discipline', 'eng_discipline', 'actual_homework')
    list_display_links = ('discipline', 'actual_homework')
    search_fields = ('discipline', 'eng_discipline')

# discipline, eng_discipline, actual_homework, actual_file
class DisciplineHomeWorkAdmin(admin.ModelAdmin):
    list_display = ('discipline', 'eng_discipline', 'actual_homework')
    list_display_links = ('discipline', 'actual_homework')
    search_fields = ('discipline', 'eng_discipline')

#  
#  Register model
#  

admin.site.register(Disciplines, DisciplinesAdmin)
admin.site.register(DisciplinesActual, DisciplinesActualAdmin)
admin.site.register(DisciplineHomeWork, DisciplineHomeWorkAdmin)