from django.db import models

class Job(models.Model):
    title = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    description = models.TextField()
    job_type = models.CharField(max_length=100, choices=[('Full-Time', 'Full-Time'),('Part-Time', 'Part-Time'),('Internship', 'Internship'),('Contract', 'Contract')], default='Full-Time')
    education = models.CharField(max_length=255, default="B.Tech")
    experience=models.CharField(max_length=255,null=True)
    package=models.CharField(max_length=255,null=True)
    apply_url = models.URLField()
    posted_at = models.DateTimeField(auto_now_add=True)
    company_logo = models.ImageField(upload_to='company_logos/', blank=True, null=True)

    def __str__(self):
        return f"{self.title} at {self.company}"
