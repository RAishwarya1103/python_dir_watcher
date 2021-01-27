import logging
from logging.handlers import RotatingFileHandler
from controller import service, task

logging.basicConfig(
    handlers=[RotatingFileHandler("./my_log.log", maxBytes=100000, backupCount=10)],
    level=logging.INFO,
    format="[%(asctime)s] %(levelname)s : %(message)s",
    datefmt="%Y-%m-%dT%H:%M:%S",
)


def main():
    """process:
    Fetch config details from API
    Start task - update db with start time and status as in progress
    process and update DB with with end time and status as success
    if exception occurs, update db with status as failed
    """
    try:
        config_details = service.get_config_detail()
        magic_string = config_details["magicString"]
        directory = config_details["directory"]
        id = config_details["id"]
        result = task.start_task_process(magic_string, directory, id)
    except Exception as e:
        logging.error(str(e))


if __name__ == "__main__":
    main()
