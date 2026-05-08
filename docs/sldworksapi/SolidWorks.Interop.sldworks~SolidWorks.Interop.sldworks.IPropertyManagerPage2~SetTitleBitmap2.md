# SetTitleBitmap2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2~SetTitleBitmap2`

Sets the bitmap to display in the title of this PropertyManager page.
Sets the bitmap to display in the title of this PropertyManager page.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SetTitleBitmap2( _
   ByVal FilePathName As System.String _
) 
```

```

Dim instance As IPropertyManagerPage2
Dim FilePathName As System.String
 
instance.SetTitleBitmap2(FilePathName)
```

```

void SetTitleBitmap2( 
   System.string FilePathName
)
```

```

void SetTitleBitmap2( 
   System.String^ FilePathName
) 
```

#### Parameters

*FilePathName*
:   Path and filename of the bitmap to display in the title of this PropertyManager page

Remarks

If your application must be x64 compatible, then use [IPropertyManagerPage2::SetTitleBitmapx64](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2~SetTitleBitmapx64.md).

You can only use this method to set properties on the PropertyManager page before it is displayed or while it is closed. See [IPropertyManagerPage2::Show2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2~Show2.md) and [IPropertyManagerPage2::Close](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2~Close.md) for details.

Create the bitmap in the resources of your application. The bitmap must have less than 256 colors. It is accessed via the path and filename passed into this method.  The recommended size for bitmaps is a square from 18- to 22-cells wide. However, the bitmap can be any size, as long as it fits on the title bar.

The bitmap appears transparent by mapping any white (RGB(255,255,255)) cells to the current PropertyManager page title bar background color. Remember the special use of this color as you design your bitmap.

|  |  |
| --- | --- |
| **If this method is...** | **Then the title bar contains...** |
| Used | Specified bitmap starting at the left edge of the PropertyManager title bar, followed by the title bar text (see [ISldWorks::CreatePropertyManagerPage](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~CreatePropertyManagerPage.md) or [ISldWorks::ICreatePropertyManagerPage](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~ICreatePropertyManagerPage.md)). |
| Not used | Only the text, centered on the title bar. |

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPropertyManagerPage2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2.md)  
[IPropertyManagerPage2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2_members.md)  
[IPropertyManagerPage2::Title Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2~Title.md)
