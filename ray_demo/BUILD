python_library(
    name = "raylib",
    sources=["*.py"],
    
    # dependencies = [],
)
pex_binary(
    dependencies=[":raylib"],
    entry_point="ray_demo.rayburst",
    #execution_mode='zipapp',
    name = "ray_demo",
    execution_mode= 'venv',
)