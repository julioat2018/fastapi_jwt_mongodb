from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class DateTimeModelMixin(BaseModel):
    # created_at: Optional[datetime] = Field(..., alias="createdAt")
    # updated_at: Optional[datetime] = Field(..., alias="updatedAt")
    created_at: Optional[datetime] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    updated_at: Optional[datetime] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")


class DBModelMixin(DateTimeModelMixin):
    id: Optional[int] = None
