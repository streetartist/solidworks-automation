# ICreatePlaneFixed2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ICreatePlaneFixed2`

Obsolete. Superseded by IFeatureManager::InsertRefPlane.
Obsolete. Superseded by [IFeatureManager::InsertRefPlane](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertRefPlane.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ICreatePlaneFixed2( _
   ByRef P1 As System.Double, _
   ByRef P2 As System.Double, _
   ByRef P3 As System.Double, _
   ByVal UseGlobal As System.Boolean _
) As RefPlane
```

```

Dim instance As IModelDoc2
Dim P1 As System.Double
Dim P2 As System.Double
Dim P3 As System.Double
Dim UseGlobal As System.Boolean
Dim value As RefPlane
 
value = instance.ICreatePlaneFixed2(P1, P2, P3, UseGlobal)
```

```

RefPlane ICreatePlaneFixed2( 
   ref System.double P1,
   ref System.double P2,
   ref System.double P3,
   System.bool UseGlobal
)
```

```

RefPlane^ ICreatePlaneFixed2( 
   System.double% P1,
   System.double% P2,
   System.double% P3,
   System.bool UseGlobal
) 
```

#### Parameters

*P1*
:   Array of 3 doubles (x, y, z) in meters; this is the first of three model-space points used to define the plane orientation; it is also used as the origin for the plane coordinate system

*P2*
:   :   Array of 3 doubles (x, y, z) in meters; this is the second of three model-space points used to define the plane orientation; the planes X-axis is directed from P1 to P2 unless useGlobal is set to True

*P3*
:   :   Array of 3 doubles (x, y, z) in meters; this is the final model-space point used to define the plane orientation

*UseGlobal*
:   Controls x-axis orientation (see **Remarks**)

#### Return Value

Newly created [reference plane](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlane.md) or NULL if the creation of the plan fails

Remarks

The resulting plane is not parametric.

The planes normal vector is calculated using the cross product of the vectors (P2 - P1) and (P3 - P1), respectively.

The x-axis of the planes' coordinate system are a vector from P1 to P2 or a vector projected from the x-axis of the global coordinate system onto the plane.

The useGlobal argument denotes whether to align the x-axis of the plane with global orientation.

|  |  |
| --- | --- |
| **If useGlobal...** | **Then x-axis of the...** |
| True | global (model) coordinate system is projected onto the plane. That vector is used to determine the direction of the plane's x-axis. This does not reorient the plane. Instead, it rotates the plane coordinate system about P1 until the x-axis of the plane aligns with the projected vector.  P1, P2, and P3 are still required because they define the plane. |
| false | plane is aligned based on your input points, P1 and P2. |

This method creates the plane in the model that is currently being edited. This behavior is consistent with the other plane creation APIs, but it is different from the original IModelDoc2::ICreatePlaneFixed, which created the plane in this model, regardless of whether a component was currently being edited.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)  
[IModelDoc2::CreatePlaneAtAngle3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~CreatePlaneAtAngle3.md)  
[IModelDoc2::CreatePlaneAtOffset3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~CreatePlaneAtOffset3.md)  
[IModelDoc2::CreatePlaneAtSurface3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~CreatePlaneAtSurface3.md)  
[IModelDoc2::CreatePlaneFixed2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~CreatePlaneFixed2.md)  
[IModelDoc2::CreatePlaneThru3Points3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~CreatePlaneThru3Points3.md)  
[IModelDoc2::CreatePlaneThruLineAndPt Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~CreatePlaneThruLineAndPt.md)  
[IModelDoc2::CreatePlaneThruPtParallelToPlane Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~CreatePlaneThruPtParallelToPlane.md)  
[IModelDoc2::GetVisibilityOfConstructPlanes Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetVisibilityOfConstructPlanes.md)  
[IModelDoc2::ICreatePlaneAtAngle3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ICreatePlaneAtAngle3.md)  
[IModelDoc2::ICreatePlaneAtOffset3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ICreatePlaneAtOffset3.md)  
[IModelDoc2::ICreatePlaneAtSurface3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ICreatePlaneAtSurface3.md)  
[IModelDoc2::ICreatePlanePerCurveAndPassPoint3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ICreatePlanePerCurveAndPassPoint3.md)  
[IModelDoc2::ICreatePlaneThru3Points3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ICreatePlaneThru3Points3.md)  
[IModelDoc2::ICreatePlaneThruLineAndPt Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ICreatePlaneThruLineAndPt.md)  
[IModelDoc2::ICreatePlaneThruPtParallelToPlane Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ICreatePlaneThruPtParallelToPlane.md)  
[IModelDoc2::ViewDispRefplanes Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ViewDispRefplanes.md)
