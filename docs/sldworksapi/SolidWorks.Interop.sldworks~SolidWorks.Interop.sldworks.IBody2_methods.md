# IBody2 Interface Methods

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_methods`

Allows access to the faces on a body and the ability to create surfaces for sewing into a body object.
For a list of all members of this type, see [IBody2 members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.md).

Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | [AddConstantFillets](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~AddConstantFillets.md) | Creates constant radius fillets on the specified edges on this body. |
| Method | [AddProfileArc](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~AddProfileArc.md) | Creates an arc profile curve and returns a pointer to that curve. |
| Method | [AddProfileBspline](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~AddProfileBspline.md) | Creates an B-spline profile curve and returns a pointer to that curve. |
| Method | [AddProfileBsplineByPts](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~AddProfileBsplineByPts.md) | Adds a profile B-spline. |
| Method | [AddProfileLine](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~AddProfileLine.md) | Creates a line profile curve and returns a pointer to that curve. |
| Method | [AddPropertyExtension](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~AddPropertyExtension.md) | Obsolete. Superseded by [IBody2::AddPropertyExtension2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~AddPropertyExtension2.md). |
| Method | [AddPropertyExtension2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~AddPropertyExtension2.md) | Adds a property extension to this body. |
| Method | [AddVertexPoint](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~AddVertexPoint.md) | Adds a vertex. |
| Method | [ApplyTransform](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~ApplyTransform.md) | Applies a transform to this body. |
| Method | [Check](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~Check.md) | Obsolete. Superseded by [IBody2::Check3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~Check3.md). |
| Method | [Check2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~Check2.md) | Obsolete. Superseded by [IBody2::Check3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~Check3.md). |
| Method | [ConvertToMeshBody](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~ConvertToMeshBody.md) | Converts a solid body to a mesh BREP (boundary representation) body. |
| Method | [Copy](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~Copy.md) | Obsolete. Superseded by [IBody2::Copy2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~Copy2.md). |
| Method | [Copy2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~Copy2.md) | Gets a copy of this body. |
| Method | [CreateBaseFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~CreateBaseFeature.md) | Creates a base feature for the imported body. |
| Method | [CreateBlendSurface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~CreateBlendSurface.md) | Creates a constant radius rolling-ball blend surface (also known as a pipe surface) between two side surfaces. |
| Method | [CreateBodyFromFaces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~CreateBodyFromFaces.md) | Creates a temporary body from the faces. |
| Method | [CreateBodyFromSurfaces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~CreateBodyFromSurfaces.md) | Creates a body from a list of trimmed surfaces. |
| Method | [CreateBoundedSurface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~CreateBoundedSurface.md) | Creates a bounded surface from an independent base surface. |
| Method | [CreateBsplineSurface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~CreateBsplineSurface.md) | Creates a new B-spline surface. |
| Method | [CreateExtrusionSurface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~CreateExtrusionSurface.md) | Creates a new surface of extrusion (infinitely long tabulated cylinder). |
| Method | [CreateNewSurface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~CreateNewSurface.md) | Creates a handle for a new surface to serve as geometry for a face to be added to the body. |
| Method | [CreateOffsetSurface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~CreateOffsetSurface.md) | Creates a new surface offset from an existing surface. |
| Method | [CreatePlanarSurface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~CreatePlanarSurface.md) | Creates a new infinite planar surface. |
| Method | [CreatePlanarTrimSurfaceDLL](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~CreatePlanarTrimSurfaceDLL.md) | Creates a planar trim surface for this body. |
| Method | [CreateRevolutionSurface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~CreateRevolutionSurface.md) | Creates a new surface of revolution. |
| Method | [CreateRuledSurface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~CreateRuledSurface.md) | Creates a ruled surface from the specified curves and apex point. |
| Method | [CreateTempBodyFromSurfaces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~CreateTempBodyFromSurfaces.md) | Creates a temporary body from a list of existing trimmed surfaces. |
| Method | [CreateTrimmedSurface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~CreateTrimmedSurface.md) | Creates a trimmed surface from a base surface and a list of existing trimming curves. |
| Method | [DeleteBlends](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~DeleteBlends.md) | Obsolete. Superseded by [IBody2::DeleteBlends2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~DeleteBlends2.md). |
| Method | [DeleteBlends2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~DeleteBlends2.md) | Obsolete. Superseded by [IBody2::DeleteBlends3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~DeleteBlends3.md). |
| Method | [DeleteBlends3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~DeleteBlends3.md) | Removes a set of fillet faces from a temporary body and heals the body. |
| Method | [DeleteFaces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~DeleteFaces.md) | Obsolete. Superseded by [IBody2::DeleteFaces3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~DeleteFaces3.md). |
| Method | [DeleteFaces2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~DeleteFaces2.md) | Obsolete. Superseded by [IBody2::DeleteFaces3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~DeleteFaces3.md). |
| Method | [DeleteFaces3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~DeleteFaces3.md) | Obsolete. Superseded by [IBody2::IDeleteFaces4](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~DeleteFaces4.md). |
| Method | [DeleteFaces4](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~DeleteFaces4.md) | Obsolete. Superseded by [IBody2::DeleteFaces5](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~DeleteFaces5.md). |
| Method | [DeleteFaces5](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~DeleteFaces5.md) | Deletes a set of faces from a temporary body. |
| Method | [DeleteFacesMakeSheetBodies](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~DeleteFacesMakeSheetBodies.md) | Creates sheet bodies from deleted faces. |
| Method | [DeSelect](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~DeSelect.md) | Deselects this body. |
| Method | [Diagnose](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~Diagnose.md) | Gets the [IDiagnoseResult](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDiagnoseResult.md) object for this body. |
| Method | [Display](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~Display.md) | Obsolete. Superseded by [IBody2::Display3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~Display3.md). |
| Method | [Display2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~Display2.md) | Obsolete. Superseded by [IBody2::Display3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~Display3.md). |
| Method | [Display3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~Display3.md) | Displays this temporary body in the context of the specified part or component. |
| Method | [DisplayWireFrameXOR](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~DisplayWireFrameXOR.md) | Displays a temporary body in the given part's context in XOR mode. |
| Method | [DraftBody](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~DraftBody.md) | Obsolete. Superseded by [IBody2::DraftBody2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~DraftBody2.md). |
| Method | [DraftBody2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~DraftBody2.md) | Adds drafts to the specified faces on a temporary body. This method modifies the body. |
| Method | [EnumFaces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~EnumFaces.md) | Returns an enumerated list of the faces in a body. |
| Method | [ExtendSurface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~ExtendSurface.md) | Creates a new temporary body by extending the selected edges. |
| Method | [FindAttribute](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~FindAttribute.md) | Finds an attribute on a body. |
| Method | [GetBodyBox](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetBodyBox.md) | Gets the bounding box for this body. |
| Method | [GetCoincidenceTransform](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetCoincidenceTransform.md) | Obsolete. Superseded by [IBody2::GetCoincidenceTransform2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetCoincidenceTransform2.md). |
| Method | [GetCoincidenceTransform2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetCoincidenceTransform2.md) | Calculates the transformation matrix, which would make the input body coincident with this body if the transformation matrix is applied. |
| Method | [GetEdgeCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetEdgeCount.md) | Gets the number of edges for this body. |
| Method | [GetEdges](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetEdges.md) | Gets the edges for this body. |
| Method | [GetExcessBodyArray](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetExcessBodyArray.md) | Gets the excess bodies after sewing. |
| Method | [GetExtremePoint](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetExtremePoint.md) | Calculates the extreme point of the model in the specified direction. |
| Method | [GetFaceCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetFaceCount.md) | Gets the number of faces in this body. |
| Method | [GetFaces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetFaces.md) | Gets all of the faces on the body. |
| Method | [GetFeatureCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetFeatureCount.md) | Gets the number of features in this body in a multibody sheet metal part. |
| Method | [GetFeatures](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetFeatures.md) | Gets the features in this body in a multibody sheet metal part. |
| Method | [GetFirstFace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetFirstFace.md) | Finds the first face in a body and returns the face. |
| Method | [GetFirstSelectedFace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetFirstSelectedFace.md) | Gets the first selected face on this body. For use with [IBody2::GetProcessedBodyWithSelFace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetProcessedBodyWithSelFace.md) and intended for IGES routines. |
| Method | [GetGraphicsBody](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetGraphicsBody.md) | Gets the graphics body associated with this body. |
| Method | [GetIgesErrorCode](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetIgesErrorCode.md) | Gets the current IGES error code. |
| Method | [GetIgesErrorCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetIgesErrorCount.md) | Gets the number of errors encountered while running an IGES routine. |
| Method | [GetIntersectionEdges](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetIntersectionEdges.md) | Obsolete. Superseded by [IBody2::GetIntersectionEdges2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetIntersectionEdges2.md). |
| Method | [GetIntersectionEdges2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetIntersectionEdges2.md) | Gets the edges resulting from the intersection of the specified tool body and this body. |
| Method | [GetMassProperties](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetMassProperties.md) | Gets the mass properties of this body. |
| Method | [GetMaterialIdName](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetMaterialIdName.md) | Obsolete. Superseded by [IBody2::GetMaterialIdName2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetMaterialIdName2.md). |
| Method | [GetMaterialIdName2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetMaterialIdName2.md) | Gets the material name for this body. |
| Method | [GetMaterialPropertyName](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetMaterialPropertyName.md) | Gets the names of the material database and the material for the specified configuration. |
| Method | [GetMaterialUserName](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetMaterialUserName.md) | Obsolete. Superseded by [IBody2::GetMaterialUserName2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetMaterialIdName2.md). |
| Method | [GetMaterialUserName2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetMaterialUserName2.md) | Gets the material name for this body; the material name is visible to the user. |
| Method | [GetMeshBody](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetMeshBody.md) | Gets the mesh body associated with this body. |
| Method | [GetMiddleSurface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetMiddleSurface.md) | Inserts a midsurface in a body. |
| Method | [GetNextSelectedFace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetNextSelectedFace.md) | Gets the next selected face. For use with [IBody2::GetProcessedBodyWithSelFace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetProcessedBodyWithSelFace.md) and intended for IGES routines. |
| Method | [GetOriginalPatternedBody](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetOriginalPatternedBody.md) | Gets the original body from this patterned body. Also gets the transformation of this body with respect to the original body. |
| Method | [GetProcessedBody](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetProcessedBody.md) | Obsolete. Superseded by [IBody2::GetProcessedBody2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetProcessedBody2.md). |
| Method | [GetProcessedBody2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetProcessedBody2.md) | Pre-processes the geometry of the body using the specified parameters. |
| Method | [GetProcessedBodyWithSelFace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetProcessedBodyWithSelFace.md) | Gets a processed body. |
| Method | [GetPropertyExtension](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetPropertyExtension.md) | Obsolete. Superseded by [IBody2::GetPropertyExtension2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetPropertyExtension2.md). |
| Method | [GetPropertyExtension2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetPropertyExtension2.md) | Gets the specified property extension on this body. |
| Method | [GetSafeBody](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetSafeBody.md) | Not implemented. |
| Method | [GetSelectedFaceCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetSelectedFaceCount.md) | Gets the number of selected faces on this body. For use with [IBody2::GetProcessedBodyWithSelFace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetProcessedBodyWithSelFace.md) and [IBody2::IGetPrcoessedBodyWithSelFace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IGetProcessedBodyWithSelFace.md) and intended for IGES routines. |
| Method | [GetSelectedFaces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetSelectedFaces.md) | Gets the selected faces. For use with [IBody2::GetProcessedBodyWithSelFace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetProcessedBodyWithSelFace.md) and intended for IGES routines. |
| Method | [GetSelectionId](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetSelectionId.md) | Gets the selection ID of the body, if one exists. |
| Method | [GetSheetBody](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetSheetBody.md) | Gets a sheet (surface) body in this body. |
| Method | [GetTessellation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetTessellation.md) | Gets the [ITessellation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation.md) object. |
| Method | [GetTexture](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetTexture.md) | Gets the texture applied to this body in the specified configuration. |
| Method | [GetTrackingIDs](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetTrackingIDs.md) | Gets the [tracking IDs assigned to this body](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~SetTrackingID.md). |
| Method | [GetTrackingIDsCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetTrackingIDsCount.md) | Gets the number of tracking IDs on this body. |
| Method | [GetType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetType.md) | Gets the type of the body. |
| Method | [GetUpdateStamp](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetUpdateStamp.md) | Gets the update stamp for the body as of the last rebuild. |
| Method | [GetVertexCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetVertexCount.md) | Gets the number of vertices in this body. |
| Method | [GetVertices](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetVertices.md) | Gets the vertices in this body. |
| Method | [HasMaterialPropertyValues](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~HasMaterialPropertyValues.md) | Gets whether this body has an appearance. |
| Method | [Hide](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~Hide.md) | Hides this temporary body in the context of the specified part. |
| Method | [HideBody](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~HideBody.md) | Hides or shows this body. |
| Method | [IAddProfileArc](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IAddProfileArc.md) | Creates an arc profile curve and returns a pointer to that curve. |
| Method | [IAddProfileArcDLL](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IAddProfileArcDLL.md) | Adds a profile arc. |
| Method | [IAddProfileBspline](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IAddProfileBspline.md) | Creates an B-spline profile curve and returns a pointer to that curve. |
| Method | [IAddProfileBsplineByPts](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IAddProfileBsplineByPts.md) | Adds a profile B-spline. |
| Method | [IAddProfileBsplineDLL](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IAddProfileBsplineDLL.md) | Adds a profile B-spline. |
| Method | [IAddProfileLine](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IAddProfileLine.md) | Creates a line profile curve and returns a pointer to that curve. |
| Method | [IAddProfileLineDLL](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IAddProfileLineDLL.md) | Adds a profile line. |
| Method | [IAddVertexPoint](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IAddVertexPoint.md) | Adds a vertex. |
| Method | [ICombineVolumes](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~ICombineVolumes.md) | Combines the volumes of two bodies. |
| Method | [ICopy](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~ICopy.md) | Gets a copy of this body. |
| Method | [ICreateBaseFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~ICreateBaseFeature.md) | Creates a base feature for the imported body. |
| Method | [ICreateBlendSurface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~ICreateBlendSurface.md) | Creates a constant radius rolling-ball blend surface (also known as a pipe surface) between two side surfaces. |
| Method | [ICreateBodyFromFaces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~ICreateBodyFromFaces.md) | Creates a temporary body from the faces. |
| Method | [ICreateBoundedSurface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~ICreateBoundedSurface.md) | Creates a bounded surface from an independent base surface. |
| Method | [ICreateBsplineSurface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~ICreateBsplineSurface.md) | Creates a new B-spline surface. |
| Method | [ICreateBsplineSurfaceDLL](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~ICreateBsplineSurfaceDLL.md) | Creates a B-spline surface in this body. |
| Method | [ICreateExtrusionSurface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~ICreateExtrusionSurface.md) | Creates a new surface of extrusion (infinitely long tabulated cylinder). |
| Method | [ICreateExtrusionSurfaceDLL](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~ICreateExtrusionSurfaceDLL.md) | Creates an extruded surface. |
| Method | [ICreateNewSurface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~ICreateNewSurface.md) | Creates a handle for a new surface to serve as geometry for a face to be added to the body. |
| Method | [ICreateOffsetSurface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~ICreateOffsetSurface.md) | Creates a new surface offset from an existing surface. |
| Method | [ICreatePlanarSurface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~ICreatePlanarSurface.md) | Creates a new infinite planar surface. |
| Method | [ICreatePlanarSurfaceDLL](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~ICreatePlanarSurfaceDLL.md) | Creates a planar surface. |
| Method | [ICreatePlanarTrimSurfaceDLL](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~ICreatePlanarTrimSurfaceDLL.md) | Creates a planar trim surface for this body. |
| Method | [ICreatePsplineSurfaceDLL](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~ICreatePsplineSurfaceDLL.md) | Creates a B-surface from a piecewise surface. |
| Method | [ICreateRevolutionSurface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~ICreateRevolutionSurface.md) | Creates a new surface of revolution. |
| Method | [ICreateRevolutionSurfaceDLL](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~ICreateRevolutionSurfaceDLL.md) | Creates a surface of revolution for this body. |
| Method | [ICreateRuledSurface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~ICreateRuledSurface.md) | Creates a ruled surface from the specified curves and apex point. |
| Method | [ICreateTempBodyFromSurfaces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~ICreateTempBodyFromSurfaces.md) | Creates a temporary body from a list of existing trimmed surfaces. |
| Method | [IDeleteBlends](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IDeleteBlends.md) | Obsolete. Superseded by [IBody2::IDeleteBlends2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IDeleteBlends2.md). |
| Method | [IDeleteBlends2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IDeleteBlends2.md) | Obsolete. Superseded by [IBody2::DeleteBlends3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IDeleteBlends3.md). |
| Method | [IDeleteBlends3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IDeleteBlends3.md) | Removes a set of fillet faces from a temporary body and heals the body. |
| Method | [IDeleteFaces2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IDeleteFaces2.md) | Obsolete. Superseded by [IBody2::IDeleteFaces3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IDeleteFaces3.md). |
| Method | [IDeleteFaces3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IDeleteFaces3.md) | Obsolete. Superseded by [IBody2::IDeleteFaces4](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~DeleteFaces4.md). |
| Method | [IDeleteFacesMakeSheetBodies](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IDeleteFacesMakeSheetBodies.md) | Creates sheet bodies from deleted faces. |
| Method | [IDeleteFacesMakeSheetBodiesCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IDeleteFacesMakeSheetBodiesCount.md) | Gets the number of sheet bodies to create from the deleted faces. |
| Method | [IDisplay](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IDisplay.md) | Obsolete. Superseded by [IBody2::Display3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~Display3.md). |
| Method | [IDisplayWireFrameXOR](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IDisplayWireFrameXOR.md) | Displays a temporary body in the given part's context in XOR mode. |
| Method | [IDraftBody](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IDraftBody.md) | Obsolete. Superseded by [IBody2::IDraftBody2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IDraftBody2.md). |
| Method | [IDraftBody2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IDraftBody2.md) | Adds drafts to the specified faces on a temporary body. This method modifies the body. |
| Method | [IExtendSurface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IExtendSurface.md) | Creates a new temporary body by extending the selected edges. |
| Method | [IGetBodyBox](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IGetBodyBox.md) | Gets the bounding box for this body. |
| Method | [IGetEdges](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IGetEdges.md) | Gets the edges for this body. |
| Method | [IGetExcessBodyArray](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IGetExcessBodyArray.md) | Gets the excess bodies after sewing. |
| Method | [IGetExcessBodyCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IGetExcessBodyCount.md) | Gets the number of excess bodies. |
| Method | [IGetFaces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IGetFaces.md) | Gets all of the faces on the body. |
| Method | [IGetFeatures](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IGetFeatures.md) | Gets the features in this body in a multibody sheet metal part. |
| Method | [IGetFirstFace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IGetFirstFace.md) | Finds the first face in a body and returns the face. |
| Method | [IGetFirstSelectedFace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IGetFirstSelectedFace.md) | Gets the first selected face on this body. For use with [IBody2::IGetProcessedBodyWithSelFace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IGetProcessedBodyWithSelFace.md) and intended for IGES routines. |
| Method | [IGetIntersectionEdgeCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IGetIntersectionEdgeCount.md) | Gets the number of intersecting edges between this body and the specified tool body. |
| Method | [IGetIntersectionEdges](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IGetIntersectionEdges.md) | Obsolete. Superseded by [IBody2::GetIntersectionEdges2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetIntersectionEdges2.md). |
| Method | [IGetMassProperties](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IGetMassProperties.md) | Gets the mass properties of this body. |
| Method | [IGetMaterialPropertyValuesForFace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IGetMaterialPropertyValuesForFace.md) | Gets the color of the specified face. |
| Method | [IGetMiddleSurface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IGetMiddleSurface.md) | Inserts a midsurface in a body. |
| Method | [IGetNextSelectedFace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IGetNextSelectedFace.md) | Gets the next selected face. For use with [IBody2::GetProcessedBodyWithSelFace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetProcessedBodyWithSelFace.md) and intended for IGES routines. |
| Method | [IGetProcessedBody](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IGetProcessedBody.md) | Obsolete. Superseded by [IBody2::GetProcessedBody2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetProcessedBody2.md). |
| Method | [IGetProcessedBodyWithSelFace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IGetProcessedBodyWithSelFace.md) | Gets a processed body. |
| Method | [IGetSelectedFaces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IGetSelectedFaces.md) | Gets the selected faces. For use with [IBody2::GetProcessedBodyWithSelFace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetProcessedBodyWithSelFace.md) and intended for IGES routines. |
| Method | [IGetSheetBody](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IGetSheetBody.md) | Gets a sheet (surface) body in this body. |
| Method | [IGetTessellation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IGetTessellation.md) | Gets the [ITessellation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation.md) object. |
| Method | [IGetTrackingIDs](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IGetTrackingIDs.md) | Gets the [tracking IDs assigned to this body](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~SetTrackingID.md). |
| Method | [IGetVertices](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IGetVertices.md) | Gets the vertices in this body. |
| Method | [IHide](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IHide.md) | Hides a temporary body using the specified part's context. |
| Method | [IMatchedBoolean](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IMatchedBoolean.md) | Obsolete. Superseded by [IBody2::IMatchedBoolean3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IMatchedBoolean3.md). |
| Method | [IMatchedBoolean2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IMatchedBoolean2.md) | Obsolete. Superseded by [IBody2::IMatchedBoolean3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IMatchedBoolean3.md). |
| Method | [IMatchedBoolean3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IMatchedBoolean3.md) | Obsolete. Superseded by [IBody2::IMatchedBoolean4](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IMatchedBoolean4.md). |
| Method | [IMatchedBoolean4](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IMatchedBoolean4.md) | Performs a matched boolean on the specified bodies and supports an optional list of faces that match exactly. |
| Method | [IOperations](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IOperations.md) | Obsolete. Superseded by [IBody2::Operations2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IOperations2.md). |
| Method | [IOperations2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IOperations2.md) | Performs add, cut, and intersect (unite, subtract, and interfere) operations between two temporary bodies. |
| Method | [IRemoveFacesFromSheet](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IRemoveFacesFromSheet.md) | Removes the specified faces from a sheet (surface) body. |
| Method | [IRemoveMaterialProperty](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IRemoveMaterialProperty.md) | Removes the material property values (e.g., color) from the body in the specified configurations in parts and assemblies. |
| Method | [ISave](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~ISave.md) | Saves this body. |
| Method | [ISectionBySheet](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~ISectionBySheet.md) | Sections a body using a sheet (surface) body. |
| Method | [ISetCurrentSurface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~ISetCurrentSurface.md) | Places an existing surface into a temporary body that is under construction. |
| Method | [ISetXform](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~ISetXform.md) | Obsolete. Superseded by [IBody2::ApplyTransform](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~ApplyTransform.md). |
| Method | [IsGraphicsBody](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IsGraphicsBody.md) | Gets whether this body is a graphics body. |
| Method | [IsMeshBody](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IsMeshBody.md) | Gets whether this body is a mesh body. |
| Method | [IsPatternSeed](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IsPatternSeed.md) | Gets whether this body is the seed of a patterned body. |
| Method | [IsSheetMetal](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IsSheetMetal.md) | Gets whether this body was created by a sheet metal feature. |
| Method | [IsTemporaryBody](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IsTemporaryBody.md) | Gets whether the body is a temporary body. |
| Method | [MakeOffset](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~MakeOffset.md) | Creates a new temporary body by offsetting the selected surface body by the specified distance and in the specified direction. |
| Method | [MatchedBoolean](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~MatchedBoolean.md) | Obsolete. Superseded by [IBody2::MatchedBoolean3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~MatchedBoolean3.md). |
| Method | [MatchedBoolean2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~MatchedBoolean2.md) | Obsolete. Superseded by [IBody2::MatchedBoolean3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~MatchedBoolean3.md). |
| Method | [MatchedBoolean3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~MatchedBoolean3.md) | Obsolete. Superseded by [IBody2::MatchedBoolean4](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~MatchedBoolean4.md). |
| Method | [MatchedBoolean4](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~MatchedBoolean4.md) | Performs a matched boolean on the specified bodies and supports an optional list of faces that match exactly. |
| Method | [MinimumRadius](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~MinimumRadius.md) | Gets the minimum radius of this body. |
| Method | [Negate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~Negate.md) | Reverses the direction (i.e., orientation) of the body. |
| Method | [OffsetPlanarWireBody](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~OffsetPlanarWireBody.md) | Offsets a planar wire body in the normal plane by the specified distance. |
| Method | [Operations](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~Operations.md) | Obsolete. Superseded by [IBody2::Operations2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~Operations2.md). |
| Method | [Operations2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~Operations2.md) | Performs add, cut, and intersect (unite, subtract, and interfere) operations between two temporary bodies. |
| Method | [RemoveFacesFromSheet](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~RemoveFacesFromSheet.md) | Removes the specified faces from a sheet (surface) body. |
| Method | [RemoveMaterialProperty](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~RemoveMaterialProperty.md) | Removes the material property values (e.g., color) from the body in the specified configurations in parts and assemblies. |
| Method | [RemoveRedundantTopology](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~RemoveRedundantTopology.md) | Removes redundant topology from the body. |
| Method | [RemoveTexture](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~RemoveTexture.md) | Removes the texture applied to this body in the specified configuration. |
| Method | [RemoveTextureByDisplayState](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~RemoveTextureByDisplayState.md) | Removes the texture applied to this body in the specified display state. |
| Method | [RemoveTrackingID](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~RemoveTrackingID.md) | Removes a [tracking ID assigned to this body](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~SetTrackingID.md). |
| Method | [ResetEdgeTolerances](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~ResetEdgeTolerances.md) | Resets the tolerance on all edges of this body. |
| Method | [ResetPropertyExtension](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~ResetPropertyExtension.md) | Obsolete. Superseded by [IBody2::ResetPropertyExtension2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~ResetPropertyExtension2.md). |
| Method | [ResetPropertyExtension2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~ResetPropertyExtension2.md) | Clears all values stored in the property extension. |
| Method | [Save](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~Save.md) | Saves this body. |
| Method | [Select](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~Select.md) | Obsolete. Superseded by [IBody2::Select2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~Select2.md). |
| Method | [Select2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~Select2.md) | Selects this body and marks it. |
| Method | [SetCurrentSurface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~SetCurrentSurface.md) | Places an existing surface into a temporary body that is under construction. |
| Method | [SetIgesInfo](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~SetIgesInfo.md) | Sends IGES-specific data to the geometric modeler. |
| Method | [SetMaterialIdName](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~SetMaterialIdName.md) | Obsolete. Superseded by [IBody2::SetMaterialIdName2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~SetMaterialIdName2.md). |
| Method | [SetMaterialIdName2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~SetMaterialIdName2.md) | Sets the material name for this body. |
| Method | [SetMaterialProperty](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~SetMaterialProperty.md) | Sets the material for this body. |
| Method | [SetMaterialUserName](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~SetMaterialUserName.md) | Obsolete. Superseded by [IBody2::SetMaterialUserName2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~SetMaterialUserName2.md). |
| Method | [SetMaterialUserName2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~SetMaterialUserName2.md) | Sets the material name for this body. This material name is visible to the user. |
| Method | [SetTexture](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~SetTexture.md) | Applies texture to this body in the specified configuration. |
| Method | [SetTextureByDisplayState](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~SetTextureByDisplayState.md) | Sets the texture applied to this body in the specified display state. |
| Method | [SetTrackingID](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~SetTrackingID.md) | Assigns a tracking ID to this body. |
| Method | [SetXform](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~SetXform.md) | Obsolete. Superseded by [IBody2::ApplyTransform](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~ApplyTransform.md). |

[Top](#top)

See Also

#### Reference

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)  
[IEnumBodies2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumBodies2.md)
