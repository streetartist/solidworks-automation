# IModeler Interface Members

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler_members`

Provides an interface to temporary body objects.
The following tables list the members exposed by [IModeler](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler.md).

Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | [GeneralTopology](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~GeneralTopology.md) | Gets or sets the Parasolid option to create general (non-manifold) bodies. |

[Top](#top)

Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | [CheckInterference](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CheckInterference.md) | Obsolete. Superseded by [IModeler::CheckInterference3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CheckInterference3.md). |
| Method | [CheckInterference3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CheckInterference3.md) | Checks for interferences among the specified bodies in a part. |
| Method | [CheckInterferenceBetweenTwoBodies](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CheckInterferenceBetweenTwoBodies.md) | Checks for interference between the specified bodies in an assembly. |
| Method | [CopyWizardHole](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CopyWizardHole.md) | Copies hole data from the source hole to the destination hole. |
| Method | [CreateArc](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateArc.md) | Creates an arc. |
| Method | [CreateBodiesFromSheets](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateBodiesFromSheets.md) | Obsolete. Superseded by [IModeler::CreateBodiesFromSheets2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateBodiesFromSheets2.md). |
| Method | [CreateBodiesFromSheets2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateBodiesFromSheets2.md) | Sews sheets to make sheet (surface) or solid bodies. |
| Method | [CreateBodyFromBox](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateBodyFromBox.md) | Obsolete. Superseded by [IModeler::CreateBodyFromBox3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateBodyFromBox3.md). |
| Method | [CreateBodyFromBox3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateBodyFromBox3.md) | Creates a temporary body from the specified box dimensions. |
| Method | [CreateBodyFromCone](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateBodyFromCone.md) | Creates a temporary body from cone dimensions. |
| Method | [CreateBodyFromCyl](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateBodyFromCyl.md) | Creates a temporary body from cylinder dimensions. |
| Method | [CreateBodyFromFaces2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateBodyFromFaces2.md) | Creates a temporary body from a list of faces. |
| Method | [CreateBrepBody](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateBrepBody.md) | Obsolete. Superseded by [IModeler::CreateBrepBody3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateBrepBody3.md). |
| Method | [CreateBrepBody3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateBrepBody3.md) | Creates a temporary body from BREP (boundary representation) data. |
| Method | [CreateBsplineCurve](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateBsplineCurve.md) | Creates a b-spline curve. |
| Method | [CreateBsplineSurface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateBsplineSurface.md) | Creates a b-spline surface. |
| Method | [CreateConicalSurface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateConicalSurface.md) | Obsolete. Superseded by [IModeler::CreateConicalSurface2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateConicalSurface2.md). |
| Method | [CreateConicalSurface2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateConicalSurface2.md) | Creates an untrimmed conical surface. |
| Method | [CreateCoonsBSurface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateCoonsBSurface.md) | Creates a coons b-surface using the four specified boundary curves. |
| Method | [CreateCylindricalSurface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateCylindricalSurface.md) | Obsolete. Superseded by [IModeler::CreateCylindricalSurface2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateCylindricalSurface2.md). |
| Method | [CreateCylindricalSurface2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateCylindricalSurface2.md) | Creates an untrimmed cylindrical surface. |
| Method | [CreateEllipse](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateEllipse.md) | Creates a temporary elliptical curve. |
| Method | [CreateExtrudedBody](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateExtrudedBody.md) | Creates a temporary extruded body. |
| Method | [CreateExtrusionSurface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateExtrusionSurface.md) | Creates an extruded surface. |
| Method | [CreateLine](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateLine.md) | Creates a line. |
| Method | [CreateLoftBody](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateLoftBody.md) | Obsolete. Superseded by [IModeler::CreateLoftBody2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateLoftBody2.md). |
| Method | [CreateLoftBody2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateLoftBody2.md) | Creates a loft body using the specified profiles, guide curves, and centerline. |
| Method | [CreateLoftSurface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateLoftSurface.md) | Creates a loft surface. |
| Method | [CreateOffsetSurface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateOffsetSurface.md) | Creates a surface that is offset from an existing surface. |
| Method | [CreatePCurve](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreatePCurve.md) | Creates a pcurve. |
| Method | [CreatePlanarSurface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreatePlanarSurface.md) | Obsolete. Superseded by [IModeler::CreatePlanarSurface2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreatePlanarSurface2.md). |
| Method | [CreatePlanarSurface2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreatePlanarSurface2.md) | Creates a new infinite planar surface. |
| Method | [CreateRuledSurface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateRuledSurface.md) | Creates a ruled surface from the curves. |
| Method | [CreateRuledSurfaceFromEdge](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateRuledSurfaceFromEdge.md) | Creates a ruled surface using the specified edges and returns a surface body. |
| Method | [CreateSheetFromFaces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateSheetFromFaces.md) | Creates a sheet (surface) body from connected faces. |
| Method | [CreateSheetFromSurface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateSheetFromSurface.md) | Creates a sheet (surface) body from a surface. |
| Method | [CreateSphericalSurface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateSphericalSurface.md) | Obsolete. Superseded by [IModeler::CreateSphericalSurface2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateSphericalSurface2.md). |
| Method | [CreateSphericalSurface2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateSphericalSurface2.md) | Creates an untrimmed spherical surface. |
| Method | [CreateSpring](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateSpring.md) | Creates the geometry for a spring. |
| Method | [CreateSweptBody](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateSweptBody.md) | Creates a swept body. |
| Method | [CreateSweptSurface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateSweptSurface.md) | Creates a swept surface from a curve. |
| Method | [CreateToroidalSurface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateToroidalSurface.md) | Creates an untrimmed toroidal surface from the specified arguments. |
| Method | [CreateWireBody](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateWireBody.md) | Creates a wire body from the input entities, which can be edges or curves. |
| Method | [DeleteFacesFromSheetBody](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~DeleteFacesFromSheetBody.md) | Deletes the unused faces of the sheet body. |
| Method | [FindTwoEdgeMaxDeviation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~FindTwoEdgeMaxDeviation.md) | Finds the maximum distance between two edges. |
| Method | [GetBodyOutline](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~GetBodyOutline.md) | Obsolete. Superseded by [IModeler::GetBodyOutline2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~GetBodyOutline2.md). |
| Method | [GetBodyOutline2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~GetBodyOutline2.md) | Gets the curves that form the outline of a body. |
| Method | [GetInitKnitGapWidth](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~GetInitKnitGapWidth.md) | Gets the initial gap bound width for knitting a body. |
| Method | [GetManifoldBodiesCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~GetManifoldBodiesCount.md) | Gets the number of manifold bodies created from the specified non-manifold body. |
| Method | [GetToleranceValue](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~GetToleranceValue.md) | Gets the current tolerance value of the given tolerance ID. |
| Method | [ICheckInterference](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICheckInterference.md) | Obsolete. Superseded by [IModeler::ICheckInterference2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICheckInterference2.md). |
| Method | [ICheckInterference2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICheckInterference2.md) | Obsolete. Superseded by [IModeler::ICheckInterference3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICheckInterference3.md). |
| Method | [ICheckInterference3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICheckInterference3.md) | Checks the interference among the specified bodies. |
| Method | [ICheckInterferenceCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICheckInterferenceCount.md) | Obsolete. Superseded by [IModeler::ICheckInterferenceCount2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICheckInterferenceCount2.md). |
| Method | [ICheckInterferenceCount2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICheckInterferenceCount2.md) | Obsolete. Superseded by [IModeler::ICheckInterferenceCount3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICheckInterferenceCount3.md). |
| Method | [ICheckInterferenceCount3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICheckInterferenceCount3.md) | Checks interference among the specified bodies and returns the number of interferences. |
| Method | [ICopyWizardHole](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICopyWizardHole.md) | Copies hole data from the source hole to the destination hole. |
| Method | [ICreateArc](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateArc.md) | Creates an arc. |
| Method | [ICreateBodiesFromSheets](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateBodiesFromSheets.md) | Obsolete. Superseded by [IModeler::ICreateBodiesFromSheets2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateBodiesFromSheets2.md). |
| Method | [ICreateBodiesFromSheets2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateBodiesFromSheets2.md) | Sews sheets to make a sheet (surface) or solid bodies. |
| Method | [ICreateBodyFromBox](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateBodyFromBox.md) | Obsolete. Superseded by [IModeler::ICreateBodyFromBox2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateBodyFromBox2.md). |
| Method | [ICreateBodyFromBox2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateBodyFromBox2.md) | Obsolete. Superseded by [IModeler::CreateBodyFromBox3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateBodyFromBox3.md). |
| Method | [ICreateBodyFromCone](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateBodyFromCone.md) | Obsolete. Superseded by [IModeler::ICreateBodyFromCone2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateBodyFromCone2.md). |
| Method | [ICreateBodyFromCone2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateBodyFromCone2.md) | Creates a temporary body from cone dimensions. |
| Method | [ICreateBodyFromCyl](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateBodyFromCyl.md) | Obsolete. Superseded by [IModeler::ICreateBodyFromCyl2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateBodyFromCyl2.md). |
| Method | [ICreateBodyFromCyl2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateBodyFromCyl2.md) | Creates a temporary body from cylinder dimensions. |
| Method | [ICreateBodyFromFaces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateBodyFromFaces.md) | Obsolete. Superseded by [IModeler::ICreateBodyFromFace3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateBodyFromFaces3.md). |
| Method | [ICreateBodyFromFaces2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateBodyFromFaces2.md) | Obsolete. Superseded by [IModeler::ICreateBodyFromFace3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateBodyFromFaces3.md). |
| Method | [ICreateBodyFromFaces3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateBodyFromFaces3.md) | Creates a temporary body from a list of faces. |
| Method | [ICreateBrepBody](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateBrepBody.md) | Obsolete. Superseded by [IModeler::ICreateBrepBody3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateBrepBody3.md). |
| Method | [ICreateBrepBody2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateBrepBody2.md) | Obsolete. Superseded by [IModeler::ICreateBrepBody3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateBrepBody3.md). |
| Method | [ICreateBrepBody3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateBrepBody3.md) | Creates a temporary body from BREP (boundary representation) data. |
| Method | [ICreateBsplineCurve](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateBsplineCurve.md) | Creates a b-spline curve. |
| Method | [ICreateBsplineSurface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateBsplineSurface.md) | Creates a b-spline surface. |
| Method | [ICreateConicalSurface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateConicalSurface.md) | Obsolete. Superseded by [IModeler::ICreateConicalSurface2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateCylindricalSurface2.md). |
| Method | [ICreateConicalSurface2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateConicalSurface2.md) | Creates an untrimmed conical surface. |
| Method | [ICreateCylindricalSurface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateCylindricalSurface.md) | Obsolete. Superseded by [IModeler::ICreateCylindricalSurface2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateCylindricalSurface2.md). |
| Method | [ICreateCylindricalSurface2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateCylindricalSurface2.md) | Creates an untrimmed cylindrical surface. |
| Method | [ICreateEllipse](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateEllipse.md) | Creates a temporary elliptical curve. |
| Method | [ICreateExtrusionSurface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateExtrusionSurface.md) | Creates an extruded surface. |
| Method | [ICreateLine](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateLine.md) | Creates a line. |
| Method | [ICreateLoftSurface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateLoftSurface.md) | Creates a loft surface. |
| Method | [ICreateOffsetSurface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateOffsetSurface.md) | Creates a surface that is offset from an existing surface. |
| Method | [ICreatePCurve](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreatePCurve.md) | Creates a pcurve. |
| Method | [ICreatePlanarSurface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreatePlanarSurface.md) | Obsolete. Superseded by [IModeler::ICreatePlanarSurface2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreatePlanarSurface2.md). |
| Method | [ICreatePlanarSurface2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreatePlanarSurface2.md) | Creates a new infinite planar surface. |
| Method | [ICreateRuledSurface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateRuledSurface.md) | Creates a ruled surface from the curves. |
| Method | [ICreateRuledSurfaceFromEdge](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateRuledSurfaceFromEdge.md) | Creates a ruled surface using the specified edges and returns a surface body. |
| Method | [ICreateSheetFromFaces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateSheetFromFaces.md) | Creates a sheet (surface) body from connected faces. |
| Method | [ICreateSheetFromSurface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateSheetFromSurface.md) | Obsolete. Superseded by [IModeler::ICreateSheetFromSurface2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateSheetFromSurface2.md). |
| Method | [ICreateSheetFromSurface2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateSheetFromSurface2.md) | Creates a sheet (surface) body from a surface. |
| Method | [ICreateSphericalSurface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateSphericalSurface.md) | Obsolete. Superseded by [IModeler::ICreateSphericalSurface2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateSphericalSurface2.md). |
| Method | [ICreateSphericalSurface2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateSphericalSurface2.md) | Creates an untrimmed spherical surface. |
| Method | [ICreateSweptSurface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateSweptSurface.md) | Creates a swept surface from a curve. |
| Method | [ICreateToroidalSurface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateToroidalSurface.md) | Creates an untrimmed toroidal surface from the specified arguments. |
| Method | [ICreateWireBody](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateWireBody.md) | Creates a wire body from the input entities, which can be edges or curves. |
| Method | [IDeleteFacesFromSheetBody](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~IDeleteFacesFromSheetBody.md) | Deletes the unused faces of the sheet body. |
| Method | [IFindTwoEdgeMaxDeviation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~IFindTwoEdgeMaxDeviation.md) | Finds the maximum distance between two edges. |
| Method | [IImprintingFaces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~IImprintingFaces.md) | Imprints the specified tool faces onto the specified target faces. |
| Method | [IImprintingFacesCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~IImprintingFacesCount.md) | Obsolete. Superseded by [IModeler::IImprintingFacesCount2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~IImprintingFacesCount2.md). |
| Method | [IImprintingFacesCount2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~IImprintingFacesCount2.md) | Gets the number of imprinted edges and vertices in the model. |
| Method | [IMakeManifoldBodies](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~IMakeManifoldBodies.md) | Creates manifold bodies from the specified non-manifold body. |
| Method | [IMergeCurves](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~IMergeCurves.md) | Merges multiple curves into one curve. |
| Method | [ImprintingFaces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ImprintingFaces.md) | Imprints the specified tool faces onto the specified target faces. |
| Method | [IReplaceSurfaces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~IReplaceSurfaces.md) | Obsolete. Superseded by [IModeler::IReplaceSurfaces2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~IReplaceSurfaces2.md). |
| Method | [IReplaceSurfaces2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~IReplaceSurfaces2.md) | Replaces the surfaces of the given faces. |
| Method | [IRestore](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~IRestore.md) | Obsolete. Superseded by [IModeler::IRestore2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~IRestore2.md). |
| Method | [IRestore2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~IRestore2.md) | Restores a temporary body object from the specified stream. |
| Method | [ISplitFaceOnParam](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ISplitFaceOnParam.md) | Obsolete. Superseded by [IModeler::ISplitFaceOnParam2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ISplitFaceOnParam2.md). |
| Method | [ISplitFaceOnParam2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ISplitFaceOnParam2.md) | Splits and retrieves the faces on the U or V parameter. |
| Method | [ISplitFaceOnParamCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ISplitFaceOnParamCount.md) | Obsolete. Superseded by [IModeler::ISplitFaceOnParamCount2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ISplitFaceOnParamCount2.md). |
| Method | [ISplitFaceOnParamCount2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ISplitFaceOnParamCount2.md) | Sets up and counts the number of new faces split on the U or V parameter. |
| Method | [MakeManifoldBodies](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~MakeManifoldBodies.md) | Creates manifold bodies from the specified non-manifold body. |
| Method | [MergeCurves](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~MergeCurves.md) | Merges multiple curves into one curve. |
| Method | [ProjectCurveOnSurface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ProjectCurveOnSurface.md) | Projects a curve on a surface. |
| Method | [ReplaceSurfaces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ReplaceSurfaces.md) | Replaces the surfaces of the given faces. |
| Method | [Restore](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~Restore.md) | Restores a temporary body object from the specified stream. |
| Method | [SetInitKnitGapWidth](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~SetInitKnitGapWidth.md) | Sets the initial gap bound width for sewing a body. Call this method before calling any calls that attempt to knit a body; for example, [IBody2::CreateBodyFromSurfaces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~CreateBodyFromSurfaces.md). |
| Method | [SetTolerances](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~SetTolerances.md) | Obsolete. Superseded by [IModeler::GetToleranceValue](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~GetToleranceValue.md) and [IModeler::SetToleranceValue](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~SetToleranceValue.md). |
| Method | [SetToleranceValue](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~SetToleranceValue.md) | Sets tolerances governing geometry output. |
| Method | [SplitFaceOnParam](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~SplitFaceOnParam.md) | Splits and retrieves the faces on the U or V parameter |
| Method | [ThickenSheet](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ThickenSheet.md) | Thickens a sheet body. |
| Method | [UnsetTolerances](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~UnsetTolerances.md) | Sets the tolerances back to system settings. |

[Top](#top)

 

See Also

#### Reference

[IModeler Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
