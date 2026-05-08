# IRefPlaneFeatureData Interface Members

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlaneFeatureData_members`

Allows access to reference plane feature data.
The following tables list the members exposed by [IRefPlaneFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlaneFeatureData.md).

Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | [Angle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlaneFeatureData~Angle.md) | Gets or sets the angle of the reference plane feature. |
| Property | [AngleOrDistance](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlaneFeatureData~AngleOrDistance.md) | Gets or sets the angle or distance of the specified [reference](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlaneFeatureData~Reference.md) for this reference plane feature. |
| Property | [AutoSize](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlaneFeatureData~AutoSize.md) | Gets or sets whether to automatically size the reference plane feature to either the geometry on which it is created or to the bounding box of the model geometry. |
| Property | [Constraint](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlaneFeatureData~Constraint.md) | Gets or sets the constraint for the specified [reference](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlaneFeatureData~Reference.md) for this reference plane feature. |
| Property | [Distance](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlaneFeatureData~Distance.md) | Gets or sets the distance, in meters, to offset the reference plane feature. |
| Property | [OriginOnCurve](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlaneFeatureData~OriginOnCurve.md) | Gets or sets whether to place the origin on the curve for this reference plane feature. |
| Property | [ProjectionType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlaneFeatureData~ProjectionType.md) | Gets or sets the projection type for this on-surface reference plane feature. |
| Property | [Reference](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlaneFeatureData~Reference.md) | Gets or sets the reference entity for the specified reference for this reference plane feature. |
| Property | [ReverseDirection](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlaneFeatureData~ReverseDirection.md) | Obsolete. Superseded by [IRefPlaneFeatureData::ReversedReferenceDirection](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlaneFeatureData~ReversedReferenceDirection.md). |
| Property | [ReversedReferenceDirection](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlaneFeatureData~ReversedReferenceDirection.md) | Gets or sets whether to reverse the direction of the specified reference for this reference plane feature. |
| Property | [Selections](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlaneFeatureData~Selections.md) | Gets or sets the selected entities used to create the reference plane feature or sets the entities to use to create the reference plane feature. |
| Property | [SolutionIndex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlaneFeatureData~SolutionIndex.md) | Gets or sets the intended plane when there are multiple planes from which to select for an on-surface reference plane feature. |
| Property | [Type](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlaneFeatureData~Type.md) | Gets the type of reference plane created in SOLIDWORKS 2009 or earlier. Can also get whether a constraint-based reference plane created in SOLIDWORKS 2010 or has angle or offset distance references.    **NOTE:** **This property is a get-only property.** **Set is not implemented**. |
| Property | [Type2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlaneFeatureData~Type2.md) | Gets whether the reference plane is constraint based; thus, created in SOLIDWORKS 2010 and later.  **NOTE:** **This property is a get-only property.** **Set is not implemented**. |
| Property | [UpdatePlane](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlaneFeatureData~UpdatePlane.md) | Gets or sets whether to update this reference plane so that it is parallel to the screen. |
| Property | [UseNormalPlane](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlaneFeatureData~UseNormalPlane.md) | Gets or sets whether to:   - Use the plane normal to the selected plane - Automatically size the plane to either the geometry on which it is created or to the bounding box of the model geometry |

[Top](#top)

Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | [AccessSelections](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlaneFeatureData~AccessSelections.md) | Gains access to the selections that define a reference plane feature. |
| Method | [GetSelectionsCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlaneFeatureData~GetSelectionsCount.md) | Gets the number of entities selected to create this reference plane feature. |
| Method | [IAccessSelections](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlaneFeatureData~IAccessSelections.md) | Gains access to the selections that define a reference plane feature. |
| Method | [IGetSelections](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlaneFeatureData~IGetSelections.md) | Gets the selected entities used to create this reference plane feature. |
| Method | [ISetSelections](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlaneFeatureData~ISetSelections.md) | Sets the entities to use to create the reference plane feature. |
| Method | [ReleaseSelectionAccess](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlaneFeatureData~ReleaseSelectionAccess.md) | Releases access to the selections that created the reference plane feature. |

[Top](#top)

 

See Also

#### Reference

[IRefPlaneFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlaneFeatureData.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)  
[IRefPlane Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlane.md)
