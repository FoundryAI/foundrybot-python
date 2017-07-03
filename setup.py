from setuptools import setup, find_packages
setup(
  name = 'foundrybot',
  packages = ['foundrybot'], # this must be the same as the name above
  version = '1.0',
  description = 'Foundrybot python bindings',
  author = 'Nick Gerner',
  author_email = 'nick@foundry.ai',
  url = 'https://github.com/FoundryAI/foundrybot-python', # use the URL to the github repo
  download_url = 'https://github.com/FoundryAI/foundrybot-python/archive/1.0.tar.gz',
  keywords = ['foundrybot', 'foundry.ai', 'foundrydc'], # arbitrary keywords
  classifiers = [],
  install_requires=[
    'requests',
    'pydash'
  ]
)