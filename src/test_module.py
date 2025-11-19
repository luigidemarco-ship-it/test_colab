import os

class DFSRunner(object):
    def __init__(self):
        pass

    def process(self, file_path: str, file_name: str):
        # Implement DFS processing logic here
        pass

    def is_target_file(self, file_path: str) -> bool:
        # Implement logic to check if the file is a target file
        pass

    def dfs(self, start_path: str):
        # Implement DFS traversal logic here
        self._dfs(start_path)

    def _dfs(self, current_path: str):
        # Implement the recursive DFS logic here
        for file in os.scandir(current_path):
            if file.is_dir():
                self._dfs(file.path)
            elif self.is_target_file(file.path):
                self.process(file.path, file.name)


class DummyDFSRunner(DFSRunner):
    def __init__(self):
        super().__init__()

    def process(self, file_path: str, file_name: str):
        print(f"Processing file: {file_name} at path: {file_path}")

    def is_target_file(self, file_path: str) -> bool:
        return file_path.endswith('.txt')