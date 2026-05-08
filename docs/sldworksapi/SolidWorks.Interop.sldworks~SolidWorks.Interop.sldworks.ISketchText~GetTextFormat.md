# GetTextFormat Method (ISketchText)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchText~GetTextFormat`

Gets the text format for this sketch text.
Gets the text format for this sketch text.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetTextFormat() As System.Object
```

```

Dim instance As ISketchText
Dim value As System.Object
 
value = instance.GetTextFormat()
```

```

System.object GetTextFormat()
```

```

System.Object^ GetTextFormat(); 
```

#### Return Value

[Text format](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITextFormat.md)

Remarks

To change the text format of an existing sketch text, get the [ITextFormat](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITextFormat.md) object using this method, next use its APIs to set the text format properties to what you want the sketch text to look like. Then use [ISketchText::SetTextFormat](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchText~SetTextFormat.md) or [ISketchText::ISetTextFormat](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchText~ISetTextFormat.md) to change how the sketch text looks. To make the sketch text use the default model text format, use ISketchText:SetTextFormat and ISketchText::ISetTextFormat with the UseDoc argument set to True.

Example

[Get All Elements (VBA)](Get_All_Elements_of_Sketch_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchText Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchText.md)  
[ISketchText Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchText_members.md)  
[ISketchText::GetUseDocTextFormat Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchText~GetUseDocTextFormat.md)  
[ISketchText::IGetTextFormat Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchText~IGetTextFormat.md)  
[ISketchText::Text Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchText~Text.md)
