from typing import Any, Dict

from fastapi import HTTPException, status
from fastapi.responses import JSONResponse

RES_SUCCESS = 1
RES_FAIL = 0


class BaseService:
    def response_success(
        self, data: Dict[str, Any], http_status: int = status.HTTP_200_OK
    ) -> JSONResponse:
        """Response success"""
        return JSONResponse(
            content={"detail": data, "success": RES_SUCCESS}, status_code=http_status
        )

    def exception(self, message: str, http_status: int = status.HTTP_400_BAD_REQUEST):
        """Throw general exception"""
        raise HTTPException(status_code=http_status, detail={"msg": message})

    def not_permission(self, message: str = "You do not have permission"):
        """Throw forbidden"""
        self.exception(message, status.HTTP_403_FORBIDDEN)

    def code_gone(self, message: str = "Resource gone"):
        """Throw gone"""
        self.exception(message, status.HTTP_410_GONE)

    def response_success_failed(
        self, data: Dict[str, Any], http_status: int = status.HTTP_200_OK
    ) -> JSONResponse:
        """Response fail (success HTTP nhưng code fail trong body)"""
        return JSONResponse(
            content={"detail": data, "success": RES_FAIL}, status_code=http_status
        )
