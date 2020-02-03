class MetaSingleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Processing(metaclass=MetaSingleton):
    def __init__(self):
        self.report = None

    def set_report(self, report):
        self.report = report

    def get_cluster(self):
        return self.report


class Model(object):  # todo SINGLETON class

    @staticmethod
    def send_report(report):
        print(report)  # todo initialization SINGLETON if python can
        Processing().set_report(report)

    @staticmethod
    def get_response():
        return "Отчёт принят!\n{}".format(Processing().get_cluster())
