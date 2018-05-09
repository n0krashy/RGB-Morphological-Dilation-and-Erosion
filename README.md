# RGB-Morphological-Dilation-and-Erosion
Vision course assignment-3, Q1

Implement a function that can increase the contrast of a colored image using morphological
operators. One way to achieve this goal is to use the following expression to increase the
contrast of image I:


   **_I (IncContrast) = I + a x (I - I ∘ B) - b x (I • B - I)_**
   
where I is the original image, B is the structuring element, a and b are constants,
 indicates opening and  indicates closing.
Apply your function to the image “Mars.jpg”.
Deliverables:
- Your code.
- The output image with a square structuring element of size 3 x 3 when a = 1 and b = 1.
- The output image with a square structuring element of size 9 x 9 when a = 1 and b = 1.
- The output image with a square structuring element of size 3 x 3 when a = 5 and b = 1.
- The output image with a square structuring element of size 3 x 3 when a = 1 and b = 5.
