# MergeCurves Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~MergeCurves`

Merges multiple curves into one curve.
Merges multiple curves into one curve.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function MergeCurves( _
   ByVal CurveVar As System.Object _
) As Curve
```

```

Dim instance As IModeler
Dim CurveVar As System.Object
Dim value As Curve
 
value = instance.MergeCurves(CurveVar)
```

```

Curve MergeCurves( 
   System.object CurveVar
)
```

```

Curve^ MergeCurves( 
   System.Object^ CurveVar
) 
```

#### Parameters

*CurveVar*
:   Array of [curves](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve.md) to merge

#### Return Value

Newly created merged [curve](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve.md) or Nothing if merge fails

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModeler Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler.md)  
[IModeler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler_members.md)  
[IModeler::IMergeCurves Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~IMergeCurves.md)
