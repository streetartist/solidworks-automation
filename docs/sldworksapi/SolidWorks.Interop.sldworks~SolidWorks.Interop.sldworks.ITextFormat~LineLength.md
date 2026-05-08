# LineLength Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITextFormat~LineLength`

Gets or sets the text line length in meters.
Gets or sets the text line length in meters.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property LineLength As System.Double
```

```

Dim instance As ITextFormat
Dim value As System.Double
 
instance.LineLength = value
 
value = instance.LineLength
```

```

System.double LineLength {get; set;}
```

```

property System.double LineLength {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Line length

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
