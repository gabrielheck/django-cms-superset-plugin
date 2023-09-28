from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from .models import EmbeddedDashboardPluginModel
from django.utils.translation import gettext as _

@plugin_pool.register_plugin  # register the plugin
class EmbeddedDashboardPluginPublisher(CMSPluginBase):
    model = EmbeddedDashboardPluginModel
    module = _("django_cms_superset_plugin")
    name = _("Superset")  
    render_template = "django_cms_superset_plugin/superset_plugin.html"

    def render(selslf, context, instance, placeholder):
        context.update({'instance': instance,
                        'dashboard': instance.superset, 
                        'request': context['request']})
        return context

