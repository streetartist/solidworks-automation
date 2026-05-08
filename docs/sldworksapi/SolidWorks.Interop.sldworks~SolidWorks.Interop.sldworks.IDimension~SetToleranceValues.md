# SetToleranceValues Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~SetToleranceValues`

Obsolete. Superseded by IDimensionTolerance::SetValues.
Obsolete. Superseded by [IDimensionTolerance::SetValues](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance~SetValues.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetToleranceValues( _
   ByVal TolMin As System.Double, _
   ByVal TolMax As System.Double _
) As System.Boolean
```

```

Dim instance As IDimension
Dim TolMin As System.Double
Dim TolMax As System.Double
Dim value As System.Boolean
 
value = instance.SetToleranceValues(TolMin, TolMax)
```

```

System.bool SetToleranceValues( 
   System.double TolMin,
   System.double TolMax
)
```

```

System.bool SetToleranceValues( 
   System.double TolMin,
   System.double TolMax
) 
```

#### Parameters

*TolMin*

*TolMax*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension.md)  
[IDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension_members.md)
