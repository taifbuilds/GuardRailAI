import typer
import sys
from guardrail_ai.adapters import get_adapter

app = typer.Typer(
    help="GuardRail AI - Evaluate LLM endpoints for jailbreak susceptibility and EU AI Act compliance"
)


@app.command()
def test(
    adapter: str = typer.Option(...,
                                help="Adapter type: openai or huggingface"),
    endpoint: str = typer.Option(..., help="Model endpoint URL"),
    auth_key: str = typer.Option(..., help="Authentication key"),
    prompt: str = typer.Option(..., help="Prompt to send to model")
):
    """
    Test adapter by running single inference.
    """
    typer.echo(f"Using adapter={adapter}, endpoint={endpoint}")
    try:
        adapter_instance = get_adapter(
            adapter, api_key=auth_key, endpoint=endpoint)
        response = adapter_instance.infer(prompt)
        typer.echo("Model response:")
        typer.echo(response)
    except Exception as e:
        typer.echo(f"Error during inference: {e}")


@app.command()
def evaluate(
    adapter: str = typer.Option(...,
                                help="Adapter type: openai or huggingface"),
    endpoint: str = typer.Option(..., help="Model endpoint URL"),
    auth_key: str = typer.Option(..., help="Authentication key"),
    prompts_file: str = typer.Option(
        "assets/eu_ai_prompts.yaml", help="Path to prompt set file"),
    output_file: str = typer.Option(
        "outputs/report.json", help="Path to save JSON report"),
    html_report: str = typer.Option(
        None, help="Path to save HTML report (optional)"),
    thresholds_file: str = typer.Option(
        "assets/thresholds.yaml", help="Path to thresholds configuration file")
):
    """
    Evaluate adapter on a prompt set and generate JSON report.
    Optionally generates HTML report and checks against thresholds.
    """
    from guardrail_ai.core import evaluate

    # If HTML report not specified, auto-generate path
    if html_report is None and output_file.endswith('.json'):
        html_report = output_file.replace('.json', '.html')

    exit_code = evaluate(
        adapter, endpoint, auth_key, prompts_file, output_file,
        thresholds_file=thresholds_file, html_output_file=html_report
    )

    # Exit with proper code for CI/CD integration
    if exit_code != 0:
        typer.echo("Evaluation failed to meet thresholds", err=True)
        sys.exit(exit_code)


@app.command()
def version():
    """
    Show version info.
    """
    typer.echo("GuardRail AI v0.1.0")
