import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="wechat_work_webhook",
    version="0.0.2",
    author="mqzhang",
    author_email="zmingqian@qq.com",
    description="A wechat work webhook client.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mqzhang/wechat_work_webhook_py",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=['requests']
)