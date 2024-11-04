from sqlalchemy import Column, Integer, String, Float
from .database import Base

class StockAlert(Base):
    """

        class StockAlert(Base):
    """
    __tablename__ = 'stock_alerts'

    id = Column(Integer, primary_key=True, index=True)
    stock_symbol = Column(String, index=True)
    alert_price = Column(Float)