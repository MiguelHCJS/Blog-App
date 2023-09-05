from django.contrib import admin
from django.http.request import HttpRequest
from blog_setup.models.AppDesignPattern.models import MenuLink, DesignPatternSetup


# @admin.register(MenuLink)
# class MenuLinkAdmin(admin.ModelAdmin):
#     list_display = 'id', 'name', 'url_or_path',
#     list_display_links = 'id', 'name', 'url_or_path',
#     search_fields = 'id', 'name', 'url_or_path',
class MenuLinkInline(admin.TabularInline):
    model = MenuLink
    extra = 1


@admin.register(DesignPatternSetup)
class AppDPSetupAdmin(admin.ModelAdmin):
    list_display = 'title', 'description',
    inlines = MenuLinkInline,

    def has_add_permission(self, request):
        return not DesignPatternSetup.objects.exists()
