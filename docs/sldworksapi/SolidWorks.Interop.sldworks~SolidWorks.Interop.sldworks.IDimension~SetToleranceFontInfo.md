# SetToleranceFontInfo Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~SetToleranceFontInfo`

Obsolete. Superseded by IDimensionTolerance::SetFont.
Obsolete. Superseded by [IDimensionTolerance::SetFont](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance~SetFont.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetToleranceFontInfo( _
   ByVal UseFontScale As System.Integer, _
   ByVal TolScale As System.Double, _
   ByVal TolHeight As System.Double _
) As System.Boolean
```

```

Dim instance As IDimension
Dim UseFontScale As System.Integer
Dim TolScale As System.Double
Dim TolHeight As System.Double
Dim value As System.Boolean
 
value = instance.SetToleranceFontInfo(UseFontScale, TolScale, TolHeight)
```

```

System.bool SetToleranceFontInfo( 
   System.int UseFontScale,
   System.double TolScale,
   System.double TolHeight
)
```

```

System.bool SetToleranceFontInfo( 
   System.int UseFontScale,
   System.double TolScale,
   System.double TolHeight
) 
```

#### Parameters

*UseFontScale*

*TolScale*

*TolHeight*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension.md)  
[IDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension_members.md)
