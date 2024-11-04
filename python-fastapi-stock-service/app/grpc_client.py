import grpc
from app.stock_service_pb2 import StockRequest, PriceAlertRequest, AlertType
from app.stock_service_pb2_grpc import StockServiceStub


class NotificationClient:
    """
    NotificationClient is a client class that communicates with a remote gRPC service to
    retrieve stock prices and set price alerts.

    Attributes:
        channel: A gRPC channel for communication.
        stub: A stub to interact with the StockService.
    """
    def __init__(self):
        self.channel = grpc.insecure_channel('java-spring-notification-service:50052')
        self.stub = StockServiceStub(self.channel)

    async def get_stock_price(self, symbol: str):
        try:
            request = StockRequest(symbol=symbol)
            response = self.stub.GetStockPrice(request)
            return response
        except grpc.RpcError as e:
            print(f"gRPC error: {e}")
            return None

    async def set_price_alert(self, symbol: str, target_price: float, alert_type: str, user_id: str):
        try:
            request = PriceAlertRequest(
                symbol=symbol,
                target_price=target_price,
                alert_type=AlertType.ABOVE if alert_type.upper() == 'ABOVE' else AlertType.BELOW,
                user_id=user_id
            )
            response = self.stub.SetPriceAlert(request)
            return response
        except grpc.RpcError as e:
            print(f"gRPC error: {e}")
            return None