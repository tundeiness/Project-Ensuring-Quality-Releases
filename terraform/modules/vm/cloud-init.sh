# #!/bin/bash

# # Variables (these will be replaced via Terraform templatefile)
# ORG_URL="${org_url}"
# AZDO_PAT="${azdo_pat}"
# ENV_NAME="${env_name}"
# AGENT_VERSION="4.255.0"

# # Install dependencies
# apt-get update -y
# apt-get install -y curl unzip libcurl4-openssl-dev libssl-dev jq

# # Add user if not present
# useradd -m -s /bin/bash devopsagent || true

# # Download Azure DevOps agent
# mkdir -p /azagent && cd /azagent
# curl -O https://vstsagentpackage.azureedge.net/agent/${AGENT_VERSION}/vsts-agent-linux-x64-${AGENT_VERSION}.tar.gz
# tar zxvf vsts-agent-linux-x64-${AGENT_VERSION}.tar.gz

# # Configure the agent
# ./config.sh --unattended \
#   --url "$ORG_URL" \
#   --auth pat \
#   --token "$AZDO_PAT" \
#   --environment \
#   --environmentname "$ENV_NAME" \
#   --acceptTeeEula \
#   --agent "$(hostname)" \
#   --replace

# # Install and start the agent
# ./svc.sh install
# ./svc.sh start


mkdir azagent;cd azagent;curl -fkSL -o vstsagent.tar.gz https://vstsagentpackage.azureedge.net/agent/4.255.0/vsts-agent-linux-x64-4.255.0.tar.gz;tar -zxvf vstsagent.tar.gz; if [ -x "$(command -v systemctl)" ]; then ./config.sh --environment --environmentname "devopsVM" --acceptteeeula --agent $HOSTNAME --url https://dev.azure.com/odluser281341/ --work _work --projectname 'project-demo' --auth PAT --token 3OZsoDRD9NTfmFMqHif2eosUQ4lTwowPAcT2yCtZPfgtXdNw3qcDJQQJ99BEACAAAAAPDBwgAAASAZDOFZoB --runasservice; sudo ./svc.sh install; sudo ./svc.sh start; else ./config.sh --environment --environmentname "devopsVM" --acceptteeeula --agent $HOSTNAME --url https://dev.azure.com/odluser281341/ --work _work --projectname 'project-demo' --auth PAT --token 3OZsoDRD9NTfmFMqHif2eosUQ4lTwowPAcT2yCtZPfgtXdNw3qcDJQQJ99BEACAAAAAPDBwgAAASAZDOFZoB; ./run.sh; fi