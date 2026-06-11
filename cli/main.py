import argparse
from packages.core import CodeBase
from services import Orchestrator


def main():
    parser = argparse.ArgumentParser(description='Code Audit Engine CLI')
    parser.add_argument('--code-base', help='Path to code base', required=True)
    args = parser.parse_args()
    code_base = CodeBase([args.code_base])
    orchestrator = Orchestrator(code_base)
    audit_plan = orchestrator.run()
    print(audit_plan.files_to_audit)