# GetSelectionsCount Method (IRefPointFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPointFeatureData~GetSelectionsCount`

Gets the number of entities selected to use to create the reference point.
Gets the number of entities selected to use to create the reference point.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetSelectionsCount() As System.Integer
```

```

Dim instance As IRefPointFeatureData
Dim value As System.Integer
 
value = instance.GetSelectionsCount()
```

```

System.int GetSelectionsCount()
```

```

System.int GetSelectionsCount(); 
```

#### Return Value

Number of selected entities

Remarks

Call this method before calling [IRefPointFeatureData::IGetSelections](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPointFeatureData~IGetSelections.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IRefPointFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPointFeatureData.md)  
[IRefPointFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPointFeatureData_members.md)  
[IRefPointFeatureData::ISetSelections Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPointFeatureData~ISetSelections.md)  
[IRefPointFeatureData::Selections Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPointFeatureData~Selections.md)
