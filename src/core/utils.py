from tomli import load


def get_from_pyproject_toml(pyproject_toml_path: str = 'pyproject.toml') -> tuple[str, str, str]:
    with open(pyproject_toml_path, 'rb') as file:
        pyproject_toml = load(file)
        poetry = pyproject_toml.get('tool', {}).get('poetry', {})
        name = poetry.get('name', 'CASHTAB')
        version = poetry.get('version', '0.0.1')
        description = poetry.get('description', '')

    return name, version, description
