#!/bin/bash

kill $(lsof -t -i :8000)



# 检查 PostgreSQL 容器是否在运行
if ! docker ps | grep -q postgresql-container; then
    echo "PostgreSQL 容器未运行,正在启动..."
    # 检查容器是否存在但未运行
    if docker ps -a | grep -q postgresql-container; then
        docker start postgresql-container
    else
        # 如果容器不存在,创建并启动新容器
        docker run --name postgresql-container -e POSTGRES_HOST_AUTH_METHOD=trust -d -p 5432:5432 postgres:14
    fi
    # 等待 PostgreSQL 启动
    echo "等待 PostgreSQL 启动..."
    # 循环检查容器状态直到启动完成
    while ! docker exec postgresql-container pg_isready -q; do
        echo "PostgreSQL 仍在启动中..."
        sleep 5
    done
    echo "PostgreSQL 容器已启动并准备就绪"
else
    echo "PostgreSQL 容器已在运行"
fi

if [ ! -f .env ]; then
  cp .env.example .env
  echo "Please add your api keys to the .env file."
fi
source "$(poetry env info --path)/bin/activate"
poetry install
./run_alembic_check.sh
poetry run python -m skyvern.forge
