import unittest
from packages.core import CodeBase
from services import Orchestrator

class TestAuditPipeline(unittest.TestCase):
    def test_audit_pipeline(self):
        code_base = CodeBase(['file1.py', 'file2.py'])
        orchestrator = Orchestrator(code_base)
        audit_plan = orchestrator.run()
        self.assertIsNotNone(audit_plan)
        self.assertIsInstance(audit_plan, CodeAuditEngine)

if __name__ == '__main__':
    unittest.main() 