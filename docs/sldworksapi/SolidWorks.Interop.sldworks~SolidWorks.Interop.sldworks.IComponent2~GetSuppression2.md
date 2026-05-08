# GetSuppression2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetSuppression2`

Gets the suppression state of this component.
Gets the suppression state of this component.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetSuppression2() As System.Integer
```

```

Dim instance As IComponent2
Dim value As System.Integer
 
value = instance.GetSuppression2()
```

```

System.int GetSuppression2()
```

```

System.int GetSuppression2(); 
```

#### Return Value

Suppression state of this component or internal ID mismatch error code as defined in [swComponentSuppressionState\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swComponentSuppressionState_e.html)

Remarks

The difference between this method and the now obsolete IComponent2::GetSuppression is that this method returns an error code (5 = swComponentSuppressionState\_e.swComponentInternalIdMismatch) if there is an internal ID mismatch.

Use this method to determine if the component is suppressed, lightweight, or fully resolved. It is critical to know the component's suppression state because lightweight and suppressed components contain only a small subset of data compared to a fully resolved component. For more information, see [Work With Lightweight Components](sldworksAPIProgGuide.chm::/OVERVIEW/Work_with_Lightweight_Components.htm).

Example

[Get and Set Component's Suppression State (VBA)](Get_and_Set_Component_s_Suppression_State_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md)  
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.md)  
[IAssemblyDoc::LightweightAllResolved Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~LightweightAllResolved.md)  
[IAssemblyDoc::SetComponentState Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~SetComponentState.md)  
[IAssemblyDoc::SetComponentSuppression Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~SetComponentSuppression.md)  
[IComponent2::IsSuppressed Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IsSuppressed.md)  
[IComponent2::SetSuppression2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~SetSuppression2.md)
