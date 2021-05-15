inotifywait -m /home/pi/HealthmailSocket/ -e create -e moved_to |
    while read path action file; do
        if [[ "$file" =~ .*zip$ ]]; then
            echo "$file"
	    sleep 3
            unzip "$file" -d "scriptsToPrint"
            for file in ./scriptsToPrint/*; do
               if [[ "$file" =~ .*html$ ]]; then
                echo "'$file' is html"
                python3 -m weasyprint "$file" "$file.pdf"
               lp -d  Brother_MFC-L2720DW_series_via_VNC_from_MPS01 $file.pdf
                rm "$file"  "$file.pdf"
               else
                echo "file is NOT html"
                lp -d  Brother_MFC-L2720DW_series_via_VNC_from_MPS01 $file
                rm "$file"
               fi;
            done;
        fi;
    done;
