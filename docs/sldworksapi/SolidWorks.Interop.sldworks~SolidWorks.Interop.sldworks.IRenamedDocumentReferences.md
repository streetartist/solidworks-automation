# IRenamedDocumentReferences Interface

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenamedDocumentReferences`

Allows you to update references to a renamed file in unopened documents.
Allows you to update references to a renamed file in unopened documents.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Interface IRenamedDocumentReferences 
```

```

Dim instance As IRenamedDocumentReferences
```

```

public interface IRenamedDocumentReferences 
```

```

public interface class IRenamedDocumentReferences 
```

Remarks

This interface corresponds to the Rename Documents dialog box in the SOLIDWORKS user interface.

To update references to a renamed file in unopened documents:

1. Set [IRenamedDocumentReferences::UpdateWhereUsedReferences](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenamedDocumentReferences~UpdateWhereUsedReferences.md) to true.
2. Set [IRenamedDocumentReferences::IncludeFileLocations](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenamedDocumentReferences~IncludeFileLocations.md) to true to search the folders listed under **Referenced Documents** in **Tools > Options > System Options > File Locations.**
3. Add or remove folders in which to search using [IRenamedDocumentReferences::AddSearchFolder](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenamedDocumentReferences~AddSearchFolder.md) or [IRenamedDocumentReferences::RemoveSearchFolder](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenamedDocumentReferences~RemoveSearchFolder.md), respectively.
4. Get the folders to search using [IRenamedDocumentReferences::GetSearchPath](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenamedDocumentReferences~GetSearchPath.md).
5. Search for references using [IRenamedDocumentReferences::Search](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenamedDocumentReferences~Search.md).
6. Get the references found in the previous step using [IRenamedDocumentReferences::ReferenceArray](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenamedDocumentReferences~ReferencesArray.md).
7. Remove a reference from the update using [IRenamedDocumentReferences::RemoveReference](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenamedDocumentReferences~RemoveReference.md).
8. Set [IRenamedDocumentReferences::CompletionAction](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenamedDocumentReferences~CompletionAction.md) to [swRenamedDocumentFinalAction\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swRenamedDocumentFinalAction_e.html).swRenamedDocumentFinalAction\_Ok.

Example

[Rename Component and Update References (C#)](Rename_Component_and_Update_References_Example_CSharp.htm)  
[Rename Component and Update References (VB.NET)](Rename_Component_and_Update_References_Example_VBNET.htm)  
[Rename Component and Update References (VBA)](Rename_Component_and_Update_References_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IRenamedDocumentReferences Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenamedDocumentReferences_members.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)  
[IModelDocExtension::HasRenamedDocuments Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~HasRenamedDocuments.md)  
[IModelDocExtension::RenameDocument Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~RenameDocument.md)
