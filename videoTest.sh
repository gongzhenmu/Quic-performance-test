videoName=$1
#loopCount=$2
echo "======== Video Name: $videoName ========" >> Videotimestamp.log;
for i in {1..5};
do
    ts=$(date +%s%N);
    /workdir/depot_tools/src/out/Debug/quic_client --host=10.0.0.1 --port=6121 --allow_unknown_root_cert https://www.example.org/$videoName;
    finalTime=$((($(date +%s%N) - $ts)/1000000));
    totalTime=$((totalTime + finalTime));
    echo $finalTime >> Videotimestamp.log;
done
averageTime=$((totalTime / 5));
echo "averageTime: $averageTime" >> Videotimestamp.log;
echo "" >> Videotimestamp.log;
