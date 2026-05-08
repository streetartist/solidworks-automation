# Color Property (IFaceHatch)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFaceHatch~Color`

Gets the color of the face hatch.
Gets the color of the face hatch.

**NOTE:** **This property is a get-only property.** **Set is not implemented**.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Color As System.Integer
```

```

Dim instance As IFaceHatch
Dim value As System.Integer
 
instance.Color = value
 
value = instance.Color
```

```

System.int Color {get; set;}
```

```

property System.int Color {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

COLORREF value for the color used for this face hatch

Example

[Get Crosshatches on View (VBA)](Get_Crosshatches_on_View_Example_VB.htm)  
[Get Face Hatch Data (C#)](Get_Face_Hatch_Data_Example_CSharp.htm)  
[Get Face Hatch Data (VB.NET)](Get_Face_Hatch_Data_Example_VBNET.htm)  
[Get Face Hatch Data (VBA)](Get_Face_Hatch_Data_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFaceHatch Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFaceHatch.md)  
[IFaceHatch Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFaceHatch_members.md)
