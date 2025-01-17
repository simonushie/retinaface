from setuptools import setup, find_packages

# pip install wheel           # 빌드 툴
# pip install setuptools     # 패키징 툴
# pip install twine            # 패키지 업로드 툴

packages = list(open('requirements.txt').readlines())
setup(
    name='retinaface',
    version='1.1.1',
    author='HEESEUNG KIM',
    author_email='heewin.kim@gmail.com',
    description='face detector',
    long_description=open('README.md', encoding="utf8").read(),
    long_description_content_type='text/markdown',
    license='MIT',
    url='https://github.com/heewinkim/retinaface',
    download_url='https://github.com/heewinkim/retinaface/archive/master.zip',
    packages=find_packages(),
    install_requires=open('requirements.txt', encoding="utf8").readlines(),
    package_data={'':['*']},
    python_requires='>=3',
    zip_safe=False,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
