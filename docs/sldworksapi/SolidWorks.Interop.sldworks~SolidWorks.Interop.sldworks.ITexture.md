# ITexture Interface

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITexture`

Use to apply 2D textures to part and assembly documents for a more realistic finish.
Use to apply 2D textures to part and assembly documents for a more realistic finish.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Interface ITexture 
```

```

Dim instance As ITexture
```

```

public interface ITexture 
```

```

public interface class ITexture 
```

Remarks

To get or set the location of a texture file, use [ISldWorks::GetUserPreferenceStringValue](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetUserPreferenceStringValue.md) or [ISldWorks::SetUserPreferenceStringValue](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SetUserPreferenceStringValue.md) and swFileLocationsTextures.

Example

[Change Texture on Face in Specified Configuration (VBA)](Change_Texture_on_Face_in_Specified_Configuration_Example_VB.htm)  
[Change Texture on Face in Specified Configuration (VB.NET)](Change_Texture_on_Face_in_Specified_Configuration_Example_VBNET.htm)  
[Change Texture on Face in Specified Configuration (C#)](Change_Texture_on_Face_in_Specified_Configuration_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ITexture Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITexture_members.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
