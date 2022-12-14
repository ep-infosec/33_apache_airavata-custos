# -*- coding: utf-8 -*-

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

# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ResourceSecretManagementService.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
import custos.server.core.ResourceSecretService_pb2 as ResourceSecretService__pb2
import custos.server.core.IdentityService_pb2 as IdentityService__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='ResourceSecretManagementService.proto',
  package='org.apache.custos.resource.secret.management.service',
  syntax='proto3',
  serialized_options=b'P\001Z\004./pb',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n%ResourceSecretManagementService.proto\x12\x34org.apache.custos.resource.secret.management.service\x1a\x1cgoogle/api/annotations.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1bResourceSecretService.proto\x1a\x15IdentityService.proto2\xe7#\n\x1fResourceSecretManagementService\x12\xb6\x01\n\tgetSecret\x12;.org.apache.custos.resource.secret.service.GetSecretRequest\x1a\x39.org.apache.custos.resource.secret.service.SecretMetadata\"1\x82\xd3\xe4\x93\x02+\x12)/resource-secret-management/v1.0.0/secret\x12\xb9\x01\n\x0fgetKVCredential\x12\x37.org.apache.custos.resource.secret.service.KVCredential\x1a\x37.org.apache.custos.resource.secret.service.KVCredential\"4\x82\xd3\xe4\x93\x02.\x12,/resource-secret-management/v1.0.0/secret/kv\x12\xce\x01\n\x0f\x61\x64\x64KVCredential\x12\x37.org.apache.custos.resource.secret.service.KVCredential\x1aL.org.apache.custos.resource.secret.service.ResourceCredentialOperationStatus\"4\x82\xd3\xe4\x93\x02.\",/resource-secret-management/v1.0.0/secret/kv\x12\xd1\x01\n\x12updateKVCredential\x12\x37.org.apache.custos.resource.secret.service.KVCredential\x1aL.org.apache.custos.resource.secret.service.ResourceCredentialOperationStatus\"4\x82\xd3\xe4\x93\x02.\x1a,/resource-secret-management/v1.0.0/secret/kv\x12\xd1\x01\n\x12\x64\x65leteKVCredential\x12\x37.org.apache.custos.resource.secret.service.KVCredential\x1aL.org.apache.custos.resource.secret.service.ResourceCredentialOperationStatus\"4\x82\xd3\xe4\x93\x02.*,/resource-secret-management/v1.0.0/secret/kv\x12\x97\x01\n\x07getJWKS\x12\x32.org.apache.custos.identity.service.GetJWKSRequest\x1a\x17.google.protobuf.Struct\"?\x82\xd3\xe4\x93\x02\x39\x12\x37/resource-secret-management/v1.0.0/openid-connect/certs\x12\xe4\x01\n\x1cgetResourceCredentialSummary\x12N.org.apache.custos.resource.secret.service.GetResourceCredentialByTokenRequest\x1a\x39.org.apache.custos.resource.secret.service.SecretMetadata\"9\x82\xd3\xe4\x93\x02\x33\x12\x31/resource-secret-management/v1.0.0/secret/summary\x12\xfa\x01\n!getAllResourceCredentialSummaries\x12P.org.apache.custos.resource.secret.service.GetResourceCredentialSummariesRequest\x1a\x46.org.apache.custos.resource.secret.service.ResourceCredentialSummaries\";\x82\xd3\xe4\x93\x02\x35\x12\x33/resource-secret-management/v1.0.0/secret/summaries\x12\xcd\x01\n\x10\x61\x64\x64SSHCredential\x12\x38.org.apache.custos.resource.secret.service.SSHCredential\x1aH.org.apache.custos.resource.secret.service.AddResourceCredentialResponse\"5\x82\xd3\xe4\x93\x02/\"-/resource-secret-management/v1.0.0/secret/ssh\x12\xdc\x01\n\x15\x61\x64\x64PasswordCredential\x12=.org.apache.custos.resource.secret.service.PasswordCredential\x1aH.org.apache.custos.resource.secret.service.AddResourceCredentialResponse\":\x82\xd3\xe4\x93\x02\x34\"2/resource-secret-management/v1.0.0/secret/password\x12\xe5\x01\n\x18\x61\x64\x64\x43\x65rtificateCredential\x12@.org.apache.custos.resource.secret.service.CertificateCredential\x1aH.org.apache.custos.resource.secret.service.AddResourceCredentialResponse\"=\x82\xd3\xe4\x93\x02\x37\"5/resource-secret-management/v1.0.0/secret/certificate\x12\xd3\x01\n\x10getSSHCredential\x12N.org.apache.custos.resource.secret.service.GetResourceCredentialByTokenRequest\x1a\x38.org.apache.custos.resource.secret.service.SSHCredential\"5\x82\xd3\xe4\x93\x02/\x12-/resource-secret-management/v1.0.0/secret/ssh\x12\xe2\x01\n\x15getPasswordCredential\x12N.org.apache.custos.resource.secret.service.GetResourceCredentialByTokenRequest\x1a=.org.apache.custos.resource.secret.service.PasswordCredential\":\x82\xd3\xe4\x93\x02\x34\x12\x32/resource-secret-management/v1.0.0/secret/password\x12\xeb\x01\n\x18getCertificateCredential\x12N.org.apache.custos.resource.secret.service.GetResourceCredentialByTokenRequest\x1a@.org.apache.custos.resource.secret.service.CertificateCredential\"=\x82\xd3\xe4\x93\x02\x37\x12\x35/resource-secret-management/v1.0.0/secret/certificate\x12\xea\x01\n\x13\x64\x65leteSSHCredential\x12N.org.apache.custos.resource.secret.service.GetResourceCredentialByTokenRequest\x1aL.org.apache.custos.resource.secret.service.ResourceCredentialOperationStatus\"5\x82\xd3\xe4\x93\x02/*-/resource-secret-management/v1.0.0/secret/ssh\x12\xef\x01\n\x13\x64\x65letePWDCredential\x12N.org.apache.custos.resource.secret.service.GetResourceCredentialByTokenRequest\x1aL.org.apache.custos.resource.secret.service.ResourceCredentialOperationStatus\":\x82\xd3\xe4\x93\x02\x34*2/resource-secret-management/v1.0.0/secret/password\x12\xfa\x01\n\x1b\x64\x65leteCertificateCredential\x12N.org.apache.custos.resource.secret.service.GetResourceCredentialByTokenRequest\x1aL.org.apache.custos.resource.secret.service.ResourceCredentialOperationStatus\"=\x82\xd3\xe4\x93\x02\x37*5/resource-secret-management/v1.0.0/secret/certificate\x12\xbd\x01\n\x10getCredentialMap\x12\x38.org.apache.custos.resource.secret.service.CredentialMap\x1a\x38.org.apache.custos.resource.secret.service.CredentialMap\"5\x82\xd3\xe4\x93\x02/\x12-/resource-secret-management/v1.0.0/secret/map\x12\xcd\x01\n\x10\x61\x64\x64\x43redentialMap\x12\x38.org.apache.custos.resource.secret.service.CredentialMap\x1aH.org.apache.custos.resource.secret.service.AddResourceCredentialResponse\"5\x82\xd3\xe4\x93\x02/\"-/resource-secret-management/v1.0.0/secret/map\x12\xd4\x01\n\x13updateCredentialMap\x12\x38.org.apache.custos.resource.secret.service.CredentialMap\x1aL.org.apache.custos.resource.secret.service.ResourceCredentialOperationStatus\"5\x82\xd3\xe4\x93\x02/\x1a-/resource-secret-management/v1.0.0/secret/map\x12\xd4\x01\n\x13\x64\x65leteCredentialMap\x12\x38.org.apache.custos.resource.secret.service.CredentialMap\x1aL.org.apache.custos.resource.secret.service.ResourceCredentialOperationStatus\"5\x82\xd3\xe4\x93\x02/*-/resource-secret-management/v1.0.0/secret/mapB\x08P\x01Z\x04./pbb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,ResourceSecretService__pb2.DESCRIPTOR,IdentityService__pb2.DESCRIPTOR,])



_sym_db.RegisterFileDescriptor(DESCRIPTOR)


DESCRIPTOR._options = None

_RESOURCESECRETMANAGEMENTSERVICE = _descriptor.ServiceDescriptor(
  name='ResourceSecretManagementService',
  full_name='org.apache.custos.resource.secret.management.service.ResourceSecretManagementService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=237,
  serialized_end=4820,
  methods=[
  _descriptor.MethodDescriptor(
    name='getSecret',
    full_name='org.apache.custos.resource.secret.management.service.ResourceSecretManagementService.getSecret',
    index=0,
    containing_service=None,
    input_type=ResourceSecretService__pb2._GETSECRETREQUEST,
    output_type=ResourceSecretService__pb2._SECRETMETADATA,
    serialized_options=b'\202\323\344\223\002+\022)/resource-secret-management/v1.0.0/secret',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='getKVCredential',
    full_name='org.apache.custos.resource.secret.management.service.ResourceSecretManagementService.getKVCredential',
    index=1,
    containing_service=None,
    input_type=ResourceSecretService__pb2._KVCREDENTIAL,
    output_type=ResourceSecretService__pb2._KVCREDENTIAL,
    serialized_options=b'\202\323\344\223\002.\022,/resource-secret-management/v1.0.0/secret/kv',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='addKVCredential',
    full_name='org.apache.custos.resource.secret.management.service.ResourceSecretManagementService.addKVCredential',
    index=2,
    containing_service=None,
    input_type=ResourceSecretService__pb2._KVCREDENTIAL,
    output_type=ResourceSecretService__pb2._RESOURCECREDENTIALOPERATIONSTATUS,
    serialized_options=b'\202\323\344\223\002.\",/resource-secret-management/v1.0.0/secret/kv',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='updateKVCredential',
    full_name='org.apache.custos.resource.secret.management.service.ResourceSecretManagementService.updateKVCredential',
    index=3,
    containing_service=None,
    input_type=ResourceSecretService__pb2._KVCREDENTIAL,
    output_type=ResourceSecretService__pb2._RESOURCECREDENTIALOPERATIONSTATUS,
    serialized_options=b'\202\323\344\223\002.\032,/resource-secret-management/v1.0.0/secret/kv',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='deleteKVCredential',
    full_name='org.apache.custos.resource.secret.management.service.ResourceSecretManagementService.deleteKVCredential',
    index=4,
    containing_service=None,
    input_type=ResourceSecretService__pb2._KVCREDENTIAL,
    output_type=ResourceSecretService__pb2._RESOURCECREDENTIALOPERATIONSTATUS,
    serialized_options=b'\202\323\344\223\002.*,/resource-secret-management/v1.0.0/secret/kv',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='getJWKS',
    full_name='org.apache.custos.resource.secret.management.service.ResourceSecretManagementService.getJWKS',
    index=5,
    containing_service=None,
    input_type=IdentityService__pb2._GETJWKSREQUEST,
    output_type=google_dot_protobuf_dot_struct__pb2._STRUCT,
    serialized_options=b'\202\323\344\223\0029\0227/resource-secret-management/v1.0.0/openid-connect/certs',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='getResourceCredentialSummary',
    full_name='org.apache.custos.resource.secret.management.service.ResourceSecretManagementService.getResourceCredentialSummary',
    index=6,
    containing_service=None,
    input_type=ResourceSecretService__pb2._GETRESOURCECREDENTIALBYTOKENREQUEST,
    output_type=ResourceSecretService__pb2._SECRETMETADATA,
    serialized_options=b'\202\323\344\223\0023\0221/resource-secret-management/v1.0.0/secret/summary',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='getAllResourceCredentialSummaries',
    full_name='org.apache.custos.resource.secret.management.service.ResourceSecretManagementService.getAllResourceCredentialSummaries',
    index=7,
    containing_service=None,
    input_type=ResourceSecretService__pb2._GETRESOURCECREDENTIALSUMMARIESREQUEST,
    output_type=ResourceSecretService__pb2._RESOURCECREDENTIALSUMMARIES,
    serialized_options=b'\202\323\344\223\0025\0223/resource-secret-management/v1.0.0/secret/summaries',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='addSSHCredential',
    full_name='org.apache.custos.resource.secret.management.service.ResourceSecretManagementService.addSSHCredential',
    index=8,
    containing_service=None,
    input_type=ResourceSecretService__pb2._SSHCREDENTIAL,
    output_type=ResourceSecretService__pb2._ADDRESOURCECREDENTIALRESPONSE,
    serialized_options=b'\202\323\344\223\002/\"-/resource-secret-management/v1.0.0/secret/ssh',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='addPasswordCredential',
    full_name='org.apache.custos.resource.secret.management.service.ResourceSecretManagementService.addPasswordCredential',
    index=9,
    containing_service=None,
    input_type=ResourceSecretService__pb2._PASSWORDCREDENTIAL,
    output_type=ResourceSecretService__pb2._ADDRESOURCECREDENTIALRESPONSE,
    serialized_options=b'\202\323\344\223\0024\"2/resource-secret-management/v1.0.0/secret/password',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='addCertificateCredential',
    full_name='org.apache.custos.resource.secret.management.service.ResourceSecretManagementService.addCertificateCredential',
    index=10,
    containing_service=None,
    input_type=ResourceSecretService__pb2._CERTIFICATECREDENTIAL,
    output_type=ResourceSecretService__pb2._ADDRESOURCECREDENTIALRESPONSE,
    serialized_options=b'\202\323\344\223\0027\"5/resource-secret-management/v1.0.0/secret/certificate',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='getSSHCredential',
    full_name='org.apache.custos.resource.secret.management.service.ResourceSecretManagementService.getSSHCredential',
    index=11,
    containing_service=None,
    input_type=ResourceSecretService__pb2._GETRESOURCECREDENTIALBYTOKENREQUEST,
    output_type=ResourceSecretService__pb2._SSHCREDENTIAL,
    serialized_options=b'\202\323\344\223\002/\022-/resource-secret-management/v1.0.0/secret/ssh',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='getPasswordCredential',
    full_name='org.apache.custos.resource.secret.management.service.ResourceSecretManagementService.getPasswordCredential',
    index=12,
    containing_service=None,
    input_type=ResourceSecretService__pb2._GETRESOURCECREDENTIALBYTOKENREQUEST,
    output_type=ResourceSecretService__pb2._PASSWORDCREDENTIAL,
    serialized_options=b'\202\323\344\223\0024\0222/resource-secret-management/v1.0.0/secret/password',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='getCertificateCredential',
    full_name='org.apache.custos.resource.secret.management.service.ResourceSecretManagementService.getCertificateCredential',
    index=13,
    containing_service=None,
    input_type=ResourceSecretService__pb2._GETRESOURCECREDENTIALBYTOKENREQUEST,
    output_type=ResourceSecretService__pb2._CERTIFICATECREDENTIAL,
    serialized_options=b'\202\323\344\223\0027\0225/resource-secret-management/v1.0.0/secret/certificate',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='deleteSSHCredential',
    full_name='org.apache.custos.resource.secret.management.service.ResourceSecretManagementService.deleteSSHCredential',
    index=14,
    containing_service=None,
    input_type=ResourceSecretService__pb2._GETRESOURCECREDENTIALBYTOKENREQUEST,
    output_type=ResourceSecretService__pb2._RESOURCECREDENTIALOPERATIONSTATUS,
    serialized_options=b'\202\323\344\223\002/*-/resource-secret-management/v1.0.0/secret/ssh',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='deletePWDCredential',
    full_name='org.apache.custos.resource.secret.management.service.ResourceSecretManagementService.deletePWDCredential',
    index=15,
    containing_service=None,
    input_type=ResourceSecretService__pb2._GETRESOURCECREDENTIALBYTOKENREQUEST,
    output_type=ResourceSecretService__pb2._RESOURCECREDENTIALOPERATIONSTATUS,
    serialized_options=b'\202\323\344\223\0024*2/resource-secret-management/v1.0.0/secret/password',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='deleteCertificateCredential',
    full_name='org.apache.custos.resource.secret.management.service.ResourceSecretManagementService.deleteCertificateCredential',
    index=16,
    containing_service=None,
    input_type=ResourceSecretService__pb2._GETRESOURCECREDENTIALBYTOKENREQUEST,
    output_type=ResourceSecretService__pb2._RESOURCECREDENTIALOPERATIONSTATUS,
    serialized_options=b'\202\323\344\223\0027*5/resource-secret-management/v1.0.0/secret/certificate',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='getCredentialMap',
    full_name='org.apache.custos.resource.secret.management.service.ResourceSecretManagementService.getCredentialMap',
    index=17,
    containing_service=None,
    input_type=ResourceSecretService__pb2._CREDENTIALMAP,
    output_type=ResourceSecretService__pb2._CREDENTIALMAP,
    serialized_options=b'\202\323\344\223\002/\022-/resource-secret-management/v1.0.0/secret/map',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='addCredentialMap',
    full_name='org.apache.custos.resource.secret.management.service.ResourceSecretManagementService.addCredentialMap',
    index=18,
    containing_service=None,
    input_type=ResourceSecretService__pb2._CREDENTIALMAP,
    output_type=ResourceSecretService__pb2._ADDRESOURCECREDENTIALRESPONSE,
    serialized_options=b'\202\323\344\223\002/\"-/resource-secret-management/v1.0.0/secret/map',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='updateCredentialMap',
    full_name='org.apache.custos.resource.secret.management.service.ResourceSecretManagementService.updateCredentialMap',
    index=19,
    containing_service=None,
    input_type=ResourceSecretService__pb2._CREDENTIALMAP,
    output_type=ResourceSecretService__pb2._RESOURCECREDENTIALOPERATIONSTATUS,
    serialized_options=b'\202\323\344\223\002/\032-/resource-secret-management/v1.0.0/secret/map',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='deleteCredentialMap',
    full_name='org.apache.custos.resource.secret.management.service.ResourceSecretManagementService.deleteCredentialMap',
    index=20,
    containing_service=None,
    input_type=ResourceSecretService__pb2._CREDENTIALMAP,
    output_type=ResourceSecretService__pb2._RESOURCECREDENTIALOPERATIONSTATUS,
    serialized_options=b'\202\323\344\223\002/*-/resource-secret-management/v1.0.0/secret/map',
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_RESOURCESECRETMANAGEMENTSERVICE)

DESCRIPTOR.services_by_name['ResourceSecretManagementService'] = _RESOURCESECRETMANAGEMENTSERVICE

# @@protoc_insertion_point(module_scope)
