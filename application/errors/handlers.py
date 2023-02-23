# from flask import Blueprint
# from http import HTTPStatus
# from application.routes.util import APIError,APIResponse
# errors=Blueprint('errors', __name__)


# @errors.app_errorhandler(400)
# def error_400(error):
#     return APIError(message="Bad Request",status=HTTPStatus.NOT_FOUND)

# @errors.app_errorhandler(401)
# def error_401(error):
#     return APIError(message="Un-Authorized",status=HTTPStatus.UNAUTHORIZED)

# @errors.app_errorhandler(403)
# def error_403(error):
#     return APIError(message="Forbidded",status=HTTPStatus.FORBIDDEN)

# @errors.app_errorhandler(500)
# def error_500(error):
#     return APIError(message="Internal Servor Error",status=HTTPStatus.INTERNAL_SERVER_ERROR)

