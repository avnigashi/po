# frontend/Dockerfile
# Simple Dockerfile to serve the index.html using Nginx.

# Use the official Nginx image as a base
FROM nginx:stable-alpine

# Remove the default Nginx welcome page
RUN rm /usr/share/nginx/html/index.html

# Copy your index.html file into the Nginx web root directory
# Assumes index.html is in the same directory as this Dockerfile in your Git repo
COPY index.html /usr/share/nginx/html/index.html

# Expose port 80 (standard HTTP port for Nginx)
EXPOSE 80

# The default Nginx command runs automatically, so no CMD is needed here.
