from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    product_count = models.IntegerField(default=0)
    image = models.ImageField(upload_to="categories/")

    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"

    def __str__(self) -> str:
        return f"{self.name} - {self.product_count} products"

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}("
            f"name={self.name!r}, "
            f"product_count={self.product_count!r}, "
            f"image={self.image!r})"
        )
