#  Licensed to the Apache Software Foundation (ASF) under one
#  or more contributor license agreements. See the NOTICE file
#  distributed with this work for additional information
#  regarding copyright ownership. The ASF licenses this file
#  to you under the Apache License, Version 2.0 (the
#  "License"); you may not use this file except in compliance
#  with the License. You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing,
#   software distributed under the License is distributed on an
#   "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
#   KIND, either express or implied. See the License for the
#   specific language governing permissions and limitations
#   under the License.

# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import custos.server.core.CredentialStoreService_pb2 as CredentialStoreService__pb2
import custos.server.integration.IdentityManagementService_pb2 as IdentityManagementService__pb2
import custos.server.core.IdentityService_pb2 as IdentityService__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


class IdentityManagementServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.authenticate = channel.unary_unary(
                '/org.apache.custos.identity.management.service.IdentityManagementService/authenticate',
                request_serializer=IdentityService__pb2.AuthenticationRequest.SerializeToString,
                response_deserializer=IdentityService__pb2.AuthToken.FromString,
                )
        self.isAuthenticated = channel.unary_unary(
                '/org.apache.custos.identity.management.service.IdentityManagementService/isAuthenticated',
                request_serializer=IdentityService__pb2.AuthToken.SerializeToString,
                response_deserializer=IdentityService__pb2.IsAuthenticatedResponse.FromString,
                )
        self.getUser = channel.unary_unary(
                '/org.apache.custos.identity.management.service.IdentityManagementService/getUser',
                request_serializer=IdentityService__pb2.AuthToken.SerializeToString,
                response_deserializer=IdentityService__pb2.User.FromString,
                )
        self.getUserManagementServiceAccountAccessToken = channel.unary_unary(
                '/org.apache.custos.identity.management.service.IdentityManagementService/getUserManagementServiceAccountAccessToken',
                request_serializer=IdentityService__pb2.GetUserManagementSATokenRequest.SerializeToString,
                response_deserializer=IdentityService__pb2.AuthToken.FromString,
                )
        self.endUserSession = channel.unary_unary(
                '/org.apache.custos.identity.management.service.IdentityManagementService/endUserSession',
                request_serializer=IdentityManagementService__pb2.EndSessionRequest.SerializeToString,
                response_deserializer=IdentityService__pb2.OperationStatus.FromString,
                )
        self.authorize = channel.unary_unary(
                '/org.apache.custos.identity.management.service.IdentityManagementService/authorize',
                request_serializer=IdentityManagementService__pb2.AuthorizationRequest.SerializeToString,
                response_deserializer=IdentityManagementService__pb2.AuthorizationResponse.FromString,
                )
        self.token = channel.unary_unary(
                '/org.apache.custos.identity.management.service.IdentityManagementService/token',
                request_serializer=IdentityService__pb2.GetTokenRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_struct__pb2.Struct.FromString,
                )
        self.getCredentials = channel.unary_unary(
                '/org.apache.custos.identity.management.service.IdentityManagementService/getCredentials',
                request_serializer=IdentityManagementService__pb2.GetCredentialsRequest.SerializeToString,
                response_deserializer=CredentialStoreService__pb2.Credentials.FromString,
                )
        self.getOIDCConfiguration = channel.unary_unary(
                '/org.apache.custos.identity.management.service.IdentityManagementService/getOIDCConfiguration',
                request_serializer=IdentityService__pb2.GetOIDCConfiguration.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_struct__pb2.Struct.FromString,
                )
        self.getAgentToken = channel.unary_unary(
                '/org.apache.custos.identity.management.service.IdentityManagementService/getAgentToken',
                request_serializer=IdentityManagementService__pb2.GetAgentTokenRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_struct__pb2.Struct.FromString,
                )
        self.endAgentSession = channel.unary_unary(
                '/org.apache.custos.identity.management.service.IdentityManagementService/endAgentSession',
                request_serializer=IdentityManagementService__pb2.EndSessionRequest.SerializeToString,
                response_deserializer=IdentityService__pb2.OperationStatus.FromString,
                )
        self.isAgentAuthenticated = channel.unary_unary(
                '/org.apache.custos.identity.management.service.IdentityManagementService/isAgentAuthenticated',
                request_serializer=IdentityService__pb2.AuthToken.SerializeToString,
                response_deserializer=IdentityService__pb2.IsAuthenticatedResponse.FromString,
                )


class IdentityManagementServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def authenticate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def isAuthenticated(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getUser(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getUserManagementServiceAccountAccessToken(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def endUserSession(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def authorize(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def token(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getCredentials(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getOIDCConfiguration(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getAgentToken(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def endAgentSession(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def isAgentAuthenticated(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_IdentityManagementServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'authenticate': grpc.unary_unary_rpc_method_handler(
                    servicer.authenticate,
                    request_deserializer=IdentityService__pb2.AuthenticationRequest.FromString,
                    response_serializer=IdentityService__pb2.AuthToken.SerializeToString,
            ),
            'isAuthenticated': grpc.unary_unary_rpc_method_handler(
                    servicer.isAuthenticated,
                    request_deserializer=IdentityService__pb2.AuthToken.FromString,
                    response_serializer=IdentityService__pb2.IsAuthenticatedResponse.SerializeToString,
            ),
            'getUser': grpc.unary_unary_rpc_method_handler(
                    servicer.getUser,
                    request_deserializer=IdentityService__pb2.AuthToken.FromString,
                    response_serializer=IdentityService__pb2.User.SerializeToString,
            ),
            'getUserManagementServiceAccountAccessToken': grpc.unary_unary_rpc_method_handler(
                    servicer.getUserManagementServiceAccountAccessToken,
                    request_deserializer=IdentityService__pb2.GetUserManagementSATokenRequest.FromString,
                    response_serializer=IdentityService__pb2.AuthToken.SerializeToString,
            ),
            'endUserSession': grpc.unary_unary_rpc_method_handler(
                    servicer.endUserSession,
                    request_deserializer=IdentityManagementService__pb2.EndSessionRequest.FromString,
                    response_serializer=IdentityService__pb2.OperationStatus.SerializeToString,
            ),
            'authorize': grpc.unary_unary_rpc_method_handler(
                    servicer.authorize,
                    request_deserializer=IdentityManagementService__pb2.AuthorizationRequest.FromString,
                    response_serializer=IdentityManagementService__pb2.AuthorizationResponse.SerializeToString,
            ),
            'token': grpc.unary_unary_rpc_method_handler(
                    servicer.token,
                    request_deserializer=IdentityService__pb2.GetTokenRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_struct__pb2.Struct.SerializeToString,
            ),
            'getCredentials': grpc.unary_unary_rpc_method_handler(
                    servicer.getCredentials,
                    request_deserializer=IdentityManagementService__pb2.GetCredentialsRequest.FromString,
                    response_serializer=CredentialStoreService__pb2.Credentials.SerializeToString,
            ),
            'getOIDCConfiguration': grpc.unary_unary_rpc_method_handler(
                    servicer.getOIDCConfiguration,
                    request_deserializer=IdentityService__pb2.GetOIDCConfiguration.FromString,
                    response_serializer=google_dot_protobuf_dot_struct__pb2.Struct.SerializeToString,
            ),
            'getAgentToken': grpc.unary_unary_rpc_method_handler(
                    servicer.getAgentToken,
                    request_deserializer=IdentityManagementService__pb2.GetAgentTokenRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_struct__pb2.Struct.SerializeToString,
            ),
            'endAgentSession': grpc.unary_unary_rpc_method_handler(
                    servicer.endAgentSession,
                    request_deserializer=IdentityManagementService__pb2.EndSessionRequest.FromString,
                    response_serializer=IdentityService__pb2.OperationStatus.SerializeToString,
            ),
            'isAgentAuthenticated': grpc.unary_unary_rpc_method_handler(
                    servicer.isAgentAuthenticated,
                    request_deserializer=IdentityService__pb2.AuthToken.FromString,
                    response_serializer=IdentityService__pb2.IsAuthenticatedResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'org.apache.custos.identity.management.service.IdentityManagementService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class IdentityManagementService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def authenticate(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/org.apache.custos.identity.management.service.IdentityManagementService/authenticate',
            IdentityService__pb2.AuthenticationRequest.SerializeToString,
            IdentityService__pb2.AuthToken.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def isAuthenticated(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/org.apache.custos.identity.management.service.IdentityManagementService/isAuthenticated',
            IdentityService__pb2.AuthToken.SerializeToString,
            IdentityService__pb2.IsAuthenticatedResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/org.apache.custos.identity.management.service.IdentityManagementService/getUser',
            IdentityService__pb2.AuthToken.SerializeToString,
            IdentityService__pb2.User.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getUserManagementServiceAccountAccessToken(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/org.apache.custos.identity.management.service.IdentityManagementService/getUserManagementServiceAccountAccessToken',
            IdentityService__pb2.GetUserManagementSATokenRequest.SerializeToString,
            IdentityService__pb2.AuthToken.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def endUserSession(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/org.apache.custos.identity.management.service.IdentityManagementService/endUserSession',
            IdentityManagementService__pb2.EndSessionRequest.SerializeToString,
            IdentityService__pb2.OperationStatus.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def authorize(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/org.apache.custos.identity.management.service.IdentityManagementService/authorize',
            IdentityManagementService__pb2.AuthorizationRequest.SerializeToString,
            IdentityManagementService__pb2.AuthorizationResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def token(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/org.apache.custos.identity.management.service.IdentityManagementService/token',
            IdentityService__pb2.GetTokenRequest.SerializeToString,
            google_dot_protobuf_dot_struct__pb2.Struct.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getCredentials(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/org.apache.custos.identity.management.service.IdentityManagementService/getCredentials',
            IdentityManagementService__pb2.GetCredentialsRequest.SerializeToString,
            CredentialStoreService__pb2.Credentials.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getOIDCConfiguration(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/org.apache.custos.identity.management.service.IdentityManagementService/getOIDCConfiguration',
            IdentityService__pb2.GetOIDCConfiguration.SerializeToString,
            google_dot_protobuf_dot_struct__pb2.Struct.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getAgentToken(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/org.apache.custos.identity.management.service.IdentityManagementService/getAgentToken',
            IdentityManagementService__pb2.GetAgentTokenRequest.SerializeToString,
            google_dot_protobuf_dot_struct__pb2.Struct.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def endAgentSession(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/org.apache.custos.identity.management.service.IdentityManagementService/endAgentSession',
            IdentityManagementService__pb2.EndSessionRequest.SerializeToString,
            IdentityService__pb2.OperationStatus.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def isAgentAuthenticated(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/org.apache.custos.identity.management.service.IdentityManagementService/isAgentAuthenticated',
            IdentityService__pb2.AuthToken.SerializeToString,
            IdentityService__pb2.IsAuthenticatedResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
