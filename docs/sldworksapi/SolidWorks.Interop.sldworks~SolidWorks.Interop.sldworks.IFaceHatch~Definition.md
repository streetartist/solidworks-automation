# Definition Property (IFaceHatch)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFaceHatch~Definition`

Gets the definition for the face hatch.
Gets the definition for the face hatch.

**NOTE:** **This property is a get-only property.** **Set is not implemented**.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Definition As System.String
```

```

Dim instance As IFaceHatch
Dim value As System.String
 
instance.Definition = value
 
value = instance.Definition
```

```

System.string Definition {get; set;}
```

```

property System.String^ Definition {
   System.String^ get();
   void set (    System.String^ value);
}
```

#### Property Value

Definition for face hatch

Example

[Get Face Hatch Data (C#)](Get_Face_Hatch_Data_Example_CSharp.htm)  
[Get Face Hatch Data (VB.NET)](Get_Face_Hatch_Data_Example_VBNET.htm)  
[Get Face Hatch Data (VBA)](Get_Face_Hatch_Data_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFaceHatch Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFaceHatch.md)  
[IFaceHatch Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFaceHatch_members.md)
