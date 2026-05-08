# Elliptical Property (IDomeFeatureData2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDomeFeatureData2~Elliptical`

Gets or sets whether this dome is a half ellipsoid, with a height equal to one of the ellipsoid radii.
Gets or sets whether this dome is a half ellipsoid, with a height equal to one of the ellipsoid radii.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Elliptical As System.Boolean
```

```

Dim instance As IDomeFeatureData2
Dim value As System.Boolean
 
instance.Elliptical = value
 
value = instance.Elliptical
```

```

System.bool Elliptical {get; set;}
```

```

property System.bool Elliptical {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True if the dome is elliptical, false if it is not

Remarks

This property does not affect geometry until you call [IFeature::ModifyDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~ModifyDefinition.md) or [IFeature::IModifyDefintion2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IModifyDefinition2.md).

Example

[Change Height of Dome (VBA)](Change_Height_of_Dome_Feature_Example_VB.htm)  
[Create and Modify Dome Feature (C#)](Create_and_Modify_Dome_Feature_Example_CSharp.htm)  
[Create and Modify Dome Feature (VB.NET)](Create_and_Modify_Dome_Feature_Example_VBNET.htm)  
[Create and Modify Dome Feature (VBA)](Create_and_Modify_Dome_Feature_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDomeFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDomeFeatureData2.md)  
[IDomeFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDomeFeatureData2_members.md)
