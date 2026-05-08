# DoubleSided Property (IRenderMaterial)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~DoubleSided`

Gets or sets whether to enable shading from both sides of a surface when rendering a model using a ray-trace rendering engine.
Gets or sets whether to enable shading from both sides of a surface when rendering a model using a ray-trace rendering engine.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property DoubleSided As System.Boolean
```

```

Dim instance As IRenderMaterial
Dim value As System.Boolean
 
instance.DoubleSided = value
 
value = instance.DoubleSided
```

```

System.bool DoubleSided {get; set;}
```

```

property System.bool DoubleSided {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to enable shading from both sides, false to not

Remarks

This method is only available when a ray-trace rendering engine is loaded.

**NOTES:**

- When this property is disabled, surfaces that do not face the camera seem invisible.
- Double-sided surfaces can cause rendering errors. Use sparingly.

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
