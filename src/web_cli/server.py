import subprocess
from fastapi import APIRouter, FastAPI, HTTPException
from pydantic import BaseModel

from web_cli.schemas import GenericInput, GenericOutput

class CLIServer(BaseModel):
    command: str

    @property
    def router(self) -> APIRouter:
        router = APIRouter(
            prefix=f"/{self.command}",
            tags=[f"{self.command}"],
            responses={
                400: {"description": "Invalid input."},
                404: {"description": "CLI not found."},
            }
        )

        @router.post("/{cli}")
        def cli_main(cli: str, structured_input: GenericInput) -> GenericOutput:
            if cli != self.command:
                raise HTTPException(status_code=404, detail="The referenced cli is not registered.")

            args = to_command_args(structured_input)
            result = run_command(cli, args)
            return GenericOutput(stdout=str(result.stdout))

        @router.post("/{cli}/{subcommand}")
        def cli_subcommand(cli: str, subcommand: str, structured_input: GenericInput) -> GenericOutput:
            if cli != self.command:
                raise HTTPException(status_code=404, detail="The referenced cli is not registered.")

            args = to_command_args(structured_input)
            result = run_command([cli, subcommand], args)
            return GenericOutput(stdout=str(result.stdout))

        return router

def to_command_args(inputs: GenericInput) -> list[str]:
    kwargs = inputs.inputs
    args: list[str] = []
    for key, value in kwargs.items():
        args += f"--{key}"
        args += str(value)
    return args

def run_command(cli_tool: str | list[str], args: list[str]) -> subprocess.CompletedProcess[bytes]:
    if isinstance(cli_tool, list):
        proc_input = cli_tool + args
    else:
        proc_input = [cli_tool] + args
    result = subprocess.run(proc_input, capture_output=True)
    if result.returncode != 0:
        raise HTTPException(status_code=400, detail="Error encountered when running CLI!")
    return result

