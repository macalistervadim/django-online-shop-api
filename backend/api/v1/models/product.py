from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(
        "Category",
        on_delete=models.CASCADE,
        related_name="products",
    )
    image = models.ImageField(upload_to="products/")

    class Meta:
        verbose_name = "product"
        verbose_name_plural = "products"

    def __str__(self) -> str:
        return f"{self.name} - {self.description[:50]}"

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}("
            f"name={self.name!r}, "
            f"description={self.description!r}, "
            f"price={self.price!r}, "
            f"category={self.category!r}, "
            f"image={self.image!r})"
        )
