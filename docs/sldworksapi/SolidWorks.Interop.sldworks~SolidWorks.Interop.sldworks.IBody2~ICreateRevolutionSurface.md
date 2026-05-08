# ICreateRevolutionSurface Method (IBody2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~ICreateRevolutionSurface`

Creates a new surface of revolution.
Creates a new surface of revolution.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ICreateRevolutionSurface( _
   ByVal ProfileCurve As Curve, _
   ByVal AxisPoint As System.Object, _
   ByVal AxisDirection As System.Object, _
   ByVal ProfileEndPtParams As System.Object _
) As Surface
```

```

Dim instance As IBody2
Dim ProfileCurve As Curve
Dim AxisPoint As System.Object
Dim AxisDirection As System.Object
Dim ProfileEndPtParams As System.Object
Dim value As Surface
 
value = instance.ICreateRevolutionSurface(ProfileCurve, AxisPoint, AxisDirection, ProfileEndPtParams)
```

```

Surface ICreateRevolutionSurface( 
   Curve ProfileCurve,
   System.object AxisPoint,
   System.object AxisDirection,
   System.object ProfileEndPtParams
)
```

```

Surface^ ICreateRevolutionSurface( 
   Curve^ ProfileCurve,
   System.Object^ AxisPoint,
   System.Object^ AxisDirection,
   System.Object^ ProfileEndPtParams
) 
```

#### Parameters

*ProfileCurve*
:   Profile curve (generatrix)

*AxisPoint*
:   Array of 3 doubles (x,y,z)

*AxisDirection*
:   Array of 3 doubles (x,y,z)

*ProfileEndPtParams*
:   Array of 2 doubles (uStart,uEnd) (see **Remarks**)

#### Return Value

Pointer to a new [surface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.md) of revolution

Remarks

You can use this method with:

- A set of related functions that construct a body from trimmed surfaces.
- Trimming curve creation routines (for example, [ISurface::IAddTrimmingLoop2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IAddTrimmingLoop2.md)) to construct a trimmed surface of revolution.

If you pass ProfileEndPtParams to this method, the surface is trimmed in the axial direction; otherwise, it is infinite. SOLIDWORKS closes the surface periodic ( period [0,2PI]) in the direction of revolution. The ProfileEndPtParams parameters indicate to SOLIDWORKS which part of the curve to spin. These parameters are used only when the profile curve intersects the revolve axis. You must pass the parameters in ascending order. SOLIDWORKS extends the curve from the given parameter range to meet the revolve axis and spins this portion of curve.

You can also pass an empty VARIANT object to ProfileEndPtParams; it cannot be NULL. You must define a variable of type VARIANT.

Any existing object created by this method is destroyed if you call this method again.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md)  
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.md)  
[IBody2::CreateRevolutionSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~CreateRevolutionSurface.md)
