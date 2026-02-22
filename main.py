from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/mesh-status")
def mesh_status():
    try:
        ip = subprocess.check_output(["tailscale", "ip"], text=True).strip()
        return {"tailscale_ip": ip}
    except Exception as e:
        return {"error": str(e)}
