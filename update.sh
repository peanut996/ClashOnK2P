CORE_TYPE="mipsle-hardfloat"
REPO="Dreamacro/clash"
TAG=$(curl -s "https://api.github.com/repos/$REPO/releases/latest" | grep '"tag_name":' | sed -E 's/.*"([^"]+)".*/\1/')
ASSET_URL=$(curl -s "https://api.github.com/repos/$REPO/releases/tags/$TAG" | jq -r --arg CORE_TYPE "$CORE_TYPE" '.assets[] | select(.name | test($CORE_TYPE)) | .browser_download_url')
echo "Downloading $ASSET_URL"
curl -L -o clash.gz "$ASSET_URL"
gzip -d clash.gz
mv clash binary/