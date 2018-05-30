from chainer import cuda
from app import application

if __name__ == "__main__":
    cuda.init()
    cuda.get_device(0).use()
    application.run('0.0.0.0', port=2424)
