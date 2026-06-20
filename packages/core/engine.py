from typing import List, Dict
from .types import CodeBase, AuditPlan, RiskMatrix
from .exceptions import AuditException, ValidationException
import logging

logger = logging.getLogger(__name__)

class CodeAuditEngine:
    def __init__(self, code_base: CodeBase):
        self.code_base = code_base
        self.audit_plan = None
        self.risk_matrix = None
    
    def analyze(self) -> AuditPlan:
        # Analyze the code base and generate an audit plan
        try:
            # Perform static analysis
            static_analysis_results = self._perform_static_analysis(self.code_base)
            # Generate audit plan based on static analysis results
            self.audit_plan = self._generate_audit_plan(static_analysis_results)
            return self.audit_plan
        except Exception as e:
            logger.error(f'Failed to analyze code base: {e}')
            raise AuditException('Failed to analyze code base')
    
    def _perform_static_analysis(self, code_base: CodeBase) -> List[Dict[str, str]]:
        # Perform static analysis on the code base
        # This could involve syntax checking, type checking, etc.
        # For simplicity, let's assume we have a function that performs static analysis
        # and returns a list of dictionaries containing the results
        analysis_results = []
        for file in code_base.files:
            try:
                analysis_results.append({'file': file, 'issues': self._analyze_file(file)})
            except Exception as e:
                logger.error(f'Failed to analyze file {file}: {e}')
                analysis_results.append({'file': file, 'issues': ['Error occurred during analysis']})
        return analysis_results
    
    def _analyze_file(self, file) -> List[str]:
        # Analyze a single file and return a list of issues
        # This could involve parsing the file, checking for syntax errors, etc.
        # For simplicity, let's assume we have a function that performs file analysis
        # and returns a list of issues
        issues = []
        # Check for syntax errors
        if not self._check_syntax(file):
            issues.append('Syntax error')
        # Check for type errors
        if not self._check_types(file):
            issues.append('Type error')
        return issues
    
    def _generate_audit_plan(self, static_analysis_results: List[Dict[str, str]]) -> AuditPlan:
        # Generate an audit plan based on the static analysis results
        # This could involve prioritizing files based on the number of issues, etc.
        # For simplicity, let's assume we have a function that generates an audit plan
        # and returns it
        audit_plan = AuditPlan()
        for result in static_analysis_results:
            if result['issues']:
                audit_plan.files_to_audit.append(result['file'])
        return audit_plan
    
    def validate(self) -> RiskMatrix:
        # Validate the code base based on the audit plan
        try:
            # Perform dynamic analysis
            dynamic_analysis_results = self._perform_dynamic_analysis(self.audit_plan)
            # Generate risk matrix based on dynamic analysis results
            self.risk_matrix = self._generate_risk_matrix(dynamic_analysis_results)
            return self.risk_matrix
        except Exception as e:
            logger.error(f'Failed to validate code base: {e}')
            raise ValidationException('Failed to validate code base')
    
    def _perform_dynamic_analysis(self, audit_plan: AuditPlan) -> List[Dict[str, str]]:
        # Perform dynamic analysis on the code base based on the audit plan
        # This could involve executing the code, checking for runtime errors, etc.
        # For simplicity, let's assume we have a function that performs dynamic analysis
        # and returns a list of dictionaries containing the results
        analysis_results = []
        for file in audit_plan.files_to_audit:
            analysis_results.append({'file': file, 'issues': self._analyze_file_dynamically(file)})
        return analysis_results
    
    def _analyze_file_dynamically(self, file) -> List[str]:
        # Analyze a file dynamically and return a list of issues
        # This could involve executing the file, checking for runtime errors, etc.
        # For simplicity, let's assume we have a function that performs dynamic file analysis
        # and returns a list of issues
        issues = []
        # Check for runtime errors
        if not self._check_runtime_errors(file):
            issues.append('Runtime error')
        return issues
    
    def _generate_risk_matrix(self, dynamic_analysis_results: List[Dict[str, str]]) -> RiskMatrix:
        # Generate a risk matrix based on the dynamic analysis results
        # This could involve prioritizing files based on the number of issues, etc.
        # For simplicity, let's assume we have a function that generates a risk matrix
        # and returns it
        risk_matrix = RiskMatrix()
        for result in dynamic_analysis_results:
            if result['issues']:
                risk_matrix.files_with_risks.append(result['file'])
        return risk_matrix
    
    def _check_syntax(self, file) -> bool:
        # Check the syntax of a file
        # This could involve parsing the file, checking for syntax errors, etc.
        # For simplicity, let's assume we have a function that checks the syntax
        # and returns True if the syntax is valid, False otherwise
        return True
    
    def _check_types(self, file) -> bool:
        # Check the types of a file
        # This could involve parsing the file, checking for type errors, etc.
        # For simplicity, let's assume we have a function that checks the types
        # and returns True if the types are valid, False otherwise
        return True
    
    def _check_runtime_errors(self, file) -> bool:
        # Check a file for runtime errors
        # This could involve executing the file, checking for errors, etc.
        # For simplicity, let's assume we have a function that checks for runtime errors
        # and returns True if there are no errors, False otherwise
        try:
            # Try to execute the file
            with open(file, 'r') as f:
                exec(f.read(), {}, {})  # <--- Added {} as default namespace and global variables
            return True
        except Exception as e:
            # If an exception occurs during execution, return False
            logger.error(f'Runtime error occurred in file {file}: {e}')
            return False
