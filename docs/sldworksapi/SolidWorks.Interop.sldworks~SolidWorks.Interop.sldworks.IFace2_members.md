# IFace2 Interface Members

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2_members`

Allows access to the underlying edge, loop, and surface to the owning body or feature, and to face tessellation, trim data.
The following tables list the members exposed by [IFace2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md).

Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | [Check](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~Check.md) | Checks whether the face is a valid, and, if not, returns the faults. |
| Property | [IMaterialPropertyValues](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IMaterialPropertyValues.md) | Gets or sets the material properties for the selected face in the active configuration. |
| Property | [INormal](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~INormal.md) | Gets the unit normal vector for any planar face.  **NOTE:** **This property is a get-only property.** **Set is not implemented**. |
| Property | [MaterialIdName](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~MaterialIdName.md) | Gets or sets the material name. |
| Property | [MaterialPropertyValues](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~MaterialPropertyValues.md) | Gets or sets the material properties for the selected face in the active configuration. |
| Property | [MaterialUserName](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~MaterialUserName.md) | Gets or sets the material name, which is visible to the user. |
| Property | [Normal](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~Normal.md) | Gets the unit normal vector for any planar face.  **NOTE:** **This property is a get-only property.** **Set is not implemented**. |

[Top](#top)

Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | [AddPropertyExtension](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~AddPropertyExtension.md) | Adds a property extension to this face. |
| Method | [AttachSurface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~AttachSurface.md) | Attaches a surface to this face. |
| Method | [CreateSheetBody](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~CreateSheetBody.md) | Creates a sheet body from this face. |
| Method | [CreateSheetBodyByFaceExtension](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~CreateSheetBodyByFaceExtension.md) | Creates a sheet body by extending the face. |
| Method | [DetachSurface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~DetachSurface.md) | Detaches a surface from this face. |
| Method | [EnumEdges](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~EnumEdges.md) | Enumerates the edges in a face. |
| Method | [EnumLoops](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~EnumLoops.md) | Enumerates the loops in a face. |
| Method | [FaceInSurfaceSense](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~FaceInSurfaceSense.md) | Checks whether the face normal has the opposite direction (sense) as the underlying surface. |
| Method | [GetAllAssemblyDecalProperties](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetAllAssemblyDecalProperties.md) | Gets all of the decal properties applied to this face in an assembly component. |
| Method | [GetAllDecalProperties](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetAllDecalProperties.md) | Gets all of the decal properties applied to this face in a part. |
| Method | [GetArea](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetArea.md) | Gets the area of this face. |
| Method | [GetBody](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetBody.md) | Gets the body containing this face. |
| Method | [GetBox](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetBox.md) | Gets the box boundaries for this face. |
| Method | [GetClosestPointOn](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetClosestPointOn.md) | Uses the X,Y,Z input point to determine the closest point on the face. |
| Method | [GetDecalsCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetDecalsCount.md) | Gets the number of decals applied to this face. |
| Method | [GetEdgeCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetEdgeCount.md) | Gets the number of the edges that bound this face. |
| Method | [GetEdges](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetEdges.md) | Get the edges bounding this face. |
| Method | [GetFaceId](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetFaceId.md) | Gets the face ID of an imported body. |
| Method | [GetFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetFeature.md) | Gets the feature that owns this face. |
| Method | [GetFeatureId](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetFeatureId.md) | Gets the order number for the owning feature of this face. |
| Method | [GetFirstLoop](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetFirstLoop.md) | Gets the first loop in this face, which is not necessarily the outer loop. |
| Method | [GetLoopCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetLoopCount.md) | Gets the number of loops in this face. |
| Method | [GetLoops](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetLoops.md) | Gets all of the loops on this face. |
| Method | [GetMaterialPropertyValues2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetMaterialPropertyValues2.md) | Gets the material property values for this face. |
| Method | [GetNextFace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetNextFace.md) | Gets the next face in a body. |
| Method | [GetPatternSeedFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetPatternSeedFeature.md) | Gets the seed feature of a pattern. |
| Method | [GetProjectedPointOn](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetProjectedPointOn.md) | Gets the point where the input point is projected on to this face. |
| Method | [GetPropertyExtension](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetPropertyExtension.md) | Gets the property extension on this face. |
| Method | [GetSeedFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetSeedFeature.md) | Gets the seed feature of a patterned, mirrored, or copied body for this face. |
| Method | [GetShellType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetShellType.md) | Gets the shell type for this face. |
| Method | [GetSilhoutteEdges](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetSilhoutteEdges.md) | Obsolete. Superseded by [IFace2::GetSilhoutteEdgesVB](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetSilhoutteEdgesVB.md). |
| Method | [GetSilhoutteEdgesVB](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetSilhoutteEdgesVB.md) | Gets the silhouette edges. |
| Method | [GetSurface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetSurface.md) | Gets the surface referenced by this face. |
| Method | [GetTessNorms](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetTessNorms.md) | Gets the normal vector for each of the triangles that make up the shaded picture tessellation. |
| Method | [GetTessTextures](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetTessTextures.md) | Gets the texture coordinates for the triangles. |
| Method | [GetTessTriangleCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetTessTriangleCount.md) | Gets the number of triangles that make up the shaded picture tessellation for this face. |
| Method | [GetTessTriangles](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetTessTriangles.md) | Gets the triangles that make up the shaded picture tessellation for this face. |
| Method | [GetTessTriStripEdges](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetTessTriStripEdges.md) | Gets the edge ID for each of the edges in the triangles that make up the tessellation for this face. |
| Method | [GetTessTriStripNorms](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetTessTriStripNorms.md) | Gets the normal vector for each of the triangles that make up the shaded picture tessellation for this face. |
| Method | [GetTessTriStrips](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetTessTriStrips.md) | Gets the vertices that make up the shaded picture tessellation for this face. |
| Method | [GetTessTriStripSize](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetTessTriStripSize.md) | Gets the array size required for [IFace2::GetTessTriStrips](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetTessTriStrips.md) and [IFace2::IGetTessTriStrips](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetTessTriStrips.md). |
| Method | [GetTessTriStripTextures](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetTessTriStripTextures.md) | Gets the texture coordinate components for each vertex on each triangle strip on this face. |
| Method | [GetTexture](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetTexture.md) | Gets the texture applied to this face in the specified configuration. |
| Method | [GetTrackingIDs](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetTrackingIDs.md) | Gets the [tracking IDs assigned to this face](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~SetTrackingID.md). |
| Method | [GetTrackingIDsCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetTrackingIDsCount.md) | Gets the number of tracking IDs on this face. |
| Method | [GetTrimCurves](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetTrimCurves.md) | Obsolete. Superseded by [IFace2::GetTrimCurves2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetTrimCurves2.md). |
| Method | [GetTrimCurves2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetTrimCurves2.md) | Gets the definition of all of the entities that describe a trimmed face. |
| Method | [GetTrimCurveTopology](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetTrimCurveTopology.md) | Gets the trim curve topology for this face. |
| Method | [GetTrimCurveTopologyCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetTrimCurveTopologyCount.md) | Gets the number of elements in the trim curve topology for this face. |
| Method | [GetTrimCurveTopologyTypes](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetTrimCurveTopologyTypes.md) | Gets the types of elements in the trim curve topology for this face. |
| Method | [GetUVBounds](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetUVBounds.md) | Gets the values that describe the U, V bounds of this face. |
| Method | [HasMaterialPropertyValues](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~HasMaterialPropertyValues.md) | Gets whether this face has an appearance. |
| Method | [HasTextureCoordinates](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~HasTextureCoordinates.md) | Gets whether this face has texture coordinates. |
| Method | [Highlight](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~Highlight.md) | Adds highlighting to or removes highlighting from a face. |
| Method | [ICreateSheetBody](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~ICreateSheetBody.md) | Creates a sheet body from this face. |
| Method | [ICreateSheetBodyByFaceExtension](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~ICreateSheetBodyByFaceExtension.md) | Creates a sheet body by extending the face. |
| Method | [IGetAllDecalProperties](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetAllDecalProperties.md) | Gets the decal properties applied to this face. |
| Method | [IGetBody](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetBody.md) | Gets the body containing this face. |
| Method | [IGetBox](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetBox.md) | Gets the box boundaries for this face. |
| Method | [IGetClosestPointOn](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetClosestPointOn.md) | Uses the X,Y,Z input point to determine the closest point on the face. |
| Method | [IGetDecalProperties](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetDecalProperties.md) | Gets the properties of the specified decal on this face. |
| Method | [IGetEdges](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetEdges.md) | Get the edges bounding this face. |
| Method | [IGetFacetData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetFacetData.md) | Obsolete. Superseded by [IFace2::GetTessNorms](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetTessNorms.md), [IFace2::IGetTessNorms](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetTessNorms.md), [IFace2::GetTessTextures](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetTessTextures.md)[, IFace2::IGetTessTextures, IFace2::GetTessTriangleCount, IFace2::GetTessTriangles,](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetTessTriangles.md) [IFace2::IGetTessTriangles](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetTessTriangles.md), [IFace2::GetTessTriStripEdges](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetTessTriStripEdges.md), [IFace2::IGetTessTriStripEdges](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetTessTriStripEdges.md), [IFace::GetTessTriStripNorms](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetTessTriStripNorms.md), [IFace2::IGetTessTriStripNorms](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetTessTriStripNorms.md), [IFace2::GetTessTriStrips](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetTessTriStrips.md), and [IFace2::IGetTessTriStrips](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetTessTriStrips.md). |
| Method | [IGetFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetFeature.md) | Gets the feature that owns this face. |
| Method | [IGetFirstLoop](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetFirstLoop.md) | Gets the first loop in this face, which is not necessarily the outer loop. |
| Method | [IGetLoops](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetLoops.md) | Gets all of the loops on this face. |
| Method | [IGetMaterialPropertyValues2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetMaterialPropertyValues2.md) | Gets the material property values for this face. |
| Method | [IGetNextFace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetNextFace.md) | Gets the next face in a body. |
| Method | [IGetPatternSeedFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetPatternSeedFeature.md) | Gets the seed feature of a pattern. |
| Method | [IGetSilhoutteEdgeCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetSilhoutteEdgeCount.md) | Gets the number of silhouette edges for this face. |
| Method | [IGetSilhoutteEdges](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetSilhoutteEdges.md) | Gets the silhouette edges for this face with the specified root point and in the specified direction. |
| Method | [IGetSurface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetSurface.md) | Gets the surface referenced by this face. |
| Method | [IGetTessNorms](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetTessNorms.md) | Gets the normal vector for each of the triangles that make up the shaded picture tessellation. |
| Method | [IGetTessTextures](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetTessTextures.md) | Gets the texture coordinates for the triangles. |
| Method | [IGetTessTriangles](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetTessTriangles.md) | Gets the triangles that make up the shaded picture tessellation for this face. |
| Method | [IGetTessTriStripEdges](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetTessTriStripEdges.md) | Gets the edge ID for each of the edges in the triangles that make up the tessellation for this face. |
| Method | [IGetTessTriStripEdgeSize](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetTessTriStripEdgeSize.md) | Gets the size of the array returned by [IFace2::GetTessTriStripEdges](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetTessTriStripEdges.md) and [IFace2::IGetTessTriStripEdges](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetTessTriStripEdges.md). |
| Method | [IGetTessTriStripNorms](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetTessTriStripNorms.md) | Gets the normal vector for each of the triangles that make up the shaded picture tessellation for this face. |
| Method | [IGetTessTriStrips](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetTessTriStrips.md) | Gets the vertices that make up the shaded picture tessellation for this face. |
| Method | [IGetTrackingIDs](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetTrackingIDs.md) | Gets the [tracking IDs assigned to this face](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~SetTrackingID.md). |
| Method | [IGetTrimCurveSize](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetTrimCurveSize.md) | Obsolete. Superseded by [IFace2::IGetTrimCurveSize2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetTrimCurveSize2.md). |
| Method | [IGetTrimCurveSize2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetTrimCurveSize2.md) | Gets the size of the array required for [IFace2::GetTrimCurves2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetTrimCurves2.md) |
| Method | [IGetTrimCurveTopology](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetTrimCurveTopology.md) | Gets the trim curve topology for this face. |
| Method | [IGetTrimCurveTopologyTypes](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetTrimCurveTopologyTypes.md) | Gets the trim curve topology type array for this face. |
| Method | [IGetUVBounds](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetUVBounds.md) | Gets the values that describe the U, V bounds of this face. |
| Method | [IHighlight](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IHighlight.md) | Adds highlighting to or removes highlighting from a face. |
| Method | [IImprintCurve](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IImprintCurve.md) | Imprints a curve on the selected face. |
| Method | [IIsCoincident](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IIsCoincident.md) | Gets whether this face and the specified face, which is located on a different body, are coincident. |
| Method | [IIsSame](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IIsSame.md) | Gets whether the two faces are the same. |
| Method | [ImprintCurve](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~ImprintCurve.md) | Imprints a curve on the selected face. |
| Method | [ImprintCurveCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~ImprintCurveCount.md) | Gets the number of new edges and faces to create when imprinting a curve. |
| Method | [IRemoveInnerLoops](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IRemoveInnerLoops.md) | Removes the inner loops on this face if the face is from a sheet (surface) body. |
| Method | [IRemoveMaterialProperty2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IRemoveMaterialProperty2.md) | Removes the material property values from this face. |
| Method | [IReverseEvaluate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IReverseEvaluate.md) | Gets the UV parameters for the given XYZ location on this face. |
| Method | [IsCoincident](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IsCoincident.md) | Gets whether this face and the specified face, which is located on a different body, are coincident. |
| Method | [ISetMaterialPropertyValues2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~ISetMaterialPropertyValues2.md) | Sets the material property values for this face. |
| Method | [IsSame](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IsSame.md) | Gets whether the two faces are the same. |
| Method | [RemoveFaceId](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~RemoveFaceId.md) | Removes the face ID on an imported body. |
| Method | [RemoveInnerLoops](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~RemoveInnerLoops.md) | Removes the inner loops on this face if the face is from a sheet (surface) body. |
| Method | [RemoveMaterialProperty](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~RemoveMaterialProperty.md) | Obsolete. Superseded by [IFace2::RemoveMaterialProperty2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~RemoveMaterialProperty2.md). |
| Method | [RemoveMaterialProperty2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~RemoveMaterialProperty2.md) | Removes the material property values from this face. |
| Method | [RemoveRedundantTopology](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~RemoveRedundantTopology.md) | Removes redundant topology from the face. |
| Method | [RemoveTexture](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~RemoveTexture.md) | Obsolete. Superseded by [IFace2::RemoveTexture2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~RemoveTexture2.md). |
| Method | [RemoveTexture2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~RemoveTexture2.md) | Removes the texture applied to this face in the specified configuration. |
| Method | [RemoveTextureByDisplayState](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~RemoveTextureByDisplayState.md) | Removes the texture applied to this face in the specified display state. |
| Method | [RemoveTrackingID](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~RemoveTrackingID.md) | Removes a [tracking ID assigned to this face](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~SetTrackingID.md). |
| Method | [ResetPropertyExtension](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~ResetPropertyExtension.md) | Clears all values stored in the property extension. |
| Method | [ReverseEvaluate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~ReverseEvaluate.md) | Gets the UV parameters for the given XYZ location on this face. |
| Method | [SetFaceId](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~SetFaceId.md) | Sets the face ID on an imported body. |
| Method | [SetMaterialPropertyValues2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~SetMaterialPropertyValues2.md) | Sets the material property values for this face. |
| Method | [SetTexture](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~SetTexture.md) | Applies texture to this face in the specified configuration. |
| Method | [SetTextureByDisplayState](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~SetTextureByDisplayState.md) | Applies texture to this face in the specified display state. |
| Method | [SetTrackingID](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~SetTrackingID.md) | Assigns a tracking ID to this face. |

[Top](#top)

 

See Also

#### Reference

[IFace2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
