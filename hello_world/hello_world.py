from dagster import (
    execute_pipeline,
    pipeline,
    solid,
)


@solid
def get_name():
    return "Kan"


@solid
def hey(context, name: str):
    context.log.info(f"Hey, {name}!")


@pipeline
def hey_pipeline():
    hey(get_name())


if __name__ == "__main__":
    result = execute_pipeline(hey_pipeline)
