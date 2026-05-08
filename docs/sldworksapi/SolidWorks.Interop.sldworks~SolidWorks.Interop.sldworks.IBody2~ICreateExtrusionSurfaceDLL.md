# ICreateExtrusionSurfaceDLL Method (IBody2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~ICreateExtrusionSurfaceDLL`

Creates an extruded surface.
Creates an extruded surface.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ICreateExtrusionSurfaceDLL( _
   ByVal ProfileCurve As Curve, _
   ByRef AxisDirection As System.Double _
) As Surface
```

```

Dim instance As IBody2
Dim ProfileCurve As Curve
Dim AxisDirection As System.Double
Dim value As Surface
 
value = instance.ICreateExtrusionSurfaceDLL(ProfileCurve, AxisDirection)
```

```

Surface ICreateExtrusionSurfaceDLL( 
   Curve ProfileCurve,
   ref System.double AxisDirection
)
```

```

Surface^ ICreateExtrusionSurfaceDLL( 
   Curve^ ProfileCurve,
   System.double% AxisDirection
) 
```

#### Parameters

*ProfileCurve*
:   Pointer to the profile [curve](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve.md)

*AxisDirection*
:   Array of 3 doubles (x,y,z)

#### Return Value

Pointer to the new [surface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.md) of extrusion (tabulated cylinder)

Remarks

Any existing object created by this method is destroyed if you call this method again.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md)  
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.md)
