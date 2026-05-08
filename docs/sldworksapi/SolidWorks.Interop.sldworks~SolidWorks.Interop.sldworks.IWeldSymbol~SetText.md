# SetText Method (IWeldSymbol)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol~SetText`

Sets the text and symbols in the upper or lower portion of the weld symbol.
Sets the text and symbols in the upper or lower portion of the weld symbol.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetText( _
   ByVal Top As System.Boolean, _
   ByVal Left As System.String, _
   ByVal Symbol As System.String, _
   ByVal Right As System.String, _
   ByVal Stagger As System.String, _
   ByVal Contour As System.Integer _
) As System.Boolean
```

```

Dim instance As IWeldSymbol
Dim Top As System.Boolean
Dim Left As System.String
Dim Symbol As System.String
Dim Right As System.String
Dim Stagger As System.String
Dim Contour As System.Integer
Dim value As System.Boolean
 
value = instance.SetText(Top, Left, Symbol, Right, Stagger, Contour)
```

```

System.bool SetText( 
   System.bool Top,
   System.string Left,
   System.string Symbol,
   System.string Right,
   System.string Stagger,
   System.int Contour
)
```

```

System.bool SetText( 
   System.bool Top,
   System.String^ Left,
   System.String^ Symbol,
   System.String^ Right,
   System.String^ Stagger,
   System.int Contour
) 
```

#### Parameters

*Top*
:   True to set the text in the portion of the symbol above the horizontal line, false to set the text in the portion of the symbol below the horizontal line

*Left*
:   Text to the left of the weld symbol

*Symbol*
:   Text representing the weld symbol (see **Remarks**)

*Right*
:   Text to the right of the weld symbol

*Stagger*
:   Text to the right of the stagger symbol (see **Remarks**)

*Contour*
:   Contour setting as defined in [swWeldSymbolContourTypes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swWeldSymbolContourTypes_e.html) (see **Remarks**)

#### Return Value

True if the text and symbols are set, false if not

Remarks

To get the individual pieces of text for a weld symbol, use [IWeldSymbol::GetText](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol~GetText.md). To get the contour setting for a weld symbol, use [IWeldSymbol::GetContour](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol~GetContour.md).

The stagger text that is specified is only visible if this option is enabled. See [IWeldSymbol::GetStagger](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol~GetStagger.md) to see the current setting and [IWeldSymbol::SetStagger](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol~SetStagger.md) to enable or disable that option.

A list of weld symbol names can be found in the text file [**gtol.sym**,](sldworksAPIProgGuide.chm::/Miscellaneous/Geometric_Tolerance_Symbol_Libraries.htm), typically installed at **C:\ProgramData\SolidWorks\SolidWorks 20***nn*\**lang**\**english**. Specify Symbol with one of the currently supported ISO weld symbols:

- BUTT
- BUSQ
- BUSV
- BUSB
- BUSVBR
- BUSBR
- BUSU
- BUSJ
- BACK
- FILL
- PLUG
- SPOT
- SEAM
- SEAMC
- JSPT
- JSM

Example

See the [IWeldSymbol](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IWeldSymbol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol.md)  
[IWeldSymbol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol_members.md)
