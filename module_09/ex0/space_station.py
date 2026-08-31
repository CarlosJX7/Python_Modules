from pydantic import BaseModel, Field, ValidationError
from datetime import datetime
from typing import Optional

class SpaceStation(BaseModel):
    station_id: str = Field(..., min_length=3, max_length=10)
    name: str = Field(..., min_length=1, max_length=50)
    crew_size: int = Field(..., ge=1, le=20)
    power_level: float = Field(..., ge=0.0, le=100.0)
    oxygen_level: float = Field(..., ge=0.0, le=100.0)
    is_operational: bool = True
    last_maintenance: datetime
    notes: Optional[str] = Field(default=None, max_length=200)


def main() -> None:
    print("Space Station Data Validation")
    print("=" * 40)

    valid_station = SpaceStation(
        station_id="ISS001",
        name="International Space Station",
        crew_size=6,
        power_level=85.5,
        oxygen_level=92.3,
        last_maintenance="2024-01-15T10:00:00",
        is_operational=True,
        notes="All systems nominal",
    )

    print("Valid station created:")
    print(f"ID: {valid_station.station_id}")
    print(f"Name: {valid_station.name}")
    print(f"Crew: {valid_station.crew_size} people")
    print(f"Power: {valid_station.power_level}%")
    print(f"Oxygen: {valid_station.oxygen_level}%")
    status = "Operational" if valid_station.is_operational else "Not Operational"
    print(f"Status: {status}")
    print("========================================")

    print("Expected validation error:")
    try:
        SpaceStation(
            station_id="ISS002",
            name="Bad Station",
            crew_size=25,
            power_level=80.0,
            oxygen_level=90.0,
            last_maintenance="2024-01-15T10:00:00",
        )
    except ValidationError as e:
        msg = e.errors()[0].get("msg", "")
        print(msg.removeprefix("Value error, "))


if __name__ == "__main__":
    main()