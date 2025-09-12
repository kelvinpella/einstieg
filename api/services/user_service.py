from ..models.user import Coordinates, NearbyUser


class UserService:
    @classmethod
    def filter_nearby_users(cls, latitude: float, longitude: float):
        return [
            NearbyUser(
                user_id="user.id",
                name="kelvin",
                distance=45.5,
                coordinates=Coordinates(latitude=34.6, longitude=45.8),
            )
        ]
