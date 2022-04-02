from dagster import graph, job, op


@op
def get_name():
    return "Kan"


@op
def hey(context, name: str):
    context.log.info(f"Hey, {name}!")


# @job
# def hey_job():
#     hey(get_name())

@graph
def hey_graph():
    hey(get_name())


# if __name__ == "__main__":
#     result = hey_job.execute_in_process()
