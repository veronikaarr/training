import zmq
context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://127.0.0.1:5000")

msg = "Hello World"
socket.send(msg)
print "Sending", msg
msg_in = socket.recv()