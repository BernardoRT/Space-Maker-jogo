import cx_Freeze
executaveis = [ 
               cx_Freeze.Executable(script="main.py", icon="assets/icone.ico") ]
cx_Freeze.setup(
    name = "Space Maker",
    options={
        "build_exe":{
            "packages":["pygame"],
            "include_files":["assets"]
        }
    }, executables = executaveis
)

