from django.db.models.signals import post_save

from .project import (
    Project,
)

from .task import (
    Task,
)
from .user import (
    AsanaUser,
)
from .workspace import Workspace

from .signals import (
    model_post_save,
    user_logged,
)
post_save.connect(model_post_save, sender=Project)
post_save.connect(model_post_save, sender=Task)
post_save.connect(model_post_save, sender=AsanaUser)
