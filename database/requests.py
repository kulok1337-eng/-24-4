from sqlalchemy import select, update
from database.models import Order, User, async_session


async def get_user(telegram_id: int) -> User | None:
    async with async_session() as session:
        result = await session.execute(select(User).where(User.telegram_id == telegram_id))
        return result.scalar_one_or_none()


async def create_user(
    telegram_id: int,
    full_name: str,
    phone: str,
    specialty: str,
    role: str = "master",
    is_approved: bool = False,
):
    async with async_session() as session:
        user = User(
            telegram_id=telegram_id,
            full_name=full_name,
            phone=phone,
            specialty=specialty,
            role=role,
            is_approved=is_approved,
        )
        session.add(user)
        await session.commit()
        return user


async def approve_user(telegram_id: int):
    async with async_session() as session:
        await session.execute(update(User).where(User.telegram_id == telegram_id).values(is_approved=True))
        await session.commit()


async def add_order(
    master_id: int,
    client_phone: str,
    address: str,
    description: str,
    desired_date: str,
    photo_id: str | None,
) -> Order:
    async with async_session() as session:
        order = Order(
            master_id=master_id,
            client_phone=client_phone,
            address=address,
            description=description,
            desired_date=desired_date,
            photo_id=photo_id,
            status="new",
        )
        session.add(order)
        await session.commit()
        await session.refresh(order)
        return order


async def get_order(order_id: int) -> Order | None:
    async with async_session() as session:
        result = await session.execute(select(Order).where(Order.id == order_id))
        return result.scalar_one_or_none()


async def update_order_status(order_id: int, status: str):
    async with async_session() as session:
        await session.execute(update(Order).where(Order.id == order_id).values(status=status))
        await session.commit()


async def close_order(order_id: int, deal_amount: float, commission_amount: float):
    async with async_session() as session:
        await session.execute(
            update(Order)
            .where(Order.id == order_id)
            .values(status="completed", deal_amount=deal_amount, commission_amount=commission_amount)
        )
        await session.commit()
