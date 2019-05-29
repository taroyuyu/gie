import modules.internals
import modules.images_internal

def average_color(image: modules.internals.Image)->modules.internals.Color:
    r = 0
    g = 0
    b = 0
    pixel_count = image.width() * image.height()

    for row in range(image.height()):
        for column in range(image.width()):
            color = image.pixel_at(row, column)
            r += color.r
            g += color.g
            b += color.b

    r = r // pixel_count
    g = g // pixel_count
    b = b // pixel_count

    return modules.internals.Color(r, g, b)

def sample(image: modules.internals.Image, row: int, column: int)->modules.internals.Color:
    return image.pixel_at(row, column)

def separate_blue_channel(image: modules.internals.Image)->modules.internals.Image:
    return modules.images_internal.separate_blue_channel(image)

def luminance_map(image: modules.internals.Image)->modules.internals.Image:
    return modules.images_internal.luminance_map(image)

def pixel_sort(source: modules.internals.Image, mask: modules.internals.Image, threshold: int)->modules.internals.Image:
    return modules.images_internal.pixel_sort(source, mask, threshold)

def pixel_distort_displace(source: modules.internals.Image, map: modules.internals.Image, row_factor: float, column_factor: float)->modules.internals.Image:
    return modules.images_internal.pixel_distort_displace(source, map, row_factor, column_factor)

def displacement(source: modules.internals.Image, map: modules.internals.Image, row_factor: float, column_factor: float)->modules.internals.Image:
    return modules.images_internal.displacement(source, map, row_factor, column_factor)