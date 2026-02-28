# Linux_2026-1
# linux_test Services

This project contains two systemd services: a background RAM monitoring utility and a simple Python Flask web server. 

---

## 1. RAM Monitoring Service

* [cite_start]**Description**: "Servicio Para Monitorear El Uso De RAM" (Service to monitor RAM usage)[cite: 23].
* [cite_start]**Core Script**: `linux_test/ram_grab.sh`[cite: 12].
* [cite_start]**Service Unit**: `linux_test/ram-grab.service`[cite: 19].
* **Functionality**:
    * [cite_start]Runs a continuous Bash loop[cite: 15].
    * [cite_start]Checks memory usage using `free -h` and formats it with `awk`[cite: 16].
    * [cite_start]Logs the current time, used RAM, and available RAM to `/tmp/used_ram.log` every 15 seconds[cite: 16].
* **Systemd Configuration**:
    * [cite_start]Runs securely as a dynamic user (`DynamicUser=yes`)[cite: 23].
    * [cite_start]Requires read/write access to `/tmp` (`ReadWritePaths=/tmp`)[cite: 23].
    * [cite_start]Cleans up previous logs by running `rm -f /tmp/used-ram.log` before starting[cite: 23].
    * [cite_start]Restarts automatically 60 seconds after a failure[cite: 23].

---

## 2. Python Web Service

* [cite_start]**Description**: A "Simple Web Hello World" application[cite: 40, 41].
* [cite_start]**Core Script**: `linux_test/web-test.py`[cite: 5].
* [cite_start]**Template**: `linux_test/templates/index.html`[cite: 29].
* [cite_start]**Service Unit**: `linux_test/python_web.service`[cite: 36].
* **Functionality**:
    * [cite_start]Uses the Python Flask framework to initialize an application[cite: 9].
    * [cite_start]Defines a single route for the homepage (`'/'`)[cite: 10, 11].
    * [cite_start]Renders an HTML template displaying "Hello, Flask!"[cite: 11, 33].
* **Systemd Configuration**:
    * [cite_start]Waits for the network to be ready before starting (`After=network.target`)[cite: 41].
    * [cite_start]Runs securely as a dynamic user (`DynamicUser=yes`)[cite: 41].
    * [cite_start]Executes via `python3`[cite: 41].
    * [cite_start]Restarts automatically 60 seconds after a failure[cite: 41].
