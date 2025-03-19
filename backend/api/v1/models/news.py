from django.contrib.auth.models import User
from django.db import models


class NewsCategory(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "news category"
        verbose_name_plural = "news categories"

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r})"


class News(models.Model):
    category = models.ForeignKey(
        NewsCategory,
        on_delete=models.CASCADE,
        related_name="news",
    )
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="news/")
    description_1 = models.TextField()
    description_2 = models.TextField()
    author = models.ForeignKey(
        User,
        related_name="author_news",
        on_delete=models.CASCADE,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "news"
        verbose_name_plural = "news"

    def __str__(self) -> str:
        return f"News '{self.title}' - author '{self.author}'"

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}("
            f"title={self.title!r}, "
            f"image={self.image!r}, "
            f"description_1={self.description_1!r}, "
            f"description_2={self.description_2!r}, "
            f"author={self.author!r}, "
            f"created_at={self.created_at!r}, "
            f"updated_at={self.updated_at!r})"
        )
