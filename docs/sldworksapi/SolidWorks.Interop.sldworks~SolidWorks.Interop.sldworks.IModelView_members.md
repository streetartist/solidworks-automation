# IModelView Interface Members

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView_members`

Allows you access to the model view's orientation, translation, and the Microsoft handle to the window.
The following tables list the members exposed by [IModelView](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView.md).

Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | [Camera](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~Camera.md) | Gets or sets the camera. |
| Property | [DisplayMode](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~DisplayMode.md) | Gets or sets the display mode for this model view. |
| Property | [DisplayZebraStripes](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~DisplayZebraStripes.md) | Gets or sets the zebra-line display state. |
| Property | [DynamicMode](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~DynamicMode.md) | Gets the dynamic mode. |
| Property | [EnableGraphicsUpdate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~EnableGraphicsUpdate.md) | Gets or sets whether or not to refresh the model view. |
| Property | [FrameHeight](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~FrameHeight.md) | Get or sets the height of the frame of the document window that contains the model view in the SOLIDWORKS client area. |
| Property | [FrameLeft](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~FrameLeft.md) | Gets or sets the left position of the frame of the document window that contains the model view in the SOLIDWORKS client area. |
| Property | [FrameState](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~FrameState.md) | Gets or sets the window state (minimum, maximum, or normal) for the frame of the document window that contains the model view in the SOLIDWORKS client area. |
| Property | [FrameTop](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~FrameTop.md) | Gets or sets the top position of the frame of the document window that contains the model view in the SOLIDWORKS client area. |
| Property | [FrameWidth](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~FrameWidth.md) | Gets or sets the width of the frame of the document window that contains the model view in the SOLIDWORKS client area. |
| Property | [HlrQuality](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~HlrQuality.md) | Gets or sets the hidden-line removal quality property of this model view. |
| Property | [IOrientation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~IOrientation.md) | Obsolete. Superseded by [IModelView::Orientation3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~Orientation3.md). |
| Property | [IOrientation2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~IOrientation2.md) | Obsolete. Superseded by [IModelView::Orientation3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~Orientation3.md). |
| Property | [ITranslation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~ITranslation.md) | Obsolete. Superseded by [IModelView::Translation3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~Translation3.md). |
| Property | [ITranslation2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~ITranslation2.md) | Obsolete. Superseded by [IModelView::Translation3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~Translation3.md). |
| Property | [Linked](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~Linked.md) | Gets whether or not this viewport is linked or not. |
| Property | [ObjectSizesAway](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~ObjectSizesAway.md) | Helps define the perspective of the current model view by relating the size of a displayed object with the distance of the object from the observer. |
| Property | [Orientation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~Orientation.md) | Obsolete. Superseded by [IModelView::Orientation3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~Orientation3.md). |
| Property | [Orientation2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~Orientation2.md) | Obsolete. Superseded by [IModelView::Orientation3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~Orientation3.md). |
| Property | [Orientation3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~Orientation3.md) | Gets or sets the model view orientation matrix. |
| Property | [Scale](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~Scale.md) | Obsolete. Superseded by [IModelView::Scale2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~Scale2.md). |
| Property | [Scale2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~Scale2.md) | Gets and sets the model view scale factor. |
| Property | [SuppressWaitCursorDuringRedraw](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~SuppressWaitCursorDuringRedraw.md) | Gets or sets the state of the wait cursor (also called the hourglass) while this model view is being redrawn. |
| Property | [Transform](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~Transform.md) | Gets the model space to the model view plane transform.  **NOTE:** **This property is a get-only property.** **Set is not implemented**. |
| Property | [Translation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~Translation.md) | Obsolete. Superseded by [IModelView::Translation3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~Translation3.md). |
| Property | [Translation2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~Translation2.md) | Obsolete. Superseded by [IModelView::Translation3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~Translation3.md). |
| Property | [Translation3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~Translation3.md) | Gets or sets the model view translation vector. |
| Property | [UpdateAllGraphicsLayers](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~UpdateAllGraphicsLayers.md) | Gets or sets whether to update all graphic layers in any mode. |
| Property | [VisibilityViewTools](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~VisibilityViewTools.md) | Gets or sets the visibility of the Heads-up View Toolbar for this model view. |
| Property | [XorHighlight](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~XorHighlight.md) | Gets or sets the Xor highlight state. |

[Top](#top)

Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | [Activate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~Activate.md) | Activates the model view. |
| Method | [AddPerspective](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~AddPerspective.md) | Adds perspective to the model view. |
| Method | [CreateCallout](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~CreateCallout.md) | Creates a callout on this model view. |
| Method | [DrawHighlightedItems](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~DrawHighlightedItems.md) | Draws or redraws the highlighted items. |
| Method | [DrawTransparentFeatureTree](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~DrawTransparentFeatureTree.md) | Draws a transparent FeatureManager design tree. |
| Method | [GetBkgdImageDisplayAreaAspectRatio](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~GetBkgdImageDisplayAreaAspectRatio.md) | Gets the aspect ratio (width/height) of the area of the window where the background image is displayed. |
| Method | [GetDisplayState](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~GetDisplayState.md) | Gets the display state of this model view. |
| Method | [GetEyePoint](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~GetEyePoint.md) | Gets the eye position for perspective viewing. |
| Method | [GetIsoPlaneDistance](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~GetIsoPlaneDistance.md) | Gets the distance, in terms of screen space, from the eye position to the plane at which there is no scaling due to perspective. |
| Method | [GetMouse](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~GetMouse.md) | Gets the mouse for this model view. |
| Method | [GetNext](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~GetNext.md) | Gets the next model view after this model view. |
| Method | [GetStereoSeparation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~GetStereoSeparation.md) | Obsolete and not superseded. Functionality no longer implemented. |
| Method | [GetViewDIB](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~GetViewDIB.md) | Gets an image of the document as it looks in Normal view or in the print preview. |
| Method | [GetViewDIBx64](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~GetViewDIBx64.md) | Gets an image of the document as it looks in Normal view or in the print preview in 64-bit applications. |
| Method | [GetViewHWnd](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~GetViewHWnd.md) | Gets the Microsoft window handle for this model view. |
| Method | [GetViewHWndx64](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~GetViewHWndx64.md) | Gets the Microsoft window handle for this model view in 64-bit applications. |
| Method | [GetViewPlaneDistance](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~GetViewPlaneDistance.md) | Gets the model view plane distance for perspective viewing. |
| Method | [GetVisibleBox](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~GetVisibleBox.md) | Gets the boundaries of the visible model view window. |
| Method | [GraphicsRedraw](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~GraphicsRedraw.md) | Redraws the specified region of or the entire SOLIDWORKS graphics window. |
| Method | [HasPerspective](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~HasPerspective.md) | Determines if the model view currently has perspective. |
| Method | [HideMagnifyingGlass](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~HideMagnifyingGlass.md) | Hides the Magnifying Glass tool. |
| Method | [IGetEyePoint](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~IGetEyePoint.md) | Gets the eye position for perspective viewing. |
| Method | [IGetNext](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~IGetNext.md) | Gets the next model view after this model view. |
| Method | [IGetStereoSeparation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~IGetStereoSeparation.md) | Obsolete and not superseded. Functionality no longer implemented. |
| Method | [IGetVisibleBox](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~IGetVisibleBox.md) | Gets the boundaries of the visible model view window. |
| Method | [IGraphicsRedraw](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~IGraphicsRedraw.md) | Redraws the specified region of or the entire SOLIDWORKS graphics window. |
| Method | [InitializeShading](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~InitializeShading.md) | Sets up the model view for OpenGL shading. |
| Method | [ISetEyePoint](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~ISetEyePoint.md) | Sets the eye position for perspective viewing. |
| Method | [ISetStereoSeparation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~ISetStereoSeparation.md) | Obsolete and not superseded. Functionality no longer implemented. |
| Method | [MoveMagnifyingGlass](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~MoveMagnifyingGlass.md) | Moves Magnifying Glass tool to the specified coordinates. |
| Method | [RemovePerspective](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~RemovePerspective.md) | Removes perspective from the model view. |
| Method | [RollBy](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~RollBy.md) | Rolls the model view about the line of sight by the specified angle. |
| Method | [RotateAboutAxis](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~RotateAboutAxis.md) | Rotates the model view about a point, by an angle in the specified direction. |
| Method | [RotateAboutCenter](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~RotateAboutCenter.md) | Rotates the model view about the screen X and Y axes. |
| Method | [RotateAboutPoint](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~RotateAboutPoint.md) | Rotates the model view about the specified point by the specified angles in the directions of the screen X and Y axes. |
| Method | [SetCameraByName](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~SetCameraByName.md) | Sets the model view to that of the specified camera, if in camera view mode. |
| Method | [SetEyePoint](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~SetEyePoint.md) | Sets the eye position for perspective viewing. |
| Method | [SetStereoSeparation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~SetStereoSeparation.md) | Obsolete and not superseded. Functionality no longer implemented. |
| Method | [ShowMagnifyingGlass](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~ShowMagnifyingGlass.md) | Shows the Magnifying Glass tool at the specified coordinates. |
| Method | [StartDynamics](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~StartDynamics.md) | Provides faster rotation of model views. |
| Method | [StopDynamics](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~StopDynamics.md) | Ends dynamic model view motion. |
| Method | [TranslateBy](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~TranslateBy.md) | Translates the model view in the screen. |
| Method | [TurnBy](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~TurnBy.md) | Rotates the camera by the specified angles about the camera's x and y axes. |
| Method | [ZoomByFactor](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~ZoomByFactor.md) | Modifies the zoom factor for the model view. |

[Top](#top)

 

See Also

#### Reference

[IModelView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)  
[IModelViewManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager.md)  
[IModelWindow Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelWindow.md)
