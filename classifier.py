import turicreate as turi
import coremltools

url = "dataset/"

data = turi.image_analysis.load_images(url)

labels = ['VEXNet Joystick', 'VEXNet Key 2.0', 'Premade Claw', 'Motor', 'VEX Cortex', 'High Strength Gear', 'Omni Directional Wheels', 'Traction Wheels', 'Normal Gear', 'High Strength Sprocket Gear', 'License Plates', 'Sprocket Gear', 'Tank Threads', 'Foam Cover', 'Programming Module', 'Chains', 'Normal Wheel']

def get_label(path, labels=labels):
    for label in labels:
        if label in path:
            return label

data['label'] = data['path'].apply(get_label)

data.save("VEXPart.frame")

data.explore()

dataBuffer = turi.SFrame("VEXPart.frame")

trainingBuffers, testingBuffers = dataBuffer.random_split(0.9)

model = turi.image_classifier.create(trainingBuffers, target="label", model="resnet-50", max_iterations = 50)

evaluations = model.evaluate(data)
print evaluations["accuracy"]

model_spec = coremltools.utils.load_spec("VEXPartIdentifier().model")
model_fp16_spec = coremltools.utils.convert_neural_network_spec_weights_to_fp16(model_spec)
coremltools.utils.save_spec(model_fp16_spec, "exampleModelFP16.mlmodel")

model.save("VEXFolder.model")

model.export_coreml("VEXPartIdentifier.mlmodel")

