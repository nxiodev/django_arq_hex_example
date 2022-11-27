from django.db import models


class TimestampedModel(models.Model):
    """
    Base model to add creation and update
    timestamp to models
    """

    fecha_creacion = models.DateTimeField(
        auto_now_add=True, editable=False, db_column="fecha_creacion"
    )
    fecha_edicion = models.DateTimeField(
        auto_now=True, editable=False, db_column="fecha_edicion"
    )

    class Meta:
        abstract = True