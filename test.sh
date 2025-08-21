#!/usr/bin/env bash
set -euo pipefail

echo "[TEST] Waiting for app to start ..."
attempts=0
until curl -fsS http://localhost:5000/health | grep -q '"status": "UP"'; do
  attempts=$((attempts+1))
  if [ $attempts -gt 60 ]; then   # wait up to 60 seconds
    echo "[TEST] App did not become healthy in time"; exit 1
  fi
  sleep 2
done
echo "[TEST] Health endpoint returned UP"
