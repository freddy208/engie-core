import pytest

from engie_core.cli import main


@pytest.mark.parametrize(
    ("arguments", "expected_output"),
    [
        (["normalize", "Hello World"], "hello world\n"),
        (["normalize", "Hello    World"], "hello world\n"),
        (["normalize", ""], "\n"),
        (["count", "Hello World"], "2\n"),
        (["count", "Hello    World"], "2\n"),
        (["count", ""], "0\n"),
        (["slug", "Hello, World!"], "hello-world\n"),
    ],
)
def test_cli_commands_print_results(arguments, expected_output, monkeypatch, capsys):
    monkeypatch.setattr("sys.argv", ["engie", *arguments])

    exit_code = main()

    assert exit_code == 0
    assert capsys.readouterr().out == expected_output


def test_cli_help_exits_successfully(monkeypatch, capsys):
    monkeypatch.setattr("sys.argv", ["engie", "--help"])

    with pytest.raises(SystemExit) as error:
        main()

    assert error.value.code == 0
    assert "usage: engie" in capsys.readouterr().out


def test_cli_unknown_command_exits_with_error(monkeypatch, capsys):
    monkeypatch.setattr("sys.argv", ["engie", "unknown"])

    with pytest.raises(SystemExit) as error:
        main()

    assert error.value.code == 2
    assert "invalid choice" in capsys.readouterr().err
