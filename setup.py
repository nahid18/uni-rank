
from setuptools import setup, find_packages

with open('requirements.txt') as f: 
    requirements = f.readlines() 

with open('README.md', encoding='utf-8') as readme, open('docs/history.md', encoding='utf-8') as history:
    DESCRIPTION = readme.read() + '\n#' + history.read()

DESCRIPTION_SHORT = 'Get the ordered list of USA universities based on their latest ranking.' 

setup(name='uni-rank',
      version='1.0.2',
      description=DESCRIPTION_SHORT,
      long_description = DESCRIPTION, 
      long_description_content_type ="text/markdown", 
      url='https://github.com/nahid18/uni-rank',
      project_urls={'Documentation': 'https://github.com/nahid18/uni-rank/blob/main/README.md'},
      author='Abdullah Al Nahid',
      author_email='nahidpatwary1@gmail.com',
      license='GPLv3',
      packages=find_packages(),
      include_package_data = True,
      zip_safe=False, 
      keywords='ranking usa university',
          classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8'
        ],
    install_requires=['requests', 'pandas'])