# GetUnloadedComponentNames Method (IAssemblyDoc)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~GetUnloadedComponentNames`

Gets the unloaded components' paths, referenced configuration names, reasons why they are unloaded, document types, and names.
Gets the unloaded components' paths, referenced configuration names, reasons why they are unloaded, document types, and names.

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

Dim instance As IAssemblyDoc
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
:   Array of the paths of the unloaded components

*UnloadedComponentReferencedConfigurationNames*
:   Array of the referenced configuration names of the unloaded components

*ReasonForUnloadingComponents*
:   Array indicating the reason each component is unloaded as defined by [swComponentLoadStatus\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swComponentLoadStatus_e.html)

*DocTypes*
:   Array of document types as defined in [swDocumentTypes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDocumentTypes_e.html)

#### Return Value

Array of the names of the unloaded components

Remarks

This method is useful when the assembly document was opened with **[Quick View/Selective open](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification~Selective.md)** or [**Do not load hidden components**](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification~IgnoreHiddenComponents.md).

To get whether an assembly has hidden or suppressed unloaded components, call [IAssemblyDoc::HasUnloadedComponents](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~HasUnloadedComponents.md).

Example

[Get Hidden Components Filenames (C#)](Get_Hidden_Components_Filenames_Example_CSharp.htm)  
[Get Hidden Components Filenames (VB.NET)](Get_Hidden_Components_Filenames_Example_VBNET.htm)  
[Get Hidden Components Filenames (VBA)](Get_Hidden_Components_Filenames_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.md)  
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.md)  
[IComponent2::HasUnloadedComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~HasUnloadedComponents.md)  
[IComponent2::GetUnloadedComponentNames Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetUnloadedComponentNames.md)  
[IComponent2::GetHiddenUnloadedChildrenCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetHiddenUnloadedChildrenCount.md)
