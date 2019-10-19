zesei
====
# Requirement
- Python 3.6
    - Django 2.2.5
- MySQL 9.6

## To develop
### Set Up the development environment
Docker上で開発を行うために以下の準備を行います
```bash
docker-compose up -d
docker-compose exec django sh

# install python3 Library
pip intsall -r requirements/local.txt

# install node Library
cd /opt/e-Learning-kamiya/dev-front
npm install

# generate .env file
# .envs/.localの内容を.envファイルにまとめる
python3 merge_dotenvs_in_dotenv.py
```

### database command
```bash
#  migrate
python3 manage.py makemigrations courses payments foods users --settings config.settings.local
python3 manage.py migrate --settings config.settings.local

# データベース中の全データの削除
python3 manage.py flush --settings config.settings.local
```

### run the app
```bash
# 開発用のバックエンドサーバーの起動
cd /app
python3 manage.py runserver 0.0.0.0:8000 --settings config.settings.local

# 開発用のフロントエンドサーバーの起動
cd /app/dev-front
npm run serve
```

## 権限の問題
Dockerコンテナ内でファイルを生成すると，ホスト側ではroot権限のファイルの作成になり，アクセスをすることができなくなる可能性がある．その際は，以下の様に，ファイルの所有者の権限を変更することができる．
```bash
chown -R 1000:1000 ./
```


## フロントエンドのビルド
以下のコマンドを入力することで、フロント側のソースコードがビルドされます
```bash
# dev-front/src/common/config.js 内のAPI_URLを /api に変更してください
cd /app/dev-front
npm run build
```
