from __future__ import absolute_import, unicode_literals

from django.apps import apps

from core import api
from offershubtest.celery import app


@app.task
def sync_model(object_id, object_type):
    print(object_id, object_type)
    model_class = apps.get_model(app_label='core', model_name=object_type)
    model_obj = model_class.objects.get(pk=object_id)
    handler = getattr(api, object_type)()
    method = handler.update
    if not model_obj.gid:
        method = handler.create
    response = method(model_obj)
    if model_obj.gid is None:
        model_obj.gid = response['gid']
    model_obj.save(synced=True)
    return True


@app.task
def populate_user_data():
    User = apps.get_model(app_label='core', model_name='AsanaUser')
    Workspace = apps.get_model(app_label='core', model_name='Workspace')
    handler = api.User()
    user_data = handler.getMe()
    User.objects.update_or_create(gid=user_data['gid'], defaults={
        "name": user_data['name'],
    })

    workspaces = list(handler.getWorkspaces())
    for workspace_data in workspaces:
        Workspace.objects.update_or_create(gid=workspace_data['gid'], defaults={
            "name": workspace_data['name'],
        })
    return True

#

#
# @app.task
# def create_task(task_id):
#     Project = apps.get_model(app_label='core', model_name='Project')
#     project_obj = Project.objects.get(pk=project_id)
#     response = api.Project.create(project_obj)
#     return True
