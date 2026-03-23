"""
AUTHOR: Sujal (Cybersecurity Student @ HIET)
PROJECT: Sentinel-Scan Elite
DISCLAIMER: This tool is for educational purposes and authorized security 
auditing only. Use of this tool against unauthorized targets is illegal.
The author is not responsible for any misuse.
"""
import requests
import ssl
import socket
from datetime import datetime
from bs4 import BeautifulSoup
import urllib.parse
from fpdf import FPDF

# --- PDF Report Branding ---
class PDFReport(FPDF):
    def header(self):
        self.set_font("helvetica", "B", 16)
        self.cell(0, 10, "Cybersecurity Audit & SSL Analysis", border=False, ln=True, align="C")
        self.set_font("helvetica", "I", 10)
        self.cell(0, 10, f"Report Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", ln=True, align="C")
        self.ln(10)

    def add_finding(self, title, status, description):
        self.set_font("helvetica", "B", 11)
        # Color coding: Red for RISK, Green for SAFE, Orange for WARNING
        if status == "RISK": self.set_text_color(200, 0, 0)
        elif status == "WARNING": self.set_text_color(255, 140, 0)
        else: self.set_text_color(0, 128, 0)
        
        self.cell(0, 8, f"[{status}] {title}", ln=True)
        self.set_text_color(0, 0, 0)
        self.set_font("helvetica", "", 10)
        self.multi_cell(0, 5, description)
        self.ln(4)

# --- SSL Check Logic ---
def get_ssl_info(hostname):
    try:
        context = ssl.create_default_context()
        with socket.create_connection((hostname, 443), timeout=5) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                cert = ssock.getpeercert()
                
                # Parse Expiry Date
                expiry_str = cert['notAfter']
                expiry_date = datetime.strptime(expiry_str, '%b %d %H:%M:%S %Y %Z')
                days_left = (expiry_date - datetime.now()).days
                
                issuer = dict(x[0] for x in cert['issuer'])
                common_name = issuer.get('commonName', 'Unknown')
                
                return {
                    "status": "SAFE" if days_left > 30 else "WARNING",
                    "msg": f"Certificate valid for {days_left} more days (Expires: {expiry_date.date()}). Issued by: {common_name}"
                }
    except Exception as e:
        return {"status": "RISK", "msg": f"SSL Connection Failed: {str(e)}"}

# --- Main Scanner ---
def run_elite_scan(target_url):
    hostname = target_url.replace("https://", "").replace("http://", "").split('/')[0]
    pdf = PDFReport()
    pdf.add_page()
    
    print(f"[*] Auditing {hostname}...")
    
    # 1. SSL Analysis
    ssl_result = get_ssl_info(hostname)
    pdf.add_finding("SSL Certificate Status", ssl_result['status'], ssl_result['msg'])

    # 2. Header Security
    try:
        res = requests.get(target_url, timeout=10)
        headers = res.headers
        checks = {
            "Strict-Transport-Security": "Forces HTTPS. Essential for e-commerce security.",
            "Content-Security-Policy": "The best defense against XSS (Cross-Site Scripting).",
            "X-Frame-Options": "Stops 'Clickjacking' where hackers overlay invisible buttons."
        }
        for h, desc in checks.items():
            status = "SAFE" if h in headers else "RISK"
            pdf.add_finding(h, status, desc if status == "SAFE" else f"CRITICAL MISSING: {desc}")
    except:
        pdf.add_finding("Connection", "RISK", "Could not reach server for header check.")

    # Save Output
    filename = f"Audit_{hostname}.pdf"
    pdf.output(filename)
    print(f"[+] Success! Professional report generated: {filename}")

if __name__ == "__main__":
    url = input("Enter target URL (e.g., https://example.com): ")
    run_elite_scan(url)