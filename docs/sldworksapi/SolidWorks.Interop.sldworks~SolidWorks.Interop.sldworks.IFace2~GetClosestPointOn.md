# GetClosestPointOn Method (IFace2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetClosestPointOn`

Uses the X,Y,Z input point to determine the closest point on the face.
Uses the X,Y,Z input point to determine the closest point on the face.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetClosestPointOn( _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Z As System.Double _
) As System.Object
```

```

Dim instance As IFace2
Dim X As System.Double
Dim Y As System.Double
Dim Z As System.Double
Dim value As System.Object
 
value = instance.GetClosestPointOn(X, Y, Z)
```

```

System.object GetClosestPointOn( 
   System.double X,
   System.double Y,
   System.double Z
)
```

```

System.Object^ GetClosestPointOn( 
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

Array of five doubles representing the X,Y,Z point on the face followed by the U, V parameter on the face that is closest to the input point

Remarks

This method returns only one point, regardless of how many points achieve the minimum distance.

Example

[Calculate Closest Distance Between Faces (VBA)](Calculate_Closest_Distance_Between_Faces_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFace2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md)  
[IFace2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2_members.md)  
[IFace2::IGetClosestPointOn Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetClosestPointOn.md)  
[ICurve::GetClosestPointOn Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~GetClosestPointOn.md)  
[ICurve::IGetClosestPointOn Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IGetClosestPointOn.md)  
[IEdge::GetClosestPointOn Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~GetClosestPointOn.md)  
[IEdge::IGetClosestPointOn Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~IGetClosestPointOn.md)  
[IFace2::GetProjectedPointOn Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetProjectedPointOn.md)  
[ISurface::GetClosestPointOn Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~GetClosestPointOn.md)  
[ISurface::IGetClosestPointOn Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IGetClosestPointOn.md)  
[IVertex::GetClosestPointOn Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex~GetClosestPointOn.md)  
[IVertex::IGetClosestPointOn Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex~IGetClosestPointOn.md)
