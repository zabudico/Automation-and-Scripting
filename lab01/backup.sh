
#!/bin/bash

# Check number of arguments
if [ $# -lt 1 ] || [ $# -gt 2 ]; then
    echo "Error: Incorrect number of arguments."
    echo "Usage: $0 <source_directory> [backup_directory]"
    echo "Note: backup_directory defaults to /backup"
    exit 1
fi

# Assign arguments to variables
SOURCE_DIR="$1"
BACKUP_DIR="${2:-/backup}"

# Check if source directory exists
if [ ! -d "$SOURCE_DIR" ]; then
    echo "Error: Source directory '$SOURCE_DIR' does not exist."
    exit 1
fi

# Check if backup directory exists
if [ ! -d "$BACKUP_DIR" ]; then
    echo "Error: Backup directory '$BACKUP_DIR' does not exist."
    exit 1
fi

# Check write permissions for backup directory
if [ ! -w "$BACKUP_DIR" ]; then
    echo "Error: No write permission for directory '$BACKUP_DIR'."
    exit 1
fi

# Create filename with current date and time
TIMESTAMP=$(date +"%Y-%m-%d_%H-%M-%S")
BACKUP_FILENAME="backup_$(basename "$SOURCE_DIR")_$TIMESTAMP.tar.gz"
BACKUP_PATH="$BACKUP_DIR/$BACKUP_FILENAME"

# Create backup
echo "Creating backup of directory '$SOURCE_DIR'..."
if tar -czf "$BACKUP_PATH" -C "$(dirname "$SOURCE_DIR")" "$(basename "$SOURCE_DIR")" 2>/dev/null; then
    # Check size of created archive
    BACKUP_SIZE=$(du -h "$BACKUP_PATH" | cut -f1)
    echo "Backup successfully created: $BACKUP_PATH (size: $BACKUP_SIZE)"
else
    echo "Error: Failed to create backup."
    exit 1
fi
