# Width Property (IRenderMaterial)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~Width`

Gets or sets the width for mapping this appearance texture.
Gets or sets the width for mapping this appearance texture.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Width As System.Double
```

```

Dim instance As IRenderMaterial
Dim value As System.Double
 
instance.Width = value
 
value = instance.Width
```

```

System.double Width {get; set;}
```

```

property System.double Width {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Width

Remarks

Call [IRenderMaterial::Height](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~Height.md) to set the height of the appearance texture. If [IRenderMaterial::FixedAspectRatio](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~FixedAspectRatio.md) is true, then the image is uniformly scaled when either the width or height is changed.

To have the height and width of the appearance texture automatically stretch to fit a selected entity, call [IRenderMaterial::FitHeight](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~FitHeight.md) and [IRenderMaterial::FitWidth](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~FitWidth.md).

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
