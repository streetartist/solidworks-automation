# GetSelectionsCount Method (IRefAxisFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefAxisFeatureData~GetSelectionsCount`

Gets the number of selections that define this reference axis feature.
Gets the number of selections that define this reference axis feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetSelectionsCount() As System.Integer
```

```

Dim instance As IRefAxisFeatureData
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

Number of selections that define this reference axis featu

Remarks

Call this method before calling [IRefAxisFeatureData::IGetSelections](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefAxisFeatureData~IGetSelections.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IRefAxisFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefAxisFeatureData.md)  
[IRefAxisFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefAxisFeatureData_members.md)  
[IRefAxisFeatureData::GetSelections Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefAxisFeatureData~GetSelections.md)  
[IRefAxisFeatureData::ISetSelections Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefAxisFeatureData~ISetSelections.md)  
[IRefAxisFeatureData::SetSelections Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefAxisFeatureData~SetSelections.md)
