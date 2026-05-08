# RenameDocument Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~RenameDocument`

Temporarily renames the selected component using the specified name.
Temporarily renames the selected component using the specified name.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function RenameDocument( _
   ByVal NewName As System.String _
) As System.Integer
```

```

Dim instance As IModelDocExtension
Dim NewName As System.String
Dim value As System.Integer
 
value = instance.RenameDocument(NewName)
```

```

System.int RenameDocument( 
   System.string NewName
)
```

```

System.int RenameDocument( 
   System.String^ NewName
) 
```

#### Parameters

*NewName*
:   New name for the component

#### Return Value

Status of temporarily renaming the component as defined in [swRenameDocumentError\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swRenameDocumentError_e.html) (see **Remarks**)

Remarks

If this method returns swRenameDocumentError\_e.swRenameDocumentError\_None, then the new name of the component is shown in the FeatureManager design tree and the file name of the component changes in memory. All currently open documents that reference the renamed file are updated to reference the new file name.

To:

- get whether the document has renamed components, call [IModelDocExtension::HasRenamedDocuments](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~HasRenamedDocuments.md).
- to avoid an error when attempting to save the document without first saving its references, use [IRenamedDocumentReferences](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenamedDocumentReferences.md) to update references to the renamed component in unopened documents.
- permanently rename the component, [save](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~Save3.md) the document.

See the SOLIDWORKS Help for details about renaming components.

Example

[Rename Components and Save Assembly (C#)](Rename_Components_and_Save_Assembly_Example_CSharp.htm)  
[Rename Components and Save Assembly (VB.NET)](Rename_Components_and_Save_Assembly_Example_VBNET.htm)  
[Rename Components and Save Assembly (VBA)](Rename_Components_and_Save_Assembly_Example_VB.htm)  
[Rename Component and Update References (C#)](Rename_Component_and_Update_References_Example_CSharp.htm)  
[Rename Component and Update References (VB.NET)](Rename_Component_and_Update_References_Example_VBNET.htm)  
[Rename Component and Update References (VBA)](Rename_Component_and_Update_References_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)
