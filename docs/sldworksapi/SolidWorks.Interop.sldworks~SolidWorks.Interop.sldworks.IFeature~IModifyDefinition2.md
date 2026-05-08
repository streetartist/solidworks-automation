# IModifyDefinition2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IModifyDefinition2`

Updates the definition of a feature with the new values in an associated feature data object obtained with IFeature::IGetDefinition.
Updates the definition of a feature with the new values in an associated feature data object obtained with [IFeature::IGetDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IGetDefinition.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IModifyDefinition2( _
   ByVal Data As System.Object, _
   ByVal TopDoc As ModelDoc2, _
   ByVal Component As Component2 _
) As System.Boolean
```

```

Dim instance As IFeature
Dim Data As System.Object
Dim TopDoc As ModelDoc2
Dim Component As Component2
Dim value As System.Boolean
 
value = instance.IModifyDefinition2(Data, TopDoc, Component)
```

```

System.bool IModifyDefinition2( 
   System.object Data,
   ModelDoc2 TopDoc,
   Component2 Component
)
```

```

System.bool IModifyDefinition2( 
   System.Object^ Data,
   ModelDoc2^ TopDoc,
   Component2^ Component
) 
```

#### Parameters

*Data*
:   IUnknown interface to the feature data object; use QueryInterface to get the interface to the actual object

*TopDoc*
:   Top-level document (see **Remarks**)

*Component*
:   Component for the feature (see **Remarks**)

#### Return Value

True if the feature is updated successfully, false if not

Remarks

| **To modify a feature in...** | **Then TopDoc argument...** |
| --- | --- |
| A part | Is the [IModelDoc2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md) object for the part and the Component argument should be Nothing or null |
| An assembly | Should be the assembly IModelDoc2 object and the Component argument should be the [IComponent2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md) object in which the feature is to be modified |

When you modify a feature in an assembly, this method leaves the assembly in Editing Part mode. You can switch back to editing the assembly by calling [IAssemblyDoc::EditAssembly](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~EditAssembly.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md)  
[IFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature_members.md)  
[IFeature::GetDefinition Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetDefinition.md)  
[IFeature::ModifyDefinition Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~ModifyDefinition.md)
