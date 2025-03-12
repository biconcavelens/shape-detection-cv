import cv2
import numpy as np

def detect_shapes(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #eliminating error due to rough footage pixels by blur
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)#(5,5 is the kernel matrix (blur strength))
    edges = cv2.Canny(blurred, 50, 150) #drawing edges/boundaries to shapes
    
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) #finding closed shape edges
    
    for contour in contours:
        approx = cv2.approxPolyDP(contour, 0.02 * cv2.arcLength(contour, True), True) #removing extra points that dont form edges
        x, y, w, h = cv2.boundingRect(approx) #drawing a bounding rectangle for the approximated shape (for rectangle square classification)
        
        if w*h>10000: # to avoid single line detection error (detected error in video footage)
            if len(approx) == 3:
                shape_name = "Triangle"
            elif len(approx) == 4:
                aspect_ratio = float(w) / h
                if 0.95 <= aspect_ratio <= 1.05:#square or rectangle based on ratio of side lengths
                    shape_name = "Square"
                else:
                    shape_name = "Rectangle"
            elif len(approx) == 5:
                shape_name = "Pentagon"
            elif len(approx) > 5:
                shape_name = "Circle"
            else: #single line (2 sided lines are eliminated with min area but backup)
                shape_name = "Unknown" 
            
            cv2.drawContours(frame, [approx], -1, (0, 255, 0), 2)
            cv2.putText(frame, shape_name, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    return frame

image = cv2.imread("test.png")
processed_image = detect_shapes(image)
cv2.imshow("Output", processed_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

'''
For video footage. very buggy on my webcam footage due to lack of clarity and lighting

vid = cv2.VideoCapture(0)

while True:
    ret, frame = vid.read()
    if not ret:
        break
    
    processed_frame = detect_shapes(frame)
    cv2.imshow("Output", processed_frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
processed_frame=cv2.imread("test.png")
detect_shapes(processed_frame)
processed_frame.release()
cv2.destroyAllWindows()'''

