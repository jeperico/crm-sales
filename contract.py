from datetime import datetime
from enum import Enum
from pydantic import BaseModel, EmailStr, PositiveFloat, PositiveInt

class ProductEnum(str, Enum):
  Gemini = 'Project with Gemini'
  ChatGPT = 'Project with ChatGPT'
  Llama = 'Project with Llama 3.0'

class SalesContract(BaseModel):
  email: EmailStr
  date_hour: datetime
  cost: PositiveFloat
  quantity: PositiveInt
  product: ProductEnum
