# SaveDraftingStandard Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SaveDraftingStandard`

Saves the current custom drafting standard to a file.
Saves the current custom drafting standard to a file.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SaveDraftingStandard( _
   ByVal FileName As System.String _
) As System.Boolean
```

```

Dim instance As IModelDocExtension
Dim FileName As System.String
Dim value As System.Boolean
 
value = instance.SaveDraftingStandard(FileName)
```

```

System.bool SaveDraftingStandard( 
   System.string FileName
)
```

```

System.bool SaveDraftingStandard( 
   System.String^ FileName
) 
```

#### Parameters

*FileName*
:   Path and filename for the current custom drafting standard to save to a file

#### Return Value

True if the current custom drafting standard is saved to a file, false if not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)  
[IModelDocExtension::CopyDraftingStandard Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~CopyDraftingStandard.md)  
[IModelDocExtension::DeleteDraftingStandard Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~DeleteDraftingStandard.md)  
[IModelDocExtension::GetDraftingStandardNames Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetDraftingStandardNames.md)  
[IModelDocExtension::LoadDraftingStandard Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~LoadDraftingStandard.md)  
[IModelDocExtension::RenameDraftingStandard Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~RenameDraftingStandard.md)
