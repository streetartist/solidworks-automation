# ICreateTrimmedSheet2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~ICreateTrimmedSheet2`

Obsolete. Superseded by ISurface::ICreateTrimmedSheet4.
Obsolete. Superseded by [ISurface::ICreateTrimmedSheet4](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~ICreateTrimmedSheet4.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ICreateTrimmedSheet2( _
   ByVal NCurves As System.Integer, _
   ByRef Curves As Curve _
) As Body2
```

```

Dim instance As ISurface
Dim NCurves As System.Integer
Dim Curves As Curve
Dim value As Body2
 
value = instance.ICreateTrimmedSheet2(NCurves, Curves)
```

```

Body2 ICreateTrimmedSheet2( 
   System.int NCurves,
   ref Curve Curves
)
```

```

Body2^ ICreateTrimmedSheet2( 
   System.int NCurves,
   Curve^% Curves
) 
```

#### Parameters

*NCurves*

*Curves*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISurface Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.md)  
[ISurface Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface_members.md)
