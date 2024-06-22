
class LogBuffer:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(LogBuffer, cls).__new__(cls)
            cls._instance._logs = {}
        return cls._instance

    def add_log(self, key, message):
        self._logs[key] = message

    def get_logs(self):
        return self._logs

    def clear_logs(self):
        self._logs.clear()

log_buffer = LogBuffer()
