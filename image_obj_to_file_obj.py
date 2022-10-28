def create_directory_if_not_exist(directory_name):
    '''
    utility responsible to create directory on server if does not exists relative to 
    root path

    :param directory_name: string representation directory_name
    :return: None

    sample input:
    directory_name = 'temporary_face_detection_data_storage'

    eg call:
    create_directory_if_not_exist('temporary_face_detection_data_storage')

    sample output:
    <directory created>
    '''
    try:
        if not os.path.exists(directory_name):
            os.makedirs(directory_name)
        return None
    except Exception as e:
        xprint(e, traceback.format_exc())
        return None


def convert_image_object_to_file(image_object, task_id, default_directory=None):
    '''
    utility responsible to convert string representation of image object to image file 
    with jpg extension

    :param image_object: string representation of image object
    :param task_id: pk of Task model (numeric id)
    :default_directory (optional):  string representation directory_name, the directory will be
                                    relatively created from root path
    :return: string representation of reduced image file path

    step 1: store file path as <task_id>-<YYYY-MM-DD-HH-MM-SS-ffffff>.jpg
            step 1.1:   when default directory argument is present call create_directory_if_not_exist
                        and replace file_path with default directory followed by earlier file 
                        path mentioned at step 2
    step 2: save the file from derived path


    sample input:
    image_object = x...................... (string representation for image binary)
    task_id = 53
    default_directory = temporary_face_detection_data_storage
    
    eg call via search face subex:
    fdd = FaceDetection(53)
    fdd.perform_source_service_type_validation('SUBEX', 'SEARCH_FACE')

    eg call direct
    convert_image_object_to_file(
        'dxx...............',
        53,
        'temporary_face_detection_data_storage',
    )

    sample output:
    temporary_face_detection_data_storage/53-2022-02-08-17-35-08-362484.jpg
    '''
    file_path = ""
    try:
        file_path = '{}-{}.jpg'.format(
            task_id, datetime.now().strftime('%Y-%m-%d-%H-%M-%S-%f')
        )

        if default_directory:
            create_directory_if_not_exist(default_directory)
            file_path = '{}/{}'.format(default_directory, file_path)

        file_instance = open(file_path, 'w')
        file_instance.write(image_object)
        file_instance.close()

        return file_path
    except Exception as e:
        xprint(e, traceback.format_exc())
        return file_path
