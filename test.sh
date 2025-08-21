#!/usr/bin/env bash
set -euo pipefail

echo "[TEST] Waiting for app to start ..."
attempts=0
until RESPONSE=$(curl -s -o /tmp/resp.txt -w "%{http_code}" http://localhost:5000/health); do
  attempts=$((attempts+1))
  if [ $attempts -gt 30 ]; then
    echo "[TEST] App did not become healthy in time"
    exit 1
  fi
  sleep 2
done

BODY=$(cat /tmp/resp.txt)
if [[ "$RESPONSE" == "200" && "$BODY" == *"UP"* ]]; then
  echo "[TEST] Health endpoint returned UP"
  exit 0
else
  echo "[TEST] Unexpected response: HTTP $RESPONSE $BODY"
  exit 1
fi
