from uuid import UUID

from fastapi import FastAPI, HTTPException, Response, status

from .models import Truck, TruckData
from .service import TruckService


def create_app() -> FastAPI:
    app = FastAPI(title="Truck Management API", version="2.0.0")
    service = TruckService()

    @app.post("/trucks/", response_model=Truck, status_code=status.HTTP_201_CREATED)
    def create_truck(truck: TruckData) -> Truck:
        return service.create(truck)

    @app.get("/trucks/", response_model=list[Truck])
    def get_all_trucks() -> list[Truck]:
        return service.read_all()

    @app.get("/trucks/{truck_id}", response_model=Truck)
    def get_truck(truck_id: UUID) -> Truck:
        truck = service.read(truck_id)
        if truck is None:
            raise HTTPException(status_code=404, detail="ТС не найдено")
        return truck

    @app.put("/trucks/{truck_id}", response_model=Truck)
    def update_truck(truck_id: UUID, truck: TruckData) -> Truck:
        updated = service.update(truck_id, truck)
        if updated is None:
            raise HTTPException(status_code=404, detail="ТС не найдено")
        return updated

    @app.delete("/trucks/{truck_id}", status_code=status.HTTP_204_NO_CONTENT)
    def delete_truck(truck_id: UUID) -> Response:
        if not service.delete(truck_id):
            raise HTTPException(status_code=404, detail="ТС не найдено")
        return Response(status_code=status.HTTP_204_NO_CONTENT)

    return app


app = create_app()
