# GetBetweenTwoPoints Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetBetweenTwoPoints`

Gets whether the between two points symbol is being used.
Gets whether the between two points symbol is being used.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetBetweenTwoPoints() As System.Boolean
```

```

Dim instance As IGtol
Dim value As System.Boolean
 
value = instance.GetBetweenTwoPoints()
```

```

System.bool GetBetweenTwoPoints()
```

```

System.bool GetBetweenTwoPoints(); 
```

#### Return Value

True if using the between two points symbol, false if not

Remarks

Use

- [IGtol::GetBetweenTwoPointsText](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetBetweenTwoPointsText.md) to get the text that is used with this symbol.
- [IGtol::SetBetweenTwoPoints](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~SetBetweenTwoPoints.md) to enable this symbol and its texts.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IGtol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol.md)  
[IGtol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol_members.md)  
[IGtol::GetBetweenTwoPointsText Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetBetweenTwoPointsText.md)  
[IGtol::SetBetweenTwoPoints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~SetBetweenTwoPoints.md)
