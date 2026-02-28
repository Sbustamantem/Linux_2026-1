# Linux_2026-1

# Linux Test Services

This project contains two automated systemd services: a background RAM monitoring utility and a lightweight Python Flask web server.

## Project Structure
```text
linux_test/
├── ram_grab.sh            # RAM monitoring logic
├── ram-grab.service       # Systemd unit for RAM monitor
├── web-test.py            # Flask application
├── python_web.service     # Systemd unit for Web server
└── templates/
    └── index.html         # Web page template
```

---

## 1. RAM Monitoring Service

**Description**: A background service that tracks system memory usage.

*   **Core Script**: `ram_grab.sh`
*   **Service Unit**: `ram-grab.service`
*   **Log Location**: `/tmp/used_ram.log`

### Functionality
- Runs a continuous Bash loop that executes every 15 seconds.
- Uses `free -h` and `awk` to extract "Used" and "Available" memory.
- Appends the current timestamp and memory stats to the log file.

### Systemd Configuration
- **Security**: Runs as a `DynamicUser` for maximum system isolation.
- **Permissions**: Explicitly granted `ReadWritePaths=/tmp` to allow logging.
- **Cleanup**: Runs `ExecStartPre=/usr/bin/rm -f /tmp/used_ram.log` to ensure a fresh log on service start.
- **Reliability**: Configured to automatically restart 60 seconds after any failure.

---

## 2. Python Web Service

**Description**: A "Hello World" Flask web application served via systemd.

*   **Core Script**: `web-test.py`
*   **Template**: `templates/index.html`
*   **Service Unit**: `python_web.service`

### Functionality
- Initializes a Python Flask application.
- Maps the root URL (`/`) to a function that renders a dynamic HTML template.
- Displays "Hello, Flask!" to users visiting the server.

### Systemd Configuration
- **Dependencies**: Waits for `network.target` to ensure the server is only started once the network is available.
- **Security**: Utilizes `DynamicUser=yes` to run the process without needing a dedicated system user.
- **Execution**: Invokes the script directly via `python3`.
- **Reliability**: Configured to restart 60 seconds after a crash.

---

## Installation & Deployment

To deploy these services on a Debian-based system:

1.  **Install Dependencies**:
    ```bash
    sudo apt update && sudo apt install python3-flask
    ```

2.  **Move Service Files**:
    ```bash
    sudo cp *.service /etc/systemd/system/
    ```

3.  **Reload and Start**:
    ```bash
    sudo systemctl daemon-reload
    sudo systemctl enable --now ram-grab.service
    sudo systemctl enable --now python_web.service
    ```

4.  **Verify**:
    - Check RAM logs: `tail -f /tmp/used_ram.log`
    - Check Web Server: Visit `http://localhost:5000`

---

### Key Improvements Made:
1.  **Naming Consistency**: I standardized `/tmp/used_ram.log` (you had a mix of underscores and hyphens in your draft).
2.  **Removal of Citations**: Removed the `[cite: X]` tags to make it look like a standard documentation file.
3.  **Deployment Section**: Added the `systemctl` commands. Since you asked about moving files and executing Python earlier, these are the most important instructions for a user.
4.  **Security Highlights**: Emphasized the `DynamicUser` aspect, as that is a very "pro" way to handle Linux services.
5.  **Visual Structure**: Added a "Project Structure" tree so the relationship between the scripts and templates is clear.
