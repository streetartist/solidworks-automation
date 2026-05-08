# Text Property (ISketchText)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchText~Text`

Gets or sets the text that makes up this sketch text.
Gets or sets the text that makes up this sketch text.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Text As System.String
```

```

Dim instance As ISketchText
Dim value As System.String
 
instance.Text = value
 
value = instance.Text
```

```

System.string Text {get; set;}
```

```

property System.String^ Text {
   System.String^ get();
   void set (    System.String^ value);
}
```

#### Property Value

Text that makes up this sketch text

Remarks

To set the text format, you must be editing the sketch. See [IModelDoc2::EditSketch](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~EditSketch.md) or [ISketchManager::InsertSketch](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~InsertSketch.md). You can only change text in visible documents.

Example

[Get All Elements of Sketch (VBA)](Get_All_Elements_of_Sketch_Example_VB.htm)  
[Get Sketch Entities (VBA)](Get_Sketch_Entities_Example_VB.htm)  
[Replace Sketch Text (VBA)](Replace_Sketch_Text_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchText Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchText.md)  
[ISketchText Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchText_members.md)  
[ISketchText::GetTextFormat Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchText~GetTextFormat.md)  
[ISketchText::GetUseDocTextFormat Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchText~GetUseDocTextFormat.md)  
[ISketchText::IGetTextFormat Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchText~IGetTextFormat.md)  
[ISketchText::ISetTextFormat Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchText~ISetTextFormat.md)  
[ISketchText::SetTextFormat Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchText~SetTextFormat.md)
