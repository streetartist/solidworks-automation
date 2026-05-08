# PartingType Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingSurfaceFeatureData~PartingType`

Gets or sets the type of parting surface.
Gets or sets the type of parting surface.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property PartingType As System.Integer
```

```

Dim instance As IPartingSurfaceFeatureData
Dim value As System.Integer
 
instance.PartingType = value
 
value = instance.PartingType
```

```

System.int PartingType {get; set;}
```

```

property System.int PartingType {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Type of parting surface as defined in [swPartingSurfaceMoldParmType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPartingSurfaceMoldParmType_e.html) (see **Remarks**)

Remarks

swPartingSurfaceMoldParmType\_e.swPartingSurfaceMoldParmTangent is not available for some geometry.

Example

[Get and Set Parting Surface Feature Data (C#)](Get_and_Set_Parting_Surface_Feature_Data_Example_CSharp.htm)  
[Get and Set Parting Surface Feature Data (VB.NET)](Get_and_Set_Parting_Surface_Feature_Data_Example_VBNET.htm)  
[Get and Set Parting Surface Feature Data (VBA)](Get_and_Set_Parting_Surface_Feature_Data_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPartingSurfaceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingSurfaceFeatureData.md)  
[IPartingSurfaceFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingSurfaceFeatureData_members.md)  
[IPartingSurfaceFeatureData::ReverseAlignment Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingSurfaceFeatureData~ReverseAlignment.md)  
[IPartingSurfaceFeatureData::OffsetAngle Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingSurfaceFeatureData~OffsetAngle.md)
