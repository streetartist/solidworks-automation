# UseMaterialHatch Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFaceHatch~UseMaterialHatch`

Gets or sets whether this face hatch uses material crosshatch.
Gets or sets whether this face hatch uses material crosshatch.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property UseMaterialHatch As System.Boolean
```

```

Dim instance As IFaceHatch
Dim value As System.Boolean
 
instance.UseMaterialHatch = value
 
value = instance.UseMaterialHatch
```

```

System.bool UseMaterialHatch {get; set;}
```

```

property System.bool UseMaterialHatch {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to use material crosshatch, false to not

Remarks

Material crosshatches are valid for [section views](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection.md) and aligned section views only.

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
