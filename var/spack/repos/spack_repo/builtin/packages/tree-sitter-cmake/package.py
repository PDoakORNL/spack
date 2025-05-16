# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class TreeSitterCmake(CMakePackage):
    """CMAKE parser for tree-sitter"""

    url = "https://github.com/uhya/tree-sitter-cmake"
    git = "git@github.com:uyha/tree-sitter-cmake.git"

    license("MIT", checked_by="PDoakORNL")

    version("master", branch="master")

    depends_on("tree-sitter")
