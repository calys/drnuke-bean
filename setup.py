from setuptools import setup, find_packages


setup(name = 'drnukebean',
      version = '0.1',
      description = "Dr Nukes's beancount arsenal",
      packages = find_packages(
            where='src',
            include=['drnukebean.importer'],
      ),
      package_dir = {'': 'src'},
      zip_safe = False)
