# MakeIsoCurve Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~MakeIsoCurve`

Creates an untrimmed curve using the specified surface parameter.
Creates an untrimmed curve using the specified surface parameter.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function MakeIsoCurve( _
   ByVal UorV As System.Boolean, _
   ByVal UvValue As System.Double _
) As System.Object
```

```

Dim instance As ISurface
Dim UorV As System.Boolean
Dim UvValue As System.Double
Dim value As System.Object
 
value = instance.MakeIsoCurve(UorV, UvValue)
```

```

System.object MakeIsoCurve( 
   System.bool UorV,
   System.double UvValue
)
```

```

System.Object^ MakeIsoCurve( 
   System.bool UorV,
   System.double UvValue
) 
```

#### Parameters

*UorV*
:   True to specify v, false to specify u

*UvValue*
:   U or v value

#### Return Value

[Curve](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve.md)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISurface Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.md)  
[ISurface Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface_members.md)  
[ISurface::IMakeIsoCurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IMakeIsoCurve.md)  
[ISurface::IMakeIsoCurves Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IMakeIsoCurves.md)  
[ISurface::MakeIsoCurves Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~MakeIsoCurves.md)  
[ISurface::IGetMakeIsoCurvesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IGetMakeIsoCurvesCount.md)
