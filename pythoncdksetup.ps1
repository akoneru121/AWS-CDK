# Set project name
$projectName = "my-demo0cdk"

# Create and enter the project directory
mkdir $projectName
cd $projectName

# Initialize the CDK project with Python
cdk init app --language python

# Create and activate virtual environment
python -m venv .venv
.venv\Scripts\activate

# Upgrade pip
#python -m pip install --upgrade pip

# Install required Python packages
pip install -r requirements.txt

# Install CDK core libraries (if needed manually)
pip install aws-cdk-lib constructs

# Bootstrap the environment (prepare your AWS account for deployment)
cdk bootstrap

# Show success message
Write-Host "`n🎉 AWS CDK Python project '$projectName' is ready!"
Write-Host "To deploy your stack, run: `n    .venv\Scripts\activate; cdk deploy"
