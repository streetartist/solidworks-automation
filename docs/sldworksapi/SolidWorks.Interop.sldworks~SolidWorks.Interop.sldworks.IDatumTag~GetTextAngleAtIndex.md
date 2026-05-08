# GetTextAngleAtIndex Method (IDatumTag)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag~GetTextAngleAtIndex`

Gets the text angle for the specified text in this datum tag.
Gets the text angle for the specified text in this datum tag.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetTextAngleAtIndex( _
   ByVal Index As System.Integer _
) As System.Double
```

```

Dim instance As IDatumTag
Dim Index As System.Integer
Dim value As System.Double
 
value = instance.GetTextAngleAtIndex(Index)
```

```

System.double GetTextAngleAtIndex( 
   System.int Index
)
```

```

System.double GetTextAngleAtIndex( 
   System.int Index
) 
```

#### Parameters

*Index*
:   Index of the text; index begins at 0

#### Return Value

Text angle for the specified piece of text in radians measured CCW from the X-axis

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDatumTag Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag.md)  
[IDatumTag Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag_members.md)  
[IDatumTag::GetTextAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag~GetTextAtIndex.md)  
[IDatumTag::GetTextCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag~GetTextCount.md)  
[IDatumTag::GetTextHeightAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag~GetTextHeightAtIndex.md)  
[IDatumTag::GetTextInvertAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag~GetTextInvertAtIndex.md)  
[IDatumTag::GetTextPositionAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag~GetTextPositionAtIndex.md)  
[IDatumTag::GetTextRefPositionAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag~GetTextRefPositionAtIndex.md)  
[IDatumTag::IGetTextPositionAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag~IGetTextPositionAtIndex.md)
