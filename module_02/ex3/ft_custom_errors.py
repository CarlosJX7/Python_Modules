class GardenError(Exception):
	def __init__(self, message: str = "Unknown Garden Error Exception") -> None:
		super().__init__(message)

