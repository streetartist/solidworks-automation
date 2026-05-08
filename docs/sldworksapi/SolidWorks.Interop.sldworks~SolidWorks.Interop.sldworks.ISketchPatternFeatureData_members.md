# ISketchPatternFeatureData Interface Members

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPatternFeatureData_members`

Allows access to a sketch-driven pattern feature in a part.
The following tables list the members exposed by [ISketchPatternFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPatternFeatureData.md).

Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | [AutoSelect](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPatternFeatureData~AutoSelect.md) | Gets whether to automatically select all bodies in a multibody part intersected by this sketch-driven pattern feature. |
| Property | [BodyPattern](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPatternFeatureData~BodyPattern.md) | Gets or sets whether to base this sketch pattern feature on bodies or features and faces. |
| Property | [FeatureScope](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPatternFeatureData~FeatureScope.md) | Gets which bodies in this multibody part are affected by this sketch-driven pattern feature. |
| Property | [FeatureScopeBodies](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPatternFeatureData~FeatureScopeBodies.md) | Gets the bodies in this multibody part to be affected by this sketch-driven pattern feature. |
| Property | [GeometryPattern](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPatternFeatureData~GeometryPattern.md) | Gets or sets whether to create the pattern using only the geometry (faces and edges) of the feature. |
| Property | [PatternBodyArray](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPatternFeatureData~PatternBodyArray.md) | Gets and sets the bodies to pattern for this sketch pattern feature. |
| Property | [PatternElement](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPatternFeatureData~PatternElement.md) | Gets or sets the type of entities to base this sketch pattern feature. |
| Property | [PatternFaceArray](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPatternFeatureData~PatternFaceArray.md) | Gets or sets the patterned faces for the sketch pattern feature. |
| Property | [PatternFeatureArray](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPatternFeatureData~PatternFeatureArray.md) | Gets or sets the seed features for the sketch pattern feature. |
| Property | [PropagateVisualProperty](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPatternFeatureData~PropagateVisualProperty.md) | Gets or sets whether to propagate visual properties (i.e., colors to all pattern instances). |
| Property | [ReferencePoint](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPatternFeatureData~ReferencePoint.md) | Gets or sets the reference point for this sketch pattern feature. |
| Property | [Sketch](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPatternFeatureData~Sketch.md) | Gets or sets the sketch from which that this sketch pattern feature is created. |
| Property | [UseCentroid](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPatternFeatureData~UseCentroid.md) | Gets or sets whether to use a centroid for this sketch pattern feature. |

[Top](#top)

Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | [AccessSelections](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPatternFeatureData~AccessSelections.md) | Gains access to selections used to define the sketch pattern feature. |
| Method | [GetBasePoint](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPatternFeatureData~GetBasePoint.md) | Gets the base point data from which this sketch pattern is created. |
| Method | [GetPatternBodyCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPatternFeatureData~GetPatternBodyCount.md) | Gets the number of seed bodies in the sketch pattern feature. |
| Method | [GetPatternFaceCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPatternFeatureData~GetPatternFaceCount.md) | Gets the number of patterned faces. |
| Method | [GetPatternFeatureCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPatternFeatureData~GetPatternFeatureCount.md) | Gets the number of seed features for this sketch pattern feature. |
| Method | [GetReferencePointType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPatternFeatureData~GetReferencePointType.md) | Gets the type of reference point for this sketch pattern feature. |
| Method | [GetTransform](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPatternFeatureData~GetTransform.md) | Gets the transform for the specified instance of this sketch pattern feature. |
| Method | [IAccessSelections](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPatternFeatureData~IAccessSelections.md) | Obsolete. Superseded by [ISketchPatternFeatureData::IAccessSelections2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPatternFeatureData~IAccessSelections2.md). |
| Method | [IAccessSelections2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPatternFeatureData~IAccessSelections2.md) | Gains access to selections used to define the sketch pattern feature. |
| Method | [IGetBasePoint](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPatternFeatureData~IGetBasePoint.md) | Gets the base point data from which this sketch pattern is created. |
| Method | [IGetPatternBodyArray](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPatternFeatureData~IGetPatternBodyArray.md) | Gets the seed bodies for the sketch pattern feature. |
| Method | [IGetPatternFaceArray](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPatternFeatureData~IGetPatternFaceArray.md) | Gets the patterned faces for the sketch pattern feature. |
| Method | [IGetPatternFeatureArray](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPatternFeatureData~IGetPatternFeatureArray.md) | Gets the seed features for the sketch pattern. |
| Method | [ISetPatternBodyArray](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPatternFeatureData~ISetPatternBodyArray.md) | Sets the seed bodies for the sketch pattern feature. |
| Method | [ISetPatternFaceArray](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPatternFeatureData~ISetPatternFaceArray.md) | Sets the patterned faces for the sketch pattern feature. |
| Method | [ISetPatternFeatureArray](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPatternFeatureData~ISetPatternFeatureArray.md) | Sets the seed features for the sketch pattern feature. |
| Method | [ReleaseSelectionAccess](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPatternFeatureData~ReleaseSelectionAccess.md) | Releases access to the selections that created this sketch pattern feature. |
| Method | [SetFeatureScope](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPatternFeatureData~SetFeatureScope.md) | Sets the feature scope, whether to autoselect the affected bodies, and the affected bodies in this sketch pattern feature. |

[Top](#top)

 

See Also

#### Reference

[ISketchPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPatternFeatureData.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
