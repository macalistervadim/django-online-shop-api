from django.db import models


class Feedback(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    message = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "feedback"
        verbose_name_plural = "feedbacks"

    def __str__(self) -> str:
        return f"{self.name} - {self.phone}"

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}("
            f"name={self.name!r}, "
            f"phone={self.phone!r}, "
            f"email={self.email!r}, "
            f"message={self.message!r}, "
            f"created_at={self.created_at!r})"
        )
