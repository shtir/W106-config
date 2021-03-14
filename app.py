from flask import Flask, render_template, request
from pyModbusTCP.client import ModbusClient

class W106:

    def __init__(self, address, port):
        c = ModbusClient()
        c.host(address)
        c.port(port)
        c.unit_id(1)
        c.open()
        if (True):
            data = c.read_holding_registers(130, 12)
            self.data=data
            c.close()
            if data:
                self.LowT1Start = format(data[0], 'x')
                self.LowT1Stop = format(data[1], 'x')
                self.LowT2Start = format(data[2], 'x')
                self.LowT2Stop = format(data[3], 'x')
                
                self.NormT1Start = format(data[4], 'x')
                self.NormT1Stop = format(data[5], 'x')
                self.NormT2Start = format(data[6], 'x')
                self.NormT2Stop = format(data[7], 'x')

                self.PeakT1Start = format(data[8], 'x')
                self.PeakT1Stop = format(data[9], 'x')
                self.PeakT2Start = format(data[10], 'x')
                self.PeakT2Stop = format(data[11], 'x')

            else:
                print("Read Volt And Amper ERROR")
                
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/setting')
def setting():
    #data=W106("192.168.88.15", 8080)
    print(request.args.get("name"))
    data = ""
    return render_template("setting.html", data=data)

@app.route('/form', methods=["POST"])
def form():
    class data:
        first_name = request.form.get("first_name")
        last_name = request.form.get("last_name")
        email = request.form.get("email")

    if not data.first_name or not data.last_name or not data.email:
        erro_statement = "All Form fild Required..."
        return render_template("setting.html", data=data, error_statement=erro_statement)
    
    return render_template("form.html", data=data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)