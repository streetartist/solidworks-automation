# IAccessSelections2 Method (IBaseFlangeFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~IAccessSelections2`

Allows access to the selections that describe this base flange feature.
Allows access to the selections that describe this base flange feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IAccessSelections2( _
   ByVal TopDoc As ModelDoc2, _
   ByVal Component As Component2 _
) As System.Boolean
```

```

Dim instance As IBaseFlangeFeatureData
Dim TopDoc As ModelDoc2
Dim Component As Component2
Dim value As System.Boolean
 
value = instance.IAccessSelections2(TopDoc, Component)
```

```

System.bool IAccessSelections2( 
   ModelDoc2 TopDoc,
   Component2 Component
)
```

```

System.bool IAccessSelections2( 
   ModelDoc2^ TopDoc,
   Component2^ Component
) 
```

#### Parameters

*TopDoc*
:   Top-level document

*Component*
:   Component in which the feature is to be modified

#### Return Value

True if the selections are successfully accessed, false if not

Remarks

|  |  |
| --- | --- |
| **To modify a feature in a...** | **Then...** |
| Part | - TopDoc argument is the [IModelDoc2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md) for the part - Component argument is NULL |
| Assembly | - TopDoc argument is the IModelDoc2 object for the assembly - Component argument is the [IComponent2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md) object in which the feature is to be modified |

This method puts the model into a rollback state to allow access to the selections that define this feature. You must use either of the following methods to restore the rollback state:

- [IFeature::IModifyDefinition2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IModifyDefinition2.md) if you modified the feature
- [IBaseFlangeFeatureData::ReleaseSelectionAccess](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~ReleaseSelectionAccess.md) if you did not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBaseFlangeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData.md)  
[IBaseFlangeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData_members.md)  
[IBaseFlangeFeatureData::AccessSelections Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~AccessSelections.md)
