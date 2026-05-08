# AccessSelections Method (IBrokenOutSectionFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBrokenOutSectionFeatureData~AccessSelections`

Gains access to the selections that define this broken-out section feature.
Gains access to the selections that define this broken-out section feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function AccessSelections( _
   ByVal TopDoc As System.Object, _
   ByVal Component As System.Object _
) As System.Boolean
```

```

Dim instance As IBrokenOutSectionFeatureData
Dim TopDoc As System.Object
Dim Component As System.Object
Dim value As System.Boolean
 
value = instance.AccessSelections(TopDoc, Component)
```

```

System.bool AccessSelections( 
   System.object TopDoc,
   System.object Component
)
```

```

System.bool AccessSelections( 
   System.Object^ TopDoc,
   System.Object^ Component
) 
```

#### Parameters

*TopDoc*
:   Top-level document

*Component*
:   Component in which the feature is to be modified

#### Return Value

True if the selections were successfully accessed, false if not

Remarks

|  |  |
| --- | --- |
| **To modify a feature in a...** | **Then...** |
| Part | - TopDoc argument is the [IModelDoc2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md) for the part - Component argument is NULL |
| Assembly | - TopDoc argument is the IModelDoc2 object for the assembly - Component argument is the [IComponent2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md) object in which the feature is to be modified |

This method puts the model into a rollback state to allow access to the selections that define this feature. You must use either of the following methods to restore the rollback state:

- [IFeature::ModifyDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~ModifyDefinition.md) if you modified the feature
- [IBrokenOutSectionFeatureData::ReleaseSelectionAccess](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBrokenOutSectionFeatureData~ReleaseSelectionAccess.md) if you did not

Example

[Get Broken-Out Section Feature Data (C#)](Get_Broken_Out_Section_Feature_Data_Example_CSharp.htm)  
[Get Broken-Out Section Feature Data (VB.NET)](Get_Broken_Out_Section_Feature_Data_Example_VBNET.htm)  
[Get Broken-Out Section Feature Data (VBA)](Get_Broken_Out_Section_Feature_Data_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBrokenOutSectionFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBrokenOutSectionFeatureData.md)  
[IBrokenOutSectionFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBrokenOutSectionFeatureData_members.md)  
[IBrokenOutSectionFeatureData::IAccessSelections Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBrokenOutSectionFeatureData~IAccessSelections.md)
