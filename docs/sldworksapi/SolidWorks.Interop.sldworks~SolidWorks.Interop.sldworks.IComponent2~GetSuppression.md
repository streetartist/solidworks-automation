# GetSuppression Method (IComponent2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetSuppression`

Obsolete. Superseded by IComponent2::GetSuppression2.
Obsolete. Superseded by [IComponent2::GetSuppression2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetSuppression2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetSuppression() As System.Integer
```

```

Dim instance As IComponent2
Dim value As System.Integer
 
value = instance.GetSuppression()
```

```

System.int GetSuppression()
```

```

System.int GetSuppression(); 
```

#### Return Value

Suppression state of this component instance as defined in [swComponentSuppressionState\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swComponentSuppressionState_e.html)

Remarks

Use this method to determine if the component is suppressed, lightweight, or fully resolved. It is critical to know the component's suppression state because lightweight and suppressed components contain only a small subset of data compared to a fully resolved component. For more information, see [Work With Lightweight Components](sldworksAPIProgGuide.chm::/OVERVIEW/Work_with_Lightweight_Components.htm).

Example

[Access Assembly (C++)](Access_Assembly_Example_CPlusPlus_COM.htm)  
[Change Material Properties (VBA)](Change_Material_Properties_Example_VB.htm)  
[Make Assembly Components Lightweight (VBA)](Make_Assembly_Components_Lightweight_Example_VB.htm)  
[Get Component State (C#)](Get_Component_State_Example_CSharp.htm)  
[Get Component State (VB.NET)](Get_Component_State_Example_VBNET.htm)  
[Get Component State (VBA)](Get_Component_State_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md)  
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.md)  
[IAssemblyDoc::LightweightAllResolved Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~LightweightAllResolved.md)  
[IAssemblyDoc::SetComponentState Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~SetComponentState.md)  
[IAssemblyDoc::SetComponentSuppression Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~SetComponentSuppression.md)  
[IComponent2::IsSuppressed Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IsSuppressed.md)  
[IComponent2::SetSuppression2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~SetSuppression2.md)
