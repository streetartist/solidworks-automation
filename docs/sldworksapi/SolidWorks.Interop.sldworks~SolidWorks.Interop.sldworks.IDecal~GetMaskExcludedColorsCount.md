# GetMaskExcludedColorsCount Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDecal~GetMaskExcludedColorsCount`

Gets the number of colors excluded from the mask image for this decal.
Gets the number of colors excluded from the mask image for this decal.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetMaskExcludedColorsCount() As System.Integer
```

```

Dim instance As IDecal
Dim value As System.Integer
 
value = instance.GetMaskExcludedColorsCount()
```

```

System.int GetMaskExcludedColorsCount()
```

```

System.int GetMaskExcludedColorsCount(); 
```

#### Return Value

Number of colors excluded from the mask image

Remarks

Call this method before calling [IDecal::IGetMaskExcludedColors](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDecal~IGetMaskExcludedColors.md) to get the size of the array for that method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDecal Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDecal.md)  
[IDecal Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDecal_members.md)  
[IDecal::ISetMaskExcludedColors Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDecal~ISetMaskExcludedColors.md)  
[IDecal::MaskFilename Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDecal~MaskFilename.md)  
[IDecal::MaskInvert Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDecal~MaskInvert.md)  
[IDecal::MaskType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDecal~MaskType.md)
