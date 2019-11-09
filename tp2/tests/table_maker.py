import csv


class TableMaker:
    def __init__(self, file_name: str = 'result.csv', header: [str] = None):
        self.file_name = file_name

        if header is None: return
        with open(self.file_name, 'w') as fd:
            writer = csv.writer(fd)
            writer.writerow(header)

    def append_row(self, data: []):
        with open(self.file_name, 'a') as fd:
            writer = csv.writer(fd)
            writer.writerow(data)
