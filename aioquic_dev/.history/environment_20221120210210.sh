conda create -n cs536_final python=3.9 
. ~/miniconda3/etc/profile.d/conda.sh
conda activate cs536_final
echo "================ cs536_final environment activated ================"

conda install -c anaconda pip
echo "================ pip installed ================"

conda install numpy=1.23.1 -y
echo "================numpy = 1.23.1 installed ================"

conda install matplotlib=3.5.1 -y
echo "================ matplotlib 3.5.1 installed ================"

conda install -c conda-forge tensorboard=2.10.0 -y
echo "================ tensorboard 2.10.0 installed ================"

pip install gym[all]
echo "================ gym[all] installed ================"

# extra packages for development convenience
pip install pretty-errors
echo "================ pretty-errors installed ================"