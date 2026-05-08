# IGetBSurfParamsSize3 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IGetBSurfParamsSize3`

Gets the allocation size necessary for Bsurface parameter data retrieval in a subsequent call to ISurface::IGetBSurfParams.
Gets the allocation size necessary for Bsurface parameter data retrieval in a subsequent call to [ISurface::IGetBSurfParams](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IGetBSurfParams.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetBSurfParamsSize3( _
   ByVal WantCubic As System.Boolean, _
   ByVal WantNonRational As System.Boolean, _
   ByRef Range As System.Double, _
   ByVal Tolerance As System.Double, _
   ByRef Sense As System.Boolean _
) As System.Integer
```

```

Dim instance As ISurface
Dim WantCubic As System.Boolean
Dim WantNonRational As System.Boolean
Dim Range As System.Double
Dim Tolerance As System.Double
Dim Sense As System.Boolean
Dim value As System.Integer
 
value = instance.IGetBSurfParamsSize3(WantCubic, WantNonRational, Range, Tolerance, Sense)
```

```

System.int IGetBSurfParamsSize3( 
   System.bool WantCubic,
   System.bool WantNonRational,
   ref System.double Range,
   System.double Tolerance,
   out System.bool Sense
)
```

```

System.int IGetBSurfParamsSize3( 
   System.bool WantCubic,
   System.bool WantNonRational,
   System.double% Range,
   System.double Tolerance,
   [Out] System.bool Sense
) 
```

#### Parameters

*WantCubic*
:   True for surface to be a cubic, false for not

*WantNonRational*
:   True if non-rational is needed, false if not; specifying true converts any surface type to a non-rational Bsurface; if you specify true, then you should only use this method for surfaces that are Bsurface or blend surface; otherwise, the underlying call is not made and the values returned from this are not initialized or contain the values from the last call

*Range*
:   Array of 4 doubles describing the U,V Range

*Tolerance*
:   Tolerance, in meters, between the approximated b-spline surface and the underlying surface; the default value is 0.01 and should generally be reduced to the tolerance desired

*Sense*
:   Approximated b-spline surface is not always in the same direction as the original surface; if sense is true, then the underlying surface and the b-spline surface are in the same direction

#### Return Value

Size of the data set

Remarks

Range contains the following values that can be obtained using [ISurface::Parameterization](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~Parameterization.md) or [ISurface::IParameterization](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IParameterization.md):

- Range[0] & Range[2] are the lower bounds of the U & V surface parameters respectively.
- Range[1] & Range[3] are the upper bounds of the U & V surface parameters respectively.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISurface Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.md)  
[ISurface Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface_members.md)
