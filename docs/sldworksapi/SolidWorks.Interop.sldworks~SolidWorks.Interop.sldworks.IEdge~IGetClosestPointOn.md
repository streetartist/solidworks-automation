# IGetClosestPointOn Method (IEdge)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~IGetClosestPointOn`

Uses the X,Y,Z input point and returns the closest point on the edge.
Uses the X,Y,Z input point and returns the closest point on the edge.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetClosestPointOn( _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Z As System.Double _
) As System.Double
```

```

Dim instance As IEdge
Dim X As System.Double
Dim Y As System.Double
Dim Z As System.Double
Dim value As System.Double
 
value = instance.IGetClosestPointOn(X, Y, Z)
```

```

System.double IGetClosestPointOn( 
   System.double X,
   System.double Y,
   System.double Z
)
```

```

System.double IGetClosestPointOn( 
   System.double X,
   System.double Y,
   System.double Z
) 
```

#### Parameters

*X*
:   X value of the input point

*Y*
:   Y value of the input point

*Z*
:   Z value of the input point

#### Return Value

Pointer to an array of five doubles (see **Remarks**)

Remarks

This method returns only one point, regardless of how many points achieve the minimum distance.

This method returns an array that contains the following values:

> **[** *PointX, PointY, PointZ, UParameter, NotUsed* **]**

where the point values represent the point on the edge, and *UParameter* is the parameter on the edge that is closest to the input point. Ignore the fifth array element.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IEdge Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md)  
[IEdge Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge_members.md)  
[IEdge::GetClosestPointOn Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~GetClosestPointOn.md)  
[ICurve::GetClosestPointOn Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~GetClosestPointOn.md)  
[ICurve::IGetClosestPointOn Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IGetClosestPointOn.md)  
[IFace2::GetClosestPointOn Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetClosestPointOn.md)  
[IFace2::IGetClosestPointOn Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetClosestPointOn.md)  
[ISurface::GetClosestPointOn Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~GetClosestPointOn.md)  
[ISurface::IGetClosestPointOn Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IGetClosestPointOn.md)  
[IVertex::GetClosestPointOn Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex~GetClosestPointOn.md)  
[IVertex::IGetClosestPointOn Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex~IGetClosestPointOn.md)
