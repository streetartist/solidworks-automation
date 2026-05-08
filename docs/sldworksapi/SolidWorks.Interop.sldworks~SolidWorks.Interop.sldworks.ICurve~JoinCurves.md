# JoinCurves Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~JoinCurves`

Joins the specified curves.
Joins the specified curves.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function JoinCurves( _
   ByVal Curves As System.Object _
) As System.Object
```

```

Dim instance As ICurve
Dim Curves As System.Object
Dim value As System.Object
 
value = instance.JoinCurves(Curves)
```

```

System.object JoinCurves( 
   System.object Curves
)
```

```

System.Object^ JoinCurves( 
   System.Object^ Curves
) 
```

#### Parameters

*Curves*
:   Curves to join

#### Return Value

Newly created joined curve

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICurve Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve.md)  
[ICurve Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve_members.md)  
[ICurve::IJoinCurves Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IJoinCurves.md)
