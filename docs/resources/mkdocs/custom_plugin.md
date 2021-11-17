# Custom plugin

## project structure
```
├── deploy.sh
├── mkdocs_plugin_include
│   ├── __init__.py
│   ├── plugin.py
├── README.md
├── requirements.txt
├── setup.py
```

### `__init__.py`
```python
# load class name `CodeInclude` into project namespace
from .plugin import CodeInclude
```

### plugin.py
- override `on_page_markdown`

### setup.py
```python hl_lines="6"
# The following rows are important to register your plugin.
# The format is "(plugin name) = (plugin folder):(class name)"
# Without them, mkdocs will not be able to recognize it.
entry_points={
    'mkdocs.plugins': [
        'code_include = mkdocs_plugin_include.plugin:CodeInclude'
    ]
}
```

### usage
#### Source file
```
{{include("/home/user/projects/mkdocs-plugin-include/tests/test_file.txt")}}
```

- include in markdown part of source file between line 2-4
  
```
{ {include("/home/user/projects/mkdocs-plugin-include/tests/test_file.txt",2,4)} }
```

!!! warning
    Remove space between curly braces
#### Result
```
{{include("/home/user/projects/mkdocs-plugin-include/tests/test_file.txt",2,4)}}
```


## Resource
- [hello-dolly-mkdocs-plugin](https://github.com/fmaida/hello-dolly-mkdocs-plugin)
- [mkdocs-plugin-template](https://github.com/byrnereese/mkdocs-plugin-template)