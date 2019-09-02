import argparse

from api.client.params.impl.api_key import ApiKey


def main():
    arguments = argparse.ArgumentParser()
    arguments.add_argument("--api-key", required=True, help="API key from apidata.mos.ru")
    api_key = ApiKey(arguments)


if __name__ == "__main__":
    main()
