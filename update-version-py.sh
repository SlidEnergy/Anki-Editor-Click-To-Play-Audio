BRANCH=$(git rev-parse --abbrev-ref HEAD)
COMMIT=$(git rev-parse HEAD)
COMMIT_SHORT=$(git rev-parse --short HEAD)
if [ -n "$(git status --porcelain)" ]; then
    DIRTY="True"
else
    DIRTY="False"
fi
VERSION=$(git describe --tags --always --dirty)

rm -rf src/version.py
echo "BRANCH = \"$BRANCH\"" >> src/version.py
echo "COMMIT = \"$COMMIT\"" >> src/version.py
echo "COMMIT_SHORT = \"$COMMIT_SHORT\"" >> src/version.py
echo "DIRTY = $DIRTY" >> src/version.py
echo "VERSION = \"$VERSION\"" >> src/version.py
