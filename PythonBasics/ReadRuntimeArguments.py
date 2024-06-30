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

    print(f"bootstrap_server - {bootstrap_server}")
    print(f"connect_server - {connect_server}")
    print(f"configFile - {properties_file}")
    print(f"kafka_installation_directory - {kafka_home_directory}")
    print(f"action - {action}")
    print(f"epoch_timestamp - {epoch_timestamp}")


if __name__ == '__main__':
    main()
