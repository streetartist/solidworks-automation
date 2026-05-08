# GetContour Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol~GetContour`

Gets the contour settings for this weld symbol.
Gets the contour settings for this weld symbol.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetContour( _
   ByVal Top As System.Boolean _
) As System.Integer
```

```

Dim instance As IWeldSymbol
Dim Top As System.Boolean
Dim value As System.Integer
 
value = instance.GetContour(Top)
```

```

System.int GetContour( 
   System.bool Top
)
```

```

System.int GetContour( 
   System.bool Top
) 
```

#### Parameters

*Top*
:   If true, then get the contour setting for the portion of the symbol above the horizontal line; if false, then get the contour setting for the portion of the symbol below the horizontal line

#### Return Value

Contour setting as defined by [swWeldSymbolContourTypes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swWeldSymbolContourTypes_e.html)

Remarks

To set the contour settings for a weld symbol, use [IWeldSymbol::SetText](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol~SetText.md).

Example

See the [IWeldSymbol](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IWeldSymbol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol.md)  
[IWeldSymbol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol_members.md)
