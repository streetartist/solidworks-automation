# ISketchManager Interface Members

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager_members`

Provides access to sketch-creation routines.
The following tables list the members exposed by [ISketchManager](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager.md).

Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | [ActiveSketch](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~ActiveSketch.md) | Gets the active sketch. |
| Property | [AddToDB](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~AddToDB.md) | Gets or sets whether sketch entities are added directly to the SOLIDWORKS database. |
| Property | [AutoInference](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~AutoInference.md) | Obsolete. Superseded by [ISldWorks::GetUserPreferenceToggle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetUserPreferenceToggle.md) or [ISldWorks::SetUserPreferenceToggle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SetUserPreferenceToggle.md) and [swUserPreferenceToggle\_e.swSketchInference.](ms-help://SolidWorks.Interop.swconst/SolidWorks/SO_SketchRelationsSnaps.htm) |
| Property | [AutoSolve](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~AutoSolve.md) | Gets or sets whether SOLIDWORKS automatically solves the sketch geometry of the part while creating it. |
| Property | [CurvatureDensity](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CurvatureDensity.md) | Gets or sets the scaling factor by which to adjust the density of the curvature combs for this spline. |
| Property | [CurvatureScale](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CurvatureScale.md) | Gets or sets the scaling factor by which to adjust the size of the curvature combs for this spline. |
| Property | [DisplayWhenAdded](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~DisplayWhenAdded.md) | Gets or sets whether new sketch entities are immediately displayed when created. |
| Property | [Document](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~Document.md) | Gets the document for this [ISketchManager](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager.md) object. |
| Property | [InferenceMode](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~InferenceMode.md) | Obsolete. Superseded by [ISldWorks::GetUserPreferenceToggle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetUserPreferenceToggle.md) or [ISldWorks::SetUserPreferenceToggle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SetUserPreferenceToggle.md) and [swUserPreferenceToggle\_e.swSketchInference.](ms-help://SolidWorks.Interop.swconst/SolidWorks/SO_SketchRelationsSnaps.htm) |

[Top](#top)

Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | [AddAlongXDimension](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~AddAlongXDimension.md) | Projects and displays along the x axis a dimension between selected points in a 3D sketch. |
| Method | [AddAlongYDimension](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~AddAlongYDimension.md) | Projects and displays along the y axis a dimension between selected points in a 3D sketch. |
| Method | [AddAlongZDimension](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~AddAlongZDimension.md) | Projects and displays along the z axis a dimension between selected points in a 3D sketch. |
| Method | [ConvertEntities](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~ConvertEntities.md) | Not implemented. Use [ISketchManager::SketchUseEdge2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~SketchUseEdge2.md). |
| Method | [Create3PointArc](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~Create3PointArc.md) | Creates a 3-point arc. |
| Method | [Create3PointCenterRectangle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~Create3PointCenterRectangle.md) | Creates a 3-point center rectangle at any angle. |
| Method | [Create3PointCornerRectangle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~Create3PointCornerRectangle.md) | Creates a 3-point corner rectangle at any angle. |
| Method | [CreateArc](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CreateArc.md) | Creates an arc based on a center point, a start point, an end point, and a direction. |
| Method | [CreateBoundaryHatch](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CreateBoundaryHatch.md) | Creates area hatch/fill boundary hatches using closed sketch profiles. |
| Method | [CreateCenterLine](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CreateCenterLine.md) | Creates a center line between the specified points. |
| Method | [CreateCenterRectangle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CreateCenterRectangle.md) | Creates a center rectangle. |
| Method | [CreateChamfer](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CreateChamfer.md) | Creates a chamfer between two selected sketch entities. |
| Method | [CreateCircle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CreateCircle.md) | Creates a circle based on a center point and a point on the circle. |
| Method | [CreateCircleByRadius](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CreateCircleByRadius.md) | Creates a circle based on a center point and a specified radius. |
| Method | [CreateCircularSketchStepAndRepeat](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CreateCircularSketchStepAndRepeat.md) | Creates circular sketch pattern. |
| Method | [CreateConic](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CreateConic.md) | Creates a conic curve in the active sketch. |
| Method | [CreateConstructionGeometry](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CreateConstructionGeometry.md) | Sets selected sketch segments to be construction geometry instead of sketch geometry. |
| Method | [CreateCornerRectangle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CreateCornerRectangle.md) | Creates a corner rectangle. |
| Method | [CreateEllipse](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CreateEllipse.md) | Creates an ellipse using the specified center, major-axis, and minor-axis points. |
| Method | [CreateEllipticalArc](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CreateEllipticalArc.md) | Creates a partial ellipse given a center point, two points that specify the major and minor axis, and two points that define the elliptical start and end points. |
| Method | [CreateEquationSpline](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CreateEquationSpline.md) | Obsolete. Superseded by [ISketchManager::CreateEquationSpline2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CreateEquationSpline2.md). |
| Method | [CreateEquationSpline2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CreateEquationSpline2.md) | Creates an equation-driven 2D explicit or parametric curve or a 3D parametric curve. |
| Method | [CreateFillet](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CreateFillet.md) | Creates a sketch fillet using the selected sketch entities. |
| Method | [CreateLine](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CreateLine.md) | Creates a sketch line in the currently active 2D or 3D sketch. |
| Method | [CreateLinearSketchStepAndRepeat](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CreateLinearSketchStepAndRepeat.md) | Creates a linear sketch pattern. |
| Method | [CreateParabola](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CreateParabola.md) | Creates a parabola in the active sketch. |
| Method | [CreateParallelogram](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CreateParallelogram.md) | Creates a parallelogram. |
| Method | [CreatePoint](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CreatePoint.md) | Creates a sketch point in the active 2D or 3D sketch. |
| Method | [CreatePolygon](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CreatePolygon.md) | Creates a polygon in the active sketch. |
| Method | [CreateRegionHatch](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CreateRegionHatch.md) | Creates an area hatch/fill region hatch using a closed sketch profile. |
| Method | [CreateSketchBelt](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CreateSketchBelt.md) | Creates a sketch belt feature. |
| Method | [CreateSketchPlane](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CreateSketchPlane.md) | Creates a 3D sketch plane. |
| Method | [CreateSketchSlot](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CreateSketchSlot.md) | Creates a sketch slot. |
| Method | [CreateSpline](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CreateSpline.md) | Obsolete. Superseded by [ISketchManager::CreateSpline2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CreateSpline2.md). |
| Method | [CreateSpline2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CreateSpline2.md) | Obsolete. Superseded by [ISketchManager::CreateSpline3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CreateSpline3.md). |
| Method | [CreateSpline3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CreateSpline3.md) | Creates either a 2D spline or a spline constrained to a surface. |
| Method | [CreateSplineByEqnParams](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CreateSplineByEqnParams.md) | Creates a B-curve from B-spline data; that is, a set of B-spline vertices (control points) and a knot vector. |
| Method | [CreateSplineParamData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CreateSplineParamData.md) | Creates an empty spline parameter data object. |
| Method | [CreateSplinesByEqnParams](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CreateSplinesByEqnParams.md) | Obsolete. Superseded by [ISketchManager::CreateSplinesByEqnParams2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CreateSplinesByEqnParams2.md). |
| Method | [CreateSplinesByEqnParams2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CreateSplinesByEqnParams2.md) | Creates one or more spline segments using the B-curve parameters provided. |
| Method | [CreateTangentArc](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CreateTangentArc.md) | Creates a tangent arc. |
| Method | [EditCircularSketchStepAndRepeat](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~EditCircularSketchStepAndRepeat.md) | Edits a circular sketch pattern. |
| Method | [EditLinearSketchStepAndRepeat](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~EditLinearSketchStepAndRepeat.md) | Edits a linear sketch pattern. |
| Method | [EditSketchBlock](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~EditSketchBlock.md) | Puts the block definition in edit mode. |
| Method | [EndEditSketchBlock](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~EndEditSketchBlock.md) | Saves or discards your edits of the block and then ends the current editing session of this block. |
| Method | [ExplodeSketchBlockInstance](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~ExplodeSketchBlockInstance.md) | Explodes the specified block instance. |
| Method | [FullyDefineSketch](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~FullyDefineSketch.md) | Fully defines a sketch. |
| Method | [GetDynamicMirror](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~GetDynamicMirror.md) | Gets whether dynamic sketch mirroring, which is the automatic mirroring of newly created sketch entities about a selected centerline, is enabled. |
| Method | [GetSketchBlockDefinitionCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~GetSketchBlockDefinitionCount.md) | Gets the number of block definitions in the model. |
| Method | [GetSketchBlockDefinitions](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~GetSketchBlockDefinitions.md) | Gets all of the block definitions. |
| Method | [ICreateSpline](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~ICreateSpline.md) | Obsolete. Superseded by [ISketchManager::ICreateSpline2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~ICreateSpline2.md). |
| Method | [ICreateSpline2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~ICreateSpline2.md) | Creates a spline passing through the given points. |
| Method | [ICreateSplineByEqnParams](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~ICreateSplineByEqnParams.md) | Creates a B-curve from B-spline data; that is, a set of B-spline vertices (control points) and a knot vector. |
| Method | [ICreateSplinesByEqnParams](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~ICreateSplinesByEqnParams.md) | Creates one or more spline segments using the B-curve parameters provided. |
| Method | [IGetSketchBlockDefinitions](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~IGetSketchBlockDefinitions.md) | Gets all of the block definitions. |
| Method | [Insert3DSketch](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~Insert3DSketch.md) | Inserts a new 3D sketch in a model or closes the active sketch. |
| Method | [InsertExplodeLineSketch](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~InsertExplodeLineSketch.md) | Inserts or closes an explode line sketch in an exploded view. |
| Method | [InsertSketch](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~InsertSketch.md) | Inserts a new sketch in the current part or assembly document. |
| Method | [InsertSketchBlockInstance](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~InsertSketchBlockInstance.md) | Inserts a block instance at the specified location using the block definition. |
| Method | [InsertSketchPicture](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~InsertSketchPicture.md) | Obsolete. Superseded by [ISketchManager::InsertSketchPicture2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~InsertSketchPicture2.md). |
| Method | [InsertSketchPicture2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~InsertSketchPicture2.md) | Inserts a picture on the current drawing sketch. |
| Method | [IntersectCurves](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~IntersectCurves.md) | Creates a sketched intersection curve. |
| Method | [MakeSketchBlockFromFile](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~MakeSketchBlockFromFile.md) | Creates a block definition using the specified file. |
| Method | [MakeSketchBlockFromSelected](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~MakeSketchBlockFromSelected.md) | Creates a block definition at the specified location from the selected entities. |
| Method | [MakeSketchBlockFromSketch](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~MakeSketchBlockFromSketch.md) | Creates a block definition at the specified location using all of the sketch entities in the active sketch. |
| Method | [MakeSketchChain](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~MakeSketchChain.md) | Creates a sketch path using the selected entities. |
| Method | [PerimeterCircle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~PerimeterCircle.md) | Draws a 3-point perimeter arc. |
| Method | [ReverseEndPointTangent](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~ReverseEndPointTangent.md) | Reverses the end point tangent direction of splines and arcs. |
| Method | [RotateOrCopy3DAboutVector](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~RotateOrCopy3DAboutVector.md) | Rotates, and optionally copies, the selected 3D sketch entities about the specified vector. |
| Method | [RotateOrCopy3DAboutXYZ](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~RotateOrCopy3DAboutXYZ.md) | Rotates, and optionally copies, the selected 3D sketch entities about the specified x, y, and z coordinates. |
| Method | [SetDynamicMirror](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~SetDynamicMirror.md) | Enables or disables dynamic sketch mirroring, which is the automatic mirroring of newly created sketch entities about a selected centerline. |
| Method | [SetGridOptions](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~SetGridOptions.md) | Sets the options for the grid. |
| Method | [SketchExtend](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~SketchExtend.md) | Adds to the length of the selected sketch entity (i.e., line, centerline, or arc) to meet the nearest sketch entity. |
| Method | [SketchOffset](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~SketchOffset.md) | Obsolete. Superseded by [ISketchManager::SketchOffset2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~SketchOffset2.md). |
| Method | [SketchOffset2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~SketchOffset2.md) | Offsets the selected sketch entities. |
| Method | [SketchReplace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~SketchReplace.md) | Obsolete. Superseded by [ISketchManager::SketchReplace2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~SketchReplace2.md). |
| Method | [SketchReplace2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~SketchReplace2.md) | Replaces a sketch entity in a model with another sketch entity, preserving all references. |
| Method | [SketchTrim](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~SketchTrim.md) | Trims the selected sketch entities. |
| Method | [SketchUseEdge](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~SketchUseEdge.md) | Obsolete. Superseded by [ISketchManager::SketchUseEdge2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~SketchUseEdge2.md). |
| Method | [SketchUseEdge2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~SketchUseEdge2.md) | Obsolete. Superseded by [ISketchManager::SketchUseEdge3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~SketchUseEdge3.md). |
| Method | [SketchUseEdge3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~SketchUseEdge3.md) | Creates sketch entities on a sketch plane by projecting selected edges, loops, faces, curves, and external sketch contours. |
| Method | [SplitClosedSegment](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~SplitClosedSegment.md) | Splits the selected closed sketch segment into two sketch segments. |
| Method | [SplitOpenSegment](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~SplitOpenSegment.md) | Splits the selected open sketch segment into two sketch segments. |

[Top](#top)

 

See Also

#### Reference

[ISketchManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
