from click.testing import CliRunner
from src.app import app


def test_add():
    runner = CliRunner()
    result = runner.invoke(app.add, ["--numbers", "5", "10"])
    assert result.exit_code == 0
    assert "15" in result.output
