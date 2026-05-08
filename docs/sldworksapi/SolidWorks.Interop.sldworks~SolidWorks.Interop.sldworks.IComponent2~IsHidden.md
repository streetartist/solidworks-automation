# IsHidden Method (IComponent2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IsHidden`

Gets whether this component is hidden or suppressed.
Gets whether this component is hidden or suppressed.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IsHidden( _
   ByVal ConsiderSuppressed As System.Boolean _
) As System.Boolean
```

```

Dim instance As IComponent2
Dim ConsiderSuppressed As System.Boolean
Dim value As System.Boolean
 
value = instance.IsHidden(ConsiderSuppressed)
```

```

System.bool IsHidden( 
   System.bool ConsiderSuppressed
)
```

```

System.bool IsHidden( 
   System.bool ConsiderSuppressed
) 
```

#### Parameters

*ConsiderSuppressed*
:   Controls whether suppressed components are hidden

#### Return Value

True or false (see **Remarks**)

Remarks

The state of this component can vary based on the active configuration.

|  |  |  |  |
| --- | --- | --- | --- |
| ConsiderSuppressed | Component | Component | IsHidden |
| True | Hidden | Unsuppressed | True |
| True | Hidden | Suppressed | True |
| True | Shown | Unsuppressed | False |
| True | Shown | Suppressed | True |
| False | Hidden | Unsuppressed | True |
| False | Hidden | Suppressed | True |
| False | Shown | Unsuppressed | False |
| False | Shown | Suppressed | False |

NOTE: For [lightweight](sldworksAPIProgGuide.chm::/OVERVIEW/Work_with_Lightweight_Components.htm) components, IsHidden returns True if ConsiderSuppressed is True.

Example

[Change Material Properties (VBA)](Change_Material_Properties_Example_VB.htm)  
[Get Transforms of Assembly Components (VBA)](Get_Transforms_of_Assembly_Components_Example_VB.htm)  
[Get Component State (C#)](Get_Component_State_Example_CSharp.htm)  
[Get Component State (VB.NET](Get_Component_State_Example_VBNET.htm)  
[Get Component State (VBA)](Get_Component_State_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md)  
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.md)  
[IComponent2::ISetVisibility Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~ISetVisibility.md)  
[IComponent2::IsSuppressed Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IsSuppressed.md)  
[IComponent2::SetSuppression2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~SetSuppression2.md)  
[IComponent2::SetVisibility Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~SetVisibility.md)  
[IComponent2::Visible Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~Visible.md)
