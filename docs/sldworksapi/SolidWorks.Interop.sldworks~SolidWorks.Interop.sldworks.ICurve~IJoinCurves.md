# IJoinCurves Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IJoinCurves`

Joins the specified curves.
Joins the specified curves.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IJoinCurves( _
   ByVal NCurves As System.Integer, _
   ByRef Curves As Curve _
) As Curve
```

```

Dim instance As ICurve
Dim NCurves As System.Integer
Dim Curves As Curve
Dim value As Curve
 
value = instance.IJoinCurves(NCurves, Curves)
```

```

Curve IJoinCurves( 
   System.int NCurves,
   ref Curve Curves
)
```

```

Curve^ IJoinCurves( 
   System.int NCurves,
   Curve^% Curves
) 
```

#### Parameters

*NCurves*
:   Number of curves to join

*Curves*
:   - in-process, unmanaged C++: Pointer to an array of [curves](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve.md) to join

    - VBA, VB.NET, C#, and C++/CLI: Not supported

    See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

#### Return Value

Newly created joined [curve](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve.md)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICurve Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve.md)  
[ICurve Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve_members.md)  
[ICurve::JoinCurves Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~JoinCurves.md)
