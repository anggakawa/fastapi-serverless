from fastapi import APIRouter, Request, HTTPException
from fastapi.responses import JSONResponse
from typing import Dict, Any
from helper.lib import load_function


router = APIRouter()


@router.post("/invoke/{function_name}")
async def invoke(function_name: str, request: Request):
    try:
        handle_function = load_function(function_name)
        
        # Construct event data based on the request
        event = {
            "queryStringParameters": dict(request.query_params),
            "pathParameters": request.path_params,
            "headers": dict(request.headers),
            "body": await request.json() if request.headers.get("content-type") == "application/json" else (await request.body()).decode('utf-8')
        }
        
        context: Dict[str, Any] = {}  # Add any additional context if necessary
        
        result = handle_function(event, context)
        return JSONResponse(content=result)
    except ImportError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except AttributeError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

