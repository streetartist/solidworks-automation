# ISetMaskExcludedColors Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDecal~ISetMaskExcludedColors`

Sets the colors to exclude from the mask image for this decal.
Sets the colors to exclude from the mask image for this decal.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub ISetMaskExcludedColors( _
   ByVal Count As System.Integer, _
   ByRef MaskColors As System.Integer _
) 
```

```

Dim instance As IDecal
Dim Count As System.Integer
Dim MaskColors As System.Integer
 
instance.ISetMaskExcludedColors(Count, MaskColors)
```

```

void ISetMaskExcludedColors( 
   System.int Count,
   ref System.int MaskColors
)
```

```

void ISetMaskExcludedColors( 
   System.int Count,
   System.int% MaskColors
) 
```

#### Parameters

*Count*
:   Number of colors to exclude from the mask image

*MaskColors*
:   - in-process, unmanaged C++: Pointer to an array of the RGB colors excluded from the mask image

    - VBA, VB.NET, C#, and C++/CLI: Not supported

    See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDecal Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDecal.md)  
[IDecal Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDecal_members.md)  
[IDecal::GetMaskExcludedColorsCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDecal~GetMaskExcludedColorsCount.md)  
[IDecal::IGetMaskExcludedColors Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDecal~IGetMaskExcludedColors.md)  
[IDecal::MaskFilename Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDecal~MaskFilename.md)  
[IDecal::MaskInvert Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDecal~MaskInvert.md)  
[IDecal::MaskType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDecal~MaskType.md)
