# IVariableFilletFeatureData2 Interface Members

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2_members`

Allows access to a variable radius fillet feature.
The following tables list the members exposed by [IVariableFilletFeatureData2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2.md).

Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | [AsymmetricFillet](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~AsymmetricFillet.md) | Gets or sets whether this variable radius fillet is asymmetric. |
| Property | [ConicTypeForCrossSectionProfile](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~ConicTypeForCrossSectionProfile.md) | Gets or sets the type of profile for this fillet. |
| Property | [CurvatureContinuous](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~CurvatureContinuous.md) | Gets or sets whether to create a smoother curvature between adjacent surfaces for this variable radius fillet feature. |
| Property | [DefaultConicRhoOrRadius](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~DefaultConicRhoOrRadius.md) | Gets or sets the default conic rho or conic radius of this fillet. |
| Property | [DefaultDistance](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~DefaultDistance.md) | Gets or sets the default Distance 2 radius of this asymmetric fillet. |
| Property | [DefaultRadius](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~DefaultRadius.md) | Gets or sets the default radius for this symmetric fillet or the default Distance 1 radius for this asymmetric fillet. |
| Property | [FilletEdgeCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~FilletEdgeCount.md) | Gets the number of edges to fillet. |
| Property | [OverflowType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~OverflowType.md) | Gets or sets the overflow type for this variable fillet feature. |
| Property | [PropagateFeatureToParts](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~PropagateFeatureToParts.md) | Gets or sets whether to extend the fillet feature to all affected parts in the assembly. |
| Property | [PropagateToTangentFaces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~PropagateToTangentFaces.md) | Gets or sets whether to extend the fillet to all faces tangent to the selected face or edge. |
| Property | [TransitionType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~TransitionType.md) | Gets or sets the type of transition between this variable fillet and an adjacent fillet. |

[Top](#top)

Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | [AccessSelections](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~AccessSelections.md) | Gains access to the selections used to define the variable fillet feature. |
| Method | [GetConicRhoOrRadius](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~GetConicRhoOrRadius.md) | Gets the conic rho, conic radius, or circular radius of this fillet. |
| Method | [GetConicRhoOrRadius2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~GetConicRhoOrRadius2.md) | Gets the conic rho or radius at the specified vertex. |
| Method | [GetControlPointConicRhoOrRadiusAtIndex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~GetControlPointConicRhoOrRadiusAtIndex.md) | Gets the conic rho or radius at the specified control point. |
| Method | [GetControlPointDistanceAtIndex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~GetControlPointDistanceAtIndex.md) | Gets the Distance 2 radius at the specified control point for the asymmetric fillet. |
| Method | [GetControlPointRadiusAtIndex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~GetControlPointRadiusAtIndex.md) | Gets the radius at the specified control point. |
| Method | [GetControlPointsCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~GetControlPointsCount.md) | Gets the number of intermediate control points on this variable fillet feature. |
| Method | [GetDistance](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~GetDistance.md) | Gets the Distance 2 radius for this asymmetric fillet. |
| Method | [GetFilletEdgeAtIndex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~GetFilletEdgeAtIndex.md) | Gets the fillet edge at the specified index. |
| Method | [GetRadius](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~GetRadius.md) | Obsolete. Superseded by [IVariableFilletFeatureData2::GetRadius2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~GetRadius2.md). |
| Method | [GetRadius2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~GetRadius2.md) | Gets the value of the Distance 1 radius at the specified vertex. |
| Method | [GetSetbackDistanceCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~GetSetbackDistanceCount.md) | Gets the number of setback distances for the specified vertex on this variable fillet feature. |
| Method | [GetSetbackVertexDistance](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~GetSetbackVertexDistance.md) | Gets the setback distance for the specified vertex on this variable fillet feature. |
| Method | [GetSetbackVertices](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~GetSetbackVertices.md) | Gets the setback vertices for this variable fillet feature. |
| Method | [GetSetbackVerticesCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~GetSetbackVerticesCount.md) | Gets the number of setback vertices for this variable fillet feature. |
| Method | [IAccessSelections](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~IAccessSelections.md) | Gains access to the selections used to define the variable fillet feature. |
| Method | [IGetConicRhoOrRadius](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~IGetConicRhoOrRadius.md) | Gets the conic rho, conic radius, or circular radius of this fillet. |
| Method | [IGetFilletEdgeAtIndex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~IGetFilletEdgeAtIndex.md) | Gets the fillet edge at the specified index. |
| Method | [IGetRadius](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~IGetRadius.md) | Obsolete. Superseded by [IVariableFilletFeatureData2::Radius2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~GetRadius2.md). |
| Method | [IGetSetbackVertexDistance](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~IGetSetbackVertexDistance.md) | Gets the setback distance for the specified vertex on this variable fillet feature. |
| Method | [IGetSetbackVertices](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~IGetSetbackVertices.md) | Gets the setback vertices for this variable fillet feature. |
| Method | [ISetConicRhoOrRadius](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~ISetConicRhoOrRadius.md) | Sets the conic rho, conic radius, or circular radius of this fillet. |
| Method | [ISetRadius](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~ISetRadius.md) | Sets the radius value for specified fillet item. |
| Method | [ISetSetbackVertexDistance](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~ISetSetbackVertexDistance.md) | Sets the setback distance for the specified vertex and its edges on this variable fillet feature. |
| Method | [ISetSetbackVertices](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~ISetSetbackVertices.md) | Sets the setback vertices for this variable fillet feature. |
| Method | [ReleaseSelectionAccess](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~ReleaseSelectionAccess.md) | Releases access to the selections used to define the variable fillet feature. |
| Method | [SetConicRhoOrRadius](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~SetConicRhoOrRadius.md) | Sets the conic rho or radius for the specified fillet item. |
| Method | [SetControlPointConicRhoOrRadiusAtIndex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~SetControlPointConicRhoOrRadiusAtIndex.md) | Sets the conic rho or radius at the specified control point. |
| Method | [SetControlPointDistanceAtIndex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~SetControlPointDistanceAtIndex.md) | Sets the Distance 2 radius at the specified control point for the asymmetric fillet. |
| Method | [SetControlPointRadiusAtIndex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~SetControlPointRadiusAtIndex.md) | Sets the radius at the specified control point. |
| Method | [SetDistance](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~SetDistance.md) | Sets the Distance 2 radius for this asymmetric fillet. |
| Method | [SetRadius](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~SetRadius.md) | Sets the value of the Distance 1 radius at the specified vertex. |
| Method | [SetSetbackVertexDistance](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~SetSetbackVertexDistance.md) | Sets the setback distances on fillet edges from the specified fillet corner vertex on this variable fillet feature. |
| Method | [SetSetbackVertices](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~SetSetbackVertices.md) | Sets the setback vertices for this variable fillet feature. |

[Top](#top)

 

See Also

#### Reference

[IVariableFilletFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)  
[ISimpleFilletFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2.md)  
[IChamferFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChamferFeatureData2.md)
