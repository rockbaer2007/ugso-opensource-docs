#!/usr/bin/env bash
# Publish exactly the already verified Pages build. No second source tree.
set -euo pipefail

site=$(realpath "${1:?Built site directory required}")
test -f "$site/index.html"
test -f "$site/en/index.html"
test -f "$site/fr/index.html"
: "${MIRROR_DEPLOY_KEY:?Missing repository-scoped mirror deploy key}"
: "${GITHUB_SHA:?Missing source revision}"
: "${GH_TOKEN:?Missing GitHub token for authenticated host-key metadata}"

temporary=$(mktemp -d)
trap 'rm -rf "$temporary"' EXIT
umask 077
printf '%s\n' "$MIRROR_DEPLOY_KEY" > "$temporary/key"
unset MIRROR_DEPLOY_KEY
# Obtain GitHub's published host keys over authenticated HTTPS, not ssh-keyscan.
curl --fail --silent --show-error --retry 3 \
  -H "Authorization: Bearer $GH_TOKEN" \
  -H 'Accept: application/vnd.github+json' \
  https://api.github.com/meta > "$temporary/meta.json"
python3 -c 'import json,sys; print("".join("github.com " + key + "\n" for key in json.load(open(sys.argv[1]))["ssh_keys"]), end="")' "$temporary/meta.json" > "$temporary/known_hosts"
export GIT_SSH_COMMAND="ssh -i $temporary/key -o IdentitiesOnly=yes -o StrictHostKeyChecking=yes -o UserKnownHostsFile=$temporary/known_hosts"

git clone --quiet git@github.com:rockbaer2007/ugso-opensource-net.git "$temporary/repository"
rsync -a --delete --exclude='.git' "$site/" "$temporary/repository/"
cd "$temporary/repository"
printf '%s\n' 'ugso-opensource.net' > CNAME
touch .nojekyll
printf '{"source":"rockbaer2007/ugso-opensource-docs","revision":"%s","locales":["de","en","fr"]}\n' "$GITHUB_SHA" > deployment.json
git config user.name 'UGSo documentation deployment'
git config user.email '41898282+github-actions[bot]@users.noreply.github.com'
git add --all
if ! git diff --cached --quiet; then
  git commit --quiet -m "Publish documentation $GITHUB_SHA"
  git push origin HEAD:main
fi
