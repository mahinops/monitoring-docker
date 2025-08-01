import os
from opentelemetry import trace
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.resources import SERVICE_NAME, Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.instrumentation.django import DjangoInstrumentor

def configure_tracing():
    # Define the service name and resource attributes
    resource = Resource(attributes={
        SERVICE_NAME: "django-project1",
        "service.version": "1.0.0",
        "environment": "development"
    })

    # Set the TracerProvider with the resource
    trace.set_tracer_provider(TracerProvider(resource=resource))
    tracer_provider = trace.get_tracer_provider()

    # Configure OTLP Exporter - use the correct endpoint for HTTP
    tempo_endpoint = os.getenv('TEMPO_ENDPOINT', 'http://tempo:4318/v1/traces')
    otlp_exporter = OTLPSpanExporter(
        endpoint=tempo_endpoint,
        headers={}
    )
    
    span_processor = BatchSpanProcessor(otlp_exporter)
    tracer_provider.add_span_processor(span_processor)

    # Instrument Django
    DjangoInstrumentor().instrument()

    print(f"Tracing configured with endpoint: {tempo_endpoint}")
    print("Django instrumentation enabled")