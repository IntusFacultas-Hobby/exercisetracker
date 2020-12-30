from django.contrib import admin
# from nested_inline.admin import admin.ModelAdmin, admin.TabularInline
from core.models import (Workout, WorkoutTemplate, Activity, Performance, Unit)
# Register your models here.


class UnitInline(admin.TabularInline):
    model = Unit
    fk_name = "activity"
    extra = 1


class ActivityInline(admin.TabularInline):
    model = WorkoutTemplate.activities.through
    # inlines = [UnitInline]
    extra = 1


class ActivityAdmin(admin.ModelAdmin):
    inlines = [UnitInline]
    model = Activity
    search_fields = ['name']


class WorkoutTemplateAdmin(admin.ModelAdmin):
    model = WorkoutTemplate
    inlines = [ActivityInline]
    search_fields = ['name']


class PerformanceAdmin(admin.ModelAdmin):
    model = Performance
    search_fields = ["name", "description"]


class PerformanceInline(admin.TabularInline):
    model = Performance
    fk_name = "workout"
    extra = 1


class WorkoutAdmin(admin.ModelAdmin):
    model = Workout
    inlines = [PerformanceInline]


admin.site.register(Activity, ActivityAdmin)
admin.site.register(WorkoutTemplate, WorkoutTemplateAdmin)
admin.site.register(Performance, PerformanceAdmin)
admin.site.register(Workout, WorkoutAdmin)
