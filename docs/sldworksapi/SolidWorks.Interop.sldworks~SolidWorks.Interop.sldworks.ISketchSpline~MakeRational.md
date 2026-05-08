# MakeRational Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~MakeRational`

Sets whether this spline is rational or non-rational.
Sets whether this spline is rational or non-rational.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function MakeRational( _
   ByVal Val As System.Boolean _
) As System.Boolean
```

```

Dim instance As ISketchSpline
Dim Val As System.Boolean
Dim value As System.Boolean
 
value = instance.MakeRational(Val)
```

```

System.bool MakeRational( 
   System.bool Val
)
```

```

System.bool MakeRational( 
   System.bool Val
) 
```

#### Parameters

*Val*
:   True to make rational, false to make non-rational

#### Return Value

True if successfully set, false if not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchSpline Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline.md)  
[ISketchSpline Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline_members.md)  
[ISketchSpline::IsRationalCurve Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~IsRationalCurve.md)
