# coding: utf-8

# flake8: noqa

"""
    Lightly API

    Lightly.ai enables you to do self-supervised learning in an easy and intuitive way. The lightly.ai OpenAPI spec defines how one can interact with our REST API to unleash the full potential of lightly.ai  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: support@lightly.ai
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

# import apis into sdk package
from lightly.openapi_generated.swagger_client.api.datasets_api import DatasetsApi
from lightly.openapi_generated.swagger_client.api.embeddings_api import EmbeddingsApi
from lightly.openapi_generated.swagger_client.api.jobs_api import JobsApi
from lightly.openapi_generated.swagger_client.api.mappings_api import MappingsApi
from lightly.openapi_generated.swagger_client.api.quota_api import QuotaApi
from lightly.openapi_generated.swagger_client.api.samples_api import SamplesApi
from lightly.openapi_generated.swagger_client.api.samplings_api import SamplingsApi
from lightly.openapi_generated.swagger_client.api.scores_api import ScoresApi
from lightly.openapi_generated.swagger_client.api.tags_api import TagsApi
from lightly.openapi_generated.swagger_client.api.versioning_api import VersioningApi

# import ApiClient
from lightly.openapi_generated.swagger_client.api_client import ApiClient
from lightly.openapi_generated.swagger_client.configuration import Configuration
# import models into sdk package
from lightly.openapi_generated.swagger_client.models.active_learning_score_create_request import ActiveLearningScoreCreateRequest
from lightly.openapi_generated.swagger_client.models.active_learning_score_data import ActiveLearningScoreData
from lightly.openapi_generated.swagger_client.models.active_learning_score_type import ActiveLearningScoreType
from lightly.openapi_generated.swagger_client.models.active_learning_scores import ActiveLearningScores
from lightly.openapi_generated.swagger_client.models.api_error_code import ApiErrorCode
from lightly.openapi_generated.swagger_client.models.api_error_response import ApiErrorResponse
from lightly.openapi_generated.swagger_client.models.async_task_data import AsyncTaskData
from lightly.openapi_generated.swagger_client.models.create_entity_response import CreateEntityResponse
from lightly.openapi_generated.swagger_client.models.dataset_create_request import DatasetCreateRequest
from lightly.openapi_generated.swagger_client.models.dataset_data import DatasetData
from lightly.openapi_generated.swagger_client.models.dataset_embedding_data import DatasetEmbeddingData
from lightly.openapi_generated.swagger_client.models.dataset_name import DatasetName
from lightly.openapi_generated.swagger_client.models.dataset_type import DatasetType
from lightly.openapi_generated.swagger_client.models.dataset_update_request import DatasetUpdateRequest
from lightly.openapi_generated.swagger_client.models.embedding_data import EmbeddingData
from lightly.openapi_generated.swagger_client.models.general_job_result import GeneralJobResult
from lightly.openapi_generated.swagger_client.models.image_type import ImageType
from lightly.openapi_generated.swagger_client.models.initial_tag_create_request import InitialTagCreateRequest
from lightly.openapi_generated.swagger_client.models.job_result_type import JobResultType
from lightly.openapi_generated.swagger_client.models.job_state import JobState
from lightly.openapi_generated.swagger_client.models.job_status_data import JobStatusData
from lightly.openapi_generated.swagger_client.models.job_status_data_result import JobStatusDataResult
from lightly.openapi_generated.swagger_client.models.job_status_meta import JobStatusMeta
from lightly.openapi_generated.swagger_client.models.jobs_data import JobsData
from lightly.openapi_generated.swagger_client.models.mongo_object_id import MongoObjectID
from lightly.openapi_generated.swagger_client.models.object_id import ObjectId
from lightly.openapi_generated.swagger_client.models.sample_create_request import SampleCreateRequest
from lightly.openapi_generated.swagger_client.models.sample_data import SampleData
from lightly.openapi_generated.swagger_client.models.sample_meta_data import SampleMetaData
from lightly.openapi_generated.swagger_client.models.sample_update_request import SampleUpdateRequest
from lightly.openapi_generated.swagger_client.models.sampling_config import SamplingConfig
from lightly.openapi_generated.swagger_client.models.sampling_config_stopping_condition import SamplingConfigStoppingCondition
from lightly.openapi_generated.swagger_client.models.sampling_create_request import SamplingCreateRequest
from lightly.openapi_generated.swagger_client.models.sampling_method import SamplingMethod
from lightly.openapi_generated.swagger_client.models.tag_active_learning_scores_data import TagActiveLearningScoresData
from lightly.openapi_generated.swagger_client.models.tag_bit_mask_data import TagBitMaskData
from lightly.openapi_generated.swagger_client.models.tag_change_data import TagChangeData
from lightly.openapi_generated.swagger_client.models.tag_create_request import TagCreateRequest
from lightly.openapi_generated.swagger_client.models.tag_creator import TagCreator
from lightly.openapi_generated.swagger_client.models.tag_data import TagData
from lightly.openapi_generated.swagger_client.models.tag_filenames_data import TagFilenamesData
from lightly.openapi_generated.swagger_client.models.tag_name import TagName
from lightly.openapi_generated.swagger_client.models.timestamp import Timestamp
from lightly.openapi_generated.swagger_client.models.version_number import VersionNumber
from lightly.openapi_generated.swagger_client.models.write_csv_url_data import WriteCSVUrlData