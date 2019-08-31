import argparse


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--api-key", required=True, help="API key from apidata.mos.ru")
    args = vars(ap.parse_args())


if __name__ == "__main__":
    main()
