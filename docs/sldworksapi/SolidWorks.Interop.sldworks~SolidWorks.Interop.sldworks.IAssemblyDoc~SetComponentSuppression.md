# SetComponentSuppression Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~SetComponentSuppression`

Suppresses, resolves, or sets to lightweight selected components of this assembly in the active configuration only.
Suppresses, resolves, or sets to lightweight selected components of this assembly in the active configuration only.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetComponentSuppression( _
   ByVal State As System.Integer _
) As System.Boolean
```

```

Dim instance As IAssemblyDoc
Dim State As System.Integer
Dim value As System.Boolean
 
value = instance.SetComponentSuppression(State)
```

```

System.bool SetComponentSuppression( 
   System.int State
)
```

```

System.bool SetComponentSuppression( 
   System.int State
) 
```

#### Parameters

*State*
:   State to set as defined by [swComponentSuppressionState\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swComponentSuppressionState_e.html) (see **Remarks**)

#### Return Value

True if the selected components are suppressed, resolved, or set to lightweight, false  
if not

Remarks

Only swComponentSuppressed, swComponentLightweight, or swComponentResolved are valid  
values for State. If you specify another value for State, this method does nothing.

This method works on selected components in the active configuration only.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.md)  
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.md)  
[IAssemblyDoc::LightweightAllResolved Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~LightweightAllResolved.md)  
[IAssemblyDoc::GetLightWeightComponentCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~GetLightWeightComponentCount.md)  
[IAssemblyDoc::MakeLightWeight Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~MakeLightWeight.md)  
[IAssemblyDoc::ResolveAllLightweight Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~ResolveAllLightweight.md)  
[IAssemblyDoc::ResolveAllLightWeightComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~ResolveAllLightWeightComponents.md)  
[IAssemblyDoc::ResolveOutOfDateLightWeightComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~ResolveOutOfDateLightWeightComponents.md)  
[IAssemblyDoc::SetComponentState Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~SetComponentState.md)  
[IComponent2::GetSuppression Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetSuppression.md)  
[IComponent2::IsSuppressed Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IsSuppressed.md)  
[IComponent2::SetSuppression2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~SetSuppression2.md)
