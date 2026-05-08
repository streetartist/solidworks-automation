# SetTextFormat Method (ISketchText)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchText~SetTextFormat`

Sets the text format for this sketch text.
Sets the text format for this sketch text.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetTextFormat( _
   ByVal UseDoc As System.Boolean, _
   ByVal TextFormat As System.Object _
) As System.Boolean
```

```

Dim instance As ISketchText
Dim UseDoc As System.Boolean
Dim TextFormat As System.Object
Dim value As System.Boolean
 
value = instance.SetTextFormat(UseDoc, TextFormat)
```

```

System.bool SetTextFormat( 
   System.bool UseDoc,
   System.object TextFormat
)
```

```

System.bool SetTextFormat( 
   System.bool UseDoc,
   System.Object^ TextFormat
) 
```

#### Parameters

*UseDoc*
:   True to use the default model text format, false to use a local text format

*TextFormat*
:   Local [text format](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITextFormat.md) to use if UseDoc is false

#### Return Value

True if the text format was successfully set, false if not

Remarks

To set the text format, you must be editing the sketch. See [IModelDoc2::EditSketch](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~EditSketch.md) or [ISketchManager::InsertSketch](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~InsertSketch.md).

To change the text format of an existing sketch text, get the [ITextFormat](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITextFormat.md) object using [ISketchText::GetTextFormat](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchText~GetTextFormat.md) or [ISketchText::IGetTextFormat](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchText~IGetTextFormat.md), next use the various ITextFormat APIs to set the text format properties to what you want the sketch text to look like. Then use this method to change how the sketch text looks. To make the sketch text use the default model text format, use this method with the useDoc argument set to True.

To determine if this sketch text is using the default model text format or not, use [ISketchText::GetUseDocTextFormat](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchText~GetUseDocTextFormat.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchText Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchText.md)  
[ISketchText Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchText_members.md)  
[ISketchText::ISetTextFormat Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchText~ISetTextFormat.md)  
[ISketchText::Text Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchText~Text.md)
