# SetScale Method (IScaleFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IScaleFeatureData~SetScale`

Sets the scale factor for this scale feature in the x, y,and z directions.
Sets the scale factor for this scale feature in the x, y,and z directions.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SetScale( _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Z As System.Double, _
   ByVal Uniform As System.Boolean _
) 
```

```

Dim instance As IScaleFeatureData
Dim X As System.Double
Dim Y As System.Double
Dim Z As System.Double
Dim Uniform As System.Boolean
 
instance.SetScale(X, Y, Z, Uniform)
```

```

void SetScale( 
   System.double X,
   System.double Y,
   System.double Z,
   System.bool Uniform
)
```

```

void SetScale( 
   System.double X,
   System.double Y,
   System.double Z,
   System.bool Uniform
) 
```

#### Parameters

*X*
:   X-direction scale factor

*Y*
:   Y-direction scale factor

*Z*
:   Z-direction scale factor

*Uniform*
:   True for uniform scaling, false for non-uniform scaling

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IScaleFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IScaleFeatureData.md)  
[IScaleFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IScaleFeatureData_members.md)  
[IScaleFeatureData::GetScale Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IScaleFeatureData~GetScale.md)  
[IScaleFeatureData::IsUniform Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IScaleFeatureData~IsUniform.md)  
[IScaleFeatureData::ScaleUniform Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IScaleFeatureData~ScaleUniform.md)  
[IScaleFeatureData::ScaleX Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IScaleFeatureData~ScaleX.md)  
[IScaleFeatureData::ScaleY Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IScaleFeatureData~ScaleY.md)  
[IScaleFeatureData::ScaleZ Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IScaleFeatureData~ScaleZ.md)
