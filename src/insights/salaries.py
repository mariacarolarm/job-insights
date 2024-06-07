from typing import Union, List, Dict
from src.insights.jobs import ProcessJobs


class ProcessSalaries(ProcessJobs):
    def __init__(self):
        super().__init__()

    def get_max_salary(self) -> int:
        max_salaries = [
            int(job['max_salary'])
            for job in self.jobs_list
            if job['max_salary'] and job['max_salary'].isdigit()
        ]
        return max(max_salaries) if max_salaries else 0

    def get_min_salary(self) -> int:
        min_salaries = [
            int(job['min_salary'])
            for job in self.jobs_list
            if job['min_salary'] and job['min_salary'].isdigit()
        ]
        return min(min_salaries) if min_salaries else 0

    def matches_salary_range(self, job: Dict, salary: Union[int, str]) -> bool:
        if 'min_salary' not in job or 'max_salary' not in job:
            raise ValueError("Keys not found in job")
        try:
            min_salary = int(job['min_salary'])
            max_salary = int(job['max_salary'])
            salary = int(salary)
        except (ValueError, TypeError):
            raise ValueError("Min and max salaries must be numeric")

        if min_salary > max_salary:
            raise ValueError("Min salary must be less than max salary")

        return min_salary <= salary <= max_salary

    def filter_by_salary_range(
        self, jobs: List[dict], salary: Union[str, int]
    ) -> List[Dict]:
        pass
