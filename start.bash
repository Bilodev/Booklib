#!/bin/bash

script_dir="$( cd "$( dirname "$0" )" && pwd )"

# Move to the client directory
cd "$script_dir/client" || { echo "Error: client folder not found"; exit 1; }

# Run npm run dev in the client directory and keep it running in background
nohup npm run dev > /dev/null 2>&1 &

# Move to the parent directory
cd "$script_dir/server" || { echo "Error: server folder not found"; exit 1; }

# Run python3 app.py in the server directory and keep it running in background
nohup python3 app.py > /dev/null 2>&1 &

# Wait for a while to ensure the processes are started
# sleep 2

# Open Brave browser at localhost:3000/home
brave "http://localhost:3000/home"

# Keep the script running to ensure the processes remain active
