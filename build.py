from pybuilder.core import use_plugin, init, Author

use_plugin("python.core")
use_plugin("python.install_dependencies")
use_plugin("python.flake8")
use_plugin("python.coverage")
use_plugin("python.distutils")
use_plugin('pypi:pybuilder_pytest')
use_plugin('python.pycharm')
use_plugin('exec')

name = "awslambdahelper"
version = "1.0.0"
default_task = "publish"
authors = (Author("Drew J. Sonne", "drew.sonne@gmail.com",),)
license = "LGLP"

RUNTIME_DEPENDENCIES = ['boto3']
BUILD_DEPENDENCIES = ['pytest-pythonpath','pytest', 'pytest-mock','moto','pytest-runner']

@init
def init(project):

    for dependency in RUNTIME_DEPENDENCIES:
        project.depends_on(dependency)

    for dependency in BUILD_DEPENDENCIES:
        project.build_depends_on(dependency)

    # project.set_property("run_unit_tests_command", "py.test %s" % project.expand_path("$dir_source_unittest_python"))
    # project.set_property("run_unit_tests_propagate_stdout", True)
    # project.set_property("run_unit_tests_propagate_stderr", True)

    # directory with unittest modules
    project.set_property("dir_source_pytest_python", "src/unittest/python")
    # extra arguments which will be passed to pytest
    project.get_property("pytest_extra_args").append("-x")


    project.set_property("flake8_break_build", True)
    project.set_property("flake8_ignore", "F403")