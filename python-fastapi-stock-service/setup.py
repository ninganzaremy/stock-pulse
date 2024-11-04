from setuptools import setup
from setuptools.command.build_py import build_py as _build_py
import subprocess
import os
import sys

class build_py(_build_py):
    """
        build_py

        A custom build command for setuptools that extends the functionality of the standard build_py
        command to include gRPC code generation.

        Methods
        -------
        run():
            Executes the custom build process, including generating necessary directories and files,
            running gRPC code generation via the protoc tool, handling exceptions, and proceeding
            with the standard build_py process.
    """
    def run(self):
        print("Starting gRPC code generation...")
        # Ensure the output directory exists
        output_dir = 'grpc_auto'
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
            open(os.path.join(output_dir, '__init__.py'), 'w').close()
        # Run the gRPC code generation
        try:
            result = subprocess.run([
                'python', '-m', 'grpc_tools.protoc',
                '-I.', '--python_out=./grpc_auto', '--grpc_python_out=./grpc_auto',
                'service.proto'
            ], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            print("gRPC code generation succeeded.")
            print("stdout:", result.stdout)
            print("stderr:", result.stderr)
        except subprocess.CalledProcessError as e:
            print("gRPC code generation failed:")
            print("Return code:", e.returncode)
            print("stdout:", e.stdout)
            print("stderr:", e.stderr)
            sys.exit(1)
        _build_py.run(self)

setup(
    name='fastapi-service',
    version='0.1',
    packages=['grpc_auto'],
    cmdclass={'build_py': build_py},
    install_requires=[
        'fastapi',
        'grpcio',
        'grpcio-tools',
        'uvicorn[standard]',
        'psycopg2-binary',
        'SQLAlchemy'
    ],
)