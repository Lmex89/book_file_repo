from django.db import models
import uuid

# Create your models here.
class BaseModel(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
    )
    visible = models.BooleanField(default=True)

    def soft_delete(self):
        """soft  delete a model instance"""
        self.visible = False
        self.save()

    class Meta:
        abstract = True
        ordering = ["-created_at"]

class Categorias(BaseModel):
    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4)
    title = models.CharField(max_length=250, null=False)

class Author(BaseModel):
    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4)
    title =models.CharField(max_length=250, null=False)

class ImgPortada(BaseModel):
    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4)
    portada = models.ImageField(upload_to='book/portada', blank=True, null=True)
    title = models.CharField(max_length=250, null=False, default="test")
    category = models.ForeignKey(Categorias, null=True, on_delete=models.SET_NULL)

class Book(BaseModel):
    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4)
    title = models.CharField(max_length=250, null=False)
