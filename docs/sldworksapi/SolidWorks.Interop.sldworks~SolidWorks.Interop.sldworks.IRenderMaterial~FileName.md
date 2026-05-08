# FileName Property (IRenderMaterial)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~FileName`

Gets or sets the path and file name (.p2m) of the appearance.
Gets or sets the path and file name (.p2m) of the appearance.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property FileName As System.String
```

```

Dim instance As IRenderMaterial
Dim value As System.String
 
instance.FileName = value
 
value = instance.FileName
```

```

System.string FileName {get; set;}
```

```

property System.String^ FileName {
   System.String^ get();
   void set (    System.String^ value);
}
```

#### Property Value

Path and file name (.p2m) of the appearance

Example

[Add Decal (VBA)](Add_Decal_Example_VB.htm)  
[Add Decal (VB.NET)](Add_Decal_Example_VBNET.htm)  
[Add Decal (C#)](Add_Decal_Example_CSharp.htm)  
[Get Appearance File Name (C#)](Get_Appearance_Filename_Example_CSharp.htm)  
[Get Appearance File Name (VB.NET)](Get_Appearance_Filename_Example_VBNET.htm)  
[Get Appearance File Name (VBA)](Get_Appearance_Filename_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IRenderMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.md)  
[IRenderMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial_members.md)
