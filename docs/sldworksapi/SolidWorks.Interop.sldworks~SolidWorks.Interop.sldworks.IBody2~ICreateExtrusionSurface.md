# ICreateExtrusionSurface Method (IBody2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~ICreateExtrusionSurface`

Creates a new surface of extrusion (infinitely long tabulated cylinder).
Creates a new surface of extrusion (infinitely long tabulated cylinder).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ICreateExtrusionSurface( _
   ByVal ProfileCurve As Curve, _
   ByVal AxisDirection As System.Object _
) As Surface
```

```

Dim instance As IBody2
Dim ProfileCurve As Curve
Dim AxisDirection As System.Object
Dim value As Surface
 
value = instance.ICreateExtrusionSurface(ProfileCurve, AxisDirection)
```

```

Surface ICreateExtrusionSurface( 
   Curve ProfileCurve,
   System.object AxisDirection
)
```

```

Surface^ ICreateExtrusionSurface( 
   Curve^ ProfileCurve,
   System.Object^ AxisDirection
) 
```

#### Parameters

*ProfileCurve*
:   [ICurve](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve.md) object

*AxisDirection*
:   Array of 3 doubles (x,y,z)

#### Return Value

[ISurface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.md) object

Remarks

You can use this method with:

- A set of related functions that construct a body from trimmed surfaces. The profile curve is extruded along the direction vector of axis direction, the new surface being the envelope of the curve. The profile curve must be of type line, circle, or B-spline curve.
- Trimming curve creation routines (for example [ISurface::IAddTrimmingLoop2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IAddTrimmingLoop2.md)) to construct a trimmed tabulated cylinder.

Any existing object created by this method is destroyed if you call this method again.

Example

[Create Imported Surface Body from Sketch (C#)](Create_Imported_Surface_Body_from_Sketch_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md)  
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.md)  
[IBody2::CreateExtrusionSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~CreateExtrusionSurface.md)
