# GetUseDocTextFormat Method (ISketchText)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchText~GetUseDocTextFormat`

Gets whether default model text format is in use in this sketch text.
Gets whether default model text format is in use in this sketch text.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetUseDocTextFormat() As System.Boolean
```

```

Dim instance As ISketchText
Dim value As System.Boolean
 
value = instance.GetUseDocTextFormat()
```

```

System.bool GetUseDocTextFormat()
```

```

System.bool GetUseDocTextFormat(); 
```

#### Return Value

True if the default model text format is used, false if not

Remarks

To change the text format of an existing sketch text, get the [ITextFormat](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITextFormat.md) object using [ISketchText::GetTextFormat](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchText~GetTextFormat.md) or [ISketchText::IGetTextFormat](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchText~IGetTextFormat.md), next use the ITextFormat APIs to set the text format properties to what you want the sketch text to look like. Then, use [ISketchText::SetTextFormat](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchText~SetTextFormat.md) or [ISketchText::ISetTextFormat](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchText~ISetTextFormat.md) to change how the sketch text looks.  To make the sketch text use the default model text format, use ISketchText::SetTextFormat and ISketchText::ISetTextFormat with the UseDoc argument set to True.

Example

[Get All Elements of Sketch (VBA)](Get_All_Elements_of_Sketch_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchText Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchText.md)  
[ISketchText Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchText_members.md)  
[ISketchText::Text Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchText~Text.md)
