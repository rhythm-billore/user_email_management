# Use a lightweight base image with SQLite installed
FROM alpine:latest

# Install SQLite
RUN apk add --no-cache sqlite

# Set a working directory
WORKDIR /data

# Copy the SQLite database file to the container
COPY sqldb/data.db /data/data.db

# Expose the database file directory (optional for debugging or access)
VOLUME /data

# Default command to interact with the SQLite database
CMD ["sh", "-c", "sqlite3 /data/data.db 'CREATE TABLE IF NOT EXISTS email_table (id INTEGER PRIMARY KEY, email TEXT UNIQUE);' && tail -f /dev/null"]