from django.db import models
from utils.model_validations import validate_png


class DesignPatternSetup(models.Model):
    class Meta:
        verbose_name = 'Design pattern - Setup'
        verbose_name_plural = 'Design pattern - Setup'

    title = models.CharField(max_length=65)
    description = models.CharField(max_length=255)
    show_header = models.BooleanField(default=True)
    show_search = models.BooleanField(default=True)
    show_menu = models.BooleanField(default=True)
    show_description = models.BooleanField(default=True)
    show_pagination = models.BooleanField(default=True)
    show_footer = models.BooleanField(default=True)
    # Faviocon implementar no Aplicativo principal
    # App teste para implementaçao em developerpy.com.br
    favicon = models.ImageField(
        upload_to='assets/favicon/%Y/%m/',
        blank=True, default='',
        validators=[validate_png],
    )

    def __str__(self):
        return self.title


class MenuLink(models.Model):
    class Meta:
        verbose_name = 'Menu link'
        verbose_name_plural = 'Menu links'

    name = models.CharField(max_length=50)
    url_or_path = models.CharField(max_length=2048)
    target_tab = models.BooleanField(default=False)
    DPSetup = models.ForeignKey(
        DesignPatternSetup,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name
