from typing import List

class CodeBase:
    def __init__(self, files: List[str]):
        self.files = files

class AuditPlan:
    def __init__(self):
        self.files_to_audit = []

class RiskMatrix:
    def __init__(self):
        self.files_with_risks = []