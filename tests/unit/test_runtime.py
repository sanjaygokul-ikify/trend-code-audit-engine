import unittest
from packages.core import CodeBase, CodeAuditEngine

class TestCodeAuditEngineRuntime(unittest.TestCase):
    def test_runtime(self):
        code_base = CodeBase(['file1.py', 'file2.py'])
        engine = CodeAuditEngine(code_base)
        audit_plan = engine.analyze()
        self.assertIsNotNone(audit_plan)

if __name__ == '__main__':
    unittest.main() 