# GetProjectedPointOn Method (IFace2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetProjectedPointOn`

Gets the point where the input point is projected on to this face.
Gets the point where the input point is projected on to this face.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetProjectedPointOn( _
   ByVal Point As MathPoint, _
   ByVal Direction As MathVector _
) As MathPoint
```

```

Dim instance As IFace2
Dim Point As MathPoint
Dim Direction As MathVector
Dim value As MathPoint
 
value = instance.GetProjectedPointOn(Point, Direction)
```

```

MathPoint GetProjectedPointOn( 
   MathPoint Point,
   MathVector Direction
)
```

```

MathPoint^ GetProjectedPointOn( 
   MathPoint^ Point,
   MathVector^ Direction
) 
```

#### Parameters

*Point*
:   [Point](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathPoint.md) to project

*Direction*
:   [Direction](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathVector.md) to project the point

#### Return Value

[Point](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathPoint.md) where the input point is projected on to the face

Example

[Get Projected Point (VBA)](Get_Projected_Point_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFace2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md)  
[IFace2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2_members.md)  
[IFace2::GetClosestPointOn Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetClosestPointOn.md)  
[IFace2::IGetClosestPointOn Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetClosestPointOn.md)
