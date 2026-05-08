# GetSelections Method (IRefAxisFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefAxisFeatureData~GetSelections`

Gets the selected entities for this reference axis feature.
Gets the selected entities for this reference axis feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetSelections( _
   ByRef EntitiesTypeVar As System.Object _
) As System.Object
```

```

Dim instance As IRefAxisFeatureData
Dim EntitiesTypeVar As System.Object
Dim value As System.Object
 
value = instance.GetSelections(EntitiesTypeVar)
```

```

System.object GetSelections( 
   out System.object EntitiesTypeVar
)
```

```

System.Object^ GetSelections( 
   [Out] System.Object^ EntitiesTypeVar
) 
```

#### Parameters

*EntitiesTypeVar*
:   Array of the types of selected entities for this reference axis feature as defined by [swSelectType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSelectType_e.html)

#### Return Value

Array of the selected entities

Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

Example

[Get Selections for Reference Axis Feature (C#)](Get_Selections_for_Reference_Axis_Feature_Example_CSharp.htm)  
[Get Selections for Reference Axis Feature (VB.NET)](Get_Selections_for_Reference_Axis_Feature_Example_VBNET.htm)  
[Get Selections for Reference Axis Feature (VBA)](Get_Selections_for_Reference_Axis_Feature_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IRefAxisFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefAxisFeatureData.md)  
[IRefAxisFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefAxisFeatureData_members.md)  
[IRefAxisFeatureData::IGetSelections Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefAxisFeatureData~IGetSelections.md)  
[IRefAxisFeatureData::GetSelectionsCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefAxisFeatureData~GetSelectionsCount.md)  
[IRefAxisFeatureData::ISetSelections Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefAxisFeatureData~ISetSelections.md)  
[IRefAxisFeatureData::SetSelections Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefAxisFeatureData~SetSelections.md)
