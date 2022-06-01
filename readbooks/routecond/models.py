from django.db import models

class Route(models.Model):
    routename = models.CharField(max_length=300)
    desc = models.CharField(max_length=500, null=True)

    def __str__(self):	
        return self.routename
        return self.desc

    def get_absolute_url(self):
        return f"/route/{self.pk}"
