# GetText Method (ISFSymbol)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~GetText`

Gets the specified text string in this surface finish symbol.
Gets the specified text string in this surface finish symbol.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetText( _
   ByVal WhichOne As System.Integer _
) As System.String
```

```

Dim instance As ISFSymbol
Dim WhichOne As System.Integer
Dim value As System.String
 
value = instance.GetText(WhichOne)
```

```

System.string GetText( 
   System.int WhichOne
)
```

```

System.String^ GetText( 
   System.int WhichOne
) 
```

#### Parameters

*WhichOne*
:   Text item to get as defined in  [swSurfaceFinishSymbolText\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSurfaceFinishSymbolText_e.html)

#### Return Value

Text string

Remarks

Call [ISFSymbol::GetTextCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~GetTextCount.md) before calling this method to get the number of text items.

To set the text strings, use [ISFSymbol::SetText](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~SetText.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISFSymbol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol.md)  
[ISFSymbol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol_members.md)  
[ISFSymbol::GetTextAngleAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~GetTextAngleAtIndex.md)  
[ISFSymbol::GetTextAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~GetTextAtIndex.md)  
[ISFSymbol::GetTextCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~GetTextCount.md)  
[ISFSymbol::GetTextFontAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~GetTextFontAtIndex.md)  
[ISFSymbol::GetTextHeightAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~GetTextHeightAtIndex.md)  
[ISFSymbol::GetTextInvertAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~GetTextInvertAtIndex.md)  
[ISFSymbol::GetTextPositionAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~GetTextPositionAtIndex.md)  
[ISFSymbol::GetTextRefPositionAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~GetTextRefPositionAtIndex.md)  
[ISFSymbol::IGetTextPositionAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~IGetTextPositionAtIndex.md)
