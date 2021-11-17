[source](https://github.com/jldiaz/mkdocs-plugin-tags)

!!! Note
    Don't live empty line in the page tag header this plug in throw unhandled exceptions
## install
```
pip install git+https://github.com/jldiaz/mkdocs-plugin-tags.git
```

## usages
### mkdocs.yaml

```yaml
plugins:
  - tags
```

### page
- Add to page header
```
---
title: node template
tags:
    - nodes
    - log
---
```