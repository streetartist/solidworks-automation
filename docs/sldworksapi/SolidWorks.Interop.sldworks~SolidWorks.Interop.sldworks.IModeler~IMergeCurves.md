# IMergeCurves Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~IMergeCurves`

Merges multiple curves into one curve.
Merges multiple curves into one curve.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IMergeCurves( _
   ByVal CurveCount As System.Integer, _
   ByRef CurveArr As Curve _
) As Curve
```

```

Dim instance As IModeler
Dim CurveCount As System.Integer
Dim CurveArr As Curve
Dim value As Curve
 
value = instance.IMergeCurves(CurveCount, CurveArr)
```

```

Curve IMergeCurves( 
   System.int CurveCount,
   ref Curve CurveArr
)
```

```

Curve^ IMergeCurves( 
   System.int CurveCount,
   Curve^% CurveArr
) 
```

#### Parameters

*CurveCount*
:   Number of curves to merge

*CurveArr*
:   Array of [curves](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve.md) to merge

#### Return Value

Newly created merged [curve](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve.md) or NULL if merge fails

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModeler Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler.md)  
[IModeler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler_members.md)  
[IModeler::MergeCurves Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~MergeCurves.md)
