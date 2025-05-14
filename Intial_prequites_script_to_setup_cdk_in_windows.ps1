# Enable script execution
Set-ExecutionPolicy Bypass -Scope Process -Force

# Install Chocolatey (if not already installed)
if (-not (Get-Command choco -ErrorAction SilentlyContinue)) {
    Write-Host "Installing Chocolatey..."
    iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
} else {
    Write-Host "Chocolatey already installed."
}

# Refresh environment variables
$env:Path = [System.Environment]::GetEnvironmentVariable("Path","Machine")

# Install Node.js (LTS version)
choco install nodejs-lts -y

# Install Python 3 (if not already installed)
choco install python --version=3.11.5 -y  # Use a supported CDK version

# Install AWS CLI
choco install awscli -y

# Install Visual Studio Code
choco install vscode -y

# Optional: Install Git (if needed for CDK projects)
choco install git -y

# Wait for installs to finish
Write-Host "Waiting for installations to complete..."
Start-Sleep -Seconds 5

# Confirm installations
Write-Host "`n--- Installed Versions ---"
node -v
npm -v
python --version
aws --version
code --version
