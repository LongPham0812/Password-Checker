from django.db import models

# Create your models here.
class Password(models.Model):
    password_text = models.CharField(max_length=200)
    password_strength = models.IntegerField(default=0)
    password_attributes = models.JSONField(default=dict)

    def get_password_text(self):
        return self.password_text

    def get_password_strength(self):
        return self.password_strength

    def get_password_attributes(self):
        return self.password_attributes

    def __str__(self):
        return f"{self.password_text} {self.password_strength} {self.password_attributes}"