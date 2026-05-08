# GetFeatureScopeBodiesCount Method (IThickenFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThickenFeatureData~GetFeatureScopeBodiesCount`

Gets the number of solid bodies affected by the thicken feature in a multibody part.
Gets the number of solid bodies affected by the thicken feature in a multibody part.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetFeatureScopeBodiesCount() As System.Integer
```

```

Dim instance As IThickenFeatureData
Dim value As System.Integer
 
value = instance.GetFeatureScopeBodiesCount()
```

```

System.int GetFeatureScopeBodiesCount()
```

```

System.int GetFeatureScopeBodiesCount(); 
```

#### Return Value

Number of solid bodies affected by the thicken feature

Remarks

COM users must call this method before calling the [IThickenFeatureData::IGetFeatureScopeBodies](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThickenFeatureData~IGetFeatureScopeBodies.md) method.

If [IThickenFeatureData::FeatureScope](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThickenFeatureData~FeatureScope.md) is false, then count is 0.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IThickenFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThickenFeatureData.md)  
[IThickenFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThickenFeatureData_members.md)  
[IThickenFeatureData::ISetFeatureScopeBodies Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThickenFeatureData~ISetFeatureScopeBodies.md)  
[IThickenFeatureData::FeatureScopeBodies Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThickenFeatureData~FeatureScopeBodies.md)  
[IThickenFeatureData::AutoSelect Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThickenFeatureData~AutoSelect.md)
