import datetime

from django.contrib import admin
from .models import Advertisement


# Register your models here.


class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'price', 'created_at', 'auction', 'image']
    list_filter = ['created_at', 'auction', 'title']
    actions = ['make_auction_as_false', 'make_auction_as_true']
    fieldsets = (
        ('Общее', {
            'fields': ('title', 'description', 'image', 'user'),
            'classes': ['collapse']
        }),

        ('Финансы', {
            'fields': ('price', 'auction'),
            'classes': ['collapse']
        })
    )

    def date(self, created_at):
        created_at = Advertisement.created_at
        if created_at == datetime.datetime.now(tz=None):
            Advertisement.created_at = f'Сегодня в {Advertisement.created_at}'


    @admin.action(description='Убрать возможность торга')
    def make_auction_as_false(self, request, queryset):
        queryset.update(auction=False)

    @admin.action(description='Добавить возможность торга')
    def make_auction_as_true(self, request, queryset):
        queryset.update(auction=True)


admin.site.register(Advertisement, AdvertisementAdmin)

