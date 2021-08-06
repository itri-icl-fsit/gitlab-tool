#!/usr/bin/env python
import argparse
import hashlib
import os

import gitlab


def get_file_hash(file_path: str) -> str:
    with open(file_path, 'br') as f:
        file_cont = f.read()
    hash_m = hashlib.sha256()
    hash_m.update(file_cont)
    return hash_m.hexdigest()


def upload_package(project: str, file_path: str, package_name: str, package_ver: str, package_file_name: str):
    gl = gitlab.Gitlab.from_config(config_files=[os.path.join(os.path.dirname(__file__), 'sit.ini')])
    proj = gl.projects.get(id=project)
    proj.generic_packages.upload(
        package_name=package_name,
        package_version=package_ver,
        file_name=package_file_name,
        path=file_path
    )


def main(args):
    file_hash = get_file_hash(args.file)
    upload_package(
        project=args.project,
        file_path=args.file,
        package_name=args.package_name,
        package_ver=args.package_ver,
        package_file_name=args.package_file_name if args.package_file_name else os.path.basename(args.file)
    )
    print(f'Package uploaded, sha256={file_hash}')


if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('--project', '-p', type=str, required=True,
                            help='project id (E.g., 24) or project path (E.g., bob/my-proj)')
    arg_parser.add_argument('--file', '-f', type=str, required=True,
                            help='file to upload')
    arg_parser.add_argument('--package_name', type=str, required=True,
                            help='package name')
    arg_parser.add_argument('--package_ver', type=str, required=True,
                            help='package version (E.g., 3.1.0-alpha)')
    arg_parser.add_argument('--package_file_name', type=str,
                            help='file name in package (default: basename of file to upload')
    main(arg_parser.parse_args())
