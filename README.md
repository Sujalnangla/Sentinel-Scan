# Sentinel-Scan
Automated Web Security &amp; SSL Auditor
________________________________________
🛡️ Sentinel-Scan Elite: Automated Web & SSL Auditor
Sentinel-Scan Elite is a lightweight, automated vulnerability scanner designed to perform rapid security audits on web applications. Built with a focus on offensive security and compliance reporting, it analyzes HTTP security headers, identifies potential injection points, and performs deep SSL certificate validation—generating a professional PDF report for stakeholders.
________________________________________
🚀 Key Features
•	SSL Certificate Intelligence: Connects directly to servers to extract issuer data and calculate real-time expiration (days remaining).
•	Security Header Analysis: Checks for the presence of critical "defence-in-depth" headers:
o	Content-Security-Policy (XSS Defence)
o	Strict-Transport-Security (HSTS)
o	X-Frame-Options (Clickjacking protection)
•	Vulnerability Surface Mapping: Automatically discovers and analyzes HTML forms for potential XSS and SQL Injection entry points.
•	Professional PDF Reporting: Generates a branded, color-coded security audit report (Audit_[hostname].pdf) ready for client delivery.
________________________________________
🛠️ Tech Stack & Requirements
•	Language: Python 3.10+
•	Libraries:
o	requests: For HTTP protocol handling.
o	BeautifulSoup4: For DOM parsing and form extraction.
o	fpdf2: For professional document generation.
o	socket & ssl: For low-level network security analysis.
________________________________________
📥 Installation
1.	Clone the Repository:
Bash
git clone https://github.com/yourusername/sentinel-scan.git
cd sentinel-scan
2.	Install Dependencies:
Bash
pip install requests beautifulsoup4 fpdf2
________________________________________
🖥️ Usage
Run the scanner directly from your terminal:
Bash
python sentinel_scan.py
1.	Enter Target: Provide the full URL (e.g., https://google.com).
2.	Review Console: Watch real-time status updates of the audit.
3.	Get Report: Locate the generated .pdf file in your project directory.
________________________________________
📊 Sample Output (PDF)
The report is structured into three priority sections:
1.	SSL/TLS Status: (Green/Orange/Red based on expiry).
2.	Missing Headers: Detailed breakdown of missing server-side shields.
3.	Form Analysis: Summary of discovered input fields requiring manual penetration testing.
________________________________________
⚠️ Legal Disclaimer
For Educational and Authorized Testing Only. This tool is designed for security professionals and students. Unauthorized scanning of third-party websites is illegal. The author, Sujal, assumes no liability for misuse of this tool. Always obtain written consent before testing any environment.
________________________________________

👨‍💻 About the Author
Developed by Sujal, a Cybersecurity student at HIET Shahpur. Passionate about Android security, network hardening, and building tools that bridge the gap between automation and offensive security.
