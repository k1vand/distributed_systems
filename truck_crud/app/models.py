from typing import Self
from uuid import UUID, uuid4

from pydantic import BaseModel, ConfigDict, Field, model_validator


class TruckData(BaseModel):
    model_config = ConfigDict(extra="forbid", allow_inf_nan=False)

    capacity: float = Field(gt=0, description="Грузоподъёмность, т")
    load_t: float = Field(ge=0, description="Масса перевозимого груза, т")
    curb_weight_t: float = Field(gt=0, description="Снаряжённая масса автомобиля, т")
    mileage: float = Field(ge=0, description="Общий пробег автомобиля, км")
    fuel_consumption_l_per_100km: float = Field(ge=0, description="Средний расход топлива, л/100 км")
    average_speed_kmh: float = Field(ge=0, description="Средняя скорость движения, км/ч")

    @model_validator(mode="after")
    def validate_load(self) -> Self:
        if self.load_t > self.capacity:
            raise ValueError("Масса груза превышает грузоподъёмность")
        return self


class Truck(TruckData):
    id: UUID = Field(default_factory=uuid4)
