# debug.py
api = {
  "openapi": "3.1.0",
  "info": {
    "title": "test_title",
    "description": "none desc",
    "version": "0.0.1"
  },
  "paths": {
    "/api/v1/token": {
      "post": {
        "tags": [
          "授权"
        ],
        "summary": "Secure Login Token",
        "operationId": "SECURE_login_token_api_v1_token_post",
        "requestBody": {
          "content": {
            "application/x-www-form-urlencoded": {
              "schema": {
                "$ref": "#/components/schemas/Body_SECURE_login_token_api_v1_token_post"
              }
            }
          },
          "required": True
        },
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/OAuth2ResponseSchema"
                }
              }
            }
          },
          "422": {
            "description": "Validation Error",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            }
          }
        }
      }
    },
    "/api/v1/wechat_token": {
      "post": {
        "tags": [
          "授权"
        ],
        "summary": "Secure Wechat Login Token",
        "operationId": "SECURE_wechat_login_token_api_v1_wechat_token_post",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/WechatLoginSchema"
              }
            }
          },
          "required": True
        },
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/OAuth2WechatInfoResponseSchema"
                }
              }
            }
          },
          "422": {
            "description": "Validation Error",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            }
          }
        }
      }
    },
    "/api/v1/wechat_bind": {
      "post": {
        "tags": [
          "授权"
        ],
        "summary": "Secure Wechat User Bind",
        "operationId": "SECURE_wechat_user_bind_api_v1_wechat_bind_post",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/WechatUserBindSchema"
              }
            }
          },
          "required": True
        },
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/StdResp"
                }
              }
            }
          },
          "422": {
            "description": "Validation Error",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            }
          }
        }
      }
    },
    "/api/v1/update/user/password": {
      "post": {
        "tags": [
          "授权"
        ],
        "summary": "Secure User Update Pwd",
        "operationId": "SECURE_User_update_pwd_api_v1_update_user_password_post",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/PasswordUpdateSchema"
              }
            }
          },
          "required": True
        },
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/StdResp"
                }
              }
            }
          },
          "422": {
            "description": "Validation Error",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            }
          }
        },
        "security": [
          {
            "OAuth2PasswordBearer": [
              "student"
            ]
          }
        ]
      }
    },
    "/api/v1/group": {
      "get": {
        "tags": [
          "调试"
        ],
        "summary": "Get Group",
        "operationId": "get_group_api_v1_group_get",
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {}
              }
            }
          }
        },
        "security": [
          {
            "OAuth2PasswordBearer": [
              "group"
            ]
          }
        ]
      }
    },
    "/api/v1/normal": {
      "get": {
        "tags": [
          "调试"
        ],
        "summary": "Get Normal",
        "operationId": "get_normal_api_v1_normal_get",
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {}
              }
            }
          }
        },
        "security": [
          {
            "OAuth2PasswordBearer": [
              "student"
            ]
          }
        ]
      }
    },
    "/api/v1/create/user": {
      "post": {
        "tags": [
          "资源管理"
        ],
        "summary": "Mf New User",
        "operationId": "MF_new_user_api_v1_create_user_post",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/UserSchema"
              }
            }
          },
          "required": True
        },
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/StdResp"
                }
              }
            }
          },
          "422": {
            "description": "Validation Error",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            }
          }
        }
      }
    },
    "/api/v1/update/user": {
      "post": {
        "tags": [
          "资源管理"
        ],
        "summary": "Mf Update User",
        "operationId": "MF_update_user_api_v1_update_user_post",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/UserSchema"
              }
            }
          },
          "required": True
        },
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/StdResp"
                }
              }
            }
          },
          "422": {
            "description": "Validation Error",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            }
          }
        }
      }
    },
    "/api/v1/openapi": {
      "get": {
        "tags": [
          "资源管理"
        ],
        "summary": "Get Openapi Json",
        "operationId": "get_openapi_json_api_v1_openapi_get",
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {}
              }
            }
          }
        }
      }
    },
    "/api/v1/upload/new": {
      "post": {
        "tags": [
          "File"
        ],
        "summary": "Upload New File",
        "operationId": "upload_new_file_api_v1_upload_new_post",
        "parameters": [
          {
            "name": "fileMIME",
            "in": "query",
            "required": True,
            "schema": {
              "type": "string",
              "title": "Filemime"
            }
          },
          {
            "name": "fileSize",
            "in": "query",
            "required": True,
            "schema": {
              "type": "integer",
              "title": "Filesize"
            }
          },
          {
            "name": "fileName",
            "in": "query",
            "required": True,
            "schema": {
              "type": "string",
              "title": "Filename"
            }
          }
        ],
        "requestBody": {
          "required": True,
          "content": {
            "multipart/form-data": {
              "schema": {
                "$ref": "#/components/schemas/Body_upload_new_file_api_v1_upload_new_post"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {}
              }
            }
          },
          "422": {
            "description": "Validation Error",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            }
          }
        }
      }
    },
    "/api/v1/upload/file": {
      "post": {
        "tags": [
          "File"
        ],
        "summary": "Upload New Fileobject",
        "operationId": "upload_new_fileObject_api_v1_upload_file_post",
        "parameters": [
          {
            "name": "filename",
            "in": "query",
            "required": True,
            "schema": {
              "type": "string",
              "title": "Filename"
            }
          }
        ],
        "requestBody": {
          "required": True,
          "content": {
            "multipart/form-data": {
              "schema": {
                "$ref": "#/components/schemas/Body_upload_new_fileObject_api_v1_upload_file_post"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {}
              }
            }
          },
          "422": {
            "description": "Validation Error",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            }
          }
        }
      }
    },
    "/api/v1/download/uid": {
      "get": {
        "tags": [
          "File"
        ],
        "summary": "Download By Uid",
        "operationId": "download_by_uid_api_v1_download_uid_get",
        "parameters": [
          {
            "name": "uid",
            "in": "query",
            "required": True,
            "schema": {
              "type": "string",
              "title": "Uid"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {}
              }
            }
          },
          "422": {
            "description": "Validation Error",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            }
          }
        }
      }
    },
    "/api/v1/basicinfo": {
      "get": {
        "summary": "Get Base Test Info",
        "operationId": "get_base_test_info_api_v1_basicinfo_get",
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {}
              }
            }
          }
        }
      }
    },
    "/api/v1/get/MoralAction": {
      "get": {
        "tags": [
          "德育分事务"
        ],
        "summary": "获取可用德育分活动",
        "description": "获取所有可用的德育分活动",
        "operationId": "获取可用德育分活动_api_v1_get_MoralAction_get",
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/MoralActionSchemaRespList"
                }
              }
            }
          }
        }
      }
    },
    "/api/v1/get/AllMoralAction": {
      "get": {
        "tags": [
          "德育分事务"
        ],
        "summary": "获取所有德育分活动",
        "description": "获取所有德育分活动，包含不可用的德育分",
        "operationId": "获取所有德育分活动_api_v1_get_AllMoralAction_get",
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/MoralActionSchemaRespList"
                }
              }
            }
          }
        }
      }
    },
    "/api/v1/add/MoralAction": {
      "post": {
        "tags": [
          "德育分事务"
        ],
        "summary": "新建德育分活动",
        "description": "注册一个新的德育分活动并公开",
        "operationId": "新建德育分活动_api_v1_add_MoralAction_post",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/MoralActionCreateSchema"
              }
            }
          },
          "required": True
        },
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/StdResp"
                }
              }
            }
          },
          "422": {
            "description": "Validation Error",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            }
          }
        }
      }
    },
    "/api/v1/update/MoralAction": {
      "post": {
        "tags": [
          "德育分事务"
        ],
        "summary": "修改德育分活动",
        "description": "更新一个德育分活动信息",
        "operationId": "修改德育分活动_api_v1_update_MoralAction_post",
        "parameters": [
          {
            "name": "action_id",
            "in": "query",
            "required": True,
            "schema": {
              "type": "integer",
              "title": "Action Id"
            }
          }
        ],
        "requestBody": {
          "required": True,
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/MoralActionCreateSchema"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/StdResp"
                }
              }
            }
          },
          "422": {
            "description": "Validation Error",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            }
          }
        }
      }
    },
    "/api/v1/delete/MoralAction": {
      "get": {
        "tags": [
          "德育分事务"
        ],
        "summary": "禁用一个德育分活动",
        "description": "禁用或是删除一个德育分活动信息",
        "operationId": "禁用一个德育分活动_api_v1_delete_MoralAction_get",
        "parameters": [
          {
            "name": "action_id",
            "in": "query",
            "required": True,
            "schema": {
              "type": "integer",
              "title": "Action Id"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/StdResp"
                }
              }
            }
          },
          "422": {
            "description": "Validation Error",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            }
          }
        }
      }
    },
    "/api/v1/add/ApplyMoralRecord": {
      "post": {
        "tags": [
          "德育分事务"
        ],
        "summary": "申请德育分活动",
        "description": "申请一个德育分活动加入到德育分列表",
        "operationId": "申请德育分活动_api_v1_add_ApplyMoralRecord_post",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/MoralRecordApplySchema"
              }
            }
          },
          "required": True
        },
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/StdResp"
                }
              }
            }
          },
          "422": {
            "description": "Validation Error",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            }
          }
        }
      }
    },
    "/api/v1/get/UserMoralRecord": {
      "get": {
        "tags": [
          "德育分事务"
        ],
        "summary": "查询用户德育分记录",
        "description": "查询用户的德育分记录",
        "operationId": "查询用户德育分记录_api_v1_get_UserMoralRecord_get",
        "parameters": [
          {
            "name": "username",
            "in": "query",
            "required": True,
            "schema": {
              "type": "string",
              "title": "Username"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/UserMoralRecordResponseSchema"
                }
              }
            }
          },
          "422": {
            "description": "Validation Error",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            }
          }
        }
      }
    },
    "/api/v1/get/uncheckedMoralRecord": {
      "get": {
        "tags": [
          "德育分事务"
        ],
        "summary": "获取待审核列表",
        "description": "获取尚未审核的德育分记录",
        "operationId": "获取待审核列表_api_v1_get_uncheckedMoralRecord_get",
        "parameters": [
          {
            "name": "status",
            "in": "query",
            "required": False,
            "schema": {
              "type": "integer",
              "default": 1,
              "title": "Status"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/UserMoralRecordResponseSchema"
                }
              }
            }
          },
          "422": {
            "description": "Validation Error",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            }
          }
        }
      }
    },
    "/api/v1/update/checkMoralRecord": {
      "post": {
        "tags": [
          "德育分事务"
        ],
        "summary": "提交审核德育分记录",
        "description": "通过部分更新审核某个德育分记录",
        "operationId": "提交审核德育分记录_api_v1_update_checkMoralRecord_post",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/MoralRecordCheckerSchema"
              }
            }
          },
          "required": True
        },
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/StdResp"
                }
              }
            }
          },
          "422": {
            "description": "Validation Error",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            }
          }
        }
      }
    },
    "/api/v1/get/userMoralScore": {
      "get": {
        "tags": [
          "德育分事务"
        ],
        "summary": "提交审核德育分记录",
        "description": "通过部分更新审核某个德育分记录",
        "operationId": "提交审核德育分记录_api_v1_get_userMoralScore_get",
        "parameters": [
          {
            "name": "username",
            "in": "query",
            "required": True,
            "schema": {
              "type": "string",
              "title": "Username"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/UserCurrentMoralScoreSchema"
                }
              }
            }
          },
          "422": {
            "description": "Validation Error",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            }
          }
        }
      }
    },
    "/api/v1/get/MoralActionInfoById": {
      "get": {
        "tags": [
          "德育分事务"
        ],
        "summary": "获取一个德育分活动",
        "description": "通过id获取一个德育分活动详细信息",
        "operationId": "获取一个德育分活动_api_v1_get_MoralActionInfoById_get",
        "parameters": [
          {
            "name": "action_id",
            "in": "query",
            "required": True,
            "schema": {
              "type": "integer",
              "title": "Action Id"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/MoralActionSchema"
                }
              }
            }
          },
          "422": {
            "description": "Validation Error",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            }
          }
        }
      }
    },
    "/api/v1/get/studentInfo": {
      "get": {
        "tags": [
          "学生信息事务"
        ],
        "summary": "获取学生信息",
        "description": "通过token获取学生信息",
        "operationId": "获取学生信息_api_v1_get_studentInfo_get",
        "security": [
          {
            "OAuth2PasswordBearer": [
              "student"
            ]
          }
        ],
        "parameters": [
          {
            "name": "username",
            "in": "query",
            "required": True,
            "schema": {
              "type": "string",
              "title": "Username"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/StudentSchema"
                }
              }
            }
          },
          "422": {
            "description": "Validation Error",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            }
          }
        }
      }
    },
    "/api/v1/update/studentInfo": {
      "post": {
        "tags": [
          "学生信息事务"
        ],
        "summary": "修改学生信息",
        "description": "通过token修改学生信息",
        "operationId": "修改学生信息_api_v1_update_studentInfo_post",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/StudentSchema"
              }
            }
          },
          "required": True
        },
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/StdResp"
                }
              }
            }
          },
          "422": {
            "description": "Validation Error",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            }
          }
        },
        "security": [
          {
            "OAuth2PasswordBearer": [
              "student"
            ]
          }
        ]
      }
    },
    "/api/v1/post/studentInfo": {
      "post": {
        "tags": [
          "学生信息事务"
        ],
        "summary": "创建学生信息",
        "description": "创建一个完整的学生信息",
        "operationId": "创建学生信息_api_v1_post_studentInfo_post",
        "requestBody": {
          "required": True,
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/StudentSchema"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/StdResp"
                }
              }
            }
          },
          "422": {
            "description": "Validation Error",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            }
          }
        }
      },
      "get": {
        "tags": [
          "学生信息事务"
        ],
        "summary": "删除学生信息",
        "description": "删除一个学生的档案信息",
        "operationId": "删除学生信息_api_v1_post_studentInfo_get",
        "parameters": [
          {
            "name": "username",
            "in": "query",
            "required": True,
            "schema": {
              "type": "string",
              "title": "Username"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/StdResp"
                }
              }
            }
          },
          "422": {
            "description": "Validation Error",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            }
          }
        }
      }
    },
    "/api/v1/get/userManagerRole": {
      "post": {
        "tags": [
          "学生信息事务"
        ],
        "summary": "获取学生的角色信息",
        "description": "通过token获取一个学生的信息",
        "operationId": "获取学生的角色信息_api_v1_get_userManagerRole_post",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/TokenSchema"
              }
            }
          },
          "required": True
        },
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {}
              }
            }
          },
          "422": {
            "description": "Validation Error",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            }
          }
        },
        "security": [
          {
            "OAuth2PasswordBearer": [
              "student"
            ]
          }
        ]
      }
    },
    "/api/v1/get/mit/static/mapping": {
      "get": {
        "tags": [
          "学生医保事务"
        ],
        "summary": "获取医保状态码映射表",
        "description": "获取静态的字典医保状态码映射表",
        "operationId": "获取医保状态码映射表_api_v1_get_mit_static_mapping_get",
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/MITStatusCodeMappingSchema"
                }
              }
            }
          }
        }
      }
    },
    "/api/v1/get/mit/userStatus": {
      "get": {
        "tags": [
          "学生医保事务"
        ],
        "summary": "获取用户的医保状态",
        "description": "获取用户的医保情况状态",
        "operationId": "获取用户的医保状态_api_v1_get_mit_userStatus_get",
        "parameters": [
          {
            "name": "username",
            "in": "query",
            "required": True,
            "schema": {
              "type": "string",
              "title": "Username"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/MITSchema"
                }
              }
            }
          },
          "422": {
            "description": "Validation Error",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            }
          }
        }
      }
    },
    "/api/v1/crete/mit": {
      "post": {
        "tags": [
          "学生医保事务"
        ],
        "summary": "新建一个医保记录",
        "description": "通过Schema新建一个记录",
        "operationId": "新建一个医保记录_api_v1_crete_mit_post",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/MITCreateSchema"
              }
            }
          },
          "required": True
        },
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/StdResp"
                }
              }
            }
          },
          "422": {
            "description": "Validation Error",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            }
          }
        }
      }
    },
    "/api/v1/post/ImageTaskAction": {
      "post": {
        "tags": [
          "材料提交事务"
        ],
        "summary": "新建一个材料申请活动",
        "description": "通过Schema创建一个全局可用的材料申请",
        "operationId": "新建一个材料申请活动_api_v1_post_ImageTaskAction_post",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/ImageTaskActionCreateSchema"
              }
            }
          },
          "required": True
        },
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/StdResp"
                }
              }
            }
          },
          "422": {
            "description": "Validation Error",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            }
          }
        }
      }
    },
    "/api/v1/post/ImageTask/Record": {
      "post": {
        "tags": [
          "材料提交事务"
        ],
        "summary": "提交某个材料活动的信息",
        "description": "提交某个材料活动的信息",
        "operationId": "提交某个材料活动的信息_api_v1_post_ImageTask_Record_post",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/ImageTaskRecordNewUploadSchema"
              }
            }
          },
          "required": True
        },
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/StdResp"
                }
              }
            }
          },
          "422": {
            "description": "Validation Error",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            }
          }
        }
      }
    },
    "/api/v1/get/ImageActions": {
      "get": {
        "tags": [
          "材料提交事务"
        ],
        "summary": "获取所有当前材料提交活动",
        "description": "获取所有可用的材料提交活动",
        "operationId": "获取所有当前材料提交活动_api_v1_get_ImageActions_get",
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {}
              }
            }
          }
        }
      }
    },
    "/api/v1/get/ImageActionById": {
      "get": {
        "tags": [
          "材料提交事务"
        ],
        "summary": "获取材料提交的某个活动详细信息",
        "description": "通过ID获取某个材料提交的详细信息",
        "operationId": "获取材料提交的某个活动详细信息_api_v1_get_ImageActionById_get",
        "parameters": [
          {
            "name": "action_id",
            "in": "query",
            "required": True,
            "schema": {
              "type": "integer",
              "title": "Action Id"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {}
              }
            }
          },
          "422": {
            "description": "Validation Error",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            }
          }
        }
      }
    },
    "/api/v1/get/userImageRecord": {
      "get": {
        "tags": [
          "材料提交事务"
        ],
        "summary": "获取用户的材料状态记录",
        "description": "通过username获取用户的材料状态记录",
        "operationId": "获取用户的材料状态记录_api_v1_get_userImageRecord_get",
        "parameters": [
          {
            "name": "act_id",
            "in": "query",
            "required": True,
            "schema": {
              "type": "integer",
              "title": "Act Id"
            }
          },
          {
            "name": "username",
            "in": "query",
            "required": True,
            "schema": {
              "type": "string",
              "title": "Username"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/ImageTaskRecordSchema"
                }
              }
            }
          },
          "422": {
            "description": "Validation Error",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            }
          }
        }
      }
    },
    "/api/v1/update/userImageRecord": {
      "post": {
        "tags": [
          "材料提交事务"
        ],
        "summary": "更新用户的材料状态记录",
        "description": "通过简要Schema更新",
        "operationId": "更新用户的材料状态记录_api_v1_update_userImageRecord_post",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/ImageTaskRecordNewUploadSchema"
              }
            }
          },
          "required": True
        },
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/StdResp"
                }
              }
            }
          },
          "422": {
            "description": "Validation Error",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            }
          }
        }
      }
    },
    "/api/v1/get/userClazzImageTaskRecord": {
      "get": {
        "tags": [
          "材料提交事务"
        ],
        "summary": "获取班级状况",
        "description": "通过id和clazz获取班级情况",
        "operationId": "获取班级状况_api_v1_get_userClazzImageTaskRecord_get",
        "parameters": [
          {
            "name": "action_id",
            "in": "query",
            "required": True,
            "schema": {
              "type": "integer",
              "title": "Action Id"
            }
          },
          {
            "name": "clazz",
            "in": "query",
            "required": True,
            "schema": {
              "type": "string",
              "title": "Clazz"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {}
              }
            }
          },
          "422": {
            "description": "Validation Error",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            }
          }
        }
      }
    },
    "/api/v1/get/latestNew": {
      "get": {
        "tags": [
          "文档信息事务"
        ],
        "summary": "最新通知",
        "description": "获取最新通知字符串",
        "operationId": "最新通知_api_v1_get_latestNew_get",
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {}
              }
            }
          }
        },
        "deprecated": True
      }
    },
    "/api/v1/update/latestNew": {
      "post": {
        "tags": [
          "文档信息事务"
        ],
        "summary": "更新最新通知",
        "description": "更新最新通知字符串",
        "operationId": "更新最新通知_api_v1_update_latestNew_post",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/MessageDocCreateSchema"
              }
            }
          },
          "required": True
        },
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {}
              }
            }
          },
          "422": {
            "description": "Validation Error",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            }
          }
        },
        "deprecated": True
      }
    },
    "/api/v1/get/richdoc": {
      "get": {
        "tags": [
          "文档信息事务"
        ],
        "summary": "获取富文本",
        "description": "根据文档名获取富文本",
        "operationId": "获取富文本_api_v1_get_richdoc_get",
        "deprecated": True,
        "parameters": [
          {
            "name": "name",
            "in": "query",
            "required": True,
            "schema": {
              "type": "string",
              "title": "Name"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {}
              }
            }
          },
          "422": {
            "description": "Validation Error",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            }
          }
        }
      }
    },
    "/api/v1/post/richdoc": {
      "post": {
        "tags": [
          "文档信息事务"
        ],
        "summary": "通过文件创建一个富文本",
        "description": "通过文件对象创建一个富文本",
        "operationId": "通过文件创建一个富文本_api_v1_post_richdoc_post",
        "deprecated": True,
        "parameters": [
          {
            "name": "name",
            "in": "query",
            "required": True,
            "schema": {
              "type": "string",
              "title": "Name"
            }
          }
        ],
        "requestBody": {
          "required": True,
          "content": {
            "multipart/form-data": {
              "schema": {
                "$ref": "#/components/schemas/Body_____________api_v1_post_richdoc_post"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {}
              }
            }
          },
          "422": {
            "description": "Validation Error",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            }
          }
        }
      }
    },
    "/api/v1/get/walk": {
      "get": {
        "tags": [
          "静态文件管理"
        ],
        "summary": "获取静态文件库的目录",
        "operationId": "获取静态文件库的目录_api_v1_get_walk_get",
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {}
              }
            }
          }
        }
      }
    },
    "/api/v1/pot/html": {
      "post": {
        "tags": [
          "静态文件管理"
        ],
        "summary": "将Html文件加入到静态文件库中",
        "operationId": "将HTML文件加入到静态文件库中_api_v1_pot_html_post",
        "requestBody": {
          "content": {
            "multipart/form-data": {
              "schema": {
                "$ref": "#/components/schemas/Body__HTML____________api_v1_pot_html_post"
              }
            }
          },
          "required": True
        },
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {}
              }
            }
          },
          "422": {
            "description": "Validation Error",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            }
          }
        }
      }
    }
  },
  "components": {
    "schemas": {
      "Body_SECURE_login_token_api_v1_token_post": {
        "properties": {
          "grant_type": {
            "anyOf": [
              {
                "type": "string",
                "pattern": "password"
              },
              {
                "type": "null"
              }
            ],
            "title": "Grant Type"
          },
          "username": {
            "type": "string",
            "title": "Username"
          },
          "password": {
            "type": "string",
            "title": "Password"
          },
          "scope": {
            "type": "string",
            "title": "Scope",
            "default": ""
          },
          "client_id": {
            "anyOf": [
              {
                "type": "string"
              },
              {
                "type": "null"
              }
            ],
            "title": "Client Id"
          },
          "client_secret": {
            "anyOf": [
              {
                "type": "string"
              },
              {
                "type": "null"
              }
            ],
            "title": "Client Secret"
          }
        },
        "type": "object",
        "required": [
          "username",
          "password"
        ],
        "title": "Body_SECURE_login_token_api_v1_token_post"
      },
      "Body__HTML____________api_v1_pot_html_post": {
        "properties": {
          "file": {
            "type": "string",
            "format": "binary",
            "title": "File"
          }
        },
        "type": "object",
        "required": [
          "file"
        ],
        "title": "Body_将HTML文件加入到静态文件库中_api_v1_pot_html_post"
      },
      "Body_____________api_v1_post_richdoc_post": {
        "properties": {
          "file": {
            "type": "string",
            "format": "binary",
            "title": "File"
          }
        },
        "type": "object",
        "required": [
          "file"
        ],
        "title": "Body_通过文件创建一个富文本_api_v1_post_richdoc_post"
      },
      "Body_upload_new_fileObject_api_v1_upload_file_post": {
        "properties": {
          "file": {
            "type": "string",
            "format": "binary",
            "title": "File"
          }
        },
        "type": "object",
        "required": [
          "file"
        ],
        "title": "Body_upload_new_fileObject_api_v1_upload_file_post"
      },
      "Body_upload_new_file_api_v1_upload_new_post": {
        "properties": {
          "file": {
            "type": "string",
            "format": "binary",
            "title": "File"
          }
        },
        "type": "object",
        "required": [
          "file"
        ],
        "title": "Body_upload_new_file_api_v1_upload_new_post"
      },
      "HTTPValidationError": {
        "properties": {
          "detail": {
            "items": {
              "$ref": "#/components/schemas/ValidationError"
            },
            "type": "array",
            "title": "Detail"
          }
        },
        "type": "object",
        "title": "HTTPValidationError"
      },
      "ImageTaskActionCreateSchema": {
        "properties": {
          "act_grant": {
            "type": "string",
            "title": "Act Grant"
          },
          "act_title": {
            "type": "string",
            "title": "Act Title"
          },
          "act_desc": {
            "anyOf": [
              {
                "type": "string"
              },
              {
                "type": "null"
              }
            ],
            "title": "Act Desc"
          },
          "act_range": {
            "anyOf": [
              {
                "type": "string"
              },
              {
                "type": "null"
              }
            ],
            "title": "Act Range",
            "default": "全体"
          },
          "act_on": {
            "type": "boolean",
            "title": "Act On",
            "default": True
          }
        },
        "type": "object",
        "required": [
          "act_grant",
          "act_title",
          "act_desc"
        ],
        "title": "ImageTaskActionCreateSchema"
      },
      "ImageTaskRecordNewUploadSchema": {
        "properties": {
          "act_id": {
            "type": "integer",
            "title": "Act Id"
          },
          "act_username": {
            "type": "string",
            "title": "Act Username"
          },
          "act_url": {
            "type": "string",
            "title": "Act Url"
          }
        },
        "type": "object",
        "required": [
          "act_id",
          "act_username",
          "act_url"
        ],
        "title": "ImageTaskRecordNewUploadSchema"
      },
      "ImageTaskRecordSchema": {
        "properties": {
          "id": {
            "type": "integer",
            "title": "Id"
          },
          "act_id": {
            "type": "integer",
            "title": "Act Id"
          },
          "act_username": {
            "type": "string",
            "title": "Act Username"
          },
          "act_clazz": {
            "type": "string",
            "title": "Act Clazz"
          },
          "act_url": {
            "type": "string",
            "title": "Act Url"
          }
        },
        "type": "object",
        "required": [
          "id",
          "act_id",
          "act_username",
          "act_clazz",
          "act_url"
        ],
        "title": "ImageTaskRecordSchema"
      },
      "MITCreateSchema": {
        "properties": {
          "username": {
            "type": "string",
            "title": "Username"
          },
          "mit_status": {
            "type": "integer",
            "title": "Mit Status"
          },
          "mit_attachments": {
            "anyOf": [
              {
                "type": "string"
              },
              {
                "type": "null"
              }
            ],
            "title": "Mit Attachments"
          },
          "mit_info": {
            "anyOf": [
              {
                "type": "string"
              },
              {
                "type": "null"
              }
            ],
            "title": "Mit Info"
          },
          "mit_choice": {
            "type": "integer",
            "title": "Mit Choice",
            "default": 0
          },
          "mit_on": {
            "type": "boolean",
            "title": "Mit On",
            "default": True
          },
          "mit_msgmap": {
            "anyOf": [
              {
                "type": "string"
              },
              {
                "type": "null"
              }
            ],
            "title": "Mit Msgmap"
          }
        },
        "type": "object",
        "required": [
          "username",
          "mit_status",
          "mit_attachments",
          "mit_info",
          "mit_msgmap"
        ],
        "title": "MITCreateSchema"
      },
      "MITSchema": {
        "properties": {
          "id": {
            "type": "integer",
            "title": "Id"
          },
          "username": {
            "type": "string",
            "title": "Username"
          },
          "mit_status": {
            "type": "integer",
            "title": "Mit Status"
          },
          "mit_attachments": {
            "anyOf": [
              {
                "type": "string"
              },
              {
                "type": "null"
              }
            ],
            "title": "Mit Attachments"
          },
          "mit_info": {
            "anyOf": [
              {
                "type": "object"
              },
              {
                "type": "null"
              }
            ],
            "title": "Mit Info"
          },
          "mit_choice": {
            "type": "integer",
            "title": "Mit Choice",
            "default": 0
          },
          "mit_on": {
            "type": "boolean",
            "title": "Mit On",
            "default": True
          },
          "mit_msgmap": {
            "anyOf": [
              {
                "type": "string"
              },
              {
                "type": "null"
              }
            ],
            "title": "Mit Msgmap"
          }
        },
        "type": "object",
        "required": [
          "id",
          "username",
          "mit_status",
          "mit_attachments",
          "mit_info",
          "mit_msgmap"
        ],
        "title": "MITSchema"
      },
      "MITStatusCodeMappingSchema": {
        "properties": {
          "data": {
            "type": "object",
            "title": "Data"
          }
        },
        "type": "object",
        "required": [
          "data"
        ],
        "title": "MITStatusCodeMappingSchema"
      },
      "MessageDocCreateSchema": {
        "properties": {
          "name": {
            "type": "string",
            "title": "Name"
          },
          "message": {
            "anyOf": [
              {
                "type": "string"
              },
              {
                "type": "null"
              }
            ],
            "title": "Message"
          }
        },
        "type": "object",
        "required": [
          "name",
          "message"
        ],
        "title": "MessageDocCreateSchema"
      },
      "MoralActionCreateSchema": {
        "properties": {
          "action_on": {
            "type": "boolean",
            "title": "Action On",
            "default": True
          },
          "action_grant": {
            "type": "string",
            "title": "Action Grant",
            "default": "系统创建"
          },
          "action_reduce": {
            "type": "boolean",
            "title": "Action Reduce",
            "default": False
          },
          "action_date": {
            "anyOf": [
              {
                "type": "string",
                "format": "date-time"
              },
              {
                "type": "null"
              }
            ],
            "title": "Action Date"
          },
          "action_score": {
            "type": "number",
            "title": "Action Score"
          },
          "action_title": {
            "type": "string",
            "title": "Action Title"
          },
          "action_type": {
            "type": "integer",
            "title": "Action Type"
          },
          "action_detail": {
            "anyOf": [
              {
                "type": "string"
              },
              {
                "type": "null"
              }
            ],
            "title": "Action Detail"
          }
        },
        "type": "object",
        "required": [
          "action_date",
          "action_score",
          "action_title",
          "action_type",
          "action_detail"
        ],
        "title": "MoralActionCreateSchema"
      },
      "MoralActionSchema": {
        "properties": {
          "action_id": {
            "type": "integer",
            "title": "Action Id"
          },
          "action_on": {
            "type": "boolean",
            "title": "Action On",
            "default": True
          },
          "action_grant": {
            "type": "string",
            "title": "Action Grant",
            "default": "系统创建"
          },
          "action_reduce": {
            "type": "boolean",
            "title": "Action Reduce",
            "default": False
          },
          "action_date": {
            "anyOf": [
              {
                "type": "string",
                "format": "date-time"
              },
              {
                "type": "null"
              }
            ],
            "title": "Action Date"
          },
          "action_score": {
            "type": "number",
            "title": "Action Score"
          },
          "action_title": {
            "type": "string",
            "title": "Action Title"
          },
          "action_type": {
            "type": "integer",
            "title": "Action Type",
            "default": 1
          },
          "action_detail": {
            "anyOf": [
              {
                "type": "string"
              },
              {
                "type": "null"
              }
            ],
            "title": "Action Detail"
          }
        },
        "type": "object",
        "required": [
          "action_id",
          "action_date",
          "action_score",
          "action_title",
          "action_detail"
        ],
        "title": "MoralActionSchema"
      },
      "MoralActionSchemaRespList": {
        "properties": {
          "data": {
            "items": {
              "$ref": "#/components/schemas/MoralActionSchema"
            },
            "type": "array",
            "title": "Data"
          }
        },
        "type": "object",
        "required": [
          "data"
        ],
        "title": "MoralActionSchemaRespList"
      },
      "MoralRecordApplySchema": {
        "properties": {
          "action_id": {
            "type": "integer",
            "title": "Action Id"
          },
          "rec_username": {
            "type": "string",
            "title": "Rec Username"
          },
          "rec_urls": {
            "type": "string",
            "title": "Rec Urls"
          },
          "rec_msg": {
            "anyOf": [
              {
                "type": "string"
              },
              {
                "type": "null"
              }
            ],
            "title": "Rec Msg"
          }
        },
        "type": "object",
        "required": [
          "action_id",
          "rec_username",
          "rec_urls",
          "rec_msg"
        ],
        "title": "MoralRecordApplySchema"
      },
      "MoralRecordCheckerSchema": {
        "properties": {
          "rec_id": {
            "type": "integer",
            "title": "Rec Id"
          },
          "rec_status": {
            "type": "integer",
            "title": "Rec Status"
          },
          "chk_username": {
            "type": "string",
            "title": "Chk Username"
          },
          "chk_commit": {
            "anyOf": [
              {
                "type": "string"
              },
              {
                "type": "null"
              }
            ],
            "title": "Chk Commit"
          }
        },
        "type": "object",
        "required": [
          "rec_id",
          "rec_status",
          "chk_username",
          "chk_commit"
        ],
        "title": "MoralRecordCheckerSchema"
      },
      "MoralRecordSchema": {
        "properties": {
          "rec_id": {
            "type": "integer",
            "title": "Rec Id"
          },
          "action_id": {
            "type": "integer",
            "title": "Action Id"
          },
          "action_score": {
            "type": "number",
            "title": "Action Score"
          },
          "rec_username": {
            "type": "string",
            "title": "Rec Username"
          },
          "rec_urls": {
            "type": "string",
            "title": "Rec Urls"
          },
          "rec_msg": {
            "anyOf": [
              {
                "type": "string"
              },
              {
                "type": "null"
              }
            ],
            "title": "Rec Msg"
          },
          "rec_status": {
            "type": "integer",
            "title": "Rec Status"
          },
          "chk_username": {
            "type": "string",
            "title": "Chk Username"
          },
          "chk_commit": {
            "anyOf": [
              {
                "type": "string"
              },
              {
                "type": "null"
              }
            ],
            "title": "Chk Commit"
          }
        },
        "type": "object",
        "required": [
          "rec_id",
          "action_id",
          "action_score",
          "rec_username",
          "rec_urls",
          "rec_msg",
          "rec_status",
          "chk_username",
          "chk_commit"
        ],
        "title": "MoralRecordSchema"
      },
      "OAuth2ResponseSchema": {
        "properties": {
          "access_token": {
            "type": "string",
            "title": "Access Token"
          },
          "token_type": {
            "type": "string",
            "title": "Token Type",
            "default": "bearer"
          }
        },
        "type": "object",
        "required": [
          "access_token"
        ],
        "title": "OAuth2ResponseSchema"
      },
      "OAuth2WechatInfoResponseSchema": {
        "properties": {
          "access_token": {
            "type": "string",
            "title": "Access Token"
          },
          "token_type": {
            "type": "string",
            "title": "Token Type",
            "default": "bearer"
          },
          "openid": {
            "type": "string",
            "title": "Openid"
          }
        },
        "type": "object",
        "required": [
          "access_token",
          "openid"
        ],
        "title": "OAuth2WechatInfoResponseSchema"
      },
      "PasswordUpdateSchema": {
        "properties": {
          "username": {
            "type": "string",
            "title": "Username"
          },
          "oldPassword": {
            "type": "string",
            "title": "Oldpassword"
          },
          "newPassword": {
            "type": "string",
            "title": "Newpassword"
          }
        },
        "type": "object",
        "required": [
          "username",
          "oldPassword",
          "newPassword"
        ],
        "title": "PasswordUpdateSchema"
      },
      "StdResp": {
        "properties": {
          "code": {
            "type": "integer",
            "title": "Code",
            "default": 200
          },
          "data": {
            "anyOf": [
              {
                "type": "string"
              },
              {
                "type": "null"
              }
            ],
            "title": "Data",
            "default": "success"
          },
          "msg": {
            "anyOf": [
              {
                "type": "string"
              },
              {
                "type": "null"
              }
            ],
            "title": "Msg"
          }
        },
        "type": "object",
        "title": "StdResp"
      },
      "StudentSchema": {
        "properties": {
          "username": {
            "type": "string",
            "title": "Username"
          },
          "stu_id": {
            "type": "string",
            "title": "Stu Id"
          },
          "stu_name": {
            "type": "string",
            "title": "Stu Name"
          },
          "stu_clazz": {
            "type": "string",
            "title": "Stu Clazz"
          },
          "stu_sex": {
            "anyOf": [
              {
                "type": "string"
              },
              {
                "type": "null"
              }
            ],
            "title": "Stu Sex"
          },
          "stu_card": {
            "anyOf": [
              {
                "type": "string"
              },
              {
                "type": "null"
              }
            ],
            "title": "Stu Card"
          },
          "stu_nation": {
            "anyOf": [
              {
                "type": "string"
              },
              {
                "type": "null"
              }
            ],
            "title": "Stu Nation"
          },
          "stu_politics": {
            "anyOf": [
              {
                "type": "string"
              },
              {
                "type": "null"
              }
            ],
            "title": "Stu Politics"
          },
          "stu_origin": {
            "anyOf": [
              {
                "type": "string"
              },
              {
                "type": "null"
              }
            ],
            "title": "Stu Origin"
          },
          "stu_home": {
            "anyOf": [
              {
                "type": "string"
              },
              {
                "type": "null"
              }
            ],
            "title": "Stu Home"
          },
          "stu_phone": {
            "anyOf": [
              {
                "type": "string"
              },
              {
                "type": "null"
              }
            ],
            "title": "Stu Phone"
          },
          "stu_email": {
            "anyOf": [
              {
                "type": "string"
              },
              {
                "type": "null"
              }
            ],
            "title": "Stu Email"
          },
          "stu_location": {
            "anyOf": [
              {
                "type": "string"
              },
              {
                "type": "null"
              }
            ],
            "title": "Stu Location"
          },
          "stu_status": {
            "anyOf": [
              {
                "type": "string"
              },
              {
                "type": "null"
              }
            ],
            "title": "Stu Status"
          },
          "stu_graduate": {
            "anyOf": [
              {
                "type": "string"
              },
              {
                "type": "null"
              }
            ],
            "title": "Stu Graduate"
          }
        },
        "type": "object",
        "required": [
          "username",
          "stu_id",
          "stu_name",
          "stu_clazz",
          "stu_sex",
          "stu_card",
          "stu_nation",
          "stu_politics",
          "stu_origin",
          "stu_home",
          "stu_phone",
          "stu_email",
          "stu_location",
          "stu_status",
          "stu_graduate"
        ],
        "title": "StudentSchema"
      },
      "TokenSchema": {
        "properties": {
          "token": {
            "type": "string",
            "title": "Token"
          }
        },
        "type": "object",
        "required": [
          "token"
        ],
        "title": "TokenSchema"
      },
      "UserCurrentMoralScoreSchema": {
        "properties": {
          "datetime": {
            "type": "string",
            "format": "date-time",
            "title": "Datetime"
          },
          "total": {
            "type": "number",
            "title": "Total"
          },
          "uncheck": {
            "type": "number",
            "title": "Uncheck"
          },
          "reduce": {
            "type": "number",
            "title": "Reduce"
          },
          "checked": {
            "type": "number",
            "title": "Checked"
          },
          "reject": {
            "type": "number",
            "title": "Reject"
          }
        },
        "type": "object",
        "required": [
          "datetime",
          "total",
          "uncheck",
          "reduce",
          "checked",
          "reject"
        ],
        "title": "UserCurrentMoralScoreSchema"
      },
      "UserMoralRecordResponseSchema": {
        "properties": {
          "data": {
            "items": {
              "$ref": "#/components/schemas/MoralRecordSchema"
            },
            "type": "array",
            "title": "Data"
          }
        },
        "type": "object",
        "required": [
          "data"
        ],
        "title": "UserMoralRecordResponseSchema"
      },
      "UserSchema": {
        "properties": {
          "username": {
            "type": "string",
            "title": "Username"
          },
          "password": {
            "type": "string",
            "title": "Password"
          },
          "user_scope": {
            "type": "integer",
            "title": "User Scope"
          },
          "user_clazz": {
            "type": "string",
            "title": "User Clazz"
          },
          "user_phone": {
            "type": "string",
            "title": "User Phone"
          },
          "user_info": {
            "type": "object",
            "title": "User Info"
          }
        },
        "type": "object",
        "required": [
          "username",
          "password",
          "user_scope",
          "user_clazz",
          "user_phone",
          "user_info"
        ],
        "title": "UserSchema"
      },
      "ValidationError": {
        "properties": {
          "loc": {
            "items": {
              "anyOf": [
                {
                  "type": "string"
                },
                {
                  "type": "integer"
                }
              ]
            },
            "type": "array",
            "title": "Location"
          },
          "msg": {
            "type": "string",
            "title": "Message"
          },
          "type": {
            "type": "string",
            "title": "Error Type"
          }
        },
        "type": "object",
        "required": [
          "loc",
          "msg",
          "type"
        ],
        "title": "ValidationError"
      },
      "WechatLoginSchema": {
        "properties": {
          "code": {
            "type": "string",
            "title": "Code"
          }
        },
        "type": "object",
        "required": [
          "code"
        ],
        "title": "WechatLoginSchema"
      },
      "WechatUserBindSchema": {
        "properties": {
          "code": {
            "type": "string",
            "title": "Code"
          },
          "username": {
            "type": "string",
            "title": "Username"
          },
          "password": {
            "type": "string",
            "title": "Password"
          }
        },
        "type": "object",
        "required": [
          "code",
          "username",
          "password"
        ],
        "title": "WechatUserBindSchema"
      }
    },
    "securitySchemes": {
      "OAuth2PasswordBearer": {
        "type": "oauth2",
        "flows": {
          "password": {
            "scopes": {
              "student": "学生权限",
              "group": "班委和班级负责人权限",
              "staff": "学生组织权限",
              "manager": "组织负责人权限",
              "system": "系统权限"
            },
            "tokenUrl": "/api/v1/token"
          }
        }
      }
    }
  }
}

all_paths = api.get("paths")
all_paths_list = []
for k,v in all_paths.items():
    all_paths_list.append(k)

with open("paths.csv","w+") as f:
    for i in all_paths_list:
        f.writelines(str(i)+"\n")