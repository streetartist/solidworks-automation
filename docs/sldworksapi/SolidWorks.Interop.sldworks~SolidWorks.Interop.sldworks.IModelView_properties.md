# IModelView Interface Properties

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView_properties`

Allows you access to the model view's orientation, translation, and the Microsoft handle to the window.
For a list of all members of this type, see [IModelView members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView_members.md).

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

See Also

#### Reference

[IModelView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)  
[IModelViewManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager.md)  
[IModelWindow Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelWindow.md)
