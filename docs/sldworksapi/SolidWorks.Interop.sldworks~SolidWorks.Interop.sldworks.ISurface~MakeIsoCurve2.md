# MakeIsoCurve2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~MakeIsoCurve2`

Creates an untrimmed curve on a surface using the specified u or v surface function parameter.
Creates an untrimmed curve on a surface using the specified u or v surface function parameter.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function MakeIsoCurve2( _
   ByVal UorV As System.Boolean, _
   ByRef UvValue As System.Double _
) As Curve
```

```

Dim instance As ISurface
Dim UorV As System.Boolean
Dim UvValue As System.Double
Dim value As Curve
 
value = instance.MakeIsoCurve2(UorV, UvValue)
```

```

Curve MakeIsoCurve2( 
   System.bool UorV,
   out System.double UvValue
)
```

```

Curve^ MakeIsoCurve2( 
   System.bool UorV,
   [Out] System.double UvValue
) 
```

#### Parameters

*UorV*
:   True to specify the surface function's v parameter in UvValue, false to specify its u parameter

*UvValue*
:   | If UorV is... | Then UvValue is the surface function's... |
    | --- | --- |
    | True | V parameter |
    | False | U parameter |

#### Return Value

[Curve](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve.md)

Remarks

This method supersedes the now obsolete ISurface::MakeIsoCurve by normalizing UvValue when it exceeds a specific value.

Example

[Create Trimmed Curve (VBA)](Return_Untrimmed_Curve_Example_VB.htm)  
[Create Trimmed Curve (VB.NET)](Return_Untrimmed_Curve_Example_VBNET.htm)  
[Create Trimmed Curve (C#)](Return_Untrimmed_Curve_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISurface Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.md)  
[ISurface Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface_members.md)  
[ISurface::MakeIsoCurves Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~MakeIsoCurves.md)  
[ISurface::IMakeIsoCurves Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IMakeIsoCurves.md)  
[ISurface::IGetMakeIsoCurvesCount Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IGetMakeIsoCurvesCount.md)  
[ISurface::IMakeIsoCurve Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IMakeIsoCurve.md)  
[ICurve::CreateTrimmedCurve2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~CreateTrimmedCurve2.md)
