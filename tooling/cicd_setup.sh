pip install -U pip setuptools wheel
pip install git+https://github.com/copier-org/copier@master  # copier==6.0.0a9
copier -f -r f615521
pip install -r tooling/requirements_cicd.txt
flit install
