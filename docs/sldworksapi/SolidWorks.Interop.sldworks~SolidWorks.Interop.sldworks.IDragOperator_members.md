# IDragOperator Interface Members

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator_members`

Allows access to settings for the Move Components command in the SOLIDWORKS user-interface.
The following tables list the members exposed by [IDragOperator](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator.md).

Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | [ApplyToThisConfiguration](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator~ApplyToThisConfiguration.md) | Gets or sets the configurations to which to apply the movement of the components. |
| Property | [Clearance](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator~Clearance.md) | Gets the clearance distance between the components. |
| Property | [CollisionDetectionEnabled](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator~CollisionDetectionEnabled.md) | Gets or sets the collision detection setting. |
| Property | [DragCorrected](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator~DragCorrected.md) | Gets whether or not the drag operation was corrected. |
| Property | [DragMode](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator~DragMode.md) | Gets or sets the drag mode for this drag operation. |
| Property | [DynamicClearanceEnabled](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator~DynamicClearanceEnabled.md) | Gets or sets the dynamic clearance setting. |
| Property | [GraphicsRedrawEnabled](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator~GraphicsRedrawEnabled.md) | Gets or sets whether or not to update the graphics display after moving components. |
| Property | [HearClashes](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator~HearClashes.md) | Gets or sets whether sound is associated with entity clashes. |
| Property | [HighlightClashes](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator~HighlightClashes.md) | Gets or sets whether to highlight clashes. |
| Property | [IgnoreComplexSurfaces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator~IgnoreComplexSurfaces.md) | Gets or sets whether complex surfaces are ignored. |
| Property | [IsDragByRay](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator~IsDragByRay.md) | Gets or sets the drag-by-ray setting. |
| Property | [IsDragSpecific](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator~IsDragSpecific.md) | Gets or sets the drag-specific setting. |
| Property | [IsRelaxationEval](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator~IsRelaxationEval.md) | Gets or sets the relaxation evaluation. |
| Property | [SmartMating](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator~SmartMating.md) | Gets or sets SmartMates. |
| Property | [TransformType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator~TransformType.md) | Gets or sets the type of transformation. |
| Property | [UseAbsoluteTransform](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator~UseAbsoluteTransform.md) | Gets or sets whether the transforms to use with [IDragOperator::Drag](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator~Drag.md) or [IDragOperator::IDrag](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator~IDrag.md) are absolute or relative. |

[Top](#top)

Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | [AddComponent](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator~AddComponent.md) | Adds a component to the list of components to drag. |
| Method | [AddDynamicClearance](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator~AddDynamicClearance.md) | Adds a dynamic clearance detector. |
| Method | [BeginDrag](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator~BeginDrag.md) | Initiates the drag operation. |
| Method | [CollisionDetection](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator~CollisionDetection.md) | Sets the collision detection parameters. |
| Method | [Drag](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator~Drag.md) | Sets the transform matrix for this drag operation. |
| Method | [DragAsUI](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator~DragAsUI.md) | Sets the transform matrix for this drag operation. |
| Method | [EndDrag](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator~EndDrag.md) | Terminates the drag operation. |
| Method | [GetDragPoint](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator~GetDragPoint.md) | Gets the drag point. |
| Method | [IAddComponent](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator~IAddComponent.md) | Adds a component to the list of components to drag. Overload List  " -->Syntax " --> |
| Method | [IAddDynamicClearance](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator~IAddDynamicClearance.md) | Adds a dynamic clearance detector. |
| Method | [ICollisionDetection](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator~ICollisionDetection.md) | Sets the collision detection parameters. |
| Method | [IDrag](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator~IDrag.md) | Sets the transform matrix for this drag operation. |
| Method | [IGetDragPoint](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator~IGetDragPoint.md) | Gets the drag point. |
| Method | [ISetDragPoint](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator~ISetDragPoint.md) | Sets the drag point. |
| Method | [SetDragPoint](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator~SetDragPoint.md) | Sets the drag point. |

[Top](#top)

 

See Also

#### Reference

[IDragOperator Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
