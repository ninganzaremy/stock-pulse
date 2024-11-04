from grpc_auto import service_pb2_grpc, service_pb2
import models
from database import engine
import os

models.Base.metadata.create_all(bind=engine)

class StockService(service_pb2_grpc.StockServiceServicer):
    """
    Class to implement StockService for gRPC.

    Methods
    -------
    CheckStockPrice(self, request, context)
        Handles incoming gRPC requests to check the stock price for a given stock symbol.

    get_current_stock_price(self, stock_symbol)
        Retrieves the current stock price for a given stock symbol.
    """
    def CheckStockPrice(self, request, context):
        stock_symbol = request.stock_symbol
        current_price = self.get_current_stock_price(stock_symbol)
        return service_pb2.StockResponse(current_price=current_price)

    def get_current_stock_price(self, stock_symbol):
        # TODO fetch  API
        return 150.0  # Example fixed price

def serve():
    """
    Starts the gRPC server and listens on port 50051.
    The server uses a thread pool executor with a maximum of 10 worker threads.

    :return:
    """
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    service_pb2_grpc.add_StockServiceServicer_to_server(StockService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("gRPC server started on port 50051")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()