# GetBodiesCount Method (IScaleFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IScaleFeatureData~GetBodiesCount`

Gets the number of scaled bodies for this scale feature.
Gets the number of scaled bodies for this scale feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetBodiesCount() As System.Integer
```

```

Dim instance As IScaleFeatureData
Dim value As System.Integer
 
value = instance.GetBodiesCount()
```

```

System.int GetBodiesCount()
```

```

System.int GetBodiesCount(); 
```

#### Return Value

Number of bodies that are scaled

Remarks

Call this method before calling [IScaleFeatureDta::IGetBodies](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IScaleFeatureData~IGetBodies.md) to get the size of the array for that method.

Example

See [IScaleFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IScaleFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IScaleFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IScaleFeatureData.md)  
[IScaleFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IScaleFeatureData_members.md)  
[IScaleFeatureData::IGetBodies Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IScaleFeatureData~IGetBodies.md)  
[IScaleFeatureData::ISetBodies Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IScaleFeatureData~ISetBodies.md)  
[IScaleFeatureData::Bodies Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IScaleFeatureData~Bodies.md)
