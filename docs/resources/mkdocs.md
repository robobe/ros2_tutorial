# Setup mkdocs

## Pip
```bash
mkdocs-material
mkdocs-include-markdown-plugin
#mkdocs
#mkdocs-material-extensions
```

## Docs folder struct

```
└── docs
    ├── img
    │   └── course.png

```

## Basic mkdocs config
```yml
site_name: ROS Coockbook
theme:
  name: material
  
nav:
    - Home: index.md
    - Launch: basics.md
    - Gazebo:
        - Spwan: wines.md
        - Camera: wine.md
        - LIDAR: tastings.md
    - ROS2: addresses.md
        - Msg: msg.md
    - Resources: resources.md
    - About: about.md

markdown_extensions:
  - attr_list
  - pymdownx.caret
  - pymdownx.highlight
  - pymdownx.inlinehilite
  - pymdownx.tabbed:
      alternate_style: true
  - pymdownx.tasklist:
      custom_checkbox: true
  - pymdownx.snippets

plugins:
  - include-markdown
```

## Mkdocs commands
```
mkdocs serve
mkdocs build --clean
mkdocs gh-deploy
```

### Deploy to git hub
- In repository `settings` select `pages`
- Set source to branch `gh-pages` and folder to `/root`

![](../img/githubpages.png)


## Extentions
### attr_list
Allows to add HTML attributes and CSS classes to Markdown elements

``` yml
markdown_extensions:
  - attr_list
```

control image width and height
```
![](../img/course.png){ width=200, height=50) }
```

### Code block
``` yml
markdown_extensions:
  - pymdownx.snippets
```

#### usage

![](../img/embedded_code_block.png)


### Heightlite code
```yml
markdown_extensions:
  - pymdownx.highlight
  - pymdownx.superfences
```
#### usage
```
> ```python hl_lines="2"
import os
print("hightlite line")
> ```
```

#### result
```python hl_lines="2"
import os
print("hightlite line")
```

&nbsp;  
&nbsp;  
### Add line numbers
#### usage
```
> ```python linenums="1"
import os
print("hightlite line")
> ```
```
&nbsp;  
&nbsp;  
## images

```
![](../img/course.png){ width=200, height=50) }
```


## Plugins
### mkdocs-include-markdown-plugin
[project readme](https://github.com/mondeja/mkdocs-include-markdown-plugin)

```
{%
   include-markdown "../README.md"
%}

```