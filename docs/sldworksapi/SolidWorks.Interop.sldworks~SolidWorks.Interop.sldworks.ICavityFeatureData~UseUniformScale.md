# UseUniformScale Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICavityFeatureData~UseUniformScale`

Gets or sets whether to uniformly scale this cavity feature.
Gets or sets whether to uniformly scale this cavity feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property UseUniformScale As System.Boolean
```

```

Dim instance As ICavityFeatureData
Dim value As System.Boolean
 
instance.UseUniformScale = value
 
value = instance.UseUniformScale
```

```

System.bool UseUniformScale {get; set;}
```

```

property System.bool UseUniformScale {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to use a uniform scaling value, false to not

Remarks

Use [ICavityFeatureData::UniformScale](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICavityFeatureData~UniformScale.md) to set the uniform scaling value for this cavity feature.

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
[ICavityFeatureData::ScaleType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICavityFeatureData~ScaleType.md)
