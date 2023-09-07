cd ./models/post_processing/pa/
python setup.py build_ext --inplace --verbose
cd ../pse/
python setup.py build_ext --inplace --verbose
cd ../ccl/
python setup.py build_ext --inplace --verbose
cd ../../../
