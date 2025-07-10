import typer

app = typer.Typer()


@app.command()
def test(
    endpoint: str = typer.Option(..., help="Model endpoint URL."),
    auth_key: str = typer.Option(None, help="Optional auth key.")
):
    typer.echo(f"Running test on {endpoint} with auth key={auth_key}")


if __name__ == "__main__":
    app()
