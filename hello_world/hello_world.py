from dagster import pipeline, solid


@solid
def get_name():
    return "dagster"


@solid
def hello(context, name: str):
    context.log.info(f"Hello, {name}!")


@pipeline
def hello_pipeline():
    hello(get_name())
