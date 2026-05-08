# SetToleranceFitValues Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~SetToleranceFitValues`

Obsolete. Superseded by IDimensionTolerance::SetFitValues.
Obsolete. Superseded by [IDimensionTolerance::SetFitValues](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance~SetFitValues.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetToleranceFitValues( _
   ByVal NewLValue As System.String, _
   ByVal NewUValue As System.String _
) As System.Boolean
```

```

Dim instance As IDimension
Dim NewLValue As System.String
Dim NewUValue As System.String
Dim value As System.Boolean
 
value = instance.SetToleranceFitValues(NewLValue, NewUValue)
```

```

System.bool SetToleranceFitValues( 
   System.string NewLValue,
   System.string NewUValue
)
```

```

System.bool SetToleranceFitValues( 
   System.String^ NewLValue,
   System.String^ NewUValue
) 
```

#### Parameters

*NewLValue*

*NewUValue*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension.md)  
[IDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension_members.md)
