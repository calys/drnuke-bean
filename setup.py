from setuptools import setup, find_namespace_packages


setup(name = 'drnukebean',
      version = '0.1.1',
      description = "Dr Nukes's beancount arsenal",
      packages = find_namespace_packages(
            where='src',
            #include=['drnukebean'],
      ),
      package_dir = {'': 'src'},
      zip_safe = False)
