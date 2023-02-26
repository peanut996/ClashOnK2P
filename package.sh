folder_name="clash"

mkdir ${folder_name}
echo "mkdir done"

cp Country.mmdb config.yaml clash ${folder_name}
echo "cp done"

tar -czf clash.tar.gz ${folder_name}
echo "tar done"
