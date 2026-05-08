# RayIntersections Method (IModelDocExtension)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~RayIntersections`

Finds the intersections between the specified set of rays and the specified set of bodies.
Finds the intersections between the specified set of rays and the specified set of bodies.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function RayIntersections( _
   ByVal BodiesIn As System.Object, _
   ByVal BasePointsIn As System.Object, _
   ByVal VectorsIn As System.Object, _
   ByVal Options As System.Integer, _
   ByVal HitRadius As System.Double, _
   ByVal Offset As System.Double, _
   ByVal HighPrecision As System.Boolean _
) As System.Integer
```

```

Dim instance As IModelDocExtension
Dim BodiesIn As System.Object
Dim BasePointsIn As System.Object
Dim VectorsIn As System.Object
Dim Options As System.Integer
Dim HitRadius As System.Double
Dim Offset As System.Double
Dim HighPrecision As System.Boolean
Dim value As System.Integer
 
value = instance.RayIntersections(BodiesIn, BasePointsIn, VectorsIn, Options, HitRadius, Offset, HighPrecision)
```

```

System.int RayIntersections( 
   System.object BodiesIn,
   System.object BasePointsIn,
   System.object VectorsIn,
   System.int Options,
   System.double HitRadius,
   System.double Offset,
   System.bool HighPrecision
)
```

```

System.int RayIntersections( 
   System.Object^ BodiesIn,
   System.Object^ BasePointsIn,
   System.Object^ VectorsIn,
   System.int Options,
   System.double HitRadius,
   System.double Offset,
   System.bool HighPrecision
) 
```

#### Parameters

*BodiesIn*
:   Array of [bodies](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md) that are hit by the rays (see **Remarks**)

*BasePointsIn*
:   Array of doubles containing the x,y,z base points of each ray

*VectorsIn*
:   Array of doubles containing the direction vectors of each ray

*Options*
:   Options as defined in [swRayPtsOpts\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swRayPtsOpts_e.html) (see **Remarks**)

*HitRadius*
:   Radius of hit cylinder; this is used mainly in grazing cases to establish a hit (see **Remarks**)

*Offset*
:   Length tolerance to use to establish whether a hit on a face represents the entry or exit of the ray from the body (see Remarks)

*HighPrecision*
:   True to use maximum precision when evaluating intersections close to the ray boundary, false to use dynamic precision based on the ray radius (see **Remarks**)

#### Return Value

Number of intersections

Remarks

The method performs intersection operations between the specified bodies and the specified ray vectors. To get the results (a set of intersection points, intersection normals, and the bodies from your BodiesIn array that were hit), you must call [IModelDoc2::GetRayIntersectionsPoints](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetRayIntersectionsPoints.md) and [IModelDoc2::GetRayIntersectionTopology](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetRayIntersectionsTopology.md).

Information returned by IModelDoc2::GetRayIntersectionsPoints and IModelDoc2::GetRayIntersectionTopology depends partially on the value of the Options parameter. Valid Option values can be combined using bitwise operations. See IModelDoc2::GetRayIntersectionsPoints to determine which data is always output regardless of the values specified by Options.

For each ray that hits an edge or a vertex, the Offset value is added in both the positive and negative directions along the ray, and the points computed are tested for spatial inclusion in the hit body. This determines whether the ray was entering, leaving, or just grazing the body at the hit point. Entry and exit for faces can be computed and does not require an offset.

The difference between this method and the now obsolete IModelDoc2::RayIntersections and IModelDoc2::IRayIntersections is the HighPrecision parameter. Setting HighPrecision to true forces use of the highest possible precision when evaluating intersections close to ray profile boundaries. Setting HighPrecision to false forces use of a dynamic tolerance that is based on the HitRadius, which is the behavior of the obsolete methods.

The actual ray profile is polygonal, approximating an ideal circular ray profile of HitRadius. Evaluating intersections very close to the ray profile boundary may produce unexpected results due to this polygonal approximation. Experimentation with HighPrecision is recommended.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)  
[IModelDoc2::MultiSelectByRay Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~MultiSelectByRay.md)  
[IModelDoc2::SelectByRay Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SelectByRay.md)
