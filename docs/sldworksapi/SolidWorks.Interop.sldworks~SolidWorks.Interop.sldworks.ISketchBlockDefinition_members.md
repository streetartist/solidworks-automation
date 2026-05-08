# ISketchBlockDefinition Interface Members

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition_members`

Allows access to information about a block definition.
The following tables list the members exposed by [ISketchBlockDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition.md).

Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | [FileName](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~FileName.md) | Gets or sets the name of the file to which the block definition is linked. |
| Property | [InsertionPoint](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~InsertionPoint.md) | Gets or sets the insertion point for the block definition. |
| Property | [LinkToFile](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~LinkToFile.md) | Gets or sets whether the block definition file is linked to a file. |

[Top](#top)

Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | [GetArcCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~GetArcCount.md) | Gets the number of arcs in this block definition. |
| Method | [GetArcs](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~GetArcs.md) | Gets information about all of the arcs in the block definition. |
| Method | [GetDisplayDimensionCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~GetDisplayDimensionCount.md) | Gets the number of display dimensions in this block definition. |
| Method | [GetDisplayDimensions](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~GetDisplayDimensions.md) | Gets the display dimensions in this block definition. |
| Method | [GetEllipseCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~GetEllipseCount.md) | Gets the number of ellipses in this block definition. |
| Method | [GetEllipses](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~GetEllipses.md) | Gets the information about all of the ellipses in this block definition. |
| Method | [GetFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~GetFeature.md) | Gets the feature for this block definition. |
| Method | [GetInstanceCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~GetInstanceCount.md) | Gets the number of block instances of this block definition. |
| Method | [GetInstances](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~GetInstances.md) | Gets all of the block instances of this block definition. |
| Method | [GetLineCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~GetLineCount.md) | Gets the number of lines in this block definition. |
| Method | [GetLines](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~GetLines.md) | Gets information about all of the lines in this block definition. |
| Method | [GetNoteCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~GetNoteCount.md) | Gets the number of notes in this block definition. |
| Method | [GetNotes](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~GetNotes.md) | Gets the notes in this block definition. |
| Method | [GetParabolaCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~GetParabolaCount.md) | Gets the number of parabolas in this block definition. |
| Method | [GetParabolas](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~GetParabolas.md) | Gets information about all of the parabolas in this block definition. |
| Method | [GetSketch](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~GetSketch.md) | Gets the underlying sketch of this block definition. |
| Method | [GetSplineCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~GetSplineCount.md) | Gets the number of splines in this block definition. |
| Method | [GetSplineInterpolateCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~GetSplineInterpolateCount.md) | Gets the number of splines in the sketch block definition and the size of array required to hold the data for the interpolation of these splines. |
| Method | [GetSplineParams](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~GetSplineParams.md) | Gets all the parameters of the splines in the sketch block definition. |
| Method | [GetSplineParamsCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~GetSplineParamsCount.md) | Gets the number of splines in the sketch block definition and the size of array required to hold the data for the parameters of these splines. |
| Method | [GetSplines](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~GetSplines.md) | Obsolete. Superseded by [ISketchBlockDefinition::GetSplines2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~GetSplines2.md) and [ISketchBlockDefinition::IGetSplines2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~IGetSplines2.md). |
| Method | [GetSplines2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~GetSplines2.md) | Gets the spline points by tessellation instead of by interpolation as is done by [ISketchBlockDefinition::GetSplinesInterpolate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~GetSplinesInterpolate.md) and [ISketchBlockDefinition::IGetSplinesInterpolate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~IGetSplinesInterpolate.md). |
| Method | [GetSplinesInterpolate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~GetSplinesInterpolate.md) | Gets all of the parameers of the splines by interpolation instead of by tessellation as is done by [ISketch::GetSplines2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~GetSplines2.md) and [ISketch::IGetSplines2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~IGetSplines2.md). |
| Method | [GetUserPoints](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~GetUserPoints.md) | Gets information about all of the user points in this block definition. |
| Method | [GetUserPointsCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~GetUserPointsCount.md) | Gets the number of user points in this block definition. |
| Method | [IGetArcs](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~IGetArcs.md) | Gets information about all of the arcs in the block definition. |
| Method | [IGetDisplayDimensions](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~IGetDisplayDimensions.md) | Gets the display dimensions in this block definition. |
| Method | [IGetEllipses](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~IGetEllipses.md) | Gets the information about all of the ellipses in this block definition. |
| Method | [IGetInstances](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~IGetInstances.md) | Gets all of the block instances of this block definition. |
| Method | [IGetLines](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~IGetLines.md) | Gets information about all of the lines in this block definition. |
| Method | [IGetNotes](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~IGetNotes.md) | Gets the notes in this block definition. |
| Method | [IGetParabolas](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~IGetParabolas.md) | Gets information about all of the parabolas in this block definition. |
| Method | [IGetSplineParams](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~IGetSplineParams.md) | Gets all the parameters of the splines in the sketch block definition. |
| Method | [IGetSplines](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~IGetSplines.md) | Obsolete. Superseded by [ISketchBlockDefinition::GetSplines2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~GetSplines2.md) and [ISketchBlockDefinition::IGetSplines2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~IGetSplines2.md). |
| Method | [IGetSplines2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~IGetSplines2.md) | Gets the spline points by tessellation instead of by interpolation as is done by [ISketchBlockDefinition::GetSplinesInterpolate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~GetSplinesInterpolate.md) and [ISketchBlockDefinition::IGetSplinesInterpolate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~IGetSplinesInterpolate.md). |
| Method | [IGetSplinesInterpolate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~IGetSplinesInterpolate.md) | Gets all of the parameers of the splines by interpolation instead of by tessellation as is done by [ISketch::GetSplines2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~GetSplines2.md) and [ISketch::IGetSplines2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~IGetSplines2.md). |
| Method | [IGetUserPoints](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~IGetUserPoints.md) | Gets information about all of the user points in this block definition. |
| Method | [Save](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~Save.md) | Saves the block definition. |

[Top](#top)

 

See Also

#### Reference

[ISketchBlockDefinition Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)  
[ISketchManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager.md)  
[ISketchBlockInstance Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance.md)
