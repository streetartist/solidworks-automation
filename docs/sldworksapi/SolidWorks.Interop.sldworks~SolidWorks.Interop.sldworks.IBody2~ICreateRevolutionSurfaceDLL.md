# ICreateRevolutionSurfaceDLL Method (IBody2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~ICreateRevolutionSurfaceDLL`

Creates a surface of revolution for this body.
Creates a surface of revolution for this body.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ICreateRevolutionSurfaceDLL( _
   ByVal ProfileCurve As Curve, _
   ByRef AxisPoint As System.Double, _
   ByRef AxisDirection As System.Double, _
   ByRef ProfileEndPtParams As System.Double _
) As Surface
```

```

Dim instance As IBody2
Dim ProfileCurve As Curve
Dim AxisPoint As System.Double
Dim AxisDirection As System.Double
Dim ProfileEndPtParams As System.Double
Dim value As Surface
 
value = instance.ICreateRevolutionSurfaceDLL(ProfileCurve, AxisPoint, AxisDirection, ProfileEndPtParams)
```

```

Surface ICreateRevolutionSurfaceDLL( 
   Curve ProfileCurve,
   ref System.double AxisPoint,
   ref System.double AxisDirection,
   ref System.double ProfileEndPtParams
)
```

```

Surface^ ICreateRevolutionSurfaceDLL( 
   Curve^ ProfileCurve,
   System.double% AxisPoint,
   System.double% AxisDirection,
   System.double% ProfileEndPtParams
) 
```

#### Parameters

*ProfileCurve*
:   Pointer to a profile [curve](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve.md) object

*AxisPoint*
:   Array of 3 doubles (x,y,z)

*AxisDirection*
:   Array of 3 doubles (x,y,z)

*ProfileEndPtParams*
:   Array of 2 doubles (uStart,uEnd)

#### Return Value

Pointer to a new [surface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.md) of revolution

Remarks

Any existing object created by this method is destroyed if you call this method again.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md)  
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.md)
