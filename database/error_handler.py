from fastapi import HTTPException


def error_handler(db):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                db.rollback()
                raise HTTPException(status_code=500, detail=str(e))
            finally:
                db.close()
        return wrapper
    return decorator
