# GetFeatureScopeBodiesCount Method (IExtrudeFeatureData2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~GetFeatureScopeBodiesCount`

Gets the number of solid bodies affected by the extrude feature in a multibody part.
Gets the number of solid bodies affected by the extrude feature in a multibody part.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetFeatureScopeBodiesCount() As System.Integer
```

```

Dim instance As IExtrudeFeatureData2
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

Call this method before calling [IExtrudeFeatureData2::IGetFeatureScopeBodies](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~IGetFeatureScopeBodies.md).

If [IExtrudeFeatureData2::FeatureScope](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~FeatureScope.md) is false, then count will be 0.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IExtrudeFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2.md)  
[IExtrudeFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2_members.md)  
[IExtrudeFeatureData2::AutoSelect Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~AutoSelect.md)  
[IExtrudeFeatureData2::FeatureScopeBodies Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~FeatureScopeBodies.md)  
[IExtrudeFeatureData2::ISetFeatureScopeBodies Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~ISetFeatureScopeBodies.md)
