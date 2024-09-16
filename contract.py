from datetime import datetime
from enum import Enum
from pydantic import BaseModel, EmailStr, PositiveFloat, PositiveInt

class ProductEnum(str, Enum):
  Gemini = 'Project with Gemini'
  ChatGPT = 'Project with ChatGPT'
  Llama = 'Project with Llama 3.0'

class Sales(BaseModel):
  """
  This is the sales class of the database. It contains the following attributes:
  
  Args:
      email (EmailStr): The email of the seller
      date_hour (datetime): The date and hour of the sale
      cost (PositiveFloat): The cost of the sale
      quantity (PositiveInt): The quantity of the sale
      product (ProductEnum): The product of the sale
  """
  
  email: EmailStr
  date_hour: datetime
  cost: PositiveFloat
  quantity: PositiveInt
  product: ProductEnum
