inotifywait -m /home/ciaran/VScode/healthmailSocket/ -e create -e moved_to |
    while read path action file; do
        if [[ "$file" =~ .*zip$ ]]; then
            echo "$file"
            unzip "$file" -d "scriptsToPrint"
            for file in ./scriptsToPrint/*; do
               if [[ "$file" =~ .*html$ ]]; then
                echo "'$file' is html"
                # python -m weasyprint "$file" "$file.pdf"
                #lp -d mcf... $file.pdf
                rm "$file" # "$file.pdf"
               else
                echo "file is NOT html"
                # python -m weasyprint "$file"
                rm "$file"
               fi;
            done;
        fi;
    done;