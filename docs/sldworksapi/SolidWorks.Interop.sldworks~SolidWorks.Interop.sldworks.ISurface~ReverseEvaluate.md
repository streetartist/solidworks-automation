# ReverseEvaluate Method (ISurface)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~ReverseEvaluate`

Gets the UV parameters at the specified location, which must be on the surface.
Gets the UV parameters at the specified location, which must be on the surface.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ReverseEvaluate( _
   ByVal PositionX As System.Double, _
   ByVal PositionY As System.Double, _
   ByVal PositionZ As System.Double _
) As System.Object
```

```

Dim instance As ISurface
Dim PositionX As System.Double
Dim PositionY As System.Double
Dim PositionZ As System.Double
Dim value As System.Object
 
value = instance.ReverseEvaluate(PositionX, PositionY, PositionZ)
```

```

System.object ReverseEvaluate( 
   System.double PositionX,
   System.double PositionY,
   System.double PositionZ
)
```

```

System.Object^ ReverseEvaluate( 
   System.double PositionX,
   System.double PositionY,
   System.double PositionZ
) 
```

#### Parameters

*PositionX*
:   X position on the surface

*PositionY*
:   Y position on the surface

*PositionZ*
:   Z position on the surface

#### Return Value

Array of doubles describing the UV parameters

Remarks

At parametric singularities, such as sphere poles, the non-degenerate parameter is returned as the lowest value in its range. To determine the UV range, call [ISurface::Parameterization](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~Parameterization.md) or [ISurface::IParameterization](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IParameterization.md).

[IFace2::ReverseEvaluate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~ReverseEvaluate.md) and [IFace2::IReverseEvaluate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IReverseEvaluate.md) return corrected UV parameters for periodic surfaces; thus, you should use either of these methods when dealing with periodic surfaces.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISurface Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.md)  
[ISurface Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface_members.md)  
[ISurface::IReverseEvaluate Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IReverseEvaluate.md)  
[ISurface::Evaluate Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~Evaluate.md)  
[ISurface::EvaluateAtPoint Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~EvaluateAtPoint.md)  
[ISurface::IEvaluate Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IEvaluate.md)  
[ISurface::IEvaluateAtPoint Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IEvaluateAtPoint.md)
