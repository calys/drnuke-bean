from setuptools import setup, find_packages


setup(name = 'drnukebean',
      version = '0.1',
      description = "Dr Nukes's beancount arsenal",
      packages = find_packages(include=['src/drnukebean']),
      package_dir = {'drnukebean': 'src/drnukebean'},
      zip_safe = False)
