"""this module contains only the DomainMetricsController class"""
from digitalpy.component.metrics_controller import MetricController
from ..configuration.domain_constants import COMPONENT_NAME, METRICS_ADDRESS


class DomainMetricsController(MetricController):
    """the metrics controller implementation for the domain
    component."""

    def __init__(self, request, response, action_mapper, configuration):
        super().__init__(
            COMPONENT_NAME,
            METRICS_ADDRESS,
            request,
            response,
            action_mapper,
            configuration,
        )

    def test_metrics(self):
        counter = self.metrics.create_counter("test", "test", "1")
        counter.increment(2, {"abc": "123"})
