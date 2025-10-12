import argparse
from dotenv import set_key, dotenv_values

def main():
    parser = argparse.ArgumentParser(
        description="Add or update variables in a .env file"
    )
    parser.add_argument(
        "--env-file",
        default=".env",
        help="Path to the .env file (default is .env)"
    )
    parser.add_argument(
        "key_values",
        nargs="+",
        help="Variables in key=value format"
    )

    args = parser.parse_args()

    existing_vars = dotenv_values(args.env_file)

    for arg in args.key_values:
        if '=' not in arg:
            print(f"❌ Invalid argument (expected key=value): {arg}")
            continue
        key, value = arg.split('=', 1)
        if key in existing_vars:
            print(f"✅ Key '{key}' already exists in {args.env_file}, skipping.")
            continue
        set_key(args.env_file, key, value, quote_mode="never")
        print(f"✅ Set {key}={value} in {args.env_file}")

if __name__ == "__main__":
    main()
