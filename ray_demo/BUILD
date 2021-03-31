python_library(
    name = "raylib",
    sources=["*.py"],
)
pex_binary(
    name = "rayburst",
    entry_point="ray_demo.rayburst",
    dependencies=[":raylib"]
)