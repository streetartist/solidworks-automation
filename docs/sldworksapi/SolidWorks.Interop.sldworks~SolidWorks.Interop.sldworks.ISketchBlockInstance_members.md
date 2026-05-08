# ISketchBlockInstance Interface Members

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance_members`

Allows access to block instances.
The following tables list the members exposed by [ISketchBlockInstance](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance.md).

Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | [Angle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance~Angle.md) | Gets or sets the angle around the insertion point which to rotate this block instance. |
| Property | [BlockToSketchTransform](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance~BlockToSketchTransform.md) | Gets the MathTransform required to transform coordinates from the sketch block space to the host sketch space. |
| Property | [Definition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance~Definition.md) | Gets or sets the block definition for this block instance. |
| Property | [DimensionDisplay](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance~DimensionDisplay.md) | Gets whether dimensions are displayed. |
| Property | [InstancePosition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance~InstancePosition.md) | Gets or sets the position for this block instance. |
| Property | [Layer](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance~Layer.md) | Gets or sets the name of the layer where this block is located. |
| Property | [LockAngle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance~LockAngle.md) | Gets or sets whether the angle around the insertion point which to rotate this block instance is locked. |
| Property | [Name](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance~Name.md) | Gets or sets the name of this block instance. |
| Property | [Scale](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance~Scale.md) | Obsolete. Superseded by [ISketchBlockInstance::Scale2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance~Scale2.md). |
| Property | [Scale2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance~Scale2.md) | Sets the scale for this block instance. |
| Property | [TextDisplay](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance~TextDisplay.md) | Gets or sets whether to display text for this block instance. |
| Property | [Visible](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance~Visible.md) | Gets or sets the visibility of this block instance. |

[Top](#top)

Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | [GetArrowHeadStyle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance~GetArrowHeadStyle.md) | Gets the arrowhead style of the leader on this block instance. |
| Method | [GetAttachedEntities](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance~GetAttachedEntities.md) | Gets the entities to which this block instance is attached. |
| Method | [GetAttributeCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance~GetAttributeCount.md) | Gets the number of attributes for this block instance. |
| Method | [GetAttributes](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance~GetAttributes.md) | Gets the attributes for this block instance. |
| Method | [GetAttributeValue](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance~GetAttributeValue.md) | Gets the value of the specified attribute for this block instance. |
| Method | [GetLeaderPoints](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance~GetLeaderPoints.md) | Gets the coordinate information for the leader on this block instance. |
| Method | [GetLeaderStyle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance~GetLeaderStyle.md) | Gets the leader style of this block instance. |
| Method | [GetScale3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance~GetScale3.md) | Gets the scale for this block instance. |
| Method | [GetSketch](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance~GetSketch.md) | Gets the sketch in which this block instance is present. |
| Method | [IGetAttributes](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance~IGetAttributes.md) | Gets the attributes for this block instance. |
| Method | [IGetLeaderPoints](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance~IGetLeaderPoints.md) | Gets the coordinate information for the leader on this block instance. |
| Method | [IsNested](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance~IsNested.md) | Gets whether this sketch block instance is nested within another block definition. |
| Method | [Select](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance~Select.md) | Selects and marks the block instance. |
| Method | [SetAttributeValue](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance~SetAttributeValue.md) | Sets the value of the specified attribute for this block instance. |
| Method | [SetLeader](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance~SetLeader.md) | Sets the leader style for this block instance. |

[Top](#top)

 

See Also

#### Reference

[ISketchBlockInstance Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)  
[ISketchBlockDefinition Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition.md)  
[ISketchManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager.md)
