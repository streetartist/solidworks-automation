# BumpTextureFilename Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~BumpTextureFilename`

Obsolete. Superseded by IRenderMaterial::SurfaceFinishFile. Gets or sets the path and file name of the pattern based on an image file for the surface finish of this appearance.
Obsolete. Superseded by IRenderMaterial::SurfaceFinishFile. Gets or sets the path and file name of the pattern based on an image file for the surface finish of this appearance.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property BumpTextureFilename As System.String
```

```

Dim instance As IRenderMaterial
Dim value As System.String
 
instance.BumpTextureFilename = value
 
value = instance.BumpTextureFilename
```

```

System.string BumpTextureFilename {get; set;}
```

```

property System.String^ BumpTextureFilename {
   System.String^ get();
   void set (    System.String^ value);
}
```

#### Property Value

Path and file name of the pattern based on an image file for the surface finish

Remarks

This property corresponds to selecting From File as the surface finish type on the Surface Finish tab of the Appearances PropertyManager page and browsing to an image.

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
