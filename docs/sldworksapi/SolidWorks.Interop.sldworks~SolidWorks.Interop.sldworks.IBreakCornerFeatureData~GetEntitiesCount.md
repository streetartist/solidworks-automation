# GetEntitiesCount Method (IBreakCornerFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBreakCornerFeatureData~GetEntitiesCount`

Gets the number of faces or edges associated with this break corner feature.
Gets the number of faces or edges associated with this break corner feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetEntitiesCount() As System.Integer
```

```

Dim instance As IBreakCornerFeatureData
Dim value As System.Integer
 
value = instance.GetEntitiesCount()
```

```

System.int GetEntitiesCount()
```

```

System.int GetEntitiesCount(); 
```

#### Return Value

Number of faces or edges

Remarks

Call this method before calling [IBreakCornerFeatureData::IGetEntities](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBreakCornerFeatureData~IGetEntities.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBreakCornerFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBreakCornerFeatureData.md)  
[IBreakCornerFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBreakCornerFeatureData_members.md)
