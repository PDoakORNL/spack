# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install tree-sitter-cmake
#
# You can edit this file again by typing:
#
#     spack edit tree-sitter-cmake
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class TreeSitterCmake(CMakePackage):
    """CMAKE parser for tree-sitter."""

    url = "https://github.com/uhya/tree-sitter-cmake"
    git = "git@github.com:uyha/tree-sitter-cmake.git"

    license("MIT", checked_by="PDoakORNL")

    version("0.7.0")

    depends_on("tree-sitter")
