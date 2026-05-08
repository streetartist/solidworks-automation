# ISketchSegment Interface Members

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment_members`

Provides access to functions that are common among sketch entities.
The following tables list the members exposed by [ISketchSegment](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment.md).

Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | [Color](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment~Color.md) | Gets or sets the color of this sketch segment. Sketch segment color is only supported in drawing documents. |
| Property | [ConstructionGeometry](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment~ConstructionGeometry.md) | Gets or sets whether this sketch segment is construction geometry, for example, a centerline for a feature revolve operation. |
| Property | [Layer](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment~Layer.md) | gets or sets the layer used by this sketch segment. |
| Property | [LayerOverride](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment~LayerOverride.md) | Gets or sets whether the sketch segment has properties that override the default properties of the layer. |
| Property | [Status](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment~Status.md) | Gets the constraint status for this sketch segment.  **NOTE: This property is a get-only property. Set is not implemented.** |
| Property | [Style](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment~Style.md) | Gets or sets the line style for this sketch segment. |
| Property | [Width](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment~Width.md) | Gets or sets the line width for this sketch segment. |

[Top](#top)

Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | [CreateWireBody](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment~CreateWireBody.md) | Creates a wire body using the selected sketch segment. |
| Method | [DeSelect](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment~DeSelect.md) | Deselects the sketch segment. |
| Method | [EqualSegment](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment~EqualSegment.md) | Divides this sketch segment into equally spaced sketch segments or points. |
| Method | [GetConstraints](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment~GetConstraints.md) | Gets the constraints for this sketch segment. |
| Method | [GetCurve](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment~GetCurve.md) | Gets the underlying curve for this sketch segment. |
| Method | [GetID](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment~GetID.md) | Gets the for this sketch segment. |
| Method | [GetLength](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment~GetLength.md) | Gets the length of this sketch segment. |
| Method | [GetName](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment~GetName.md) | Gets the name of this sketch segment. |
| Method | [GetRelations](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment~GetRelations.md) | Gets the sketch relations for this sketch segment. |
| Method | [GetRelationsCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment~GetRelationsCount.md) | Gets the number of sketch relations for this sketch segment. |
| Method | [GetSketch](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment~GetSketch.md) | Gets the sketch for the current sketch segment. |
| Method | [GetSketchPathCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment~GetSketchPathCount.md) | Gets the number of sketch paths for this sketch segment |
| Method | [GetSketchPaths](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment~GetSketchPaths.md) | Gets the sketch paths for this sketch segment. |
| Method | [GetSketchSlot](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment~GetSketchSlot.md) | Gets sketch slot with which this sketch segment is associated. |
| Method | [GetType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment~GetType.md) | Gets the type of sketch segment. |
| Method | [IGetConstraints](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment~IGetConstraints.md) | Gets the constraints for this sketch segment. |
| Method | [IGetConstraintsCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment~IGetConstraintsCount.md) | Gets the number of constraints on the sketch segment. |
| Method | [IGetCurve](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment~IGetCurve.md) | Gets the underlying curve for this sketch segment. |
| Method | [IGetID](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment~IGetID.md) | Gets the ID for this sketch segment. |
| Method | [IGetRelations](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment~IGetRelations.md) | Gets the sketch relations for this sketch segment. |
| Method | [IGetSketchPaths](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment~IGetSketchPaths.md) | Gets the sketch paths in this sketch segment. |
| Method | [IsBendLine](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment~IsBendLine.md) | Gets whether the sketch segment is a bendline. |
| Method | [JogLine](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment~JogLine.md) | Creates rectangular jog on the specified line. |
| Method | [Select](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment~Select.md) | Obsolete. Superseded by [ISketchSegment::Select4](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment~Select4.md). |
| Method | [Select2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment~Select2.md) | Obsolete. Superseded by [ISketchSegment::Select4](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment~Select4.md). |
| Method | [Select3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment~Select3.md) | Obsolete. Superseded by [ISketchSegment::Select4](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment~Select4.md). |
| Method | [Select4](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment~Select4.md) | Selects this sketch segment and marks it. |
| Method | [SelectByMark](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment~SelectByMark.md) | Obsolete. Superseded by [ISketchSegment::Select4](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment~Select4.md). |
| Method | [SelectChain](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment~SelectChain.md) | Selects chains of entities attached to this sketch segment. |
| Method | [SplitEntity](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment~SplitEntity.md) | Splits the selected sketch entity at the specified point. |

[Top](#top)

 

See Also

#### Reference

[ISketchSegment Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
