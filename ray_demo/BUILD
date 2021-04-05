python_library(
    name = "raylib",
    interpreter_constraints = ["CPython==3.8.*"]
)
pex_binary(
    dependencies=[":raylib"],
    entry_point="ray_demo.rayburst",
    name = "ray_demo",
    execution_mode= 'venv',
)
