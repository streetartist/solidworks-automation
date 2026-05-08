# SolidFill Property (IFaceHatch)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFaceHatch~SolidFill`

Gets whether the face hatch is a solid color.
Gets whether the face hatch is a solid color.

**NOTE:** **This property is a get-only property.** **Set is not implemented**.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property SolidFill As System.Boolean
```

```

Dim instance As IFaceHatch
Dim value As System.Boolean
 
instance.SolidFill = value
 
value = instance.SolidFill
```

```

System.bool SolidFill {get; set;}
```

```

property System.bool SolidFill {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True if face hatch is a solid color, false if not

Example

[Get Crosshatches on the View (VBA)](Get_Crosshatches_on_View_Example_VB.htm)  
[Get Face Hatch Data (C#)](Get_Face_Hatch_Data_Example_CSharp.htm)  
[Get Face Hatch Data (VB.NET)](Get_Face_Hatch_Data_Example_VBNET.htm)  
[Get Face Hatch Data (VBA)](Get_Face_Hatch_Data_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFaceHatch Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFaceHatch.md)  
[IFaceHatch Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFaceHatch_members.md)
