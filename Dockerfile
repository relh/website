FROM linode:latest
MAINTAINER Richard Higgins richard@relh.net

# Update and Clone Repo
RUN apt-get update
apt-get install git && \
mkdir /var/www/relh.io/ && \
cd /var/www/relh.io/ && \
git clone https://github.com/relh/website

