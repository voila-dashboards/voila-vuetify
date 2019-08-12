import sys
import os
from setuptools import setup
from setuptools.command.develop import develop
import contextlib

pjoin = os.path.join


# these are based on jupyter_core.paths
def jupyter_config_dir():
    """Get the Jupyter config directory for this platform and user.

    Returns JUPYTER_CONFIG_DIR if defined, else ~/.jupyter
    """

    env = os.environ
    home_dir = get_home_dir()

    if env.get('JUPYTER_NO_CONFIG'):
        return _mkdtemp_once('jupyter-clean-cfg')

    if env.get('JUPYTER_CONFIG_DIR'):
        return env['JUPYTER_CONFIG_DIR']

    return pjoin(home_dir, '.jupyter')


def user_dir():
    homedir = os.path.expanduser('~')
    # Next line will make things work even when /home/ is a symlink to
    # /usr/home as it is on FreeBSD, for example
    homedir = os.path.realpath(homedir)
    if sys.platform == 'darwin':
        return os.path.join(homedir, 'Library', 'Jupyter')
    elif os.name == 'nt':
        appdata = os.environ.get('APPDATA', None)
        if appdata:
            return os.path.join(appdata, 'jupyter')
        else:
            return os.path.join(jupyter_config_dir(), 'data')
    else:
        # Linux, non-OS X Unix, AIX, etc.
        xdg = env.get("XDG_DATA_HOME", None)
        if not xdg:
            xdg = pjoin(home, '.local', 'share')
        return pjoin(xdg, 'jupyter')


class DevelopCmd(develop):
    prefix_targets = [
        ("voila/templates", 'vuetify-base'),
        ("voila/templates", 'vuetify-default'),
        ("voila/templates", 'custom')
    ]
    def run(self):
        target_dir = os.path.join(sys.prefix, 'share', 'jupyter')
        if '--user' in sys.prefix:  # TODO: is there a better way to find out?
            target_dir = user_dir()
        target_dir = os.path.join(target_dir)

        for prefix_target, name in self.prefix_targets:
            source = os.path.join('share', 'jupyter', prefix_target, name)
            target = os.path.join(target_dir, prefix_target, name)
            target_subdir = os.path.dirname(target)
            if not os.path.exists(target_subdir):
                os.makedirs(target_subdir)
            rel_source = os.path.relpath(os.path.abspath(source), os.path.abspath(target_subdir))
            try:
                os.remove(target)
            except:
                pass
            print(rel_source, '->', target)
            os.symlink(rel_source, target)

        super(DevelopCmd, self).run()


# WARNING: all files generates during setup.py will not end up in the source distribution
data_files = []
# Add all the templates
for (dirpath, dirnames, filenames) in os.walk('share/jupyter/voila/templates/'):
    if filenames:
        data_files.append((dirpath, [os.path.join(dirpath, filename) for filename in filenames]))


setup(
    name='voila-vuetify',
    version="0.0.1a8",
    description="A vuetify template for voila",
    data_files=data_files,
    include_package_data=True,
    author='Mario Buikhuizen, Maarten Breddels',
    author_email='mbuikhuizen@gmail.com, maartenbreddels@gmail.com',
    url='https://github.com/QuantStack/voila-vuetify',
    keywords=[
        'ipython',
        'jupyter',
        'widgets',
        'voila'
    ],
    cmdclass={
         'develop': DevelopCmd,
   },
)
