from flask import Flask, render_template_string, request, send_file, redirect, url_for
import qrcode
import qrcode.image.svg
from io import BytesIO
import datetime

app = Flask(__name__)

INDEX_HTML = """
<!doctype html>
<title>QR Generator</title>
<h2>Static QR Code Generator</h2>
<form method="post" action="/generate">
  <label>Data (text or URL):<br><input name="data" style="width:400px" required></label><br><br>
  <label>Format:
    <select name="fmt">
      <option value="png">PNG</option>
      <option value="svg">SVG</option>
    </select>
  </label>
  <label> Box size: <input type="number" name="box_size" value="10" min="1" max="40"></label>
  <label> Border: <input type="number" name="border" value="4" min="0" max="10"></label>
  <label> Error correction:
    <select name="ecc">
      <option value="L">L (7%)</option>
      <option value="M" selected>M (15%)</option>
      <option value="Q">Q (25%)</option>
      <option value="H">H (30%)</option>
    </select>
  </label>
  <br><br>
  <button type="submit">Generate</button>
</form>

{% if qr_url %}
  <h3>Preview:</h3>
  <img src="{{qr_url}}" alt="QR preview"><br><br>
  <a href="{{download_url}}">Download {{fmt.upper()}}</a>
{% endif %}
"""

def ecc_from_code(c):
    return {
        "L": qrcode.constants.ERROR_CORRECT_L,
        "M": qrcode.constants.ERROR_CORRECT_M,
        "Q": qrcode.constants.ERROR_CORRECT_Q,
        "H": qrcode.constants.ERROR_CORRECT_H
    }[c]

@app.route("/", methods=["GET"])
def index():
    return render_template_string(INDEX_HTML)

@app.route("/generate", methods=["POST"])
def generate():
    data = request.form.get("data", "").strip()
    fmt = request.form.get("fmt", "png")
    try:
        box_size = int(request.form.get("box_size", 10))
        border = int(request.form.get("border", 4))
    except ValueError:
        box_size = 10
        border = 4
    ecc = request.form.get("ecc", "M")
    if not data:
        return redirect(url_for("index"))

    # Create QR object
    qr = qrcode.QRCode(
        version=None,
        error_correction=ecc_from_code(ecc),
        box_size=box_size,
        border=border,
    )
    qr.add_data(data)
    qr.make(fit=True)

    timestamp = datetime.datetime.utcnow().strftime("%Y%m%d%H%M%S")

    if fmt == "svg":
        img = qr.make_image(image_factory=qrcode.image.svg.SvgImage)
        buf = BytesIO()
        img.save(buf)
        buf.seek(0)
        filename = f"qr_{timestamp}.svg"
        # Serve preview via data URI is messy for svg; create a download route and preview as inline svg
        # We'll save bytes in session-like storage by encoding in URL (simple approach: return download route)
        return send_file(buf, mimetype="image/svg+xml", as_attachment=False, download_name=filename)

    # PNG path
    img = qr.make_image(fill_color="black", back_color="white")
    buf = BytesIO()
    img.save(buf, format="PNG")
    buf.seek(0)
    filename = f"qr_{timestamp}.png"

    # Return image inline for preview (data served directly)
    return send_file(buf, mimetype="image/png", as_attachment=False, download_name=filename)

@app.route("/download", methods=["POST"])
def download():
    # Optional: if you'd rather have a dedicated download endpoint
    data = request.form.get("data", "").strip()
    fmt = request.form.get("fmt", "png")
    box_size = int(request.form.get("box_size", 10))
    border = int(request.form.get("border", 4))
    ecc = request.form.get("ecc", "M")
    if not data:
        return redirect(url_for("index"))

    qr = qrcode.QRCode(
        version=None,
        error_correction=ecc_from_code(ecc),
        box_size=box_size,
        border=border,
    )
    qr.add_data(data)
    qr.make(fit=True)

    if fmt == "svg":
        img = qr.make_image(image_factory=qrcode.image.svg.SvgImage)
        buf = BytesIO()
        img.save(buf)
        buf.seek(0)
        return send_file(buf, mimetype="image/svg+xml", as_attachment=True, download_name="qr.svg")
    img = qr.make_image(fill_color="black", back_color="white")
    buf = BytesIO()
    img.save(buf, "PNG")
    buf.seek(0)
    return send_file(buf, mimetype="image/png", as_attachment=True, download_name="qr.png")

if __name__ == "__main__":
    app.run(debug=True)
