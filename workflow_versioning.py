from prefect import flow, task

@task
def version_task():
    return "Version 2"

@flow
def versioned_workflow():
    print(version_task())
