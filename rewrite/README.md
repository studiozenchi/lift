Modules

```
lift-cli
lift-core
lift-ext
lift-io
lift-codegen
```

- cli - argument parsing, actual usage entrypoint
- core - depgraph, incremental, build plan, build rules
- io - file reading, writing, watching, shell execution
- lift-ext - extensions
- codegen - generate C code using attributes `// @lift(json) - generates a JSON encoder and decoder function`
