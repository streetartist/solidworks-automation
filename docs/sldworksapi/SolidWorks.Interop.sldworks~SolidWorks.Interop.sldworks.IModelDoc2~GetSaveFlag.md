# GetSaveFlag Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetSaveFlag`

Gets whether the document is currently dirty and needs to be saved.
Gets whether the document is currently dirty and needs to be saved.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetSaveFlag() As System.Boolean
```

```

Dim instance As IModelDoc2
Dim value As System.Boolean
 
value = instance.GetSaveFlag()
```

```

System.bool GetSaveFlag()
```

```

System.bool GetSaveFlag(); 
```

#### Return Value

True if this document needs to be saved, false if not

Remarks

This flag:

- determines if the Do you wish to save changes? dialog is displayed when the user tries to close the document. Many operations cause this flag to be set, and you can use [IModelDoc2::SetSaveFlag](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SetSaveFlag.md) to set this flag.
- is set to true if the document was created in an older version of SOLIDWORKS.
- is set to true for assemblies only when a subassembly has been saved. If this flag is set to true for a subassembly, then the assembly is not marked as dirty until the subassembly is saved.
- is reset to false after an end-user has saved the file.

NOTE: This method returns true if the model is opened read-only, the system option Don't prompt to save read-only referenced documents is not selected, and the model is dirty and visible.

Example

[Determine If Document Is Dirty (VBA)](Determine_if_Document_is_Dirty_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)  
[IModelDoc2::SetSaveFlag Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SetSaveFlag.md)  
[IConfiguration::IsDirty Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~IsDirty.md)
