# FixedAspectRatio Property (IRenderMaterial)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~FixedAspectRatio`

Gets or sets whether the aspect ratio is fixed for mapping this appearance texture.
Gets or sets whether the aspect ratio is fixed for mapping this appearance texture.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property FixedAspectRatio As System.Boolean
```

```

Dim instance As IRenderMaterial
Dim value As System.Boolean
 
instance.FixedAspectRatio = value
 
value = instance.FixedAspectRatio
```

```

System.bool FixedAspectRatio {get; set;}
```

```

property System.bool FixedAspectRatio {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True if the aspect ratio is fixed, false if not

Remarks

When FixedAspect is true, then the image is uniformly scaled when either the [height](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~Height.md) or [width](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~Width.md) is changed.

Use this property when changing the height or width of an appearance texture and wanting it uniformly scaled.

Example

[Get Surface-finish Image Path and File Name (C#)](Get_Surface-finish_Image_Path_and_Filename_Example_CSharp.htm)  
[Get Surface-finish Image Path and File Name (VB.NET)](Get_Surface-finish_Image_Path_and_Filename_Example_VBNET.htm)  
[Get Surface-finish Image Path and File Name (VBA)](Get_Surface-finish_Image_Path_and_Filename_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IRenderMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.md)  
[IRenderMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial_members.md)
