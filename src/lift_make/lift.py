import os
import sys
import importlib.util

import lift_make.print_color as Out
import lift_make.helpers as helpers
from lift_make.lift_class import LiftClass
import lift_make.template_lift_build as Template

def main():
    Out.print_info("- - - lift - - -")

    # CLI parsing
    if len(sys.argv) == 1:
        Out.print_help()
        exit()

    first_argument = sys.argv[1]
    second_argument = None
    if len(sys.argv) >= 3:
        second_argument = sys.argv[2]

    if first_argument == "init":
        Out.print_debug("> init")
        if not os.path.exists(os.getcwd() + "/lift_build.py"):
            with open(os.getcwd() + "/lift_build.py", "w") as file:
                file.write(Template.template)
                Out.print_info("> lift_build.py is created form a template")
        else:
            Out.print_error("> lift_build.py already exist")

    # Working dir which lift was called from, must contain lift_build.py
    lift_build_path = helpers.get_lift_build_path()
    if not os.path.isfile(lift_build_path):
        Out.print_error("lift_build.py is not found")
        exit()

    # Load the module using import_module
    spec = importlib.util.spec_from_file_location("lift_build", lift_build_path)
    lift_build_py = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(lift_build_py)

    # Passing default LiftClass to users lift_build.py->setup(lift) to conifigure
    build_LiftClass = LiftClass()
    Out.print_debug("> lift_build.py->setup(lift)")
    build_LiftClass = lift_build_py.setup(build_LiftClass)


    if first_argument == "build" or first_argument == "run":
        # build mode selection
        if second_argument == "release":
            Out.print_debug("> lift_build.py->build(\"release\")")
            lift_build_py.build(build_LiftClass, "release")
        else:
            Out.print_debug("> lift_build.py->build(\"debug\")")
            lift_build_py.build(build_LiftClass, "debug")
        # run the app's executable
        if first_argument == "run":
            Out.print_debug("> lift_build.py->run()")
            lift_build_py.run(build_LiftClass)
    elif first_argument == "test":
        Out.print_debug("> lift_build.py->test()")
        lift_build_py.test(build_LiftClass)
    elif first_argument == "clean":
        Out.print_debug("> lift_build.py->clean()")
        lift_build_py.clean(build_LiftClass)

if __name__ == "__main__":
    main()
