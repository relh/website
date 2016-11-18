FROM linode/lamp:latest
MAINTAINER Richard Higgins richard@relh.net

# Update, clone repo, start services
RUN apt-get update -y && \
apt-get install -y git && \
cd /var/www/example.com/ && \
git clone https://github.com/relh/website && \
cp -r website/* public_html/ #&& \
#service apache2 start && \
#service mysql start

