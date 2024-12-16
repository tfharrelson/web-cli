import subprocess
from fastapi import FastAPI

from web_cli.server import CLIServer


def create_app(registered_cli: str) -> FastAPI:
    help_result = subprocess.run([registered_cli, "--help"])
    if help_result.returncode != 0:
        help_result = subprocess.run([registered_cli, "-h"])
        if help_result.returncode != 0:
            raise RuntimeError("CLI does not appear to be locally installed.")

    # now that all the routes have been defined return the app
    app = FastAPI()
    app.include_router(CLIServer(command=registered_cli).router)
    return app

