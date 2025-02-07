# Sample echo server

```shell
docker run -e ROOT_PATH=/app  -p 8080:8080 wonderflow/simpleapp
```

Then you will get the output like:

```shell
    _    _      _ _         __        __         _     _ _ 
   | |  | |    | | |        \ \      / /        | |   | | | 
   | |__| | ___| | | ___     \ \ /\ / /__  _ __ | | __| | |
   |  __  |/ _ \ | |/ _ \     \ V  V / _ \| '_ \| |/ _` | |
   | |  | |  __/ | | (_) |     \_/\_/ (_) | | | | | (_| |_|
   |_|  |_|\___|_|_|\___( )         (_) |_| |_|_|\__,_(_)
                       |/                                 
    Hello World, API Gateway!
    
```

## Configuration

| Configuration | Source | Description |
| --- | --- | --- | 
| `ROOT_PATH` | Environment | Define the root path for this server. Default is `/` |
| `TARGET` | Environment | Greet to a target. Default is `World` |
| `PORT` | Environment | Define the server's listening port. Default is `8080` |
| `STATUS_CODE` | Environment | Define default response status code. If not specified default is `200` |
| `timeout` | Query Parameter | Add timeout to a request (in seconds). Default is no timeout. |
| `status_code` | Query Parameter | Return a specific status code. Default value depends on the environment variable `STATUS_CODE`. |

## Build and Push Multi-Platform Image

```bash
docker buildx build \
  --platform linux/amd64,linux/arm64 \
  -t <your-dockerhub-username>/simpleapp:<tag> \
  --push \
  .
```
