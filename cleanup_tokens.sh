days=7
authfile="$PWD/.storage/auth"
tmp=$(mktemp /tmp/abc-script.XXXXXX)
jq --arg s "$(date -d "-$days days" +"%Y-%m-%dT%H:%M")" 'del( .data.refresh_tokens[] | select(.last_used_at < $s) )' $authfile >$tmp && cp $tmp $authfile && rm $tmp