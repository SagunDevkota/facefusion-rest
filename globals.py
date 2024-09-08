import facefusion.face_analyser
import facefusion.globals
import facefusion.processors.frame.globals
import facefusion.processors.frame.modules
import facefusion.processors.frame.modules.face_swapper
import cv2

facefusion.globals.face_selector_mode = 'reference'
facefusion.globals.frame_processors = ['face_swapper']
facefusion.globals.output_path = "./outputs/"
facefusion.globals.face_detector_model = "yoloface"
facefusion.globals.face_recognizer_model = "arcface_inswapper"
facefusion.globals.execution_device_id = 0
facefusion.globals.execution_providers = ['CPUExecutionProvider']
facefusion.globals.execution_thread_count = 4
facefusion.globals.execution_queue_count = 1
facefusion.globals.face_analyser_order = 'left-right'
facefusion.globals.video_memory_strategy = 'strict'
facefusion.globals.system_memory_limit = 0
facefusion.globals.face_detector_size = '640x640'
facefusion.globals.face_detector_score = 0.5
facefusion.globals.face_landmarker_score = 0.5
facefusion.globals.reference_face_position = 0
facefusion.globals.reference_face_distance = 0.6
facefusion.globals.reference_frame_number = 0
facefusion.globals.face_mask_types = ['box']
facefusion.globals.face_mask_blur = 0.3
facefusion.globals.face_mask_padding = (0,0,0,0)
facefusion.globals.face_mask_regions = ['skin', 'left-eyebrow', 'right-eyebrow', 'left-eye', 'right-eye', 'glasses', 'nose', 'mouth', 'upper-lip', 'lower-lip']
facefusion.globals.temp_frame_format = 'png'
facefusion.globals.output_image_quality = 80
facefusion.globals.config_path = 'facefusion.ini'
facefusion.processors.frame.globals.face_swapper_model = 'inswapper_128'


def update_globals(source,destination):
    facefusion.globals.source_paths = [source]
    facefusion.globals.target_path = destination
    image = cv2.imread(facefusion.globals.target_path)
    shape = image.shape
    facefusion.globals.output_image_resolution = f'{shape[1]}x{shape[0]}'