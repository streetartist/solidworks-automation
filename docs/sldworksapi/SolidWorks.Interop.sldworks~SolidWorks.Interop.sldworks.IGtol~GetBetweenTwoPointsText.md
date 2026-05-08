# GetBetweenTwoPointsText Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetBetweenTwoPointsText`

Gets the text used in the between two points symbol.
Gets the text used in the between two points symbol.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetBetweenTwoPointsText( _
   ByVal Index As System.Integer _
) As System.String
```

```

Dim instance As IGtol
Dim Index As System.Integer
Dim value As System.String
 
value = instance.GetBetweenTwoPointsText(Index)
```

```

System.string GetBetweenTwoPointsText( 
   System.int Index
)
```

```

System.String^ GetBetweenTwoPointsText( 
   System.int Index
) 
```

#### Parameters

*Index*
:   0 for the text on the left end of the symbol, 1 for the text on the right end of the symbol

#### Return Value

Symbol text

Remarks

This method returns the requested text whether the between two points symbol is currently enabled. Use [IGtol::GetBetweenTwoPoints](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetBetweenTwoPoints.md) to determine if this symbol is enabled.

Use [IGtol::SetBetweenTwoPoints](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~SetBetweenTwoPoints.md) to enable this symbol and its texts.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IGtol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol.md)  
[IGtol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol_members.md)  
[IGtol::SetBetweenTwoPoints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~SetBetweenTwoPoints.md)  
[IGtol::GetBetweenTwoPoints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetBetweenTwoPoints.md)
