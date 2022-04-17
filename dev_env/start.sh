# This script starts the development environment.
#
# IT MUST BE RUN from the root of the repository.
#
# BEFORE USING THIS SCRIPT, you need to run 'build_linux.sh' in the 'dev_env' folder
# to build the image.
#
#    $ dev_env/start.sh

# ON WINDOWS, before running the next line, replace $(pwd) with %cd%

docker run -it -d -p 6000:6000 -v $(pwd):/host_files --name flask_srv flask_img /bin/bash

# Start the Flask server in the container

docker exec -it flask_srv bash -c "cd /host_files && python3 api.py"

# You should be able to reach the Flask server at http://localhost:6000/ using Postman (GET)
