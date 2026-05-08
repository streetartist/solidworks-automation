# ResolveAllLightWeightComponents Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~ResolveAllLightWeightComponents`

Resolves the lightweight components in this assembly.
Resolves the lightweight components in this assembly.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ResolveAllLightWeightComponents( _
   ByVal WarnUser As System.Boolean _
) As System.Integer
```

```

Dim instance As IAssemblyDoc
Dim WarnUser As System.Boolean
Dim value As System.Integer
 
value = instance.ResolveAllLightWeightComponents(WarnUser)
```

```

System.int ResolveAllLightWeightComponents( 
   System.bool WarnUser
)
```

```

System.int ResolveAllLightWeightComponents( 
   System.bool WarnUser
) 
```

#### Parameters

*WarnUser*
:   True prompts the user to resolve components, false does not

#### Return Value

Status of resolving the components as defined in [swComponentResolveStatus\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swComponentResolveStatus_e.html)

Remarks

The assembly must be open in its own window. Call [ISldWorks::ActivateDoc2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~ActivateDoc2.md) or [IModelDoc2::Visible](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~Visible.md) to ensure that it is. If the assembly is only open as a reference in another document, then this method returns swComponentResolveStatus\_e.swResolveNotPerformed.

Example

[Get Display Dimensions, GTols, and Surface-finish Symbols (VBA)](Get_Display_Dimensions,_Gtols,_and_Surface-Finish_Symbols_Example_VB.htm)  
[Get Visibility of and Resolve Lightweight Components (VBA)](Get_Visibility_of_and_Resolve_Lightweight_Components_Example_VB.htm)  
[Lock all External References (VBA)](Lock_All_External_References_Example_VB.htm)  
[Resolve All Components and Fix a Component (C#)](Resolve_All_Components_Fix_A_Component_Example_CSharp.htm)  
[Resolve All Components and Fix a Component (VB.NET)](Resolve_All_Components_Fix_A_Component_Example_VBNET.htm)  
[Resolve All Components and Fix a Component (VBA)](Resolve_All_Components_Fix_A_Component_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.md)  
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.md)  
[IAssemblyDoc::GetLightWeightComponentCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~GetLightWeightComponentCount.md)  
[IAssemblyDoc::LightweightAllResolved Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~LightweightAllResolved.md)  
[IAssemblyDoc::ResolveAllLightweight Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~ResolveAllLightweight.md)  
[IAssemblyDoc::ResolveOutOfDateLightWeightComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~ResolveOutOfDateLightWeightComponents.md)  
[IAssemblyDoc::SetComponentSuppression Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~SetComponentSuppression.md)  
[IAssemblyDoc::SelectiveOpen Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~SelectiveOpen.md)
