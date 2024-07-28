# Python CLI

A template for building Python CLIs.

## Prerequisites

- Python v3.9+

## Getting Started

### Development

1. Install the dependencies in editable mode:

   ```bash
   pip install -e .
   ```

2. Run the CLI:

   ```bash
   pycli --help
   ```

### Using the template

1. Fill the `pyproject.toml` based on your CLI specification:

   - `name`: The name of the project.
   - `authors`: Your name or your organization name.
   - `description`: A brief description of the CLI project.

2. Define a custom CLI executable (optional):

   ```toml
   [build-system]
   ...

   [project]
   ...

   [project.scripts]
   pycli = "cli.__main__:cli"
   ```

   Allows you to run your CLI through: `pycli <command>`.

   After changing the CLI executable, make sure to update the `Dockerfile` so your `ENTRYPOINT` matches your new executable.

3. Add the CLI description by changing the `cli()` method docstring at `cli/__main__.py`. This is the text that will be shown when calling `pycli --help`.

4. Create `click` commands within the `cli/commands` directory. For demo purposes, we have included the `cli/commands/demo.py` so you can see how `click` commands are defined.

5. Add your commands to the CLI by add the `click` command method in the `cli/__main__.py` as follow:

   ```python
   @click.group()
   @click.version_option(__version__.version)
   def cli():
      """
      CLI template for Python projects.
      """


   # Add commands to the CLI
   cli.add_command(cmd_sum) <---
   ```

6. Now you can run your command:

   ```bash
   # If you install the dependencies through "pip install .", use:
   python -m cli sum --num1 14 --num2 16

   # If you install the package itself through "pip install -e .", use:
   pycli sum --num1 14 --num2 16
   ```
