# swRayTraceRenderImageFormat_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swRayTraceRenderImageFormat_e`

Image formats.
Image formats.

Syntax

- [Visual Basic](#Syntax-VBAll)
- [C#](#Syntax-CS)
- [Delphi](#Syntax-Delphi)
- [JScript](#Syntax-JScript)
- [Managed Extensions for C++](#Syntax-CPP)
- [C++/CLI](#Syntax-CPP2005)

```

'Declaration
 
```

```

<System.Runtime.InteropServices.GuidAttribute("0B05588B-0819-4BD0-9552-AB64C674E6B8")>
Public Enum swRayTraceRenderImageFormat_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swRayTraceRenderImageFormat_e
```

```

[System.Runtime.InteropServices.Guid("0B05588B-0819-4BD0-9552-AB64C674E6B8")]
public enum swRayTraceRenderImageFormat_e : System.Enum 
```

```

public enum swRayTraceRenderImageFormat_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("0B05588B-0819-4BD0-9552-AB64C674E6B8")
public enum swRayTraceRenderImageFormat_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("0B05588B-0819-4BD0-9552-AB64C674E6B8")]
__value public enum swRayTraceRenderImageFormat_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("0B05588B-0819-4BD0-9552-AB64C674E6B8")]
public enum class swRayTraceRenderImageFormat_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swImageFormat\_FlexiblePrecision** | 0 = Flexible Precision (**\*.flx**) |
| **swImageFormat\_HDR** | 3 = Radiance High Dynamic Range (**\*.hdr**) |
| **swImageFormat\_JPEG** | 7 = JPEG (**\*.jpg**) |
| **swImageFormat\_JPEG2000** | 4 = JPEG 2000 (**\*.jp2**) |
| **swImageFormat\_JPEG2000\_16bit** | 5 = JPEG 2000 16-bit (**\*.jp2**) |
| **swImageFormat\_JPEG2000\_16bit\_Lossless** | 6 = JPEG 2000 16-bit Lossless (**\*.jp2**) |
| **swImageFormat\_OpenEXR** | 14 = OpenEXR Half 16-bit (**\*.exr**) |
| **swImageFormat\_OpenEXR\_32bit** | 15 = OpenEXR Flat 32-bit (**\*.exr**) |
| **swImageFormat\_OpenEXR\_TILED16bit** | 16 = OpenEXR Tiled Half 16-bit (**\*.exr**) |
| **swImageFormat\_OpenEXR\_TILED32bit** | 17 = OpenEXR Tiled Flat 32-bit (**\*.exr**) |
| **swImageFormat\_PNG** | 8 = Portable Network Graphic (**\*.png**) |
| **swImageFormat\_PNG\_16bit** | 9 = 16-bit Portable Network Graphic (**\*.png**) |
| **swImageFormat\_SGI\_RGB** | 10 = SGI RGB (**\*.sgi**) |
| **swImageFormat\_Targa** | 1 = Targa (**\*.tga**) |
| **swImageFormat\_TIF** | 11 = Tagged Image File Format (**\*.tif**) |
| **swImageFormat\_TIF\_16bit** | 12 = 16-bit Tagged Image File Format (**\*.tif**) |
| **swImageFormat\_TIF\_16bit\_uncompr** | 13 = 16-bit uncompressed Tagged Image File Format (**\*.tif**) |
| **swImageFormat\_WindowsBmp** | 2 = Windows Bitmap (**\*.bmp**) |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swRayTraceRenderImageFormat\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
