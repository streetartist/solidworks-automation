# CreateExtrusionSurface Method (IBody2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~CreateExtrusionSurface`

Creates a new surface of extrusion (infinitely long tabulated cylinder).
Creates a new surface of extrusion (infinitely long tabulated cylinder).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function CreateExtrusionSurface( _
   ByVal ProfileCurve As System.Object, _
   ByVal AxisDirection As System.Object _
) As System.Object
```

```

Dim instance As IBody2
Dim ProfileCurve As System.Object
Dim AxisDirection As System.Object
Dim value As System.Object
 
value = instance.CreateExtrusionSurface(ProfileCurve, AxisDirection)
```

```

System.object CreateExtrusionSurface( 
   System.object ProfileCurve,
   System.object AxisDirection
)
```

```

System.Object^ CreateExtrusionSurface( 
   System.Object^ ProfileCurve,
   System.Object^ AxisDirection
) 
```

#### Parameters

*ProfileCurve*
:   Profile curve

*AxisDirection*
:   Array of 3 doubles (x,y,z)

#### Return Value

New surface of extrusion (tabulated cylinder)

Remarks

You can use this method with:

- A set of related functions that construct a body from trimmed surfaces. The profile curve is extruded along the direction vector of axis direction, the new surface being the envelope of the curve. The profile curve must be of type line, circle, or B-spline curve.
- Trimming curve creation routines (for example [ISurface::AddTrimmingLoop2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~AddTrimmingLoop2.md)) to construct a trimmed tabulated cylinder.

Any existing object created by this method is destroyed if you call this method again.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md)  
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.md)  
[IBody2::ICreateExtrusionSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~ICreateExtrusionSurface.md)
