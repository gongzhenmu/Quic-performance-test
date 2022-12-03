conda create -n cs536_final python=3.9 
. ~/miniconda3/etc/profile.d/conda.sh
conda activate cs536_final
echo "================ cs536_final environment activated ================"

conda install -c anaconda pip=22.2.2 -y
echo "================ pip installed ================"

pip install aioquic=0.9.20 -y
echo "================aioquic installed ================"
