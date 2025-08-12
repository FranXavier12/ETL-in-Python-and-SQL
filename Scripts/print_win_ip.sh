#(Get the Windows host IP as seen from WSL.)
#!/usr/bin/env bash
ip route | awk '/default/ {print $3; exit}'
