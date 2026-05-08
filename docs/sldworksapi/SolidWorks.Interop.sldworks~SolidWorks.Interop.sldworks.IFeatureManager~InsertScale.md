# InsertScale Method (IFeatureManager)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertScale`

Applies the specified scaling to either the current model or a selected graphic body.
Applies the specified scaling to either the current model or a selected graphic body.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertScale( _
   ByVal Type As System.Short, _
   ByVal Uniform As System.Boolean, _
   ByVal Xscale As System.Double, _
   ByVal YScale As System.Double, _
   ByVal ZScale As System.Double _
) As Feature
```

```

Dim instance As IFeatureManager
Dim Type As System.Short
Dim Uniform As System.Boolean
Dim Xscale As System.Double
Dim YScale As System.Double
Dim ZScale As System.Double
Dim value As Feature
 
value = instance.InsertScale(Type, Uniform, Xscale, YScale, ZScale)
```

```

Feature InsertScale( 
   System.short Type,
   System.bool Uniform,
   System.double Xscale,
   System.double YScale,
   System.double ZScale
)
```

```

Feature^ InsertScale( 
   System.short Type,
   System.bool Uniform,
   System.double Xscale,
   System.double YScale,
   System.double ZScale
) 
```

#### Parameters

*Type*
:   Value as defined in [swScaleType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swScaleType_e.html)

*Uniform*
:   True if scaling should be uniform, false if not

*Xscale*
:   X direction scale factor

*YScale*
:   Y direction scale factor; valid only if Uniform is false

*ZScale*
:   Z direction scale factor; valid only if Uniform is false

#### Return Value

[IFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md) if scaling the current model; Null or Nothing if scaling a selected graphic body

Remarks

To scale a graphic body:

1. Select the graphic body in the Graphic Bodies folder of the FeatureManager design tree.
2. Call this method.

This method scales the selected graphic body up in the graphics view, but no scale feature is created.

|  |  |
| --- | --- |
| **If Uniform is...** | **Then the scaling factor is...** |
| True | Xscale, applied in three directions. |
| False | All three scaling factors (Xscale, YScale, and ZScale). |

Use [IFeature::GetDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetDefinition.md) and [IFeature::IGetDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IGetDefinition.md) and [IFeature::ModifyDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~ModifyDefinition.md) and [IFeature::IModifyDefinition2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IModifyDefinition2.md) to gain access to the [IScaleFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IScaleFeatureData.md) object.

Example

[Insert Scale Feature (VBA)](Insert_Scale_Feature_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.md)  
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.md)  
[IScaleFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IScaleFeatureData.md)
