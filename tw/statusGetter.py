from tw.status import Status, Type
import subprocess

class TWCheck:
    def get_status(self) -> Status:
        try:
            count = get_tasks_count_by_tag('+OVERDUE')
            if count > 0:
                return Status(Type.OVERDUE, count)
            count = get_tasks_count_by_tag('+TODAY')
            if count > 0:
                return Status(Type.TODAY, count)
            count = get_tasks_count_by_tag('+WEEK')
            if count > 0:
                return Status(Type.WEEK, count)
            count = get_tasks_for_review()
            if count > 0:
                return Status(Type.REVIEW, count)
            return Status(Type.OK, 0)
        except (RuntimeError, Exception):
            return Status(Type.ERROR, 0)

def get_tasks_count_by_tag(tag: str) -> int:
    return exec_extract_number(['task', tag, '+READY', 'count'])

def get_tasks_for_review() -> int:
    return exec_extract_number(['bash', '-c', 'task _reviewed | wc -l'])

def exec_extract_number(args) -> int:
    result = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if result.returncode != 0:
        print('Error during execution')
        print(result.stdout)
        print(result.stderr)
        raise RuntimeError("TW failed during execution")
    
    return int(result.stdout.strip())
