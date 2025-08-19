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

- Tooling TEST, `pytest` and `pytest-cov`
```
pip install pytest pytest-cov
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
    },
    "[markdown]": {
        "editor.formatOnSave": false,
        "editor.formatOnType": false,
        "editor.formatOnPaste": false,
        "editor.codeActionsOnSave": {
          "source.fixAll": "never"
        }
    }	
}
```


- DEBUGGING
  - Use the Debug panel (Cmd/Ctrl + Shift + D)
  - Configure `launch.json` for custom debug configurations
  
  
## POETRY

- install GLOBALLY
```
pip install poetry
```

- Poetry manage multiple packages in configuration files: 
  - `requirements.txt` for pip, and 
  - `pyproject.toml` for Poetry.

- useful commands
```
poetry add pytest
poetry show
```

- Validate installation
```
$ poetry --version
Poetry (version 1.8.5)
```

- Show the default GLOBAL config:
```
$ poetry config list

cache-dir = "C:\\Users\\thend\\AppData\\Local\\pypoetry\\Cache"
experimental.system-git-client = false
installer.max-workers = null
installer.modern-installation = true
installer.no-binary = null
installer.parallel = true
keyring.enabled = true
solver.lazy-wheel = true
virtualenvs.create = true
virtualenvs.in-project = null
virtualenvs.options.always-copy = false
virtualenvs.options.no-pip = false
virtualenvs.options.no-setuptools = false
virtualenvs.options.system-site-packages = false
virtualenvs.path = "{cache-dir}\\virtualenvs"  # C:\Users\thend\AppData\Local\pypoetry\Cache\virtualenvs
virtualenvs.prefer-active-python = false
virtualenvs.prompt = "{project_name}-py{python_version}"
warnings.export = true    
```
- GLOBAL POETRY SETUP: **NOTE:** my windows environment has two version of python 3.8 and 3.11; by default
poetry picked up 3.8. Need to explicitly specify:
```
poetry config virtualenvs.prefer-active-python true
# NEED to check whether the following is STILL needed!!!
poetry env use python311
```
- GLOBAL POETRY SETUP: store the virtualenv in the same folder as the project
```
poetry config virtualenvs.in-project true
```

- PROJECT SETUP: generate `pyproject.toml` file
```
poetry init
```
- create virtual environment & add python module
```
poetry add <python_module_name>
```



