//
//  ViewController.swift
//  UofTHacks
//
//  Created by Arjun Dureja on 2020-01-18.
//  Copyright © 2020 Arjun Dureja. All rights reserved.
//

import UIKit
import PencilKit
import FirebaseStorage
import Kingfisher

class ViewController: UIViewController, PKCanvasViewDelegate, PKToolPickerObserver, UIScreenshotServiceDelegate {

    @IBOutlet weak var canvasView: PKCanvasView!
    
    var dataModelController: DataModelController!
    var drawingIndex: Int = 0
    var hasModifiedDrawing = false
    static let canvasOverscrollHeight: CGFloat = 500
    /// Set up the drawing initially.
    override func viewWillAppear(_ animated: Bool) {
        super.viewWillAppear(animated)

        // Set up the canvas view with the first drawing from the data model.
        canvasView.delegate = self
        canvasView.drawing = dataModelController.drawings[drawingIndex]
        canvasView.alwaysBounceVertical = true
        canvasView.allowsFingerDrawing = false
                view.addSubview(canvasView)
        
        // Set up the tool picker, using the window of our parent because our view has not
        // been added to a window yet.
        if let window = parent?.view.window, let toolPicker = PKToolPicker.shared(for: window) {
            toolPicker.setVisible(true, forFirstResponder: canvasView)
            toolPicker.addObserver(canvasView)
            toolPicker.addObserver(self)
            updateLayout(for: toolPicker)
            canvasView.becomeFirstResponder()
        }
        
        // Always show a back button.
        navigationItem.leftItemsSupplementBackButton = true
        
        // Set this view controller as the delegate for creating full screenshots.
        parent?.view.window?.windowScene?.screenshotService?.delegate = self
    }
   
    func updateLayout(for toolPicker: PKToolPicker) {
        let obscuredFrame = toolPicker.frameObscured(in: view)
        
        // If the tool picker is floating over the canvas, it also contains
        // undo and redo buttons.
        if obscuredFrame.isNull {
            canvasView.contentInset = .zero
            navigationItem.leftBarButtonItems = []
        }
            
        
        // Otherwise, the bottom of the canvas should be inset to the top of the
        // tool picker, and the tool picker no longer displays its own undo and
        // redo buttons.
        else {
            canvasView.contentInset = UIEdgeInsets(top: 0, left: 0, bottom: view.bounds.maxY - obscuredFrame.minY, right: 0)
           // navigationItem.leftBarButtonItems = [undoBarButtonItem, redoBarButtonItem]
        }
        canvasView.scrollIndicatorInsets = canvasView.contentInset
    }
 
    /// When the view is resized, adjust the canvas scale so that it is zoomed to the default `canvasWidth`.
    override func viewDidLayoutSubviews() {
        super.viewDidLayoutSubviews()
        
        let canvasScale = canvasView.bounds.width / DataModel.canvasWidth
        canvasView.minimumZoomScale = canvasScale
        canvasView.maximumZoomScale = canvasScale
        canvasView.zoomScale = canvasScale
        
        // Scroll to the top.
        updateContentSizeForDrawing()
        canvasView.contentOffset = CGPoint(x: 0, y: -canvasView.adjustedContentInset.top)
    }
    
    /// When the view is removed, save the modified drawing, if any.
    override func viewWillDisappear(_ animated: Bool) {
        super.viewWillDisappear(animated)
        
        // Update the drawing in the data model, if it has changed.
        if hasModifiedDrawing {
            dataModelController.updateDrawing(canvasView.drawing, at: drawingIndex)
        }
        
        // Remove this view controller as the screenshot delegate.
        view.window?.windowScene?.screenshotService?.delegate = nil
    }
    
    /// Hide the home indicator, as it will affect latency.
    override var prefersHomeIndicatorAutoHidden: Bool {
        return true
    }
    
    /// Helper method to set a new drawing, with an undo action to go back to the old one.
    func setNewDrawingUndoable(_ newDrawing: PKDrawing) {
        let oldDrawing = canvasView.drawing
        undoManager?.registerUndo(withTarget: self) {
            $0.setNewDrawingUndoable(oldDrawing)
        }
        canvasView.drawing = newDrawing
    }
    
    /// Delegate method: Note that the drawing has changed.
    func canvasViewDrawingDidChange(_ canvasView: PKCanvasView) {
        hasModifiedDrawing = true
        updateContentSizeForDrawing()
    }
    
    /// Helper method to set a suitable content size for the canvas view.
    func updateContentSizeForDrawing() {
        // Update the content size to match the drawing.
        let drawing = canvasView.drawing
        let contentHeight: CGFloat
        
        // Adjust the content size to always be bigger than the drawing height.
        if !drawing.bounds.isNull {
            contentHeight = max(canvasView.bounds.height, (drawing.bounds.maxY + ViewController.canvasOverscrollHeight) * canvasView.zoomScale)
        } else {
            contentHeight = canvasView.bounds.height
        }
        canvasView.contentSize = CGSize(width: DataModel.canvasWidth * canvasView.zoomScale, height: contentHeight)
    }
    
    /// Delegate method: Note that the tool picker has changed which part of the canvas view
    /// it obscures, if any.
    func toolPickerFramesObscuredDidChange(_ toolPicker: PKToolPicker) {
        updateLayout(for: toolPicker)
    }
    
    /// Delegate method: Note that the tool picker has become visible or hidden.
    func toolPickerVisibilityDidChange(_ toolPicker: PKToolPicker) {
        updateLayout(for: toolPicker)
    }
    

    @IBAction func mathButton(_ sender: Any) {
        upload("math")
        
    }
    @IBAction func writeButton(_ sender: Any) {
        upload("write")
    }
    @IBAction func javaButton(_ sender: Any) {
        upload("java")
    }
    @IBAction func pythonButton(_ sender: Any) {
        upload("python")
    }
    
    func upload(_ userMode: String) {
        let pasteboard = UIPasteboard.general
        if !pasteboard.hasImages {
            print("No Images")
        }
        else {
            let topImage = pasteboard.image
            let bottomImage = UIImage(named: "bottom.png")

            let size = CGSize(width: topImage!.size.width*2, height: topImage!.size.height*2)
            UIGraphicsBeginImageContext(size)

            let areaSize = CGRect(x: 0, y: 0, width: size.width, height: size.height)
            
            bottomImage?.draw(in: areaSize)
            
            if self.traitCollection.userInterfaceStyle == .dark {
                bottomImage?.withTintColor(.black)
            }

            topImage!.draw(in: areaSize, blendMode: .normal, alpha: 1)

            let newImage:UIImage = UIGraphicsGetImageFromCurrentImageContext()!

            UIGraphicsEndImageContext()
            
            guard let data = newImage.jpegData(compressionQuality: 1.0) else { return  }
            let imageName = "photo"
            let imageReference = Storage.storage().reference().child(imageName)
            
            var newMetadata = StorageMetadata()
            newMetadata.customMetadata = [
                "mode": userMode]
                    
            imageReference.putData(data, metadata: newMetadata) { (metadata, err) in
                if let err = err {
                    return
                }
            }
            
            imageReference.downloadURL(completion: { (url, err) in
                if let err = err {
                    return
                }
                
                guard let url = url else {
                    return
                }
            })
        }
    }

    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view.
        
    }
}

