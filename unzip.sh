inotifywait -m /home/ciaran/VScode/healthmailSocket/ -e create -e moved_to |
    while read path action file; do
        if [[ "$file" =~ .*zip$ ]]; then
            echo "$file"
        fi
    done
