# UpsideDown Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITextFormat~UpsideDown`

Gets or sets whether the whole text string is upside down.
Gets or sets whether the whole text string is upside down.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property UpsideDown As System.Boolean
```

```

Dim instance As ITextFormat
Dim value As System.Boolean
 
instance.UpsideDown = value
 
value = instance.UpsideDown
```

```

System.bool UpsideDown {get; set;}
```

```

property System.bool UpsideDown {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True if the string is upside down, false if not

Example

[Get All Elements of Sketch (VBA)](Get_All_Elements_of_Sketch_Example_VB.htm)  
[Get Arrow in Projected View (C#)](Get_Arrow_in_Projected_View_Example_CSharp.htm)  
[Get Arrow in Projected View (VB.NET)](Get_Arrow_in_Projected_View_Example_VBNET.htm)  
[Get Arrow in Projected View (VBA)](Get_Arrow_in_Projected_View_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ITextFormat Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITextFormat.md)  
[ITextFormat Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITextFormat_members.md)
