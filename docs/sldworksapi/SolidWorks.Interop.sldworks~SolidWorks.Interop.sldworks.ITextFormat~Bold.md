# Bold Property (ITextFormat)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITextFormat~Bold`

Gets or sets the whether the text format is bold.
Gets or sets the whether the text format is bold.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Bold As System.Boolean
```

```

Dim instance As ITextFormat
Dim value As System.Boolean
 
instance.Bold = value
 
value = instance.Bold
```

```

System.bool Bold {get; set;}
```

```

property System.bool Bold {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True if the text is bold, false otherwise

Example

[Change Text Format (VBA)](Change_Text_Format_Example_VB.htm)  
[Get All Elements of Sketch (VBA)](Get_All_Elements_of_Sketch_Example_VB.htm)  
[Get Note Text Formatting Properties (VBA)](Get_Note_Text_Formatting_Properties_Example_VB.htm)  
[Get Arrow in Projected View (C#)](Get_Arrow_in_Projected_View_Example_CSharp.htm)  
[Get Arrow in Projected View (VB.NET)](Get_Arrow_in_Projected_View_Example_VBNET.htm)  
[Get Arrow in Projected View (VBA)](Get_Arrow_in_Projected_View_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ITextFormat Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITextFormat.md)  
[ITextFormat Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITextFormat_members.md)
