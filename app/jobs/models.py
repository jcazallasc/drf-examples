from django.db import models


class JobOffer(models.Model):
    company_name = models.CharField(max_length=60)
    company_email = models.EmailField(max_length=120)
    job_title = models.CharField(max_length=60)
    job_description = models.TextField()
    salary = models.DecimalField(decimal_places=2, max_digits=8)
    city = models.CharField(max_length=60)
    state = models.CharField(max_length=60)
    available = models.BooleanField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} {}'.format(self.company_name, self.job_title)
