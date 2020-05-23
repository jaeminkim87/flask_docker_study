# Docker - flask 공부

## 사용법
```shell script
  # config.py에 암호를 넣어야 합니다.
  # docker-compose에도 MYSQL_ROOT_PASSWORD 부분에 암호를 넣어야 합니다.
  docker-compose up -d
```

만약 nvidia-docker를 사용하기 원한다면 미리 pull로 받은 다음 docker daemon.json에 아래 내용으로 수정합니다.
```json
{
    "default-runtime": "nvidia",
    "runtimes": {
        "nvidia": {
            "path": "/usr/bin/nvidia-container-runtime",
            "runtimeArgs": []
        }
    }
}
```


