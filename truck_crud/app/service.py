from uuid import UUID

from .models import Truck, TruckData


class TruckService:
    def __init__(self) -> None:
        self._storage: dict[UUID, Truck] = {}

    def create(self, data: TruckData) -> Truck:
        truck = Truck(**data.model_dump())
        self._storage[truck.id] = truck
        return truck

    def read(self, truck_id: UUID) -> Truck | None:
        return self._storage.get(truck_id)

    def read_all(self) -> list[Truck]:
        return list(self._storage.values())

    def update(self, truck_id: UUID, data: TruckData) -> Truck | None:
        if truck_id not in self._storage:
            return None
        truck = Truck(id=truck_id, **data.model_dump())
        self._storage[truck_id] = truck
        return truck

    def delete(self, truck_id: UUID) -> bool:
        return self._storage.pop(truck_id, None) is not None
