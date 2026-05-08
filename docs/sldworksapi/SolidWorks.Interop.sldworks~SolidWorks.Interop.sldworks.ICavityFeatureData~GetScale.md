# GetScale Method (ICavityFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICavityFeatureData~GetScale`

Gets the values used to scale this cavity feature.
Gets the values used to scale this cavity feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub GetScale( _
   ByRef Xscale As System.Double, _
   ByRef YScale As System.Double, _
   ByRef ZScale As System.Double _
) 
```

```

Dim instance As ICavityFeatureData
Dim Xscale As System.Double
Dim YScale As System.Double
Dim ZScale As System.Double
 
instance.GetScale(Xscale, YScale, ZScale)
```

```

void GetScale( 
   out System.double Xscale,
   out System.double YScale,
   out System.double ZScale
)
```

```

void GetScale( 
   [Out] System.double Xscale,
   [Out] System.double YScale,
   [Out] System.double ZScale
) 
```

#### Parameters

*Xscale*
:   Scaling value for the x direction

*YScale*
:   Scaling value for the y direction

*ZScale*
:   Scaling value for the z direction

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
[ICavityFeatureData::SetScale Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICavityFeatureData~SetScale.md)  
[ICavityFeatureData::ScaleType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICavityFeatureData~ScaleType.md)  
[ICavityFeatureData::UniformScale Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICavityFeatureData~UniformScale.md)  
[ICavityFeatureData::UseUniformScale Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICavityFeatureData~UseUniformScale.md)
