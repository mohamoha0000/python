import websocket

def on_open(ws):
    print("✅ Good")
    ws.close()

def on_error(ws, error):
    print("❌ Failed:", error)

def on_close(ws, close_status_code, close_msg):
    pass

if __name__ == "__main__":
    try:
        ws = websocket.WebSocketApp(
            "ws://proxyhttp-mmgp.onrender.com",  # Replace with your target WebSocket URL
            on_open=on_open,
            on_error=on_error,
            on_close=on_close
        )
        ws.run_forever()
    except Exception as e:
        print("❌ Exception:", e)
