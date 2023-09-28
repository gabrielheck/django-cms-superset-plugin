from django.contrib import admin
from django.forms import ModelForm, PasswordInput, forms
from .forms import EmbeddedDashboardForm
from .models import EmbeddedDashboard, RowLevelSecurityFilter

class RowLevelSecurityFilterInline(admin.StackedInline):
    model = RowLevelSecurityFilter
    extra = 0

class EmbeddedDashboardAdmin(admin.ModelAdmin):
    form = EmbeddedDashboardForm

    fieldsets = [
        ("Embedded Dashboard", {"fields": ["description", "superset_domain", "dashboard_id"]}),
        ("Display Settings", {"fields": ["hide_title", "hide_tab", "hide_chart_controls", "filters_visible", "filters_expanded", "width", "height"]}),
        ("Authentication", {"fields": ["username", "password"]}),
    ]

    inlines = [RowLevelSecurityFilterInline]

# Register your models here.
admin.site.register(EmbeddedDashboard, EmbeddedDashboardAdmin)
