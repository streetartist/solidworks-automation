# GetComponentsCount Method (IHoleSeriesFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData~GetComponentsCount`

Obsolete. Superseded by IHoleSeriesFeatureData2::GetComponentsCount.
Obsolete. Superseded by [IHoleSeriesFeatureData2::GetComponentsCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData2~GetComponentsCount.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetComponentsCount() As System.Integer
```

```

Dim instance As IHoleSeriesFeatureData
Dim value As System.Integer
 
value = instance.GetComponentsCount()
```

```

System.int GetComponentsCount()
```

```

System.int GetComponentsCount(); 
```

#### Return Value

Number of components in this hole series

Remarks

Call this method before calling [IHoleSeriesFeatureData::IGetComponents](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData~IGetComponents.md) to get the size of the array for that method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IHoleSeriesFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData.md)  
[IHoleSeriesFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData_members.md)  
[IHoleSeriesFeatureData::GetComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData~GetComponents.md)
