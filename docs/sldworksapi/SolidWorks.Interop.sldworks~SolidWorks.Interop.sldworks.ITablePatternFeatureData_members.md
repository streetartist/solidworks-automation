# ITablePatternFeatureData Interface Members

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData_members`

Allows access to a table-driven pattern feature.
The following tables list the members exposed by [ITablePatternFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData.md).

Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | [CoordinateSystem](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData~CoordinateSystem.md) | Gets or sets the coordinate system of the table-driven pattern feature. |
| Property | [GeometryPattern](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData~GeometryPattern.md) | Gets or sets whether to create the pattern using only the geometry (faces and edges) of the features for the table-driven pattern feature. |
| Property | [PatternBodyArray](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData~PatternBodyArray.md) | Gets or sets the seed bodies to pattern for this table-driven pattern feature. |
| Property | [PatternFaceArray](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData~PatternFaceArray.md) | Gets or sets the patterned faces for this table-driven pattern feature. |
| Property | [PatternFeatureArray](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData~PatternFeatureArray.md) | Gets or sets the seed features used to create the table-driven pattern feature. |
| Property | [PointArray](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData~PointArray.md) | Gets or sets the array of points that describe the x,y, and z locations of the repeating elements in the table-driven pattern feature. |
| Property | [PropagateVisualProperty](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData~PropagateVisualProperty.md) | Gets or sets whether to propagate visual properties (e.g., colors, textures, etc.) in the table-driven pattern feature. |
| Property | [ReferencePoint](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData~ReferencePoint.md) | Gets or sets the reference point for pattern instances of this table-driven pattern feature. |
| Property | [SkippedItemArray](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData~SkippedItemArray.md) | Gets or sets the skipped items for this table-driven pattern feature. |
| Property | [UseCentroid](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData~UseCentroid.md) | Gets or sets whether to set the reference point to the centroid of the seed feature for this table-driven pattern feature. |

[Top](#top)

Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | [AccessSelections](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData~AccessSelections.md) | Gains access to selections used to define the table-driven pattern feature. |
| Method | [GetBasePoint](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData~GetBasePoint.md) | Gets the base point for this table-driven pattern feature. |
| Method | [GetPatternBodyCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData~GetPatternBodyCount.md) | Gets the number of seed bodies for this table-driven pattern feature. |
| Method | [GetPatternFaceCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData~GetPatternFaceCount.md) | Gets the number of patterned faces in this table-driven feature. |
| Method | [GetPatternFeatureCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData~GetPatternFeatureCount.md) | Gets the number of distinct seed features used to create this table-driven pattern feature. |
| Method | [GetPointCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData~GetPointCount.md) | Gets the number of x, y, and z locations of the repeating elements in this table-driven pattern. |
| Method | [GetReferencePointType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData~GetReferencePointType.md) | Gets whether the table-driven pattern's reference point is a closed curve, a sketch point, or a vertex. |
| Method | [GetSkippedItemCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData~GetSkippedItemCount.md) | Gets the number of skipped items in this table-driven pattern feature. |
| Method | [GetTransform](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData~GetTransform.md) | Gets the transform for the specified repeating element in this table-driven pattern feature. |
| Method | [IAccessSelections](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData~IAccessSelections.md) | Obsolete. Superseded by [ITablePatternFeatureData::IAccessSelections2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData~IAccessSelections2.md). |
| Method | [IAccessSelections2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData~IAccessSelections2.md) | Gains access to selections used to define the table-driven pattern feature. |
| Method | [IGetBasePoint](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData~IGetBasePoint.md) | Gets the base point for this table-driven pattern feature. |
| Method | [IGetPatternBodyArray](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData~IGetPatternBodyArray.md) | Gets the seed bodies for this table-driven pattern feature. |
| Method | [IGetPatternFaceArray](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData~IGetPatternFaceArray.md) | Gets the patterned faces in this table-driven pattern feature. |
| Method | [IGetPatternFeatureArray](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData~IGetPatternFeatureArray.md) | Gets the seed features used to create the table-driven pattern. |
| Method | [IGetPointArray](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData~IGetPointArray.md) | Gets an array of doubles that describe the x, y, and z locations of the repeating elements in this table-driven pattern feature. |
| Method | [IGetSkippedItemArray](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData~IGetSkippedItemArray.md) | Gets the skipped items in this table-driven pattern feature. |
| Method | [ISetPatternBodyArray](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData~ISetPatternBodyArray.md) | Sets the seed bodies for this table-driven pattern feature. |
| Method | [ISetPatternFaceArray](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData~ISetPatternFaceArray.md) | Sets the patterned faces for this table-driven pattern feature. |
| Method | [ISetPatternFeatureArray](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData~ISetPatternFeatureArray.md) | Sets the seed features used to create the table-driven pattern feature. |
| Method | [ISetPointArray](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData~ISetPointArray.md) | Sets the points that describe the x, y, and z locations of the repeating elements in the table-driven pattern feature. |
| Method | [ISetSkippedItemArray](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData~ISetSkippedItemArray.md) | Sets the skipped items in this table-driven pattern feature. |
| Method | [LoadPointsFromFile](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData~LoadPointsFromFile.md) | Loads the location points of the table-driven pattern from a \*.sldptab file. |
| Method | [ReleaseSelectionAccess](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData~ReleaseSelectionAccess.md) | Releases access to the selections that created this table-driven pattern feature. |
| Method | [SavePointsToFile](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData~SavePointsToFile.md) | Saves the location of the table-driven pattern feature's points to a \*.sldptab file. |

[Top](#top)

 

See Also

#### Reference

[ITablePatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
