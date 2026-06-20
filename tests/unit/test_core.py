import unittest
from packages.core import CodeBase, CodeAuditEngine

class TestCodeAuditEngine(unittest.TestCase):
    def test_analyze(self):
        code_base = CodeBase(['file1.py', 'file2.py'])
        engine = CodeAuditEngine(code_base)
        audit_plan = engine.analyze()
        self.assertIsNotNone(audit_plan)
        self.assertIsInstance(audit_plan, type(engine.audit_plan))

if __name__ == '__main__':
    unittest.main() 