# GetTextInvertAtIndex Method (IDatumTargetSym)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTargetSym~GetTextInvertAtIndex`

Gets the invert flag for the specified text item.
Gets the invert flag for the specified text item.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetTextInvertAtIndex( _
   ByVal Index As System.Integer _
) As System.Integer
```

```

Dim instance As IDatumTargetSym
Dim Index As System.Integer
Dim value As System.Integer
 
value = instance.GetTextInvertAtIndex(Index)
```

```

System.int GetTextInvertAtIndex( 
   System.int Index
)
```

```

System.int GetTextInvertAtIndex( 
   System.int Index
) 
```

#### Parameters

*Index*
:   Index of the text; index begins at 0

#### Return Value

Invert flag

Remarks

The invert flag specifies whether the text is mirrored (reflected) about the X axis. SOLIDWORKS applies reflection after text rotation.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDatumTargetSym Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTargetSym.md)  
[IDatumTargetSym Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTargetSym_members.md)  
[IDatumTargetSym::GetTextAngleAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTargetSym~GetTextAngleAtIndex.md)  
[IDatumTargetSym::GetTextAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTargetSym~GetTextAtIndex.md)  
[IDatumTargetSym::GetTextCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTargetSym~GetTextCount.md)  
[IDatumTargetSym::GetTextHeightAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTargetSym~GetTextHeightAtIndex.md)  
[IDatumTargetSym::GetTextPositionAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTargetSym~GetTextPositionAtIndex.md)  
[IDatumTargetSym::GetTextRefPositionAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTargetSym~GetTextRefPositionAtIndex.md)  
[IDatumTargetSym::IGetTextPositionAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTargetSym~IGetTextPositionAtIndex.md)
