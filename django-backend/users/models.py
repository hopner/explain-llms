from django.db import models
import uuid

class User(models.Model):
    guid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    model_config = models.JSONField(default=dict, blank=True)

    def save(self, *args, **kwargs):
        if 'selected_features' not in self.model_config:
            self.model_config['selected_features'] = []
        super().save(*args, **kwargs)
    
    def __str__(self):
        return str(self.guid)
    
    class Meta:
        db_table = 'users'
