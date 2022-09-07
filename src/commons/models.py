from django.contrib.auth.models import User
from django.db import models
from crum import get_current_user

class Audit(models.Model):
    """Audit Model
    AuditModel acts as an abstract base class from which every
    other model in the project will inherit. This class provides
    every table with the following attributes:
        + created_at (DateTime): Stores the datetime the object was created.
        + modified_at (DateTime): Stores the last datetime the object was modified.
        + created_by (ForeignKey): Stores the user who created the object.
        + modified_by (ForeignKey): Stores the user who modified the object.
    """

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='creation date',
        help_text="date when the object was created",
        blank=True, null=True
    )
    modified_at = models.DateTimeField(
        auto_now=True,
        verbose_name='update date',
        help_text="date when the object was modified",
    )
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='%(class)s_created_by',
        null=True, blank=True,
        verbose_name='creation user',
        help_text="user who created the object",
    )
    modified_by = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='%(class)s_modified_by',
        null=True, blank=True,
        verbose_name='update user',
        help_text="user who performed the update",
    )

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        user = get_current_user()
        if user:
            if self.created_at is None and not user.is_anonymous:
                self.created_by = user
                self.modified_by = user
            elif not user.is_anonymous:
                self.modified_by = user
        super(Audit, self).save(*args, **kwargs)