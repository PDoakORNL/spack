# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class GdkPixbuf(Package):
    """The Gdk Pixbuf is a toolkit for image loading and pixel buffer
       manipulation. It is used by GTK+ 2 and GTK+ 3 to load and
       manipulate images. In the past it was distributed as part of
       GTK+ 2 but it was split off into a separate package in
       preparation for the change to GTK+ 3."""

    homepage = "https://developer.gnome.org/gdk-pixbuf/"
    git      = "https://gitlab.gnome.org/GNOME/gdk-pixbuf.git"
    url      = "https://gitlab.gnome.org/GNOME/gdk-pixbuf/-/archive/2.38.1/gdk-pixbuf-2.38.1.tar.gz"

    version('2.38.1', sha256='d9d4ee7a1b90fa28fca8f417b9eeef956479a5d1742b3cef837455ac3e58e116')
    version('2.38.0', sha256='dd50973c7757bcde15de6bcd3a6d462a445efd552604ae6435a0532fbbadae47')
    version('2.31.2', '6be6bbc4f356d4b79ab4226860ab8523')

    depends_on('docbook-xsl')
    depends_on('cmake@3.4.0:', type='build', when='@2.38.0:')
    depends_on('meson@0.50.0:', type='build', when='@2.38.0:')
    depends_on('meson@0.46.0:', type='build', when='@2.37.92:')
    depends_on('meson@0.45.0:', type='build', when='@2.37.0:')
    depends_on('ninja', type='build', when='@2.37.0:')
    depends_on('shared-mime-info', type='build', when='@2.36.8: platform=linux')
    depends_on('shared-mime-info', type='build', when='@2.36.8: platform=cray')
    depends_on('pkgconfig', type='build')
    depends_on('libx11', type='build')
    depends_on('xdm', type='build')
    # Building the man pages requires libxslt and the Docbook stylesheets
    depends_on('libxslt', type='build')
    depends_on('docbook-xsl', type='build')
    depends_on('gettext')
    depends_on('glib@2.38.0:')
    depends_on('jpeg')
    depends_on('libpng')
    depends_on('zlib')
    depends_on('libtiff')
    depends_on('gobject-introspection')

    # Replace the docbook stylesheet URL with the one that our
    # docbook-xsl package uses/recognizes.
    patch('docbook-cdn.patch')

    def setup_dependent_environment(self, spack_env, run_env, dependent_spec):
        spack_env.prepend_path("XDG_DATA_DIRS",
                               self.prefix.share)
        run_env.prepend_path("XDG_DATA_DIRS",
                             self.prefix.share)

    def install(self, spec, prefix):
        with working_dir('spack-build', create=True):
            meson('..', *std_meson_args)
            ninja('-v')
            if self.run_tests:
                ninja('test')
            ninja('install')

    def configure_args(self):
        args = []
        # disable building of gtk-doc files following #9771
        args.append('--disable-gtk-doc-html')
        true = which('true')
        args.append('GTKDOC_CHECK={0}'.format(true))
        args.append('GTKDOC_CHECK_PATH={0}'.format(true))
        args.append('GTKDOC_MKPDF={0}'.format(true))
        args.append('GTKDOC_REBASE={0}'.format(true))
        return args

    @when('@:2.36')
    def install(self, spec, prefix):
        configure('--prefix={0}'.format(prefix), *self.configure_args())
        make()
        if self.run_tests:
            make('check')
        make('install')
        if self.run_tests:
            make('installcheck')

    def setup_environment(self, spack_env, run_env):
        # The "post-install.sh" script uses gdk-pixbuf-query-loaders,
        # which was installed earlier.
        spack_env.prepend_path('PATH', self.prefix.bin)
