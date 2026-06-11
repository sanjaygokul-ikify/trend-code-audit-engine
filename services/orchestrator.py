from packages.core import CodeAuditEngine
from packages.utils import logging

class Orchestrator:
    def __init__(self, code_base):
        self.code_base = code_base
        self.engine = CodeAuditEngine(code_base)
        self.logger = logging.setup_logger(__name__)

    def run(self):
        try:
            audit_plan = self.engine.analyze()
            self.logger.info('Audit plan generated')
            return audit_plan
        except Exception as e:
            self.logger.error(f'Failed to run audit: {e}')
            raise