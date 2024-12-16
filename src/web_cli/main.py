from typing import Annotated
import rich
import typer
import uvicorn

from web_cli.app import create_app

app = typer.Typer()


@app.command()
def main(
    command: Annotated[str, "The main entrypoint of the CLI that you want to create a webserver for"],
):
    rich.print(f"attempting to run a server with the command: {command}")
    try:
        app = create_app(command)
    except RuntimeError as e:
        raise RuntimeError("invalid something") from e
    uvicorn.run(app)


if __name__ == "__main__":
    app()

