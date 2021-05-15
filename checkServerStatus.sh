if ! lsof -i -P -n | grep -q 5000; then
./server.py
fi
rm *zip;
