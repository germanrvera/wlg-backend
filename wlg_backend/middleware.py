import traceback
import sys


class ExceptionTraceback:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)

    def process_exception(self, request, exception):
        print(
            f"[TRACEBACK] {request.method} {request.path}\n"
            + traceback.format_exc(),
            file=sys.stdout,
            flush=True,
        )
        return None
