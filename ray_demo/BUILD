python_library(
    name = "raylib",
  #  interpreter_constraints = ["CPython==3.8.*"]
)
pex_binary(
    dependencies=[":raylib"],
    entry_point="ray_demo.rayburst",
    name = "ray_demo",
    execution_mode= 'venv',
)
python_distribution(
  name="ray_dist",
  # Because this has no source code, Pants cannot infer dependencies.
  dependencies=[":raylib"],
  setup_py_commands=["bdist_wheel", "sdist"],
  provides=setup_py(
      name='rayburst_example',
      version='0.0.1',
      description='LOAD A RAY',
  ),
)