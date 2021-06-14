# Time-Series-Smoothing

本リポジトリはTime-Series-Smoothing のテンプレートリポジトリです。


## リポジトリ構成
```
.
├── Dockerfile
├── README.md
├── example
├── requirements.txt
└── src
    └── __init__.py
```

## 環境詳細

- Python : 3.9.4


## 事前準備

- Docker インストール


## 環境構築

* Dockderfileがあるホスト側のフォルダへ移動（例：Desktop/Time-Series-Smoothing）
```
cd Desktop/Time-Series-Smoothing
```

* Dockerによる環境構築（フォルダをマウント：Desktop/Time-Series-Smoothing）
```
docker-compose up --build
```

* ブラウザーを立ち上げてlocalhost:8888へアクセス
* ローカルフォルダがマウントされている


## 動作環境
マシンスペック（Mac)
- MacBook Air (Retina, 13-inch, 2018)
- 1.6 GHz デュアルコアIntel Core i5
- 8 GB 2133 MHz LPDDR3
