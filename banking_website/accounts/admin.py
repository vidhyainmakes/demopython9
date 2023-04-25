from django.contrib import admin

from .models import BankAccountType, User, UserAddress, UserBankAccount,  District

admin.site.register(BankAccountType)
admin.site.register(User)
admin.site.register(UserAddress)
admin.site.register(UserBankAccount)

class DistrictAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(District,DistrictAdmin)




