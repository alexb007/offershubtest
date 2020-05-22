from __future__ import absolute_import, unicode_literals

from celery import shared_task
from django.apps import apps

from core import api
from offershubtest.celery import app


@app.task
def sync_model(object_id, object_type):
    model_class = apps.get_model(app_label='core', model_name=object_type)
    project_obj = model_class.objects.get(pk=object_id)
    handler = getattr(api, object_type)
    method = handler.update
    if not project_obj.gid:
        method = handler.create
    response = method(project_obj)
    print(response)
    return True

#
# @app.task
# def create_task(task_id):
#     Project = apps.get_model(app_label='core', model_name='Project')
#     project_obj = Project.objects.get(pk=project_id)
#     response = api.Project.create(project_obj)
#     return True
