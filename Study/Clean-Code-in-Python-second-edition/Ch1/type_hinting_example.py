import logging
from typing import Union, List, Tuple


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def broadcast_notification(
    message: str,
    relevant_user_emails: Union[List[str], Tuple[str]]
):
    for email in relevant_user_emails:
        logger.info(f"{message} 메시지를 {email}에게 전달")
        

broadcast_notification("welcome", ["user1@domain.com", "user2@domain.com"])
broadcast_notification("welcome", "user1@domain.com") # type: ignore