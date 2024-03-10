from django.db import models

# Create your models here.

class Todo(models.Model):
    todo_name = models.CharField(max_length=50)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.todo_name
  
    class Meta:
        db_table = 'todos'
