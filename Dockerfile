# Microsoftが提供するVisual Studio Codeの開発コンテナ用のPythonイメージ
FROM mcr.microsoft.com/vscode/devcontainers/python:3

# 環境変数を設定
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# 作業ディレクトリを設定
WORKDIR /workspaces

# 依存関係をインストール
COPY requirements.txt /workspaces/
RUN pip install --upgrade pip && pip install -r requirements.txt

# プロジェクトをコピー
COPY . /workspaces/