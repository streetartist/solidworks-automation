# GetTextInvertAtIndex Method (IWeldSymbol)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol~GetTextInvertAtIndex`

Gets whether the text has been mirrored (reflected) about the X axis; any reflection is applied after text rotation.
Gets whether the text has been mirrored (reflected) about the X axis; any reflection is applied after text rotation.

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

Dim instance As IWeldSymbol
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
:   Index of the piece of text where the index begins at 0

#### Return Value

Text item's invert flag

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IWeldSymbol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol.md)  
[IWeldSymbol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol_members.md)  
[IWeldSymbol::GetText Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol~GetText.md)  
[IWeldSymbol::GetTextAngleAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol~GetTextAngleAtIndex.md)  
[IWeldSymbol::GetTextAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol~GetTextAtIndex.md)  
[IWeldSymbol::GetTextCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol~GetTextCount.md)  
[IWeldSymbol::GetTextHeightAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol~GetTextHeightAtIndex.md)  
[IWeldSymbol::GetTextPositionAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol~GetTextPositionAtIndex.md)  
[IWeldSymbol::GetTextRefPositionAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol~GetTextRefPositionAtIndex.md)  
[IWeldSymbol::IGetTextPositionAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol~IGetTextPositionAtIndex.md)  
[IWeldSymbol::SetText Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol~SetText.md)
