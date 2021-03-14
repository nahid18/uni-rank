
from setuptools import setup, find_packages

with open('requirements.txt') as f: 
    requirements = f.readlines() 

long_description = 'Uni-rank provides you the latest list of university rankings around the world.' 

setup(name='uni-rank',
      version='0.1',
      description='Get latest university rankings',
      url='http://github.com/nahid18/uni-rank',
      author='Abdullah Al Nahid',
      author_email='nahidpatwary1@gmail.com',
      long_description = long_description, 
      long_description_content_type ="text/markdown", 
      license='GPL',
      packages=find_packages(),
      include_package_data = True,
      zip_safe=False, install_requires=['requests', 'pandas'])