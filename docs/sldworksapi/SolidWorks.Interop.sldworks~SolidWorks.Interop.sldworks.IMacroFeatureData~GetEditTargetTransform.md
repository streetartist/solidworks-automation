# GetEditTargetTransform Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetEditTargetTransform`

Gets the transform of the component where the macro feature resides if at least one selection in the macro feature belongs to a different component.
Gets the transform of the component where the macro feature resides if at least one selection in the macro feature belongs to a different component.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetEditTargetTransform() As MathTransform
```

```

Dim instance As IMacroFeatureData
Dim value As MathTransform
 
value = instance.GetEditTargetTransform()
```

```

MathTransform GetEditTargetTransform()
```

```

MathTransform^ GetEditTargetTransform(); 
```

#### Return Value

[Math transform](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathTransform.md) of the component where the macro feature resides if at least one selection in the macro feature belongs to a different component, or NULL if all of the selections in the macro feature belong to the component where the macro feature resides

Remarks

When [regenerating a macro feature](sldworksapiprogguide.chm::/Macro_Features/Rebuild_Function.htm) in a part that is a component in an assembly, you cannot get the component's transform where the macro feature resides because you cannot get the component using [IEntity::GetComponent](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEntity~GetComponent.md) or [IEntity::IGetComponent2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEntity~IGetComponent2.md) in a part document. However, you may need the component's transform because references from other components to it often need to be transformed.

This method provides this transform. If there are no external references among the macro feature selections ([IMacroFeatureData::GetSelections3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetSelections3.md) or [IMacroFeatureData::IGetSelections3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~IGetSelections3.md)), then this method returns NULL. If there are external references among the macro feature selections, then this method returns the transform of the component where the macro feature resides.

For example, if the macro feature includes a selection box in which the user can select a face, and the user selects a face on a different component, then this method can get the component's transform where the macro feature resides. However, if all of the selections in the macro feature belong to the component where the macro feature resides, then this method returns NULL because you probably will not need the transform. See also [Macro Features and Component Transforms](sldworksapiprogguide.chm::/Macro_Features/Macro_Features_and_Component_Transforms.htm).

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMacroFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData.md)  
[IMacroFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData_members.md)  
[IMacroFeatureData::FeatureTransform Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~FeatureTransform.md)  
[IMacroFeatureData::PatternTransform Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~PatternTransform.md)
