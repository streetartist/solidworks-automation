# GetFeatureScopeBodiesCount Method (ISimpleHoleFeatureData2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleHoleFeatureData2~GetFeatureScopeBodiesCount`

Gets the number of solid bodies affected by the simple hole feature in a multibody part.
Gets the number of solid bodies affected by the simple hole feature in a multibody part.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetFeatureScopeBodiesCount() As System.Integer
```

```

Dim instance As ISimpleHoleFeatureData2
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

Number of solid bodies affected

Remarks

Call this method before calling [ISimpleHoleData2::IGetFeatureScopeBodies](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleHoleFeatureData2~IGetFeatureScopeBodies.md) to get the size of the array for that method.

 If [ISimpleHoleFeatureData2::FeatureScope](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleHoleFeatureData2~FeatureScope.md) is false, then count is 0.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISimpleHoleFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleHoleFeatureData2.md)  
[ISimpleHoleFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleHoleFeatureData2_members.md)  
[ISimpleHoleFeatureData2::ISetFeatureScopeBodies Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleHoleFeatureData2~ISetFeatureScopeBodies.md)  
[ISimpleHoleFeatureData2::FeatureScopeBodies Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleHoleFeatureData2~FeatureScopeBodies.md)  
[ISimpleHoleFeatureData2::AutoSelect Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleHoleFeatureData2~AutoSelect.md)
