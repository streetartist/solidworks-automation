# GetUnloadedComponentNames Method (IComponent2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetUnloadedComponentNames`

Gets the component's unloaded children components' path names, referenced configuration names, reasons why they are unloaded, document types, and names.
Gets the component's unloaded children components' path names, referenced configuration names, reasons why they are unloaded, document types, and names.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetUnloadedComponentNames( _
   ByRef UnloadedComponentPathNames As System.Object, _
   ByRef UnloadedComponentReferencedConfigurationNames As System.Object, _
   ByRef ReasonForUnloadingComponents As System.Object, _
   ByRef DocTypes As System.Object _
) As System.Object
```

```

Dim instance As IComponent2
Dim UnloadedComponentPathNames As System.Object
Dim UnloadedComponentReferencedConfigurationNames As System.Object
Dim ReasonForUnloadingComponents As System.Object
Dim DocTypes As System.Object
Dim value As System.Object
 
value = instance.GetUnloadedComponentNames(UnloadedComponentPathNames, UnloadedComponentReferencedConfigurationNames, ReasonForUnloadingComponents, DocTypes)
```

```

System.object GetUnloadedComponentNames( 
   out System.object UnloadedComponentPathNames,
   out System.object UnloadedComponentReferencedConfigurationNames,
   out System.object ReasonForUnloadingComponents,
   out System.object DocTypes
)
```

```

System.Object^ GetUnloadedComponentNames( 
   [Out] System.Object^ UnloadedComponentPathNames,
   [Out] System.Object^ UnloadedComponentReferencedConfigurationNames,
   [Out] System.Object^ ReasonForUnloadingComponents,
   [Out] System.Object^ DocTypes
) 
```

#### Parameters

*UnloadedComponentPathNames*
:   Array of children components' path names

*UnloadedComponentReferencedConfigurationNames*
:   Array of children components' referenced configuration names

*ReasonForUnloadingComponents*
:   Array indicating the reason each child component is unloaded as defined by [swComponentLoadStatus\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swComponentLoadStatus_e.html)

*DocTypes*
:   Array of document types as defined in [swDocumentTypes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDocumentTypes_e.html)

#### Return Value

Array of children components' names

Remarks

This method is useful when the assembly document was opened with **[Quick View/Selective open](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification~Selective.md)**.

To get whether a component has hidden or suppressed children components, call [IComponent2::HasUnloadedComponents](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~HasUnloadedComponents.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md)  
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.md)  
[IComponent2::GetHiddenUnloadedChildrenCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetHiddenUnloadedChildrenCount.md)  
[IComponent2::HasUnloadedComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~HasUnloadedComponents.md)  
[IAssemblyDoc::GetUnloadedComponentNames Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~GetUnloadedComponentNames.md)  
[IAssemblyDoc::HasUnloadedComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~HasUnloadedComponents.md)
