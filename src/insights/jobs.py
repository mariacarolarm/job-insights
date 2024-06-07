from typing import List, Dict
import csv


class ProcessJobs:
    def __init__(self) -> None:
        self.jobs_list = list()

    def read(self, path) -> List[Dict]:
        with open(path, 'r') as file:
            read = csv.DictReader(file)
            for row in read:
                self.jobs_list.append(row)
        return self.jobs_list

    def get_unique_job_types(self) -> List[str]:
        job_types = {
            job['job_type']
            for job in self.jobs_list
            if job['job_type']
        }
        return list(job_types)

    def filter_by_multiple_criteria(
         self, jobs: List[Dict], filter_criteria: Dict
    ) -> List[Dict]:
        if not isinstance(filter_criteria, dict):
            raise TypeError("Filter must be a dict")

        filtered_jobs = [
            job for job in jobs
            if all(
                job.get(key) == value
                for key, value in filter_criteria.items()
            )
        ]
        return filtered_jobs
