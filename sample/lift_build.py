
import os

from lift_make.lift_class import LiftClass
import lift_make.print_color as Out

Out.TOGGLE_DEBUG = True

def setup(lift):
    Out.print_debug(". Running lift_build.py->setup(lift)")
    # Project settings
    lift.app_name = "app"
    lift.dir_root = os.getcwd();
    lift.dir_source = "/src"
    lift.dir_build = "/build"
    lift.dir_lib = ""
    lift.dir_include = ""
    lift.libs = ""

    # Compiler settings
    lift.compiler = "clang"
    lift.flags_debug = lift.flags_default("debug")
    lift.flags_release = lift.flags_default("release")

    # Incremental compilation settings
    lift.incremental_compilation = True

    # Compilation & Linker settings
    lift.threads = 8

    # Compiler formatting
    lift.str_format_compiler = "{FLAGS} -c '{C_FILE}' -o '{O_FILE}'"
    lift.str_format_linker = "{DIR_LIB} {LIBS} {DIR_INCLUDE} {FLAGS} {OBJECTS} -o '{APP_NAME}'"
    
    return lift

def build(lift, mode):
    Out.print_debug(f". Running lift_build.py->build({mode})")
    lift.build(mode)

def run(lift):
    Out.print_debug(". Running lift_build.py->run()")
    args = [""]
    lift.run(args)

def clean(lift):
    Out.print_debug(". Running lift_build.py->clean()")
    lift.clean()

def test(lift):
    Out.print_debug(". Running lift_build.py->test()")
    lift.test()
    
if __name__ == "__main__":
    Out.print_error("This scipt is not designed do be executed with Python itself, its part of the lift build system")
