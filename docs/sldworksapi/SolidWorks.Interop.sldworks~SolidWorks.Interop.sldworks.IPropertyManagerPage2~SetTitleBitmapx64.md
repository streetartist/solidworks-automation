# SetTitleBitmapx64 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2~SetTitleBitmapx64`

Sets the bitmap to display in the title of this PropertyManager page.
Sets the bitmap to display in the title of this PropertyManager page.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetTitleBitmapx64( _
   ByVal ModuleHandle As System.Long, _
   ByVal Identifier As System.Integer _
) As System.Boolean
```

```

Dim instance As IPropertyManagerPage2
Dim ModuleHandle As System.Long
Dim Identifier As System.Integer
Dim value As System.Boolean
 
value = instance.SetTitleBitmapx64(ModuleHandle, Identifier)
```

```

System.bool SetTitleBitmapx64( 
   System.long ModuleHandle,
   System.int Identifier
)
```

```

System.bool SetTitleBitmapx64( 
   System.int64 ModuleHandle,
   System.int Identifier
) 
```

#### Parameters

*ModuleHandle*
:   Module handle of the application instance that contains the bitmap resource (see **Remarks**)

*Identifier*
:   Resource ID of the bitmap (see **Remarks**)

#### Return Value

True if successful, false if not

Remarks

This method is only available through early binding and with 64-bit versions of the SOLIDWORKS software. Its intended use is for SOLIDWORKS PropertyManager .NET add-ins. For VBA PropertyManager pages, use [IPropertyManagerPage2::SetTitleBitmap2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2~SetTitleBitmap2.md).

You can only use this method to set properties on the PropertyManager page before it is displayed or while it is closed. See [IPropertyManagerPage2::Show2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2~Show2.md) and [IPropertyManagerPage2::Close](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2~Close.md) for details.

The bitmap:

- must have less than 256 colors. Its recommended size is 18 - 22 cells wide. However, the bitmap can be any size, as long as it fits on the title bar.
- appears transparent by mapping any white (RGB(255,255,255)) cells to the current PropertyManager page title bar background color. Remember the special use of this color as you design your bitmap.
- must be a resource in your Visual Studio application.  You must discover its resource ID before you can specify Identifier.

Specify ModuleHandle using the add-in ID.

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
