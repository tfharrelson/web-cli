from pydantic import BaseModel

from web_cli.types import AllowedInput



class GenericInput(BaseModel):
    inputs: dict[str, AllowedInput]


class GenericOutput(BaseModel):
    stdout: str
