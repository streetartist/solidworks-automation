# SetScale Method (ICavityFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICavityFeatureData~SetScale`

Sets the values by which to scale this cavity feature.
Sets the values by which to scale this cavity feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SetScale( _
   ByVal Xscale As System.Double, _
   ByVal YScale As System.Double, _
   ByVal ZScale As System.Double _
) 
```

```

Dim instance As ICavityFeatureData
Dim Xscale As System.Double
Dim YScale As System.Double
Dim ZScale As System.Double
 
instance.SetScale(Xscale, YScale, ZScale)
```

```

void SetScale( 
   System.double Xscale,
   System.double YScale,
   System.double ZScale
)
```

```

void SetScale( 
   System.double Xscale,
   System.double YScale,
   System.double ZScale
) 
```

#### Parameters

*Xscale*
:   Scaling value for the x direction

*YScale*
:   Scaling value for the y direction

*ZScale*
:   Scaling value for the z direction

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICavityFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICavityFeatureData.md)  
[ICavityFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICavityFeatureData_members.md)  
[ICavityFeatureData::GetScale Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICavityFeatureData~GetScale.md)  
[ICavityFeatureData::ScaleType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICavityFeatureData~ScaleType.md)  
[ICavityFeatureData::UniformScale Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICavityFeatureData~UniformScale.md)  
[ICavityFeatureData::UseUniformScale Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICavityFeatureData~UseUniformScale.md)
