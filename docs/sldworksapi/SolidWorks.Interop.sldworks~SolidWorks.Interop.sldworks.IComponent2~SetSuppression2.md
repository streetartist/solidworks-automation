# SetSuppression2 Method (IComponent2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~SetSuppression2`

Sets the suppression state of this component.
Sets the suppression state of this component.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetSuppression2( _
   ByVal State As System.Integer _
) As System.Integer
```

```

Dim instance As IComponent2
Dim State As System.Integer
Dim value As System.Integer
 
value = instance.SetSuppression2(State)
```

```

System.int SetSuppression2( 
   System.int State
)
```

```

System.int SetSuppression2( 
   System.int State
) 
```

#### Parameters

*State*
:   Suppression state of this component as defined in [swComponentSuppressionState\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swComponentSuppressionState_e.html)

#### Return Value

Status as defined in [swSuppressionError\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSuppressionError_e.html)

Remarks

SOLIDWORKS does not allow suppressing components while a PropertyManager page is open.

Example

[Access Assembly (C++)](Access_Assembly_Example_CPlusPlus_COM.htm)  
[Set All Assembly Components Lightweight or Resolved (VBA)](Set_All_Assembly_Components_Lightweight_or_Resolved_Example_VB.htm)  
[Set Fully Resolved Assembly to Lightweight (C#)](Set_Fully_Resolved_Assembly_to_Lightweight_Example_CSharp.htm)  
[Set Fully Resolved Assembly to Lightweight (VB.NET)](Set_Fully_Resolved_Assembly_to_Lightweight_Example_VBNET.htm)  
[Set Fully Resolved Assembly to Lightweight (VBA)](Set_Fully_Resolved_Assembly_to_Lightweight_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md)  
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.md)  
[IAssemblyDoc::LightweightAllResolved Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~LightweightAllResolved.md)  
[IAssemblyDoc::SetComponentSuppression Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~SetComponentSuppression.md)  
[IComponent2::GetSuppression Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetSuppression.md)  
[IComponent2::IsSuppressed Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IsSuppressed.md)  
[IComponent2::IsHidden Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IsHidden.md)  
[IAssemblyDoc::CompConfigProperties5 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~CompConfigProperties5.md)
