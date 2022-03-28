folder_name="clash-v1.5.0"

mkdir ${folder_name}
echo "mkdir done"

cp Country.mmdb config.yaml clash ${folder_name}
echo "cp done"

tar -czf clash-v1.5.0.tar.gz clash-v1.5.0
echo "tar done"
