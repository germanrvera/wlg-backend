import traceback
import sys


class ExceptionTraceback:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        # Force TemplateResponse to render so template errors are caught here,
        # not silently swallowed by gunicorn during response iteration.
        if hasattr(response, 'render') and callable(response.render) and not response.is_rendered:
            try:
                response.render()
            except Exception:
                print(
                    f"[TEMPLATE ERROR] {request.method} {request.path}\n"
                    + traceback.format_exc(),
                    file=sys.stdout,
                    flush=True,
                )
                raise
        return response

    def process_exception(self, request, exception):
        print(
            f"[VIEW ERROR] {request.method} {request.path}\n"
            + traceback.format_exc(),
            file=sys.stdout,
            flush=True,
        )
        return None
