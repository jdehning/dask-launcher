"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main() -> None:
    """Dask Launcher."""


if __name__ == "__main__":
    main(prog_name="dask-launcher")  # pragma: no cover
