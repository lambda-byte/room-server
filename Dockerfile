# Before anything happens with Python, we must build the frontend
FROM node:16-alpine as frontend_builder
WORKDIR /static
COPY static/* .
RUN yarn install

# Now, we build our main image.
FROM python:3.9 as room_server

RUN addgroup --gid 1000 server && adduser --uid 1000 --gid 1000 --system server
WORKDIR /home/server

# Copy requirements first as to not disturb cache for other changes.
COPY requirements.txt .

RUN pip3 install -r requirements.txt && \
  pip3 install gunicorn

USER server

# Copy the entire source.
COPY . .
# Copy the built frontend.
COPY --from=frontend_builder /static/node_modules static/node_modules

ENV FLASK_APP room.py
EXPOSE 5000
ENTRYPOINT ["gunicorn", "-b", ":5000", "--access-logfile", "-", "--error-logfile", "-", "room:app"]
