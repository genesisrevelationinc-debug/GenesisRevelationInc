FROM python:3.11-slim

RUN apt-get update && apt-get install -y \
    curl iproute2 iptables \
    && rm -rf /var/lib/apt/lists/*

# Install Tailscale
RUN curl -fsSL https://tailscale.com/install.sh | sh

WORKDIR /app
COPY . /app

RUN pip install -r requirements.txt

ENV TS_STATE_DIR=/var/lib/tailscale

CMD tailscaled --state=${TS_STATE_DIR}/tailscaled.state & \
    sleep 2 && \
    tailscale up --authkey=${TAILSCALE_AUTHKEY} --hostname=fly-node --accept-routes=true --accept-dns=true && \
    uvicorn main:app --host 0.0.0.0 --port 8080
