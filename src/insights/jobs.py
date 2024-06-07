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

    def filter_by_multiple_criteria(self) -> List[dict]:
        pass
