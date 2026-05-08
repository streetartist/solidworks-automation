# ScaleType Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICavityFeatureData~ScaleType`

Gets or sets the point about which scaling occurs in this cavity feature.
Gets or sets the point about which scaling occurs in this cavity feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ScaleType As System.Integer
```

```

Dim instance As ICavityFeatureData
Dim value As System.Integer
 
instance.ScaleType = value
 
value = instance.ScaleType
```

```

System.int ScaleType {get; set;}
```

```

property System.int ScaleType {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Scale type as defined in [swCavityScaleType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swCavityScaleType_e.html)

Example

[Create and Modify Cavity Feature (C#)](Create_and_Modify_Cavity_Feature_Example_CSharp.htm)  
[Create and Modify Cavity Feature (VB.NET)](Create_and_Modify_Cavity_Feature_Example_VBNET.htm)  
[Create and Modify Cavity Feature (VBA)](Create_and_Modify_Cavity_Feature_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICavityFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICavityFeatureData.md)  
[ICavityFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICavityFeatureData_members.md)  
[ICavityFeatureData::GetScale Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICavityFeatureData~GetScale.md)  
[ICavityFeatureData::SetScale Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICavityFeatureData~SetScale.md)  
[ICavityFeatureData::UniformScale Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICavityFeatureData~UniformScale.md)  
[ICavityFeatureData::UseUniformScale Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICavityFeatureData~UseUniformScale.md)
