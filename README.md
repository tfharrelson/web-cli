# web-cli

The package where you provide a CLI that you like to use, and the package produces a web server! This is great for taking projects originally designed for local computer execution, and porting them to the cloud, making them much more shareable and powerful.

## Background

How many packages have you seen that execute through a command-line interface (CLI)? In many academic fields and labs, it is very common to create a CLI that executes some scientific task. This is great for papers, but proves to not be very useful for others to use and share. It ties your existing project dependencies (including compute resources) with the CLI tool, which is not always desired. It turns out that a lot of web infrastructure has already considered this sort of problem, and basically just says, your project can be completely distinct from the CLI and only has to interact through a contract layer where you are required to call out to a service in a specific way to get it to do what you want. Your application and the CLI application need not be executed on the same machine or even have the compute resources or installed dependencies.

The connection doesn't really matter, but common ones include REST and gRPC. In both cases, the compute application provides a spec for how to invoke it, and as long as you adhere to that spec (e.g. provide a valid JSON that is in the form expected by the app) you can call the application and not worry about the details.

This project tries to simplify the conversion from a CLI application to a webserver so that packages like scientific CLIs can be more easily shared and used by others.
