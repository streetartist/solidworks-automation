# IDocumentSpecification Interface

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification`

Allows you to specify how to open a model document. Use this interface's properties before calling ISldWorks::OpenDoc7 to specify how you want to open a model document.
Allows you to specify how to open a model document. Use this interface's properties before calling [ISldWorks::OpenDoc7](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~OpenDoc7.md) to specify how you want to open a model document.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Interface IDocumentSpecification 
```

```

Dim instance As IDocumentSpecification
```

```

public interface IDocumentSpecification 
```

```

public interface class IDocumentSpecification 
```

Remarks

The following properties are not valid when opening a 3DEXPERIENCE file using [SOLIDWORKS Connected](sldworksapiprogguide.chm::/Overview/SOLIDWORKS_Connected.htm):

- [IDocumentSpecification::FileName](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification~FileName.md)
- [IDocumentSpecification::ConfigurationName](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification~ConfigurationName.md)
- [IDocumentSpecification::DocumentType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification~DocumentType.md)
- [IDocumentSpecification::DisplayState](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification~DisplayState.md)
- [IDocumentSpecification::InteractiveAdvancedOpen](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification~InteractiveAdvancedOpen.md)
- [IDocumentSpecification::InteractiveComponentSelection](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification~InteractiveComponentSelection.md)
- [IDocumentSpecification::LoadExternalReferencesInMemory](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification~LoadExternalReferencesInMemory.md)

Example

See the [IPLMObjectSpecification](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPLMObjectSpecification.md) examples.

Example

[Hide All Edges in Drawing View (VBA)](Hide_All_Edges_in_Drawing_View_Example_VB.htm)  
[Open Drawing Document Read-only (VBA)](Open_Drawing_Document_Read-only_Example_VB.htm)  
[Get Whether Components Are Loaded (C#)](Get_Whether_Components_Are_Loaded_Example_CSharp.htm)  
[Get Whether Components Are Loaded (VB.NET)](Get_Whether_Components_Are_Loaded_Example_VBNET.htm)  
[Get Whether Components Are Loaded (VBA)](Get_Whether_Components_Are_Loaded_Example_VB.htm)  
[Open Assembly Document (C#)](Open_Assembly_Document_Example_CSharp.htm)  
[Open Assembly Document (VB.NET)](Open_Assembly_Document_Example_VBNET.htm)  
[Open Assembly Document (VBA)](Open_Assembly_Document_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDocumentSpecification Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification_members.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)  
[ISldWorks::OpenDoc6 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~OpenDoc6.md)
