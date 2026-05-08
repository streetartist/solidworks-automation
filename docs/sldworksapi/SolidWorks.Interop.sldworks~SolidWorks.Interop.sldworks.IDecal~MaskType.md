# MaskType Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDecal~MaskType`

Gets or sets the type of mask used with this decal.
Gets or sets the type of mask used with this decal.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property MaskType As System.Integer
```

```

Dim instance As IDecal
Dim value As System.Integer
 
instance.MaskType = value
 
value = instance.MaskType
```

```

System.int MaskType {get; set;}
```

```

property System.int MaskType {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Type of mask:

- 0 = No mask
- 1 = Image mask file
- 2 = Selective color mask
- 3 = Use decal image alpha channel

Example

[Get Mask Types of Each Decal (VBA)](Get_Mask_Types_of_Each_Decal_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDecal Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDecal.md)  
[IDecal Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDecal_members.md)  
[IDecal::GetMaskExcludedColorsCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDecal~GetMaskExcludedColorsCount.md)  
[IDecal::IGetMaskExcludedColors Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDecal~IGetMaskExcludedColors.md)  
[IDecal::ISetMaskExcludedColors Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDecal~ISetMaskExcludedColors.md)  
[IDecal::MaskFilename Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDecal~MaskFilename.md)  
[IDecal::MaskInvert Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDecal~MaskInvert.md)
