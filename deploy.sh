# pip install --upgrade setuptools wheel
# pip install --upgrade twine

python setup.py sdist bdist_wheel
twine upload dist/*