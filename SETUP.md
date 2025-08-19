# SETUP Python Development Environment

## SETUP vscode

- Based on: 
  - [The Ultimate VS Code Setup for Python](https://medium.com/ordinaryindustries/the-ultimate-vs-code-setup-for-python-538026b34d94)
  - [Cursor Python](https://docs.cursor.com/en/guides/languages/python)

- Command Palette, remember this as it is used often, `Ctrl + Shift + P` (Windows/Linux), `Cmd + Shift + P` (Mac).
  - Type “User Settings” and select the JSON option from the command list.
  - To access the GUI settings click the gear icon in the lower-left corner of the VS Code window.

- See the article for Themes setup; also see [VS Code Themes](https://vscodethemes.com/)

- Set rulers (`settings.json`):
```
"editor.rulers": [
        88, 120
    ],
```

- EXTENSION [Python - ms-python](cursor:extension/ms-python.python)
  Python extension for Visual Studio Code;

- EXTENSION [Cursor Pyright](cursor:extension/anysphere.cursorpyright);
  this is CURSOR Python Language Server; already installed on cursor, NOT sure when it was installed
  but install it if not already!
  REMOVE Pylance to use Pyright

- EXTENSION [Python Debugger - my-python](cursor:extension/ms-python.debugpy)
  Python Debugger extension for Visual Studio Code; may have been installed with Python extension.

- EXTENSION [Ruff extension for Visual Studio Code - charliermarsh] 
  Linter: use Ruff because it's faster (other popular options: Flake8, PyLint)
  - install from the marketplace [Ruff](https://marketplace.visualstudio.com/items?itemName=charliermarsh.ruff)
  - Set rulers (`settings.json`):
```
    "[python]": {
		"editor.codeActionsOnSave": {
			"source.organizeImports": "explicit",
			"source.fixAll": "explicit"
		},
    }
    "notebook.formatOnSave.enabled": true,
    "notebook.codeActionsOnSave": {
        "notebook.source.organizeImports": "explicit"
        "notebook.source.fixAll": "explicit",
    },
```
  - **NOTE:** there is an existing code formatter "Prettier" for Javascript/Typescript
```
    "[javascript]": {
        "editor.defaultFormatter": "esbenp.prettier-vscode"
    }
```

- Extension Formatting: [Black](https://black.readthedocs.io/en/stable/index.html);
  (other popular options: YAPF, autopep8)
```
    "[python]": {
		"editor.defaultFormatter": "ms-python.black-formatter",
	}
```

- Tooling Type Checking
```
pip install mypy

{
  "python.linting.mypyEnabled": true
}
```

- Tooling TEST, `pytest`
```
pip install pytest
```

- Final `settings.json`
```
{
    "window.commandCenter": true,
    "cursor.cpp.enablePartialAccepts": true,
    "terminal.integrated.defaultProfile.windows": "Command Prompt",
    "editor.rulers": [
        88, 120
    ],
    "workbench.activityBar.orientation": "vertical",
    "editor.tabSize": 2,
    "editor.wrappingIndent": "indent",
    "editor.formatOnSave": true,
    "[python]": {
        "editor.defaultFormatter": "ms-python.black-formatter",
        "editor.codeActionsOnSave": {
            "source.organizeImports": "explicit",
            "source.fixAll": "explicit"
        },
    },
    "notebook.formatOnSave.enabled": true,
    "notebook.codeActionsOnSave": {
        "notebook.source.organizeImports": "explicit",
        "notebook.source.fixAll": "explicit",
    },
    "[javascript]": {
        "editor.defaultFormatter": "esbenp.prettier-vscode"
    }
}
```


- DEBUGGING
  - Use the Debug panel (Cmd/Ctrl + Shift + D)
  - Configure launch.json for custom debug configurations
  
  
## POETRY

- install
```
pip install poetry
```

- Poetry manage multiple packages in configuration files: 
  - `requirements.txt` for pip, and 
  - `pyproject.toml` for Poetry.


