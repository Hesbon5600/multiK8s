from app import celery_app
from celery.utils.log import get_task_logger
from .models import UserModel
logger = get_task_logger(__name__)


@celery_app.task(name="test docker")
def test_docker(data):
    logger.info(data)

    try:
        user = UserModel.objects.filter(id=data['id']).first()
        user.status = 'O'
        user.save()
    except Exception as e:
        logger.info(f"\n\n\n\n\n {e} \n\n\n\n\n")

