#!/bin/bash
set -euo pipefail

###### NEW PROCESS ######
# We are going to start using a github action to run the compression and generate
# the hashh. A rough outline of the new process is as follows:
# 1. Generate dated release as we do now
# 2. Copy generated release to releases/final/release.zip
# 3. Generate SHA1 checksum on release.zip
# 4. Write SHA1 checksum to releases/final/hash.txt
# 5. Copy current README to releases/final/

### Generate dated release ###
CURRENT_DATE=$(date "+%Y-%m-%d")
SEASON=$(tr -d '[:space:]' < season.txt)
SEASON_DIR="./$SEASON"
RELEASES_DIR="$SEASON_DIR/releases"
ZIPFILE="$RELEASES_DIR/$CURRENT_DATE.zip"

if [ -z "$SEASON" ]; then
    echo "season.txt is empty."
    exit 1
fi

if [ ! -d "$SEASON_DIR/assets" ]; then
    echo "Expected season assets at $SEASON_DIR/assets, but that directory does not exist."
    exit 1
fi

mkdir -p "$RELEASES_DIR"

echo "Compressing current pack..."
zip -r "$ZIPFILE" pack.mcmeta pack.png README.md
(
    cd "$SEASON_DIR"
    zip -r "../$ZIPFILE" assets/ -x "*.DS_Store"
)

### Copy dated release to releases/final/release.zip ###
FINAL_RELEASE_DIR="$RELEASES_DIR/final"
FINAL_RELEASE_ZIP="$FINAL_RELEASE_DIR/release.zip"
FINAL_RELEASE_SHA="$FINAL_RELEASE_DIR/hash.txt"

mkdir -p "$FINAL_RELEASE_DIR"

# Copy file
echo "Creating new release..."
rm -f "$FINAL_RELEASE_ZIP"
cp "$ZIPFILE" "$FINAL_RELEASE_ZIP"

### Generate SHA1 checksum ###
echo "Generating SHA1 checksum..."
if command -v sha1sum >/dev/null 2>&1; then
    CHECKSUM=$(sha1sum "$FINAL_RELEASE_ZIP" | awk '{print $1}')
else
    CHECKSUM=$(shasum -a 1 "$FINAL_RELEASE_ZIP" | awk '{print $1}')
fi

# Create file if needed
if ! [ -f "$FINAL_RELEASE_SHA" ]; then
    echo "hash.txt does not exist, creating..."
    touch "$FINAL_RELEASE_SHA"
fi

### Write SHA1 checksum to file ###
echo "Writing SHA1 checksum to file..."
echo "$CHECKSUM" > "$FINAL_RELEASE_SHA"

printf "\e[1;31mThe latest release has been generated at $ZIPFILE.\e[0m\n"
printf "\e[1;31mA final release has been generated at $FINAL_RELEASE_ZIP.\e[0m\n"
printf "\e[1;31mThe SHA1 checksum for the final release has been saved to $FINAL_RELEASE_SHA.\e[0m\n"
printf "\e[1;31mFor posterity, the generated checksum is $CHECKSUM.\e[0m\n"

### Copy README to releases/final
echo "Copying README.md to release..."
CURRENT_README="./README.md"
RELEASE_README="$FINAL_RELEASE_DIR/README.md"

# Copy file
rm -f "$RELEASE_README"
cp "$CURRENT_README" "$RELEASE_README"

### Commit release ###
