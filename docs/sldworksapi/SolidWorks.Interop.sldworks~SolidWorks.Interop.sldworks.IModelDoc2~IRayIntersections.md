# IRayIntersections Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IRayIntersections`

Obsolete. Superseded by IModelDocExtension::RayIntersections.
Obsolete. Superseded by [IModelDocExtension::RayIntersections](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~RayIntersections.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IRayIntersections( _
   ByRef BodiesIn As Body2, _
   ByVal NumBodies As System.Integer, _
   ByRef BasePointsIn As System.Double, _
   ByRef VectorsIn As System.Double, _
   ByVal NumRays As System.Integer, _
   ByVal Options As System.Integer, _
   ByVal HitRadius As System.Double, _
   ByVal Offset As System.Double _
) As System.Integer
```

```

Dim instance As IModelDoc2
Dim BodiesIn As Body2
Dim NumBodies As System.Integer
Dim BasePointsIn As System.Double
Dim VectorsIn As System.Double
Dim NumRays As System.Integer
Dim Options As System.Integer
Dim HitRadius As System.Double
Dim Offset As System.Double
Dim value As System.Integer
 
value = instance.IRayIntersections(BodiesIn, NumBodies, BasePointsIn, VectorsIn, NumRays, Options, HitRadius, Offset)
```

```

System.int IRayIntersections( 
   ref Body2 BodiesIn,
   System.int NumBodies,
   ref System.double BasePointsIn,
   ref System.double VectorsIn,
   System.int NumRays,
   System.int Options,
   System.double HitRadius,
   System.double Offset
)
```

```

System.int IRayIntersections( 
   Body2^% BodiesIn,
   System.int NumBodies,
   System.double% BasePointsIn,
   System.double% VectorsIn,
   System.int NumRays,
   System.int Options,
   System.double HitRadius,
   System.double Offset
) 
```

#### Parameters

*BodiesIn*
:   Array [bodies](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md) that are hit by the rays (see **Remarks**)

*NumBodies*
:   Number of bodies in the BodiesIn array

*BasePointsIn*
:   Array containing the x,y,z base points of each ray

*VectorsIn*
:   Array containing the direction vectors of each ray

*NumRays*
:   Number of rays specified; this should be equal to the number of elements in the (basePointsIn / 3) or (vectorsIn / 3) arrays

*Options*
:   Number of options as defined in [swRayPtsOpts\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swRayPtsOpts_e.html)

*HitRadius*
:   Radius of hit cylinder used mainly in grazing cases to establish a hit

*Offset*
:   Length tolerance to use to establish whether a hit on a face represents the entry or exit of the ray from the body (see Remarks)

#### Return Value

Number of intersections found

Remarks

The method performs the intersection operations between the specified bodies and the ray vectors. To get the results (a set of intersection points, intersection normals, and the bodies that were hit from your bodiesIn array) of the intersection operations, you must call [IModelDoc2::GetRayIntersectionsPoints](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetRayIntersectionsPoints.md) or [IModelDoc2::IGetRayIntersectionPoints](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IGetRayIntersectionsPoints.md) and [IModelDoc2::GetRayIntersectionTopology](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetRayIntersectionsTopology.md) or [IModelDoc2::IGetRayIntersectionsTopology](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IGetRayIntersectionsTopology.md).

Information returned by IModelDoc2::GetRayIntersectionsPoints, IModelDoc2::IGetRayIntersectionPoints, IModelDoc2::GetRayIntersectionTopology, and IModelDoc2::IGetRayIntersectionsTopology depends partially on the value of the options argument. Valid values can be concatenated together using bitwise operations. See IModelDoc2::GetRayIntersectionsPoints or IModelDoc2::IGetRayIntersectionPoints to see which data is always output regardless of the values specified in the options argument.

For the COM interface, the return value, the intersection count, must be used in determining the size of arrays to allocate for return values from IModelDoc2::IGetRayIntersectionsPoints and IModelDoc2::IGetRayIntersectionsTopology.

For each ray that hits an edge or a vertex, the offset distance is added in both the positive and negative directions along the ray and the points computed are tested for spatial inclusion in the hit body. This determines if the ray was entering, leaving, or just grazing the body at the hit point. Entry and exit onto faces can be computed does not require such an offset.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)  
[IModelDoc2::IMultiSelectByRay Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IMultiSelectByRay.md)  
[IModelDoc2::ISelectByRay Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ISelectByRay.md)  
[IModelDoc2::MultiSelectByRay Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~MultiSelectByRay.md)  
[IModelDoc2::RayIntersections Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~RayIntersections.md)  
[IModelDoc2::SelectByRay Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SelectByRay.md)
