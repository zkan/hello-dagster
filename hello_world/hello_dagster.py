from dagster import graph, op


@op
def get_name():
    return "dagster"


@op
def hello(name: str):
    print(f"Hello, {name}!")


@graph
def hello_dagster():
    hello(get_name())


if __name__ == "__main__":
    hello_dagster_job = hello_dagster.to_job()
    hello_dagster_job.execute_in_process()
