from django.db import models
from cms.models import CMSPlugin
import requests, uuid

class EmbeddedDashboard(models.Model):
    description = models.CharField(max_length=200, default="Dashboard description")
    superset_domain = models.CharField(max_length=200, default="http://localhost:8088")
    dashboard_id = models.CharField(max_length=200)
    hide_title = models.BooleanField(default=False)
    hide_tab = models.BooleanField(default=False)
    hide_chart_controls = models.BooleanField(default=False)
    filters_visible =  models.BooleanField(default=True)
    filters_expanded =  models.BooleanField(default=False)
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    width = models.CharField(max_length=6, default="90%")
    height = models.CharField(max_length=6,default="90%")

    def __str__(self):
        return self.description
    
    def fetchAccessToken(self):
        login_url = f"{self.superset_domain}/api/v1/security/login"

        login_payload = {
            "password": self.password,
            "provider": "db",
            "refresh": True,
            "username": self.username
        }

        login_response = requests.post(login_url, json=login_payload)

        if login_response.status_code == 200:
            access_token = login_response.json().get("access_token")
            return access_token
        else: 
            return ""
        
    def fetchGuestToken(self):
        try:
            access_token = self.fetchAccessToken()

            rls_filters = RowLevelSecurityFilter.objects.filter(embeddedDashboard = self)

            guest_token_url = f"{self.superset_domain}/api/v1/security/guest_token/"

            guest_token_payload = {
                "user": {
                    "username": "dev_svc_django.cms",
                    "first_name": "Django",
                    "last_name": "CMS"
                },
                "resources": [{
                    "type": "dashboard",
                    "id": self.dashboard_id
                }],
                "rls": [
                    # TODO: support jinja templating to create dynamic clauses
                    {"dataset": filter.dataset, "clause": filter.clause} if filter.dataset != 0 else {"clause": filter.clause}
                    for filter in rls_filters
                ]
            }

            headers = {
                "Authorization": f"Bearer {access_token}"
            }

            guest_token_response = requests.post(guest_token_url, json=guest_token_payload, headers=headers)

            if guest_token_response.status_code == 200:
                guest_token = guest_token_response.json().get("token")
                return guest_token
            else:
                return ""
        except Exception as err:
            # TODO: improve error handling
            return err


class RowLevelSecurityFilter(models.Model):
    embeddedDashboard = models.ForeignKey(EmbeddedDashboard, on_delete=models.CASCADE)
    dataset = models.IntegerField(default=0)
    clause = models.CharField(max_length=200, default="username = 'john.doe'")

class EmbeddedDashboardPluginModel(CMSPlugin):
    superset = models.ForeignKey(EmbeddedDashboard, on_delete=models.CASCADE)