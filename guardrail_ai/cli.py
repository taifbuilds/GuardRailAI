import typer

app = typer.Typer(
    help="GuardRail AI - Evaluate LLM endpoints for jailbreak susceptibility and EU AI Act compliance"
)


@app.command()
def test(
    endpoint: str = typer.Option(..., help="Model endpoint URL."),
    auth_key: str = typer.Option(None, help="Optional auth key.")
):
    """
    Dummy test command to verify CLI wiring.
    """
    typer.echo(f"Running test on {endpoint} with auth key={auth_key}")


@app.command()
def version():
    """
    Show version info.
    """
    typer.echo("GuardRail AI v0.1.0")
