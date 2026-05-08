# AccessSelections Method (ILibraryFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData~AccessSelections`

Gains access to selections that define this library feature.
Gains access to selections that define this library feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function AccessSelections( _
   ByVal PTopDoc As ModelDoc2, _
   ByVal PComponent As Component2 _
) As System.Boolean
```

```

Dim instance As ILibraryFeatureData
Dim PTopDoc As ModelDoc2
Dim PComponent As Component2
Dim value As System.Boolean
 
value = instance.AccessSelections(PTopDoc, PComponent)
```

```

System.bool AccessSelections( 
   ModelDoc2 PTopDoc,
   Component2 PComponent
)
```

```

System.bool AccessSelections( 
   ModelDoc2^ PTopDoc,
   Component2^ PComponent
) 
```

#### Parameters

*PTopDoc*
:   Top-level document (see **Remarks**)

*PComponent*
:   Component in which the feature is to be modified (see **Remarks**)

#### Return Value

True if the selections were successfully accessed, false if not

Remarks

|  |  |
| --- | --- |
| **To modify a feature in a...** | **Then...** |
| Part | - PTopDoc argument is the [IModelDoc2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md) for the part - PComponent argument is NULL |
| Assembly | - PTopDoc is the IModelDoc2 object for the assembly - PComponent argument is the [IComponent2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md) object in which the feature is to be modified |

This method puts the model into a rollback state to allow access to the selections that define this feature. You must use either of the following methods to restore the rollback state:

- [IFeature::ModifyDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~ModifyDefinition.md) or [IFeature::IModifyDefinition2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IModifyDefinition2.md) if you modified the feature
- [ILibraryFeatureData::ReleaseSelectionAccess](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData~ReleaseSelectionAccess.md) if you did not

Example

[Get Library Feature Data (VBA)](Get_Library_Feature_Data_Example_VB.htm)  
[Get Library Feature Data (VB.NET)](Get_Library_Feature_Data_Example_VBNET.htm)  
[Get Library Feature Data (C#)](Get_Library_Feature_Data_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ILibraryFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData.md)  
[ILibraryFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData_members.md)
