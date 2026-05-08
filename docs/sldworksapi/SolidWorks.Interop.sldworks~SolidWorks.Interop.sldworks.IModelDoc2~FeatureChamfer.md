# FeatureChamfer Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~FeatureChamfer`

Creates a chamfer feature.
Creates a chamfer feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub FeatureChamfer( _
   ByVal Width As System.Double, _
   ByVal Angle As System.Double, _
   ByVal Flip As System.Boolean _
) 
```

```

Dim instance As IModelDoc2
Dim Width As System.Double
Dim Angle As System.Double
Dim Flip As System.Boolean
 
instance.FeatureChamfer(Width, Angle, Flip)
```

```

void FeatureChamfer( 
   System.double Width,
   System.double Angle,
   System.bool Flip
)
```

```

void FeatureChamfer( 
   System.double Width,
   System.double Angle,
   System.bool Flip
) 
```

#### Parameters

*Width*
:   Width of the chamfer in meters

*Angle*
:   Angle of the chamfer

*Flip*
:   - 0 if angle is to be measured from the right face
    - 1 if angle is to be measured from the left face

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)  
[IChamferFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChamferFeatureData2.md)
