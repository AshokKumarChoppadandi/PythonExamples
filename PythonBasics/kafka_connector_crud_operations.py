from argparse import ArgumentParser
import json
import subprocess


def main():
    parser = ArgumentParser()

    parser.add_argument("-b", "--bootstrapServer", required=True, type=str, help="Kafka Bootstrap Server URL")
    parser.add_argument("-c", "--connectServer", required=True, type=str, help="Kafka Connect Server URL")
    parser.add_argument("-p", "--propertiesFile", required=True, type=str, help="Connector Config File")
    parser.add_argument("-H", "--kafkaHomeDir", required=False, type=str, default="/opt/dotomi/confluent",
                        help="Kafka Installation Directory")
    parser.add_argument("-a", "--action", required=False, type=str, default="dryRun",
                        help="Action to perform - allowed values are dryRun | execute | status | stop")
    parser.add_argument("-e", "--epochTimestamp", required=False, type=int,
                        help="Epoch Timestamp in milliseconds to reset Kafka Connector in GMT")

    args = parser.parse_args()

    bootstrap_server = args.bootstrapServer
    connect_server = args.connectServer
    properties_file = args.propertiesFile
    kafka_home_directory = args.kafkaHomeDir
    action = args.action
    epoch_timestamp = args.epochTimestamp

    """
    print(f"bootstrap_server - {bootstrap_server}")
    print(f"connect_server - {connect_server}")
    print(f"configFile - {properties_file}")
    print(f"kafka_installation_directory - {kafka_installation_directory}")
    print(f"action - {action}")
    """

    parsed_configs = parse_properties_file(properties_file=properties_file)

    connector_name = parsed_configs['name']
    print(f"Connector Name - {connector_name}")

    kafka_topic = parsed_configs['config']['topics']
    print(f"kafka_topics - {kafka_topic}")

    match action:
        case "dryRun":
            dry_run_command = get_reset_offsets_dry_run_command(kafka_home_directory, bootstrap_server, connector_name,
                                                                kafka_topic, epoch_timestamp)
            execute_command(dry_run_command)
        case "execute":
            if epoch_timestamp:
                reset_timestamps_command = get_reset_offsets_execute_command(
                    kafka_home_directory, bootstrap_server, connector_name, kafka_topic, epoch_timestamp)
                execute_command(reset_timestamps_command)
            else:
                print("Epoch timestamp is required to reset connector offsets. Re-run by providing "
                      "the epoch timestamp in GMT")
        case "status":
            status_command = get_connector_status_command(connect_server, connector_name)
            execute_command(status_command)
        case "stop" | "delete":
            stop_or_delete_connector_command = get_stop_or_delete_connector_command(connect_server, connector_name,
                                                                                    action)
            execute_command(stop_or_delete_connector_command)
        case "resume":
            resume_connector_command = get_resume_connector_command(connect_server, connector_name)
            execute_command(resume_connector_command)
        case "start":
            start_connector_command = get_start_connector_command(connect_server, properties_file)
            execute_command(start_connector_command)


def parse_properties_file(properties_file):
    file = open(properties_file)
    configs = json.load(file)
    return configs


def get_connector_status_command(connect_server, connector_name):
    return f"curl -X GET {connect_server}/connectors/{connector_name}/status"


def get_stop_or_delete_connector_command(connect_server, connector_name, action):
    return f"curl -X PUT {connect_server}/connectors/{connector_name}/{action}"


def get_resume_connector_command(connect_server, connector_name):
    return f"curl -X PUT {connect_server}/connectors/{connector_name}/resume"


def get_start_connector_command(connect_server, properties_file):
    return (f"curl -X POST -H \"Content-Type: application/json\" -H \"Accept: application/json\" "
            f"-d @'{properties_file}' {connect_server}/connectors")


def get_reset_offsets_dry_run_command(kafka_home_directory, bootstrap_server, connector_name, topics, datetime_to_reset,
                                      connector_prefix="connect-"):
    reset_offsets_command = get_reset_offsets_command(kafka_home_directory, bootstrap_server, connector_name, topics,
                                                      datetime_to_reset, connector_prefix)
    return f"{reset_offsets_command} --dry-run"


def get_reset_offsets_execute_command(kafka_home_directory, bootstrap_server, connector_name, topics, datetime_to_reset,
                                      connector_prefix="connect-"):
    reset_offsets_command = get_reset_offsets_command(kafka_home_directory, bootstrap_server, connector_name, topics,
                                                      datetime_to_reset, connector_prefix)
    return f"{reset_offsets_command} --execute"


def get_reset_offsets_command(kafka_home_directory, bootstrap_server, connector_name, topics, datetime_to_reset,
                              connector_prefix="connect-"):
    return (f"{kafka_home_directory}/bin/kafka_consumer_groups --bootstrap-server {bootstrap_server} --topic {topics} "
            f"--group {connector_prefix}{connector_name} --reset-offsets --to-datetime {datetime_to_reset}")


def execute_command(shell_command):
    shell_command_arr = shell_command.split(" ")
    # result = subprocess.run(shell_command_arr, capture_output=True, text=True).stdout
    # print(result)
    for cmd in shell_command_arr:
        print(cmd)


if __name__ == '__main__':
    main()
