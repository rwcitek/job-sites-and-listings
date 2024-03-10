#!/bin/bash
set -e

DOCTL_VERSION="1.101.0"
wget https://github.com/digitalocean/doctl/releases/download/v${DOCTL_VERSION}/doctl-${DOCTL_VERSION}-linux-amd64.tar.gz
tar xf doctl-${DOCTL_VERSION}-linux-amd64.tar.gz
sudo mv doctl /usr/local/bin
