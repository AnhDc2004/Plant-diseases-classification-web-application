class LabelMapper:
    PLANT_LABELS = [
        'apple', 'bell_pepper', 'cassava', 'cherry', 'coffee', 'corn',
        'gourd', 'grape', 'hibiscus', 'papaya', 'peach', 'potato',
        'rice', 'rose', 'strawberry', 'sugarcane', 'tomato', 'watermelon'
    ]

    DISEASE_LABELS = [
        'alternaria_leaf_spot', 'anthracnose', 'bacterial_blight', 'bacterial_spot', 'bacterial_wilt',
        'black_measles', 'black_rot', 'blast', 'brown_spot', 'brown_streak_disease',
        'cercospora_leaf', 'cercospora_leaf_spot', 'chlorosis', 'common_rust', 'cucumber_mosaic_virus',
        'downy_mildew', 'early_blight', 'fungal_leaf_spot', 'gray_leaf_spot', 'gray_spot',
        'green_mottle', 'gummy_stem_blight', 'healthy', 'insect_damage', 'iron_deficiency',
        'late_blight', 'leaf_blight', 'leaf_mold', 'leaf_scorch', 'leaf_spot',
        'leafroll_virus', 'magnesium_deficiency', 'mosaic', 'mosaic_disease', 'mosaic_virus',
        'nematode', 'northern_leaf_blight', 'nutrient_deficiency', 'pest_damage', 'pests',
        'phytophthora', 'powdery_mildew', 'red_rot', 'red_spider_mite', 'ringspot_virus',
        'rust', 'scab', 'septoria_leaf_spot', 'slug_sawfly', 'spider_mites',
        'target_spot', 'tungro', 'viral_mosaic', 'yellow_leaf', 'yellow_leaf_curl_virus',
        'yellow_mosaic_virus'
    ]

    @staticmethod
    def id_to_label(task_type: str, label_id: int) -> str:
        task = task_type.lower().strip()

        if task == 'plant':
            labels = LabelMapper.PLANT_LABELS
        elif task == 'disease':
            labels = LabelMapper.DISEASE_LABELS
        else:
            return "Error: Invalid task_type. Use 'plant' or 'disease'."

        if 0 <= label_id < len(labels):
            return labels[label_id]
        else:
            return f"Error: ID {label_id} out of range (Max: {len(labels) - 1})"

    @staticmethod
    def label_to_id(task_type: str, label_name: str) -> int:
        task = task_type.lower().strip()
        label_name = label_name.strip()

        if task == 'plant':
            labels = LabelMapper.PLANT_LABELS
        elif task == 'disease':
            labels = LabelMapper.DISEASE_LABELS
        else:
            return -1

        try:
            return labels.index(label_name)
        except ValueError:
            return -1