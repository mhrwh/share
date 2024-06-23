import json
import jwt

def lambda_handler(event, context):
    try:
        # リクエストからIDトークンを取得
        id_token = event['headers']['Authorization'].split(" ")[1]

        # JWTトークンをデコード
        user_attributes = decode_jwt_token(id_token)
        
        return {
            'statusCode': 200,
            'body': json.dumps(user_attributes),
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            }
        }

    except Exception as e:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': str(e)}),
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            }
        }

def decode_jwt_token(token):
    # JWTトークンのペイロード部分をデコード（署名の検証はしない）
    return jwt.decode(token, options={"verify_signature": False})
