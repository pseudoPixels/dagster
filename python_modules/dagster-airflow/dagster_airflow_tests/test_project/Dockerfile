# Making this image as minimal as possible to speed up build & pull times; k8s (kind) has a 2 min
# pull timeout
FROM python:3.7.4-slim-stretch

ADD dagster dagster
ADD dagster-graphql dagster-graphql
ADD dagster-aws dagster-aws
ADD dagster-cron dagster-cron
ADD dagster-pandas dagster-pandas
ADD dagster-gcp dagster-gcp

RUN pip install --no-deps -e dagster -e dagster-graphql -e dagster-aws -e dagster-cron -e dagster-pandas -e dagster-gcp
RUN pip install -e dagster -e dagster-graphql -e dagster-aws -e dagster-cron -e dagster-pandas -e dagster-gcp

ADD . .

ENV GOOGLE_APPLICATION_CREDENTIALS="/gac.json"

ENTRYPOINT [ "dagster-graphql" ]
