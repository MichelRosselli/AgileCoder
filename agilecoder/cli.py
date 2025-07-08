import argparse

from agilecoder.run_api import run_task


def main():
    parser = argparse.ArgumentParser(description='argparse')
    parser.add_argument('--config', type=str, default="Agile",
                        help="Name of config, which is used to load configuration under CompanyConfig/")
    parser.add_argument('--org', type=str, default="game",
                        help="Name of organization, your software will be generated in WareHouse/name_org_timestamp")
    parser.add_argument('--name', type=str, default="snake",
                        help="Name of software, your software will be generated in WareHouse/name_org_timestamp")
    parser.add_argument('--model', type=str, default="OLLAMA",
                        help="GPT Model, choose from {'GPT_3_5_TURBO','GPT_4','GPT_4_32K', 'GPT_3_5_AZURE','CLAUDE', 'OLLAMA'}")
    parser.add_argument('--task', type=str, default="prompt.txt",
                        help="Path to a text file containing the task prompt")
    args = parser.parse_args()
    if args.task:
        with open(args.task, 'r', encoding='utf-8') as f:
            args.task = f.read()
    run_task(args)


if __name__ == "__main__":
    main()
